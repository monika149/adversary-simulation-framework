import nmap
import sys
sys.path.append(".")

from c2_server.database import SessionLocal
from c2_server.models import Agent

def scan_target(ip):
    scanner = nmap.PortScanner()
    print(f"[+] Scanning {ip}...")
    scanner.scan(ip, arguments='-O')  # -O = OS detection

    os_guess = scanner[ip]['osmatch'][0]['name'] if 'osmatch' in scanner[ip] and scanner[ip]['osmatch'] else 'Unknown'
    ports = []

    for proto in scanner[ip].all_protocols():
        for port in scanner[ip][proto].keys():
            ports.append(f"{port}/{proto}")

    return {
        "ip": ip,
        "os": os_guess,
        "ports": ports
    }

def save_as_agent(recon_data):
    db = SessionLocal()

    agent = Agent(
        hostname="unidentified",  # Will update later
        ip=recon_data['ip'],
        os=recon_data['os'],
        last_seen=None
    )
    db.add(agent)
    db.commit()

    print(f"[+] Agent registered: IP={recon_data['ip']} OS={recon_data['os']}")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    result = scan_target(target_ip)
    save_as_agent(result)