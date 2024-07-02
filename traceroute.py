# Developer: Jadan Morrow
# Description: This script performs a traceroute to a target domain or IP address to see the path packets take.
# Use Case: Use this script to diagnose network routing issues and understand the path packets take through the network.
# Command to run: python traceroute.py

import subprocess

def traceroute(target):
    result = subprocess.run(['traceroute', target], capture_output=True, text=True)
    print(result.stdout)

def main():
    target = input("Enter the target domain or IP: ")
    traceroute(target)

if __name__ == "__main__":
    main()