import tkinter as tk
import csv
from datetime import datetime

# Function to add items to the receipt and update the total amount
def add_to_receipt(item, price):
    receipt.insert(tk.END, f'{item:<15} ${price:>5.2f}\n')
    items.append((item, price))

# Function to display the total amount in the receipt
def show_total():
    total_amount = sum(price for _, price in items)
    receipt.insert(tk.END, "-" * 25 + "\n")
    receipt.insert(tk.END, f"{'Total':<15} ${total_amount:>5.2f}\n")

# Function to save the transaction to a CSV file and clear the receipt for a new transaction
def save_and_clear():
    # Save receipt to a CSV file
    filename = f"transaction_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Price"])
        for item, price in items:
            writer.writerow([item, f"${price:.2f}"])
        writer.writerow(["Total", f"${sum(price for _, price in items):.2f}"])
    
    # Clear the receipt and reset items list
    receipt.delete(1.0, tk.END)
    items.clear()

# Main program
root = tk.Tk()
root.title("Simple Menu")

# Initialize the list to store transaction items
items = []

# Layout setup
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

left_frame = tk.Frame(main_frame)
left_frame.pack(side=tk.LEFT, padx=10)

right_frame = tk.Frame(main_frame)
right_frame.pack(side=tk.RIGHT, padx=10)

# Buttons for items
btn_hamburger = tk.Button(left_frame, text="Hamburger", width=15, command=lambda: add_to_receipt("Hamburger", 2.00))
btn_hamburger.pack(pady=5)

btn_fries = tk.Button(left_frame, text="Fries", width=15, command=lambda: add_to_receipt("Fries", 1.50))
btn_fries.pack(pady=5)

btn_pop = tk.Button(left_frame, text="Pop", width=15, command=lambda: add_to_receipt("Pop", 1.00))
btn_pop.pack(pady=5)

# Button to show the total amount
btn_total = tk.Button(left_frame, text="Total", width=15, command=show_total)
btn_total.pack(pady=10)

# Button to save and clear
btn_save_clear = tk.Button(left_frame, text="Save & Clear", width=15, command=save_and_clear)
btn_save_clear.pack(pady=10)

# Text box for receipt printout
receipt = tk.Text(right_frame, width=40, height=15, borderwidth=2, relief="solid")
receipt.pack()

# Run the application
root.mainloop()