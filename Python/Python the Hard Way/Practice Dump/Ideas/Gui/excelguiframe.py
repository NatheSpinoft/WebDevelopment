import tkinter as tk
from tkinter import ttk
import pandas as pd

# Load the CSV data
df = pd.read_csv('items.csv')

class ReceiptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Receipt GUI")

        # Left Frame for item selection
        self.left_frame = tk.Frame(self.root)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10)

        # Add headers for the "Excel" like frame
        tk.Label(self.left_frame, text="Item").grid(row=0, column=0)

        # Create a list to hold the dropdowns
        self.item_vars = []
        self.row_count = 1

        # Add the first row
        self.add_row()

        # Right Frame for receipt and total
        self.right_frame = tk.Frame(self.root)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10)

        # Receipt frame
        self.receipt_frame = tk.Frame(self.right_frame)
        self.receipt_frame.grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.receipt_frame, text="Receipt").grid(row=0, column=0)

        self.receipt_items = []
        self.total_label = tk.Label(self.right_frame, text="Total: $0.00")
        self.total_label.grid(row=1, column=0)

    def add_row(self):
        # Create dropdown for items
        item_var = tk.StringVar()
        item_dropdown = ttk.Combobox(self.left_frame, textvariable=item_var, values=df['item'].tolist())
        item_dropdown.grid(row=self.row_count, column=0)

        # Bind the item selection to update receipt
        item_dropdown.bind("<<ComboboxSelected>>", lambda event, iv=item_var: self.add_to_receipt(iv))

        # Keep track of variables
        self.item_vars.append(item_var)

        # Increment row count
        self.row_count += 1

    def add_to_receipt(self, item_var):
        # Get the selected item and its price
        item = item_var.get()
        if item:
            price = df.loc[df['item'] == item, 'price'].values[0]
            price_str = f"${price:.2f}"

            # Add item to receipt
            receipt_text = f"{item}: {price_str}"
            self.receipt_items.append(receipt_text)

            # Update receipt display
            self.update_receipt_display()

            # Update the total
            self.calculate_total()

    def update_receipt_display(self):
        # Clear current receipt display
        for widget in self.receipt_frame.winfo_children():
            widget.destroy()
        
        # Add header
        tk.Label(self.receipt_frame, text="Receipt").grid(row=0, column=0)

        # Display items
        for idx, item_text in enumerate(self.receipt_items, start=1):
            tk.Label(self.receipt_frame, text=item_text).grid(row=idx, column=0)

    def calculate_total(self):
        # Calculate the total from selected items
        total = 0
        for item_text in self.receipt_items:
            price = item_text.split(': ')[1].replace('$', '')
            total += float(price)
        self.total_label.config(text=f"Total: ${total:.2f}")

# Create the main window
root = tk.Tk()
app = ReceiptApp(root)
root.mainloop()