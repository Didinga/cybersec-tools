Už jsme skoro v cíli! Na tom screenshotu je vidět, že se tam pořád pletou ty popisky jako "Bash" nebo "Plaintext" – to se tam dostalo, když jsi omylem zkopíroval i text mého rozhraní (ty popisky tlačítek pro kopírování), místo jen toho obsahu.

Pojďme na to naposledy a tentokrát absolutně čistě. Uděláme to tak, že ti sem dám ten text v Raw formátu (prostý text bez jakýchkoliv boxů kolem), aby se ti tam nic nepřimíchalo.

Postup:

Jdi na GitHub a klikni na Edit (tužtička).

Smaž úplně všechno, co v tom okně teď máš.

Zkopíruj pouze řádky níže (od # 🛡️ až po účely.):

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
