import subprocess

def scan_sqlmap(url):
    try:
        cmd = ['sqlmap', '-u', url, '--batch', '--risk=1', '--level=1', '--timeout=30']
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if "is vulnerable" in result.stdout:
            return ["SQLMAP: Vulnerabilidade confirmada!"]
        return ["SQLMAP: Nenhuma vulnerabilidade encontrada"]
    except FileNotFoundError:
        return ["sqlmap não instalado (pip install sqlmap)"]
    except:
        return ["Falha ao executar sqlmap"]