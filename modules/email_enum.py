# modules/email_enum.py

import re
import requests
from bs4 import BeautifulSoup

EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

def google_dork_emails(domain):
    print(f"[!] Google Dorks to use manually:")
    print(f"https://www.google.com/search?q=%22@{domain}%22")
    print(f"https://www.google.com/search?q=site:{domain}+email")

def scrape_emails_from_url(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            emails = re.findall(EMAIL_REGEX, response.text)
            unique_emails = set(emails)
            for email in unique_emails:
                print(f"[+] Found email: {email}")
        else:
            print(f"[-] Failed to fetch {url}")
    except Exception as e:
        print(f"[-] Error scraping {url}: {str(e)}")

def basic_hibp_check(email):
    print(f"[*] Check breaches manually: https://haveibeenpwned.com/account/{email}")
