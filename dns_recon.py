import dns.resolver

def get_dns_records(domain):
    record_types = ['A', 'MX', 'TXT']
    print(f"--- DNS Reconnaissance pro doménu: {domain} ---")

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            print(f"\n[+] {rtype} Records:")
            for rdata in answers:
                print(f"  {rdata.to_text()}")
                
                # Speciální kontrola pro bezpečnostní TXT záznamy
                if rtype == 'TXT':
                    if 'v=spf1' in rdata.to_text():
                        print("    [!] Nalezen SPF záznam (Ochrana proti podvržení e-mailů)")
                    if 'v=DMARC1' in rdata.to_text():
                        print("    [!] Nalezen DMARC záznam (Politika pro nakládání s e-maily)")

        except dns.resolver.NoAnswer:
            print(f"[-] Žádné {rtype} záznamy nenalezeny.")
        except Exception as e:
            print(f"[!] Chyba při dotazu na {rtype}: {e}")

if __name__ == "__main__":
    target = input("Zadej doménu pro analýzu (např. google.com): ")
    get_dns_records(target)
