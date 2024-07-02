# Developer: Jadan Morrow
# Description: This script performs a ping sweep to determine which hosts are up within a specified IP range.
# Use Case: Use this script to identify active devices on a local network for network management or troubleshooting.
# Command to run: python ping_sweep.py

import subprocess

def ping_sweep(ip_range):
    alive_hosts = []
    for ip in ip_range:
        result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            alive_hosts.append(ip)
    return alive_hosts

def main():
    ip_base = input("Enter the base IP (e.g., 192.168.1.): ")
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
    ip_range = [f"{ip_base}{i}" for i in range(start_range, end_range + 1)]
    alive_hosts = ping_sweep(ip_range)
    print(f"Alive hosts: {alive_hosts}")

if __name__ == "__main__":
    main()