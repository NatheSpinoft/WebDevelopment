import tkinter as tk
import csv
from datetime import datetime

# Initialize the list to store transaction items and the accumulated total
items = []
csv_filename = "simplified_transactions_with_logo.csv"

# Function to add items to the receipt and update the running total
def add_to_receipt(item, price):
    receipt.insert(tk.END, f"{item:<15} ${price:>5.2f}\n")
    items.append((item, price))
    
    # Update the running total
    update_running_total()

# Function to show total for the current transaction and calculate change
def show_total():
    total_amount = sum(price for _, price in items)

    # Get the amount entered by the user in the "Amount Paid" entry
    try:
        amount_paid = float(amount_paid_entry.get())
    except ValueError:
        receipt.insert(tk.END, "Invalid amount entered. Please enter a valid number.\n")
        return

    # Calculate the change
    if amount_paid >= total_amount:
        change = amount_paid - total_amount
        receipt.insert(tk.END, "-" * 25 + "\n")
        receipt.insert(tk.END, f"{'Total':<15} ${total_amount:>5.2f}\n")
        receipt.insert(tk.END, f"{'Paid':<15} ${amount_paid:>5.2f}\n")
        receipt.insert(tk.END, f"{'Change':<15} ${change:>5.2f}\n")
    else:
        receipt.insert(tk.END, "-" * 25 + "\n")
        receipt.insert(tk.END, f"{'Total':<15} ${total_amount:>5.2f}\n")
        receipt.insert(tk.END, f"Not enough payment. Short by ${total_amount - amount_paid:>5.2f}\n")

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
    
    # Reset running total to $0.00
    update_running_total()

# Function to update the running total in the receipt
def update_running_total():
    total_amount = sum(price for _, price in items)
    running_total_label.config(text=f"Running Total: ${total_amount:.2f}")

# Main program
root = tk.Tk()
root.title("Simple Receipt GUI with Change and Logo")

# Layout setup
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

left_frame = tk.Frame(main_frame)
left_frame.pack(side=tk.LEFT, padx=10)

right_frame = tk.Frame(main_frame)
right_frame.pack(side=tk.RIGHT, padx=10)

# Add a permanent title/logo at the top of the receipt frame (centered)
shop_logo = tk.Label(right_frame, text="Pinto Shop", font=("Helvetica", 16, "bold"))
shop_logo.pack(pady=10)

# Text box for receipt printout (below the logo)
receipt = tk.Text(right_frame, width=40, height=15, borderwidth=2, relief="solid")
receipt.pack()

# Label for the running total (always visible at the bottom of the receipt frame)
running_total_label = tk.Label(right_frame, text="Running Total: $0.00", font=("Helvetica", 12, "bold"))
running_total_label.pack(pady=10)

# Buttons for items
btn_hamburger = tk.Button(left_frame, text="Hamburger", width=15, command=lambda: add_to_receipt("Hamburger", 2.00))
btn_hamburger.pack(pady=5)

btn_fries = tk.Button(left_frame, text="Fries", width=15, command=lambda: add_to_receipt("Fries", 1.50))
btn_fries.pack(pady=5)

btn_pop = tk.Button(left_frame, text="Pop", width=15, command=lambda: add_to_receipt("Pop", 1.00))
btn_pop.pack(pady=5)

btn_kebab = tk.Button(left_frame, text="Kebab", width=15, command=lambda: add_to_receipt("Kebab", 3.00))
btn_kebab.pack(pady=5)

btn_hotdog = tk.Button(left_frame, text="Hot Dog", width=15, command=lambda: add_to_receipt("Hot Dog", 2.00))
btn_hotdog.pack(pady=5)

# Button to show total for the current transaction
btn_total = tk.Button(left_frame, text="Tabulate", width=15, command=show_total, bg="#ff5533", fg="white")
btn_total.pack(pady=10)

# Label and entry for amount paid
tk.Label(left_frame, text="Amount Paid").pack(pady=5)
amount_paid_entry = tk.Entry(left_frame, width=15)
amount_paid_entry.pack(pady=5)

# Button to save the transaction to CSV and clear the receipt
btn_save = tk.Button(left_frame, text="Save Transaction", width=15, command=save_transaction)
btn_save.pack(pady=10)

# Create the CSV file with headers (if not already created)
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date & Time", "Item", "Price"])
    writer.writerow([])  # Blank line for spacing

# Run the application
root.mainloop()