#runs in python3

import socket  #network operations like DNS lookup and port scanning
import argparse  #for parsing command-line arguments
import whois  #library to perform WHOIS lookups
import requests  #for making HTTP requests to external APIs


#Function for DNS Lookup, converts domain to IP
def dns_lookup(target):
    try:
        ip=socket.gethostbyname(target)  #translates domain name to IP address
        print(f"- DNS Lookup: {target} --> {ip}")  #prints the resolved IP
        return ip  #returns the IP for use in other functions
    except:
        print(f"- DNS Lookup Failed for {target}")  #prints failure message
        return None  #returns None if lookup fails


#Function for scanning the basic ports
def port_scan(target, ports=[21,22,80,443,8080]):
    print(f"- Starting Port Scan on {target}")  #indicates port scanning has started
    for port in ports:  #iterates through the list of ports
        soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #creates TCP socket
        soc.settimeout(1)  #sets 1 second timeout to avoid delays
        result=soc.connect_ex((target,port))  #tries to connect, returns 0 if successful
        if result==0:
            print(f"- Port {port} is OPEN")  #prints open port
        soc.close()  #closes the socket


#Function for WHOIS Lookup, retrieves domain registration details
def whois_lookup(target):
    try:
        w=whois.whois(target)  #performs WHOIS query
        print(f"- WHOIS Data for {target}:")
        print(f"    Domain Name: {w.domain_name}")  #displays domain name
        print(f"    Registrar: {w.registrar}")  #displays registrar info
        print(f"    Creation Date: {w.creation_date}")  #displays domain creation date
    except:
        print(f"- WHOIS Lookup Failed for {target}")  #prints failure message


#Function for IP Geolocation lookup using public API
def ip_geolocation(ip):
    try:
        response=requests.get(f"http://ip-api.com/json/{ip}")  #HTTP GET request to geolocation API
        data=response.json()  #parses JSON response
        print(f"- IP Geolocation for {ip}:")
        print(f"    Country: {data['country']}")  #displays country
        print(f"    Region: {data['regionName']}")  #displays region
        print(f"    City: {data['city']}")  #displays city
    except:
        print("- Geolocation API Failed")  #prints failure message if API call fails


#Main function 
def main():
    #the description reveals the meaning of this tool when commannd 'The description reveals' is being ran 
    parser=argparse.ArgumentParser(description="PJ's Recon CLI Tool")  #creates argument parser
    parser.add_argument("target",help="Domain or IP to scan")  #defines expected argument
    args=parser.parse_args()  #parses command-line arguments

    ip=dns_lookup(args.target)  #performs DNS lookup and gets IP
    if ip:  #if IP was successfully retrieved
        port_scan(ip)  #performs port scan
        whois_lookup(args.target)  #retrieves WHOIS information
        ip_geolocation(ip)  #performs IP geolocation lookup


#If script is executed directly, run main() 
if __name__=="__main__":
    main()
