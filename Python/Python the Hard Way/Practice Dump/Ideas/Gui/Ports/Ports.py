import tkinter as tk
from tkinter import scrolledtext
import psutil

def list_ports():
    # Clear the text widget before displaying new data
    output_box.delete(1.0, tk.END)
    
    # Fetch all network connections
    connections = psutil.net_connections()

    if not connections:
        output_box.insert(tk.END, "No active ports found.")
        return

    # Categorize ports by their status
    listening_ports = []
    established_ports = []
    other_ports = []

    for conn in connections:
        try:
            # Only consider local ports with a valid process ID
            if conn.laddr:
                port = conn.laddr.port
                try:
                    proc = psutil.Process(conn.pid) if conn.pid else None
                    process_name = proc.name() if proc else "N/A"
                except:
                    process_name = "N/A"

                port_info = (port, process_name, conn.status)

                # Classify the connections based on their status
                if conn.status == 'LISTEN':
                    listening_ports.append(port_info)
                elif conn.status == 'ESTABLISHED':
                    established_ports.append(port_info)
                else:
                    other_ports.append(port_info)
        except Exception as e:
            output_box.insert(tk.END, f"Error reading connection: {str(e)}\n")

    # Sort the lists by port number
    listening_ports.sort(key=lambda x: x[0])
    established_ports.sort(key=lambda x: x[0])
    other_ports.sort(key=lambda x: x[0])

    # Display the ports in categories
    output_box.insert(tk.END, "Listening Ports:\n")
    for port, app, status in listening_ports:
        output_box.insert(tk.END, f"Port: {port}, Application: {app}, Status: {status}\n")

    output_box.insert(tk.END, "\nEstablished Ports:\n")
    for port, app, status in established_ports:
        output_box.insert(tk.END, f"Port: {port}, Application: {app}, Status: {status}\n")

    output_box.insert(tk.END, "\nOther Ports:\n")
    for port, app, status in other_ports:
        output_box.insert(tk.END, f"Port: {port}, Application: {app}, Status: {status}\n")

# GUI Setup
root = tk.Tk()
root.title("Port and Application Viewer")
root.geometry("600x500")

# Scrolled text box for displaying the output
output_box = scrolledtext.ScrolledText(root, width=70, height=25)
output_box.pack(pady=10)

# Button to refresh and list ports
refresh_button = tk.Button(root, text="List Ports and Applications", command=list_ports)
refresh_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
