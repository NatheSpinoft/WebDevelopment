import nmap
import time

# Initialize the Nmap PortScanner
nm = nmap.PortScanner()

# Function to perform a network scan
def perform_scan(network):
    nm.scan(network, '22-80')
    for host in nm.all_hosts():
        print('Host : {} ({})'.format(host, nm[host].hostname()))
        print('State : {}'.format(nm[host].state()))
        for proto in nm[host].all_protocols():
            print('Protocol : {}'.format(proto))
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                print('Port : {}\tState : {}'.format(port, nm[host][proto][port]['state']))

# Schedule scans every hour
while True:
    perform_scan('192.168.1.0/24')
    time.sleep(3600)  # Sleep for 1 hour
