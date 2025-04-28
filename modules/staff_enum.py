# modules/staff_enum.py

import re
import requests
from bs4 import BeautifulSoup
import os

def linkedin_dork(domain):
    print(f"[!] LinkedIn Dorks to use manually:")
    print(f"https://www.google.com/search?q=site:linkedin.com/in+@{domain}")
    print(f"https://www.linkedin.com/search/results/people/?keywords={domain}")

def google_staff_search(domain):
    print(f"[!] Google Dork for employees:")
    print(f"https://www.google.com/search?q=site:{domain}+team+contact")

def scrape_names_from_about_page(url):
    print(f"[*] Scraping names from {url}")
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text(separator=' ')
            potential_names = re.findall(r'\b[A-Z][a-z]+(?:\s[A-Z]\.)?(?:\s[A-Z][a-z]+)+\b', text)
            unique_names = set(potential_names)
            if unique_names:
                os.makedirs("output", exist_ok=True)
                save_path = "output/staff_names.txt"
                with open(save_path, 'w') as f:
                    for name in unique_names:
                        print(f"[+] {name}")
                        f.write(name + "\n")
                print(f"\n[✔] Saved {len(unique_names)} names to {save_path}")
            else:
                print("[-] No names found.")
        else:
            print(f"[-] Failed to fetch {url}")
    except Exception as e:
        print(f"[-] Error: {str(e)}")

def generate_email_guesses(domain, names_file):
    try:
        with open(names_file, 'r') as f:
            names = f.read().splitlines()
        print("\n[*] Generated email guesses:")
        for name in names:
            parts = name.lower().split()
            if len(parts) >= 2:
                first, last = parts[0], parts[-1]
                guesses = [
                    f"{first}.{last}@{domain}",
                    f"{first}{last}@{domain}",
                    f"{first[0]}{last}@{domain}"
                ]
                for email in guesses:
                    print(f"[+] {email}")
    except Exception as e:
        print(f"[-] Error generating emails: {str(e)}")
