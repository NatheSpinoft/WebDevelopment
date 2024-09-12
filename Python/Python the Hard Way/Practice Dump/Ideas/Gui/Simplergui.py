import tkinter as tk
import csv
from datetime import datetime

# Initialize the list to store transaction items and the accumulated total
items = []
csv_filename = "simplified_transactions.csv"

# Function to add items to the receipt and update the total amount
def add_to_receipt(item, price):
    receipt.insert(tk.END, f"{item:<15} ${price:>5.2f}\n")
    items.append((item, price))

# Function to show total for the current transaction
def show_total():
    total_amount = sum(price for _, price in items)
    
    # Show total in the receipt
    receipt.insert(tk.END, "-" * 25 + "\n")
    receipt.insert(tk.END, f"{'Total':<15} ${total_amount:>5.2f}\n")

# Function to save the current transaction to a CSV file and clear the receipt
def save_transaction():
    # Calculate the total for the current transaction
    total_amount = sum(price for _, price in items)

    # Get the current date and time
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Append the current transaction to the CSV file
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write each item and its price with the date for the transaction
        for item, price in items:
            writer.writerow([current_datetime, item, f"${price:.2f}"])
        writer.writerow([current_datetime, "Total", f"${total_amount:.2f}"])
        writer.writerow([])  # Blank line for spacing
    
    # Clear the receipt and reset items list
    items.clear()
    receipt.delete(1.0, tk.END)

# Main program
root = tk.Tk()
root.title("Simple Receipt GUI")

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

# Button to show total for the current transaction
btn_total = tk.Button(left_frame, text="Show Total", width=15, command=show_total)
btn_total.pack(pady=10)

# Button to save the transaction to CSV and clear the receipt
btn_save = tk.Button(left_frame, text="Save Transaction", width=15, command=save_transaction)
btn_save.pack(pady=10)

# Text box for receipt printout
receipt = tk.Text(right_frame, width=40, height=15, borderwidth=2, relief="solid")
receipt.pack()

# Create the CSV file with headers (if not already created)
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date & Time", "Item", "Price"])
    writer.writerow([])  # Blank line for spacing

# Run the application
root.mainloop()