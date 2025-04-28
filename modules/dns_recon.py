# modules/dns_recon.py

import dns.resolver
import dns.query
import dns.zone

def dns_zone_transfer(domain):
    print(f"[*] Attempting DNS Zone Transfer for {domain}")
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        for rdata in answers:
            ns = str(rdata.target)
            print(f"[*] Trying nameserver: {ns}")
            try:
                zone = dns.zone.from_xfr(dns.query.xfr(ns, domain))
                for name, node in zone.nodes.items():
                    print(f"[+] Found: {name}.{domain}")
            except Exception as e:
                print(f"[-] Failed zone transfer on {ns}: {str(e)}")
    except Exception as e:
        print(f"[-] Error finding nameservers: {str(e)}")

def dns_brute_force_subdomains(domain, wordlist):
    print(f"[*] Brute forcing subdomains for {domain}")
    try:
        with open(wordlist, 'r') as f:
            for line in f:
                subdomain = line.strip() + '.' + domain
                try:
                    dns.resolver.resolve(subdomain, 'A')
                    print(f"[+] Found subdomain: {subdomain}")
                except:
                    pass
    except Exception as e:
        print(f"[-] Error: {str(e)}")

def dns_wildcard_check(domain):
    print(f"[*] Checking for wildcard DNS on {domain}")
    try:
        fake_subdomain = 'random-nonexistent.' + domain
        dns.resolver.resolve(fake_subdomain, 'A')
        print("[!] Wildcard DNS Detected!")
    except:
        print("[+] No wildcard DNS detected.")
