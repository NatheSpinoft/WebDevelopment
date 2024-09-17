from scapy.all import ARP, sniff

connected_devices = set()

def process_packet(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:  # ARP response (is-at)
        mac_address = packet[ARP].hwsrc
        ip_address = packet[ARP].psrc

        if mac_address not in connected_devices:
            print(f"Device connected: {mac_address} (IP: {ip_address})")
            connected_devices.add(mac_address)

def monitor_network(interface):
    print(f"Listening for devices on {interface}...")
    sniff(iface=interface, filter="arp", prn=process_packet, store=0)

# Call the function to monitor a specific network interface (e.g., 'wlan0')
monitor_network("en0")
