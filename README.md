# 🛡️ CyberSec Tools Portfolio - Python

Tento repozitář obsahuje sadu praktických nástrojů pro kybernetickou bezpečnost, které jsem vyvinul v Pythonu na svém Latitude E6440. Projekt slouží jako ukázka mých znalostí v oblastech síťové analýzy, defenzivního monitoringu a auditování webových aplikací.

---

## 🚀 Přehled nástrojů

### 1. TCP Port Scanner (`port_scanner.py`)
Nástroj pro aktivní průzkum sítě. Zjišťuje, které porty jsou na cílovém stroji otevřené, což pomáhá identifikovat běžící služby a potenciální vstupní body.
* **Funkce:** Překlad doménových jmen na IP, skenování běžných portů (SSH, HTTP, SQL), ošetření chyb.
* **Technologie:** Knihovna `socket`.



### 2. Web Security Auditor (`web_audit.py`)
Audituje HTTP hlavičky odpovědí serveru. Kontroluje, zda web používá moderní ochranné mechanismy proti útokům jako XSS nebo Clickjacking.
* **Hledané hlavičky:** CSP, HSTS, X-Frame-Options, X-Content-Type-Options.

### 3. Defensive Security Monitor (`security_monitor.py`)
Jednoduchý IDS (Intrusion Detection System), který v reálném čase analyzuje síťový provoz a upozorňuje na komunikaci mimo povolený seznam portů.
* **Technologie:** Knihovna `scapy`.

### 4. Network Sniffer (`sniffer.py`)
Základní nástroj pro zachytávání a analýzu paketů na IP vrstvě. Slouží k pochopení struktury dat proudících sítí.

### 5. DNS Reconnaissance (`dns_recon.py`)
Provádí lookup DNS záznamů (A, MX, TXT) a analyzuje bezpečnostní politiky pro e-maily (SPF/DMARC), což je klíčové pro prevenci phishingu.

---

## 🛠️ Instalace a použití

1. **Klonování repozitáře:**
   ```bash
   git clone [https://github.com/Didinga/cybersec-tools.git](https://github.com/Didinga/cybersec-tools.git)
   cd cybersec-tools
Instalace závislostí:

Bash

pip3 install scapy requests
Spuštění Port Scanneru:

Bash

python3 port_scanner.py
(Poznámka: Nástroje jako sniffer vyžadují oprávnění sudo.)

📝 Ukázky výstupů (Proof of Concept)
Audit webu (google.com):
Plaintext

[OK] Nalezena hlavička: X-Frame-Options
[!!] CHYBÍ: Content-Security-Policy -> Riziko: Prevence XSS útoků.
[!] Server prozrazuje svou identitu: gws
Skenování portů (Localhost):
Plaintext

--- Zahajuji skenování pro: 127.0.0.1 ---
[+] Port    80: OTEVŘENÝ
[+] Port   443: OTEVŘENÝ
Skenování dokončeno.
⚠️ Prohlášení (Disclaimer)
Tyto nástroje jsou určeny výhradně pro vzdělávací účely a etické testování. Jakékoli použití na systémech bez předchozího souhlasu majitele je nelegální.
