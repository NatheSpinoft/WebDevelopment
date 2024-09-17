import tkinter as tk
from tkinter import messagebox
from scapy.all import ARP, Ether, srp
import requests

# Function to get device type using macvendors.com API
def get_device_type(mac_address):
    try:
        url = f"https://api.macvendors.com/{mac_address}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "Unknown Device"
    except Exception as e:
        return f"Error: {e}"

# Function to scan for ARP MAC addresses and infer device types
def scan_network():
    try:
        # Get local network IP range
        ip_range = entry_ip.get()
        if not ip_range:
            messagebox.showwarning("Input Error", "Please enter a valid IP range.")
            return

        # Create an ARP request
        arp_request = ARP(pdst=ip_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp_request

        # Send the packet and receive responses
        result = srp(packet, timeout=3, verbose=False)[0]

        # Display results in the textbox
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "{:<18} {:<20} {}\n".format("IP", "MAC", "Device Type"))
        text_output.insert(tk.END, "-"*60 + "\n")

        for sent, received in result:
            # Identify device type from the MAC address using macvendors.com API
            device_type = get_device_type(received.hwsrc)
            text_output.insert(tk.END, "{:<18} {:<20} {}\n".format(received.psrc, received.hwsrc, device_type))

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("ARP MAC Address Scanner with Device Types (via macvendors.com)")

# Create widgets
label_ip = tk.Label(root, text="Enter IP range (e.g., 192.168.1.1/24):")
label_ip.pack(pady=10)

entry_ip = tk.Entry(root, width=30)
entry_ip.pack(pady=5)

button_scan = tk.Button(root, text="Scan Network", command=scan_network)
button_scan.pack(pady=10)

text_output = tk.Text(root, height=15, width=60)
text_output.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
