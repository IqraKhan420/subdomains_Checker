import socket

# Function to find subdomains
def find_subdomains(domain, subdomain_list):
    found_subdomains = []
    for subdomain in subdomain_list:
        full_domain = f"{subdomain}.{domain}"
        try:
            # Try to resolve the subdomain to an IP address
            ip = socket.gethostbyname(full_domain)
            print(f"Found: {full_domain} -> {ip}")
            found_subdomains.append(full_domain)
        except socket.gaierror:
            # If subdomain is not found, skip
            pass
    return found_subdomains

if __name__ == "__main__":
    # Input the domain to search for subdomains
    domain = input("Enter the domain to find subdomains (e.g., example.com): ")

    # List of common subdomains (you can extend this list)
    subdomain_list = [
        "www", "mail", "admin", "ftp", "localhost", "webmail", "test", 
        "blog", "shop", "dev", "api", "vpn", "secure", "beta"
    ]
    
    print(f"\nFinding subdomains for {domain}...\n")

    # Find and display subdomains
    found_subdomains = find_subdomains(domain, subdomain_list)

    if found_subdomains:
        print("\nSubdomains found:")
        for subdomain in found_subdomains:
            print(subdomain)
    else:
        print("No subdomains found.")
