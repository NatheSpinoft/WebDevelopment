import psutil
import tkinter as tk
from tkinter import ttk, messagebox

# Sort the treeview by the clicked column
def sort_treeview_column(treeview, col, reverse):
    data_list = [(treeview.set(k, col), k) for k in treeview.get_children('')]
    
    # Convert column data to appropriate type (int for PID, float for percentages)
    if col in ('PID', 'CPU Usage (%)', 'Memory Usage (%)'):
        data_list.sort(key=lambda t: float(t[0]) if t[0] else 0, reverse=reverse)
    else:
        data_list.sort(key=lambda t: t[0].lower(), reverse=reverse)
    
    # Re-arrange the rows based on sorted data
    for index, (val, k) in enumerate(data_list):
        treeview.move(k, '', index)

    # Reverse sort direction for next click
    treeview.heading(col, command=lambda: sort_treeview_column(treeview, col, not reverse))

# Function to refresh the process list
def refresh_process_list():
    for row in process_tree.get_children():
        process_tree.delete(row)
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            process_tree.insert('', 'end', values=(
                proc.info['pid'], proc.info['name'], 
                proc.info['cpu_percent'], proc.info['memory_percent']
            ))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

# Function to kill the selected process
def kill_selected_process():
    selected_item = process_tree.selection()
    if selected_item:
        pid = int(process_tree.item(selected_item)['values'][0])
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            messagebox.showinfo("Success", f"Process {pid} terminated.")
            refresh_process_list()
        except psutil.NoSuchProcess:
            messagebox.showerror("Error", "Process not found.")
        except psutil.AccessDenied:
            messagebox.showerror("Error", "Access Denied.")
    else:
        messagebox.showwarning("Warning", "No process selected.")

# Create the main window
root = tk.Tk()
root.title("Task Manager")

# Set the window size
root.geometry("600x400")

# Create a treeview to display the processes
columns = ("PID", "Name", "CPU Usage (%)", "Memory Usage (%)")
process_tree = ttk.Treeview(root, columns=columns, show='headings', height=15)
for col in columns:
    process_tree.heading(col, text=col, command=lambda _col=col: sort_treeview_column(process_tree, _col, False))
    process_tree.column(col, minwidth=50, width=150)

process_tree.pack(pady=10)

# Refresh button
refresh_button = tk.Button(root, text="Refresh", command=refresh_process_list)
refresh_button.pack(pady=5)

# Kill process button
kill_button = tk.Button(root, text="Kill Process", command=kill_selected_process)
kill_button.pack(pady=5)

# Initial load of the process list
refresh_process_list()

# Run the Tkinter event loop
root.mainloop()
