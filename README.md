# 🛡️ CyberSec Toolkit

Sada Python nástrojů pro síťovou bezpečnost, průzkum infrastruktury a audit webových aplikací. Určeno pro vzdělávací účely a etický hacking.

---

## 🧰 Nástroje

| Nástroj | Popis |
|---|---|
| `port_scanner.py` | Skenování otevřených TCP portů na cílovém hostu |
| `dns_recon.py` | Průzkum DNS záznamů a mapování domény |
| `sniffer.py` | Zachytávání a analýza síťových paketů |
| `security_monitor.py` | Monitoring sítě a detekce anomálií v reálném čase |
| `web_audit.py` | Audit bezpečnostních hlaviček a konfigurace webových aplikací |
| `example_output.txt` | Ukázky výstupů jednotlivých nástrojů |

---

## 🚀 Instalace

```bash
git clone https://github.com/Didinga/cybersec-tools.git
cd cybersec-tools
pip3 install scapy requests
```

---

## 📖 Použití

```bash
# Skenování portů
python3 port_scanner.py

# DNS průzkum
python3 dns_recon.py

# Zachytávání paketů (vyžaduje root/admin)
sudo python3 sniffer.py

# Monitoring sítě
python3 security_monitor.py

# Audit webu
python3 web_audit.py
```

---

## 📋 Ukázka výstupu

```
[*] Zahajuji skenování: google.com
[*] Cílová IP: 142.250.185.78
-------------------------------------------
[+] Port  80  (HTTP)  : OPEN
[+] Port  443 (HTTPS) : OPEN
[-] Port  22  (SSH)   : CLOSED
-------------------------------------------
[*] Skenování dokončeno.
```

---

## ⚖️ Disclaimer

Tyto nástroje jsou určeny **výhradně pro vzdělávací účely** a testování vlastních systémů nebo systémů, ke kterým máš výslovné povolení. Autor nenese odpovědnost za jakékoli zneužití.

---

*Vyvinuto v Pythonu 3 · Open Source*
