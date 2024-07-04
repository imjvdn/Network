# Network Utility Scripts


## Description

This repository contains a collection of Python scripts developed for various network utility tasks. These scripts are designed to fetch DNS records, IP address information, perform network scans, and more. Each script is tailored for specific tasks and includes detailed comments explaining its purpose, usage, and how to run it.

## Scripts Overview

### DNSQuery

- `dns_query.py`: Queries DNS servers for NS, A, and MX records of a given domain.

### IPInfoLookup

- `ip_info_lookup.py`: Fetches location information for a given IP address using the `ipinfo.io` API.

### PingSweep

- `ping_sweep.py`: Performs a ping sweep on a range of IP addresses to check their availability.

### PortScanner

- `port_scanner.py`: Scans a given IP address for open ports within a specified range.

### Traceroute

- `traceroute.py`: Performs a traceroute to a given IP address or domain to determine the path packets take to the destination.

### WhoisLookup

- `whois_lookup.py`: Fetches WHOIS information for a given domain or IP address.

## Usage

Each script can be executed from the command line. For example:

### DNSQuery

```bash
python dns_query.py example.com
