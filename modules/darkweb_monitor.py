import requests

def breach_check_manual(email):
    try:
        # Use Have I Been Pwned API for breach check (or alternatives)
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        headers = {
            "User-Agent": "ReconX - Dark Web Monitor"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            breaches = response.json()
            print(f"[+] Found breaches for {email}:")
            for breach in breaches:
                print(f"  - {breach['Name']} | {breach['BreachDate']}")
        elif response.status_code == 404:
            print(f"[-] No breaches found for {email}")
        else:
            print(f"[-] Error: {response.status_code}")
    except Exception as e:
        print(f"[-] Error during breach check: {str(e)}")
