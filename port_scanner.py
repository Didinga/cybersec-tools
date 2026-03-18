import socket
import sys
from datetime import datetime

def port_scan(target, ports):
    print(f"\n--- Zahajuji skenování pro: {target} ---")
    print(f"Čas zahájení: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)
    
    try:
        target_ip = socket.gethostbyname(target)
        print(f"[*] Cílová IP adresa: {target_ip}")
    except socket.gaierror:
        print(f"[!] Chyba: Nepodařilo se přeložit hostitele {target}")
        return

    for port in ports:
        # Tohle ti ukáže, na čem skener zrovna pracuje
        print(f"[*] Zkouším port {port}...", end="\r")
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # Zkus klidně 0.5 pokud je síť rychlá
        
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            # Smažeme řádek "Zkouším..." a vypíšeme úspěch
            print(f"[+] Port {port:5}: OTEVŘENÝ      ")
        s.close()

    print("\n" + "-" * 40)
    print(f"Skenování dokončeno: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    target_input = input("Zadej IP adresu nebo doménu ke skenování: ")
    # Přidáme port 80 a 443 na začátek, ty bývají u routerů nejčastěji
    common_ports = [80, 443, 21, 22, 23, 25, 53, 110, 3306, 3389]
    port_scan(target_input, common_ports)
