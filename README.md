# recon-cli-tool
Simple Python Reconnaissance Tool
It performs DNS lookup, port scanning, WHOIS query, and IP geolocation.

## Requirements

- Python 3.x
- python-whois
- requests

### Install the required libraries:

pip install python-whois requests

## Usage

Run the tool from the terminal:

python recon.py <target>

**Example:**

python recon.py google.com

## What it does:

- Performs DNS lookup to get the IP address  
- Scans a few common ports (21, 22, 80, 443, 8080)
- Retrieves WHOIS domain information  
- Shows IP geolocation (country, region, city)

