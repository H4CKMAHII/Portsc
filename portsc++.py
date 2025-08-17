#!/usr/bin/env python3
import argparse
import socket
import concurrent.futures
import random
import re
import json
import time
from datetime import datetime
from termcolor import colored
from pyfiglet import Figlet
from typing import List, Dict, Optional, Tuple

# Configuration
COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan"]
BANNER_TEXT = "PORTSC++"
MAX_THREADS = 200  # Increased for better parallelism
TIMEOUT = 1.5  # Slightly higher for reliability
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 993, 995, 3389, 8080, 8443]
DEFAULT_PORTS = "1-1024,3000-4000,8080,8443"  # Customizable port ranges

# Banner
def show_banner() -> None:
    f = Figlet(font=random.choice(Figlet().getFonts()))
    ascii_art = f.renderText(BANNER_TEXT)
    print(colored(ascii_art, random.choice(COLORS)))
    print(colored("CREATED BY H4CKMAHII", "cyan"))
    print("-" * 60)

# Validate target (IP or domain)
def validate_target(target: str) -> str:
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    domain_pattern = r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(ip_pattern, target) or re.match(domain_pattern, target):
        try:
            return socket.gethostbyname(target)
        except socket.gaierror:
            print(colored(f"Error: Cannot resolve '{target}'. Check hostname/network.", "red"))
            sys.exit(1)
    else:
        print(colored("Invalid target. Use IP (e.g., 192.168.1.1) or domain (e.g., example.com).", "red"))
        sys.exit(1)

# Parse port ranges (e.g., "1-100,8080,9000-9100")
def parse_ports(port_str: str) -> List[int]:
    ports = set()
    for part in port_str.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            ports.update(range(start, end + 1))
        else:
            ports.add(int(part))
    return sorted(ports)

# Service and version detection
def detect_service(port: int) -> Tuple[str, Optional[str]]:
    try:
        service = socket.getservbyport(port)
        banner = None
        if port == 80:  # HTTP
            banner = grab_http_banner(port)
        elif port == 22:  # SSH
            banner = grab_ssh_banner(port)
        return service, banner
    except:
        return "unknown", None

# Banner grabbing functions
def grab_http_banner(port: int) -> Optional[str]:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(TIMEOUT)
            s.connect((target, port))
            s.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
            return s.recv(1024).decode().split('\n')[0]
    except:
        return None

def grab_ssh_banner(port: int) -> Optional[str]:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(TIMEOUT)
            s.connect((target, port))
            return s.recv(1024).decode().strip()
    except:
        return None

# Scan a single port
def scan_port(target: str, port: int) -> Optional[Tuple[int, str, Optional[str]]]:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(TIMEOUT)
            if s.connect_ex((target, port)) == 0:
                service, banner = detect_service(port)
                return port, service, banner
    except:
        pass
    return None

# Main function
def main() -> None:
    show_banner()

    # Parse arguments
    parser = argparse.ArgumentParser(description="Advanced Python Port Scanner")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("-p", "--ports", default=DEFAULT_PORTS, help="Ports to scan (e.g., '1-1024,8080')")
    parser.add_argument("-t", "--threads", type=int, default=MAX_THREADS, help="Max threads (default: 200)")
    args = parser.parse_args()

    target = validate_target(args.target)
    ports_to_scan = parse_ports(args.ports)

    # Scan info
    print(colored(f"\nTarget: {target}", "cyan"))
    print(colored(f"Scanning ports: {args.ports}", "cyan"))
    print(colored(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n", "cyan"))

    # Threaded scanning
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = {executor.submit(scan_port, target, port): port for port in ports_to_scan}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                port, service, banner = result
                status = colored(f"[+] Port {port}/tcp open", "green")
                service_info = colored(f"Service: {service}", "yellow")
                print(f"{status} {service_info}")
                if banner:
                    print(colored(f"   Banner: {banner.strip()}", "blue"))
                open_ports.append(port)

    # Summary
    print(colored("\nScan Summary:", "magenta"))
    print(colored(f"Scanned Ports: {len(ports_to_scan)}", "cyan"))
    print(colored(f"Open Ports: {len(open_ports)}", "green" if open_ports else "red"))
    if open_ports:
        print(colored(f"Open Ports List: {sorted(open_ports)}", "yellow"))

    # Save results
    with open("scan_results.json", "w") as f:
        json.dump({"target": target, "open_ports": open_ports}, f, indent=4)
    print(colored("\nResults saved to 'scan_results.json'", "cyan"))

if __name__ == "__main__":
    main()
