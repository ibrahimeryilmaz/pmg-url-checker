# === README.md ===
# Bu dosyayý "README.md" olarak repoya ekle
# pmg-url-checker

This script integrates Google Safe Browsing API with Proxmox Mail Gateway (PMG) 8.2.

## Features
- Scans incoming emails for URLs
- Checks URLs against Google Safe Browsing
- Quarantines emails containing malicious URLs

## Installation
```bash
git clone https://github.com/ibrahimeryilmaz/pmg-url-checker.git
cd pmg-url-checker
chmod +x install.sh
./install.sh
```

## Configuration
Edit `config.json` and insert your Google Safe Browsing API key.

## Usage
You can integrate this script with PMG by calling:
```bash
python3 url_checker.py /path/to/email.eml
```

## Logs
Check logs at: `/var/log/pmg-url-checker.log`

## Quarantine
Emails with malicious URLs are moved to: `/var/quarantine/`

## License
MIT