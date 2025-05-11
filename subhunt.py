import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init
import threading

# Initialize colorama and lock
init(autoreset=True)
lock = threading.Lock()
found_subdomains = []

def resolve_subdomain(subdomain):
    try:
        ip = socket.gethostbyname(subdomain)
        with lock:
            print(f"{Fore.GREEN}[+] Found: {subdomain} -> {ip}")
            found_subdomains.append((subdomain, ip))
    except socket.gaierror:
        print(f"{Fore.RED}[-] Not Found: {subdomain}")

def main():
    parser = argparse.ArgumentParser(description="SubHunt - Fast Subdomain Enumeration Tool")
    parser.add_argument("domain", help="Target domain (e.g. example.com)")
    parser.add_argument("-w", "--wordlist", default="subdomains.txt", help="Subdomain wordlist file")
    parser.add_argument("-t", "--threads", type=int, default=50, help="Number of threads (default: 50)")
    parser.add_argument("-o", "--output", default="found_subdomains.txt", help="Output file to save valid subdomains")
    args = parser.parse_args()

    try:
        with open(args.wordlist, "r") as f:
            subdomains = [line.strip() + "." + args.domain for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}[!] Wordlist file not found: {args.wordlist}")
        return

    print(f"{Fore.CYAN}🔍 Enumerating subdomains for {args.domain} using {args.threads} threads...\n")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(resolve_subdomain, subdomains)

    # Save results
    with open(args.output, "w") as out_file:
        for sub, ip in found_subdomains:
            out_file.write(f"{sub} -> {ip}\n")

    print(f"\n{Fore.YELLOW}[✓] Valid subdomains saved to: {args.output}")

if __name__ == "__main__":
    main()
