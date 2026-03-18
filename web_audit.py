import requests

def audit_web(url):
    if not url.startswith('http'):
        url = 'https://' + url
    
    print(f"--- Spouštím bezpečnostní audit pro: {url} ---")
    
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        
        # Seznam důležitých bezpečnostních hlaviček
        security_headers = {
            "Strict-Transport-Security": "Chrání před odposlechem (vynucuje HTTPS).",
            "Content-Security-Policy": "Prevence XSS útoků (vkládání cizího kódu).",
            "X-Content-Type-Options": "Zabraňuje prohlížeči hádat typ souboru (MIME sniffing).",
            "X-Frame-Options": "Chrání před Clickjackingem (vkládání webu do i-framu)."
        }

        for header, description in security_headers.items():
            if header in headers:
                print(f"[OK] Nalezena hlavička: {header}")
            else:
                print(f"[!!] CHYBÍ: {header}")
                print(f"     -> Riziko: {description}")

        # Bonus: Kontrola verze serveru (Info Leakage)
        server = headers.get("Server")
        if server:
            print(f"\n[!] Server prozrazuje svou identitu: {server}")
            print("    (Profi tip: Skryjte verzi serveru, ať útočník neví, na co cílit.)")

    except Exception as e:
        print(f"[!] Chyba při spojení: {e}")

if __name__ == "__main__":
    target = input("Zadej URL webu k auditu: ")
    audit_web(target)
