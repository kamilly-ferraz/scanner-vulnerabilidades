import requests

def scan_headers(url):
    try:
        r = requests.get(url, timeout=10)
        headers = r.headers
        faltando = []
        verificacoes = {
            'X-Frame-Options': 'Clickjacking',
            'Content-Security-Policy': 'Proteção contra XSS',
            'X-Content-Type-Options': 'MIME sniffing',
            'Strict-Transport-Security': 'HSTS (apenas HTTPS)'
        }
        for h, risco in verificacoes.items():
            if h not in headers:
                if h == 'Strict-Transport-Security' and not url.startswith('https'):
                    continue
                faltando.append(f"{h} ausente → {risco}")
        return faltando or ["Todos os cabeçalhos críticos presentes"]
    except:
        return ["Falha ao obter cabeçalhos"]