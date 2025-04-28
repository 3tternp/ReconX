# modules/staff_enum.py
import os
import re
import requests
from bs4 import BeautifulSoup

def scrape_about_page(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Collect all text
            text = soup.get_text(separator=' ')
            # Basic regex for Firstname Lastname pattern
            pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
            matches = re.findall(pattern, text)
            return matches
        else:
            print(f"[-] Failed to access {url}")
            return []
    except Exception as e:
        print(f"[-] Error scraping About page: {str(e)}")
        return []

def google_dork_search(query):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        url = f"https://www.google.com/search?q={query}"
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            snippets = soup.find_all('span')
            text = ' '.join([s.get_text() for s in snippets])
            pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
            matches = re.findall(pattern, text)
            return matches
        else:
            print(f"[-] Failed Google Dork: {query}")
            return []
    except Exception as e:
        print(f"[-] Error during Google Dorking: {str(e)}")
        return []

def scrape_staff_names(domain):
    all_names = set()

    about_url = f"https://{domain}/about"
    print(f"[+] Scraping About Page: {about_url}")
    names = scrape_about_page(about_url)
    all_names.update(names)

    dork1 = f'site:linkedin.com "at {domain}"'
    print(f"[+] Dorking LinkedIn...")
    names = google_dork_search(dork1)
    all_names.update(names)

    dork2 = f'"work at {domain}"'
    print(f"[+] Dorking Google for work mentions...")
    names = google_dork_search(dork2)
    all_names.update(names)

    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file = os.path.join(output_folder, "staff_list.txt")
    with open(output_file, "w") as f:
        for name in sorted(all_names):
            f.write(name + "\n")

    if all_names:
        print(f"[+] Found {len(all_names)} unique staff names. Saved to {output_file}")
    else:
        print(f"[-] No staff names found.")
