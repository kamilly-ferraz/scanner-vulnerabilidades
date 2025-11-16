from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

def scan_forms(url, session):
    try:
        r = session.get(url, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        forms = soup.find_all('form')
        resultados = []
        for form in forms:
            action = urljoin(url, form.get('action') or '')
            method = form.get('method', 'get').lower()
            inputs = [i.get('name') for i in form.find_all('input') if i.get('name')]
            resultados.append(f"Formulário: {action} ({method.upper()}), Campos: {inputs}")
        return resultados or ["Nenhum formulário encontrado"]
    except:
        return ["Falha ao analisar formulários"]