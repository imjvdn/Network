# Developer: Jadan Morrow
# Description: This script queries DNS records (NS, A, MX) for a given domain using multiple DNS servers.
# Use Case: Use this script to gather DNS information from different DNS servers to verify consistency and diagnose DNS issues.
# Command to run: python dns_query.py <domain>

import dns.resolver
import datetime
import sys

# Check if the domain is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <domain>")
    sys.exit(1)

# Domain to query
domain = sys.argv[1]

# DNS servers to query
dns_servers = [
    "8.8.8.8", "8.8.4.4", "208.67.222.222", "208.67.220.220", "8.20.247.10", "8.20.247.11", "50.87.144.163"
]

for dns_server in dns_servers:
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [dns_server]

        ns_records = resolver.resolve(domain, 'NS')
        a_records = resolver.resolve(domain, 'A')
        mx_records = resolver.resolve(domain, 'MX')

        if ns_records or a_records or mx_records:
            print(
                "*****************************************************************************************************************************************")
            print("DNS Server Used:", dns_server)

            if ns_records:
                print("NS Records:")
                for ns in ns_records:
                    print(ns.to_text())

            if a_records:
                print("A Records:")
                for a in a_records:
                    print(a.to_text())

            if mx_records:
                print("MX Records:")
                for mx in mx_records:
                    print(mx.to_text())

        print("Timestamp:", datetime.datetime.now())
        # Query time is not directly available in dns.resolver, so we skip this part.

    except Exception as e:
        print(f"An error occurred: {e}")