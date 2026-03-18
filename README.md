# 🛡️ CyberSec Tools Portfolio - Python

Tento repozitář obsahuje sadu praktických nástrojů pro kybernetickou bezpečnost, které jsem vyvinul v Pythonu na svém Latitude E6440.

---

## 🔧 Přehled nástrojů

### 1. TCP Port Scanner (`port_scanner.py`)

Nástroj pro aktivní průzkum sítě. Zjišťuje, které porty jsou na cílovém stroji otevřené.

- **Technologie:** Knihovna `socket`
- **Princip:** TCP Three-Way Handshake

---

## 🚀 Instalace a použití

### 1. Klonování repozitáře

```bash
git clone https://github.com/Didinqa/cybersec-tools.git
```

### 2. Vstup do složky

```bash
cd cybersec-tools
```

### 3. Instalace závislostí

```bash
pip3 install scapy requests
```

### 4. Spuštění

```bash
python3 port_scanner.py
```

---

## 📋 Ukázka výstupu

```
--- Zahajuji skenování pro: google.com ---
[*] Cílová IP adresa: 142.250.185.78
[+] Port 80: OTEVŘENÝ
[+] Port 443: OTEVŘENÝ
Skenování dokončeno.
```

---

## ⚠️ Prohlášení

Tyto nástroje jsou určeny výhradně pro vzdělávací účely. Jakékoli použití na systémech bez předchozího souhlasu majitele je nelegální.
