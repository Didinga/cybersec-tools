🛡️ CyberSec Tools Portfolio - Python
Tento repozitář obsahuje sadu praktických nástrojů pro kybernetickou bezpečnost, které jsem vyvinul v Pythonu na svém Latitude E6440. Projekt slouží jako ukázka mých znalostí v oblastech síťové analýzy, defenzivního monitoringu a auditování webových aplikací.

🚀 Přehled nástrojů
1. TCP Port Scanner (port_scanner.py)
Nástroj pro aktivní průzkum sítě. Zjišťuje, které porty jsou na cílovém stroji otevřené, což pomáhá identifikovat běžící služby a potenciální vstupní body.

Funkce: Překlad doménových jmen na IP, skenování běžných portů, ošetření chyb.

Technologie: Knihovna socket.

Princip fungování (TCP Three-Way Handshake):
Skript se pokouší navázat spojení se serverem. Pokud port odpoví příznakem SYN-ACK, skript jej označí jako otevřený.

2. Web Security Auditor (web_audit.py)
Audituje HTTP hlavičky odpovědí serveru. Kontroluje, zda web používá moderní ochranné mechanismy proti útokům jako XSS nebo Clickjacking.

3. Defensive Security Monitor (security_monitor.py)
Jednoduchý IDS (Intrusion Detection System), který v reálném čase analyzuje síťový provoz a upozorňuje na podezřelou aktivitu.

🛠️ Instalace a použití
Klonování repozitáře:

Bash

git clone https://github.com/Didinga/cybersec-tools.git
cd cybersec-tools
Instalace závislostí:

Bash

pip3 install scapy requests
Spuštění Port Scanneru:

Bash

python3 port_scanner.py
📝 Ukázky výstupů (Proof of Concept)
Skenování portů (google.com):
Plaintext

--- Zahajuji skenování pro: google.com ---
[*] Cílová IP adresa: 142.250.185.78
----------------------------------------
[+] Port    80: OTEVŘENÝ
[+] Port   443: OTEVŘENÝ
----------------------------------------
Skenování dokončeno.
⚠️ Prohlášení (Disclaimer)
Tyto nástroje jsou určeny výhradně pro vzdělávací účely a etické testování. Jakékoli použití na systémech bez předchozího souhlasu majitele je nelegální.
