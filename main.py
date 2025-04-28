from modules import dns_recon, email_enum, staff_enum
import pyfiglet

def banner():
    ascii_banner = pyfiglet.figlet_format("ReconX")
    print(ascii_banner)
    print("Developed by 3tternp | Refined by ChatGPT")
    print("=" * 50)

def main():
    banner()
    print("""
    ReconX - Reconnaissance Tool
    =============================
    1. DNS Zone Transfer
    2. DNS Brute Force
    3. DNS Wildcard Check
    4. Email Enumeration - Google Dork
    5. Email Enumeration - Scrape Website
    6. Email Enumeration - Breach Check (Manual)
    7. Staff Enumeration - LinkedIn Dork
    8. Staff Enumeration - Google Dork
    9. Staff Enumeration - Scrape About Page
    10. Staff Enumeration - Generate Email Guesses
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
        domain = input("Enter domain: ")
        dns_recon.dns_zone_transfer(domain)
    elif choice == '2':
        domain = input("Enter domain: ")
        wordlist = input("Enter wordlist path: ")
        dns_recon.dns_brute_force_subdomains(domain, wordlist)
    elif choice == '3':
        domain = input("Enter domain: ")
        dns_recon.dns_wildcard_check(domain)
    elif choice == '4':
        domain = input("Enter domain: ")
        email_enum.google_dork_emails(domain)
    elif choice == '5':
        url = input("Enter URL to scrape: ")
        email_enum.scrape_emails_from_url(url)
    elif choice == '6':
        email = input("Enter email to check: ")
        email_enum.basic_hibp_check(email)
    elif choice == '7':
        domain = input("Enter domain: ")
        staff_enum.linkedin_dork(domain)
    elif choice == '8':
        domain = input("Enter domain: ")
        staff_enum.google_staff_search(domain)
    elif choice == '9':
        url = input("Enter About page URL: ")
        staff_enum.scrape_names_from_about_page(url)
    elif choice == '10':
        domain = input("Enter domain: ")
        names_file = 'output/staff_names.txt'
        staff_enum.generate_email_guesses(domain, names_file)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
