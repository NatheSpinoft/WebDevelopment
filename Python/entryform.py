import tkinter as tk
from tkinter import ttk
import psycopg2

def save_to_database():
    receipt_name = entry_name.get()
    receipt_date = entry_date.get()
    item_name = entry_item.get()
    item_amount = entry_amount.get()
    item_account = entry_account.get()
    
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            dbname="receipt_db",
            user="stefanpinto",
            password="",
            host="localhost",
            port="5432"
        )

        # Create a cursor object
        cur = conn.cursor()

        # Execute SQL INSERT statement for receipt_info table
        cur.execute(
            "INSERT INTO receipt_info (receipt_name, receipt_date) VALUES (%s, %s) RETURNING receipt_id",
            (receipt_name, receipt_date)
        )
        receipt_id = cur.fetchone()[0]  # Get the generated receipt ID
        
        # Execute SQL INSERT statement for receipt_items table
        cur.execute(
            "INSERT INTO receipt_items (receipt_id, item_name, item_amount, item_account) VALUES (%s, %s, %s, %s)",
            (receipt_id, item_name, item_amount, item_account)
        )

        # Commit changes and close connection
        conn.commit()
        conn.close()

        # Clear entry fields
        entry_name.delete(0, tk.END)
        entry_date.delete(0, tk.END)
        entry_item.delete(0, tk.END)
        entry_amount.delete(0, tk.END)
        entry_account.delete(0, tk.END)

        # Show success message
        label_status.config(text="Receipt saved successfully!")
    except psycopg2.Error as e:
        # Show error message
        label_status.config(text=f"Error: {e}")

# Create main window
root = tk.Tk()
root.title("Receipt Entry Form")

# Create receipt info fields
label_name = ttk.Label(root, text="Receipt Name:")
entry_name = ttk.Entry(root)
label_name.grid(row=0, column=0, sticky="w")
entry_name.grid(row=0, column=1)

label_date = ttk.Label(root, text="Receipt Date:")
entry_date = ttk.Entry(root)
label_date.grid(row=1, column=0, sticky="w")
entry_date.grid(row=1, column=1)

# Create receipt item fields
label_item = ttk.Label(root, text="Item Name:")
entry_item = ttk.Entry(root)
label_item.grid(row=2, column=0, sticky="w")
entry_item.grid(row=2, column=1)

label_item_amount = ttk.Label(root, text="Item Amount:")
entry_amount = ttk.Entry(root)
label_item_amount.grid(row=3, column=0, sticky="w")
entry_amount.grid(row=3, column=1)

label_account = ttk.Label(root, text="Item Account:")
entry_account = ttk.Entry(root)
label_account.grid(row=4, column=0, sticky="w")
entry_account.grid(row=4, column=1)

# Create save button
button_save = ttk.Button(root, text="Save", command=save_to_database)
button_save.grid(row=5, column=1)

# Create status label
label_status = ttk.Label(root, text="")
label_status.grid(row=6, column=0, columnspan=2)

# Run the main event loop
root.mainloop()
