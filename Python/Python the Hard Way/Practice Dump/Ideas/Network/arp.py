from scapy.all import ARP, Ether, srp

def arp_request(target_ip):
    # Create an ARP request packet to the target IP
    arp = ARP(pdst=target_ip)
    # Create an Ethernet broadcast packet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine both to create the full packet
    packet = ether / arp

    # Send the packet and receive the response
    result = srp(packet, timeout=2, verbose=False)[0]

    # Parse the result
    for sent, received in result:
        print(f"IP: {received.psrc}, MAC: {received.hwsrc}")

# Use the function to send an ARP request
target_ip = "192.168.2."
number = 1



for number in range(255):
    number += 1
    new = target_ip + str(number)
    arp_request(new)
