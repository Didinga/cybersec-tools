from scapy.all import sniff, IP, TCP

# Seznam "bezpečných" portů, které běžně používáš
ALLOWED_PORTS = [80, 443, 53, 22] 

def monitor_callback(packet):
    if packet.haslayer(TCP):
        dst_port = packet[TCP].dport
        src_ip = packet[IP].src
        
        # Pokud někdo komunikuje na jiném než běžném portu, vypíšeme varování
        if dst_port not in ALLOWED_PORTS:
            print(f"[!] VAROVÁNÍ: Neobvyklý provoz! {src_ip} se připojuje na port {dst_port}")
        else:
            print(f"[OK] Běžný provoz na portu {dst_port}")

print("[*] Spouštím defenzivní monitor na tvém Latitude...")
sniff(prn=monitor_callback, store=0)
