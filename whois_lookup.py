# Developer: Jadan Morrow
# Description: This script performs a WHOIS lookup on a domain to get registration information.
# Use Case: Use this script to obtain information about domain ownership, registration dates, and contact information.
# Command to run: python whois_lookup.py

import whois

def whois_lookup(domain):
    result = whois.whois(domain)
    print(result)

def main():
    domain = input("Enter the domain: ")
    whois_lookup(domain)

if __name__ == "__main__":
    main()