from modules import dns_recon, email_enum, staff_enum, darkweb_monitor, telegram_notify
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
    ReconX - Reconnaissance Tool
    Developed by 3tternp | Refined by ChatGPT
    ==========================================
    1. DNS Zone Transfer
    2. DNS Brute Force
    3. DNS Wildcard Check
    4. Email Enumeration - Google Dork
    5. Email Enumeration - Scrape Website
    6. Dark Web Breach Check (Manual)
    7. Telegram Channel Monitoring
    8. Dark Web Monitoring (OSINT Tools)
    9. Monitor Dark Web with Tor/I2P
    10. Real-Time Telegram Breach Alerts
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
        email = input("Enter email for breach check: ")
        darkweb_monitor.breach_check_manual(email)  # New Dark Web Breach Check option
    elif choice == '7':
        telegram_channel = input("Enter Telegram channel: ")
        telegram_notify.monitor_telegram_channel(telegram_channel)  # Telegram monitoring
    elif choice == '8':
        domain = input("Enter domain: ")
        darkweb_monitor.osint_tools_darkweb_monitoring(domain)  # OSINT Dark Web Monitoring
    elif choice == '9':
        darkweb_monitor.monitor_darkweb_tor_i2p()  # Dark web with Tor/I2P
    elif choice == '10':
        telegram_channel = input("Enter Telegram channel: ")
        telegram_notify.real_time_breach_alerts(telegram_channel)  # Real-time Telegram Breach Alerts
    else:
        print("[-] Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
