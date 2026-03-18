🛡️ CyberSec Tools Portfolio - Python
Tento repozitář obsahuje sadu praktických nástrojů pro kybernetickou bezpečnost, které jsem vyvinul v Pythonu na svém Latitude E6440.

🚀 Přehled nástrojů
1. TCP Port Scanner (port_scanner.py)
Nástroj pro aktivní průzkum sítě. Zjišťuje, které porty jsou na cílovém stroji otevřené.

Technologie: Knihovna socket.

Princip: TCP Three-Way Handshake.

🛠️ Instalace a použití
Klonování repozitáře:

Bash

git clone https://github.com/Didinga/cybersec-tools.git
cd cybersec-tools
Instalace závislostí:

Bash

pip3 install scapy requests
Spuštění:

Bash

python3 port_scanner.py
📝 Ukázky výstupů (PoC)
Plaintext

--- Zahajuji skenování pro: google.com ---
[*] Cílová IP adresa: 142.250.185.78
[+] Port    80: OTEVŘENÝ
[+] Port   443: OTEVŘENÝ
⚠️ Prohlášení
Tyto nástroje jsou určeny výhradně pro vzdělávací účely.
