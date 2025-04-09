# === install.sh ===
# Bu dosyayý "install.sh" olarak oluþtur ve çalýþtýrmadan önce chmod +x ver
#!/bin/bash

# Gereksinimleri yükle
echo "[+] Installing dependencies..."
apt update && apt install -y python3 python3-pip
pip3 install requests

# Log ve karantina klasörlerini oluþtur
echo "[+] Creating folders..."
mkdir -p /var/log
mkdir -p /var/quarantine

# Log dosyasý oluþtur
touch /var/log/pmg-url-checker.log

# Kurulum tamamlandý
echo "[+] Installation completed! Don't forget to set your API key in config.json."