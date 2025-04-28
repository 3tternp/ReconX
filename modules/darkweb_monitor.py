import requests

def breach_check_manual(email):
    try:
        # Have I Been Pwned API for checking email breaches
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

def shodan_darkweb_check(domain):
    try:
        # Using Shodan API to check for exposed services or data related to the domain
        url = f"https://api.shodan.io/shodan/host/search?key=YOUR_API_KEY&query={domain}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['matches']:
                print(f"[+] Exposed services found for {domain}:")
                for match in data['matches']:
                    print(f"  - IP: {match['ip_str']} | {match['data']}")
            else:
                print(f"[-] No exposed services found for {domain}")
        else:
            print(f"[-] Error fetching data from Shodan: {response.status_code}")
    except Exception as e:
        print(f"[-] Error during Shodan check: {str(e)}")
