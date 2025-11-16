#!/usr/bin/env python3
import sys
import requests
from scanner import scan_forms, scan_xss, scan_sqli, scan_headers, scan_sqlmap
from datetime import datetime

def main():
    if len(sys.argv) != 2:
        print("Uso: python scanner.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    if not url.startswith('http'):
        url = 'http://' + url

    session = requests.Session()
    session.headers.update({'User-Agent': 'VulnScanner-CLI/1.0'})

    print(f"[+] Escaneando: {url}")
    print(f"[+] Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")

    results = {
        "Cabeçalhos de Segurança": scan_headers(url),
        "Formulários": scan_forms(url, session),
        "XSS Refletido": scan_xss(url, session),
        "SQL Injection": scan_sqli(url, session),
        "SQLMAP": scan_sqlmap(url)
    }

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(f"RELATÓRIO DE VULNERABILIDADES\n")
        f.write(f"Alvo: {url}\n")
        f.write(f"Data: {datetime.now().strftime('%d/%m/%Y às %H:%M')}\n")
        f.write("="*60 + "\n\n")
        for secao, dados in results.items():
            f.write(f"{secao.upper()}\n")
            f.write("-" * 40 + "\n")
            if "Nenhum" in dados[0] or "Todos" in dados[0]:
                f.write(f"   {dados[0]}\n")
            else:
                for linha in dados:
                    status = "VULNERABILIDADE" if any(x in linha.lower() for x in ['xss', 'sqli', 'ausente', 'vulnerable', 'possível']) else "INFO"
                    f.write(f"   • [{status}] {linha}\n")
            f.write("\n")
        f.write("Fim do relatório.\n")

    print("[+] Escaneamento concluído! Relatório salvo em: report.txt")

if __name__ == "__main__":
    main()