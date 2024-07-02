# Developer: Jadan Morrow
# Description: This script retrieves location information for a given IP address using the ipinfo.io API.
# Use Case: Use this script to get details about the geographic location, ISP, and other information for an IP address.
# Command to run: python ip_info_lookup.py <IP Address> OR python ip_info_lookup.py

import sys
import requests
import datetime
import ipaddress

# Check if the IP address is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <IP Address>")
    sys.exit(1)

# IP address to query
ip_address = sys.argv[1]

# Validate the IP address format
try:
    ip = ipaddress.ip_address(ip_address)
except ValueError:
    print("Invalid IP address format")
    sys.exit(1)

# URL for IP information
url = f"https://ipinfo.io/{ip_address}/json"

try:
    response = requests.get(url)
    response.raise_for_status()
    location = response.json()

    print("------- IP Info Lookup --------")
    print(f"IP Address: {ip_address}")
    print(f"Hostname: {location.get('hostname', 'N/A')}")
    print(f"ISP: {location.get('org', 'N/A')}")
    print(f"City: {location.get('city', 'N/A')}")
    print(f"Region: {location.get('region', 'N/A')}")
    print(f"Country: {location.get('country', 'N/A')}")
    loc = location.get('loc', 'N/A').split(',')
    if len(loc) == 2:
        print(f"Latitude: {loc[0]}")
        print(f"Longitude: {loc[1]}")
    else:
        print("Latitude: N/A")
        print("Longitude: N/A")
    print(f"Timezone: {location.get('timezone', 'N/A')}")
    print("-------------------------------")
    print("--------- System Time ---------")
    print(f"    {datetime.datetime.now().strftime('%d %B %Y %H:%M:%S')}")
    print("-------------------------------")

except requests.RequestException as e:
    print(f"Error getting location information for IP address {ip_address}: {e}")