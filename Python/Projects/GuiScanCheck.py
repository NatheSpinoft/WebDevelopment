import tkinter as tk
from tkinter import ttk, filedialog
import platform
import socket
import uuid
import psutil
import subprocess
import os
import datetime


class SystemScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced System Scanner")
        self.os_type = tk.StringVar()

        self.dark_mode = False

        self.setup_ui()
        self.auto_detect_os()

    def setup_ui(self):
        # Operating System Radio
        os_frame = ttk.LabelFrame(self.root, text="Operating System")
        os_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        ttk.Radiobutton(os_frame, text="Windows", variable=self.os_type, value="Windows").pack(side="left")
        ttk.Radiobutton(os_frame, text="Mac", variable=self.os_type, value="Mac").pack(side="left")

        # Buttons
        button_data = [
            ("Scan IP Address", self.get_ip),
            ("Scan MAC Address", self.get_mac),
            ("Show Gateway IP", self.get_gateway),
            ("Check RAM Info", self.get_ram),
            ("CPU & Disk Info", self.get_cpu_disk),
            ("Export Output to File", self.export_output),
            ("Toggle Dark Mode", self.toggle_dark_mode),
        ]

        for idx, (label, command) in enumerate(button_data):
            ttk.Button(self.root, text=label, command=command).grid(row=1+idx, column=0, sticky="ew", padx=10, pady=4)

        # Output Box
        self.output_box = tk.Text(self.root, height=15, width=70, bg="white", fg="black")
        self.output_box.grid(row=1, column=1, rowspan=len(button_data), padx=10, pady=10)

    def auto_detect_os(self):
        system = platform.system()
        if system == "Darwin":
            self.os_type.set("Mac")
        elif system == "Windows":
            self.os_type.set("Windows")
        else:
            self.os_type.set("Windows")  # default

        self.log(f"Auto-detected OS: {self.os_type.get()}")

    def log(self, text):
        self.output_box.config(state='normal')
        timestamp = datetime.datetime.now().strftime("[%H:%M:%S] ")
        self.output_box.insert(tk.END, timestamp + text + "\n")
        self.output_box.see(tk.END)
        self.output_box.config(state='disabled')

    def get_ip(self):
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            self.log(f"IP Address: {ip_address}")
        except Exception as e:
            self.log(f"Error getting IP: {e}")

    def get_mac(self):
        try:
            mac = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff)
                            for i in range(0, 8 * 6, 8)][::-1])
            self.log(f"MAC Address: {mac}")
        except Exception as e:
            self.log(f"Error getting MAC: {e}")

    def get_gateway(self):
        os_choice = self.os_type.get()
        try:
            if os_choice == "Windows":
                result = subprocess.check_output("ipconfig", shell=True).decode()
                for line in result.splitlines():
                    if "Default Gateway" in line:
                        gateway = line.split(":")[-1].strip()
                        if gateway:
                            self.log(f"Gateway IP: {gateway}")
                            return
            else:  # macOS
                result = subprocess.check_output("netstat -rn | grep default", shell=True).decode()
                gateway = result.strip().split()[1]
                self.log(f"Gateway IP: {gateway}")
        except Exception as e:
            self.log(f"Error getting Gateway: {e}")

    def get_ram(self):
        try:
            mem = psutil.virtual_memory()
            total_gb = round(mem.total / (1024 ** 3), 2)
            self.log(f"Total RAM: {total_gb} GB")
        except Exception as e:
            self.log(f"Error getting RAM: {e}")

    def get_cpu_disk(self):
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            disk_usage = psutil.disk_usage('/')
            disk_total = round(disk_usage.total / (1024 ** 3), 2)
            disk_free = round(disk_usage.free / (1024 ** 3), 2)
            self.log(f"CPU Usage: {cpu_percent}%")
            self.log(f"Disk Total: {disk_total} GB | Free: {disk_free} GB")
        except Exception as e:
            self.log(f"Error getting CPU/Disk info: {e}")

    def export_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")],
                                                 title="Save Output As")
        if file_path:
            try:
                content = self.output_box.get("1.0", tk.END)
                with open(file_path, 'w') as file:
                    file.write(content)
                self.log(f"Output exported to: {file_path}")
            except Exception as e:
                self.log(f"Failed to export file: {e}")

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        bg = "black" if self.dark_mode else "white"
        fg = "lime" if self.dark_mode else "black"
        self.output_box.config(bg=bg, fg=fg)
        self.log("Dark mode enabled" if self.dark_mode else "Dark mode disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = SystemScannerApp(root)
    root.mainloop()
