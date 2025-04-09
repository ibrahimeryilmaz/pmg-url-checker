# === install.sh ===
# Bu dosyay� "install.sh" olarak olu�tur ve �al��t�rmadan �nce chmod +x ver
#!/bin/bash

# Gereksinimleri y�kle
echo "[+] Installing dependencies..."
apt update && apt install -y python3 python3-pip
pip3 install requests

# Log ve karantina klas�rlerini olu�tur
echo "[+] Creating folders..."
mkdir -p /var/log
mkdir -p /var/quarantine

# Log dosyas� olu�tur
touch /var/log/pmg-url-checker.log

# Kurulum tamamland�
echo "[+] Installation completed! Don't forget to set your API key in config.json."