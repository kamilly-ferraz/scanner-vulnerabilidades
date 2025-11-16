import requests
from urllib.parse import urljoin

def scan_xss(url, session):
    payload = '<script>alert(1)</script>'
    try:
        from bs4 import BeautifulSoup
        r = session.get(url, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        forms = soup.find_all('form')
        resultados = []
        for form in forms:
            action = urljoin(url, form.get('action') or '')
            method = form.get('method', 'get').lower()
            data = {inp.get('name'): payload for inp in form.find_all('input') if inp.get('name')}
            try:
                resp = session.post(action, data=data) if method == 'post' else session.get(action, params=data)
                if payload in resp.text:
                    resultados.append(f"XSS refletido no formulário: {action}")
            except:
                pass
        return resultados or ["Nenhum XSS refletido encontrado"]
    except:
        return ["Falha no teste de XSS"]