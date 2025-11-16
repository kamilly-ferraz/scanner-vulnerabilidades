# scanner-vulnerabilidades
# VulnScanner

![Python](https://img.shields.io/badge/python-3.9%2B-blue?logo=python&logoColor=white)
![Pentest](https://img.shields.io/badge/pentest-RED%20TEAM-red)
![Hacker](https://img.shields.io/badge/hacker-approved-brightgreen)
![Brazil](https://img.shields.io/badge/made%20in-BRASIL-greenyellow)

> **"Se está na web, está no alvo."**  
> **Scanner de vulnerabilidades web em Python com relatório em português (PT-BR)**  
> Desenvolvido por **Kamilly Ferraz** 

---

## O que ele faz?

| Checkmark | Missão |
|-----------|--------|
| Checkmark | **XSS Refletido** — Injeta `<script>alert(1)</script>` e vê se o site "fala" |
| Checkmark | **SQL Injection** — Testa `'`, `1' OR '1'='1`, `DROP TABLE` — *tremor no banco* |
| Checkmark | **Cabeçalhos de Segurança** — CSP, HSTS, X-Frame? Se não tiver, *alerta vermelho* |
| Checkmark | **sqlmap no piloto automático** — O monstro do SQLi entra em ação |
| Checkmark | **Relatório em `report.txt`** — Em português, com legenda, *pronto pra apresentação* |

---

## Legenda do Relatório (Decifre o Código)

| Ícone | Tradução |
|------|--------|
| **[VULNERABILIDADE]** | **CORRA!** — Exploit real. O site está *sangrando*. |
| **[INFO]** | **Melhore isso** — Não quebra, mas um atacante agradece. |

---

## Exemplo de Relatório (report.txt)

<img width="619" height="368" alt="Captura de Tela 2025-11-15 às 23 31 47" src="https://github.com/user-attachments/assets/1e8be127-fb38-42df-8264-34b955a74448" />


## Como Instalar (em 30 segundos)

```bash
# 1. Clone o arsenal
git clone https://github.com/kamillyferraz/vulnscanner-pro.git
cd vulnscanner-pro

# 2. Crie seu bunker (ambiente virtual)
python3 -m venv venv

# 3. Entre no modo hacker
source venv/bin/activate    # macOS/Linux
# venv\Scripts\activate     # Windows

# 4. Armamento completo
pip install requests beautifulsoup4 sqlmap
