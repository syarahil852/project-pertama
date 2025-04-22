# Enhanced DNS Lookup Tool
import socket

def find_ip():
    print("Welcome to the DNS Lookup Tool!")
    domain = input("Enter a domain name (e.g., example.com): ").strip()
    
    try:
        ip = socket.gethostbyname(domain)
        print(f"The IP address of {domain} is: {ip}")
    except socket.gaierror:
        print(f"Failed to find the IP address for {domain}. Please check the domain name and try again.")

if __name__ == "__main__":
    find_ip()   