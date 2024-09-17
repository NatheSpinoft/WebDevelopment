import tkinter as tk
from tkinter import messagebox
from scapy.all import ARP, Ether, srp
import subprocess

# Function to scan for ARP MAC addresses
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
        for sent, received in result:
            text_output.insert(tk.END, f"IP: {received.psrc} - MAC: {received.hwsrc}\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("ARP MAC Address Scanner")

# Create widgets
label_ip = tk.Label(root, text="Enter IP range (e.g., 192.168.1.1/24):")
label_ip.pack(pady=10)

entry_ip = tk.Entry(root, width=30)
entry_ip.pack(pady=5)

button_scan = tk.Button(root, text="Scan Network", command=scan_network)
button_scan.pack(pady=10)

text_output = tk.Text(root, height=10, width=50)
text_output.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
