# Developer: Jadan Morrow
# Description: This script scans open ports on a target domain or IP address within a specified port range.
# Use Case: Use this script to identify open ports on a server for security assessment or network troubleshooting.
# Command to run: python port_scanner.py

import socket

def scan_ports(target, port_range):
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def main():
    target = input("Enter the target domain or IP: ")
    port_range = input("Enter the port range (e.g., 1-1024): ")
    start_port, end_port = map(int, port_range.split('-'))
    open_ports = scan_ports(target, (start_port, end_port))
    if open_ports:
        print(f"Open ports on {target}:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print(f"No open ports found on {target} within the range {start_port}-{end_port}")

if __name__ == "__main__":
    main()