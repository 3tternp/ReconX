from modules import dns_recon, email_enum, darkweb_monitor, telegram_notify
import os

def warning_message():
    print("=" * 50)
    print("!!! WARNING !!!")
    print("=" * 50)
    print("This tool is for educational and authorized testing purposes only.")
    print("Unauthorized usage against systems without permission is illegal.")
    print("=" * 50)
    accept = input("Do you accept the terms and wish to proceed? (yes/no): ").strip().lower()
    if accept != 'yes':
        print("Exiting... User did not accept the terms.")
        exit()

def main():
    warning_message()
    print("""
    ReconX - Simplified Dark Web Monitoring Tool
    ==========================================
    1. DNS Zone Transfer
    2. DNS Brute Force
    3. DNS Wildcard Check
    4. Email Breach Check - Have I Been Pwned
    5. Domain Exposure Check - Shodan (Dark Web)
    6. Real-Time Telegram Breach Alerts
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
        email = input("Enter email for breach check: ")
        darkweb_monitor.breach_check_manual(email)  # Using Have I Been Pwned API
    elif choice == '5':
        domain = input("Enter domain for exposure check: ")
        darkweb_monitor.shodan_darkweb_check(domain)  # Shodan check for exposed services
    elif choice == '6':
        telegram_channel = input("Enter Telegram channel: ")
        telegram_notify.real_time_breach_alerts(telegram_channel)  # Send real-time alerts
    else:
        print("[-] Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
