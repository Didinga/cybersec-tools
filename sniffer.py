from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        protocol = "Other"
        
        # Rozpoznání protokolu a portů
        if packet.haslayer(TCP):
            protocol = "TCP"
            port_info = f"Src Port: {packet[TCP].sport} -> Dst Port: {packet[TCP].dport}"
        elif packet.haslayer(UDP):
            protocol = "UDP"
            port_info = f"Src Port: {packet[UDP].sport} -> Dst Port: {packet[UDP].dport}"
        else:
            port_info = ""

        print(f"[+] {protocol} | {ip_layer.src} -> {ip_layer.dst} {port_info}")

print("[*] Monitoring network traffic on Latitude E6440... (Ctrl+C to stop)")
sniff(prn=packet_callback, store=0)
