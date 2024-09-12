import tkinter as tk
from tkinter import ttk
import pandas as pd

# Load the CSV data
df = pd.read_csv('items.csv')

class ReceiptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Receipt GUI")

        # Left Frame for items and price
        self.left_frame = tk.Frame(self.root)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10)

        # Add headers for the "Excel" like frame
        tk.Label(self.left_frame, text="Item").grid(row=0, column=0)
        tk.Label(self.left_frame, text="Price").grid(row=0, column=1)

        # Create a list to hold the dropdowns and price entries
        self.item_vars = []
        self.price_vars = []
        self.row_count = 1

        # Add first row
        self.add_row()

        # Button to add more rows
        add_row_btn = tk.Button(self.left_frame, text="Add Row", command=self.add_row)
        add_row_btn.grid(row=self.row_count, column=2)

        # Right Frame for total
        self.right_frame = tk.Frame(self.root)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.right_frame, text="Total:").grid(row=0, column=0)
        self.total_label = tk.Label(self.right_frame, text="0.00")
        self.total_label.grid(row=0, column=1)

    def add_row(self):
        # Create dropdown for items
        item_var = tk.StringVar()
        item_dropdown = ttk.Combobox(self.left_frame, textvariable=item_var, values=df['item'].tolist())
        item_dropdown.grid(row=self.row_count, column=0)

        # Create label for price
        price_var = tk.StringVar()
        price_label = tk.Label(self.left_frame, textvariable=price_var)
        price_label.grid(row=self.row_count, column=1)

        # Bind the item selection to update price and total
        item_dropdown.bind("<<ComboboxSelected>>", lambda event, iv=item_var, pv=price_var: self.update_price(iv, pv))

        # Keep track of variables
        self.item_vars.append(item_var)
        self.price_vars.append(price_var)

        # Increment row count
        self.row_count += 1

    def update_price(self, item_var, price_var):
        # Get the selected item and update the corresponding price
        item = item_var.get()
        price = df.loc[df['item'] == item, 'price'].values[0]
        price_var.set(f"${price:.2f}")

        # Update the total automatically
        self.calculate_total()

    def calculate_total(self):
        # Calculate the total from selected items
        total = 0
        for price_var in self.price_vars:
            price = price_var.get().replace('$', '')
            if price:
                total += float(price)
        self.total_label.config(text=f"${total:.2f}")

# Create the main window
root = tk.Tk()
app = ReceiptApp(root)
root.mainloop()