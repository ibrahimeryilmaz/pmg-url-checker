# === url_checker.py ===
import os
import re
import json
import requests
import email
from email import policy
import sys
import logging

# Logging ayarý
logging.basicConfig(filename='/var/log/pmg-url-checker.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

# Config yükle
CONFIG_FILE = 'config.json'
with open(CONFIG_FILE) as config_file:
    config = json.load(config_file)
API_KEY = config['google_safe_browsing_api_key']

# Google Safe Browsing URL
GSB_URL = 'https://safebrowsing.googleapis.com/v4/threatMatches:find?key=' + API_KEY

def extract_urls(email_content):
    urls = re.findall(r'(https?://\S+)', email_content)
    return urls

def check_url_with_google(url):
    payload = {
        "client": {
            "clientId": "pmg-url-checker",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    }
    response = requests.post(GSB_URL, json=payload)
    if response.status_code == 200:
        threats = response.json().get('matches', [])
        if threats:
            return True
    return False

def quarantine_email(email_path):
    quarantine_dir = '/var/quarantine/'
    os.makedirs(quarantine_dir, exist_ok=True)
    base_name = os.path.basename(email_path)
    quarantine_path = os.path.join(quarantine_dir, base_name)
    os.rename(email_path, quarantine_path)
    logging.info(f'Email quarantined: {email_path}')

def process_email(email_path):
    with open(email_path, 'r', encoding='utf-8', errors='ignore') as f:
        msg = email.message_from_file(f, policy=policy.default)
        email_content = msg.as_string()

    urls = extract_urls(email_content)
    logging.info(f'Found URLs: {urls}')

    for url in urls:
        if check_url_with_google(url):
            logging.warning(f'Malicious URL found: {url}')
            quarantine_email(email_path)
            return  # Zararlý bulursa karantinaya alýp çýkýyor

    logging.info(f'No malicious URLs found in: {email_path}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 url_checker.py /path/to/email.eml')
        sys.exit(1)

    email_file = sys.argv[1]
    process_email(email_file)