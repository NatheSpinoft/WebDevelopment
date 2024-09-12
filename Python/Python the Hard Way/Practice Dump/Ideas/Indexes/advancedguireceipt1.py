import tkinter as tk
from tkinter import messagebox

# Create a dictionary to store items and their prices
item_prices = {
    "apple": 1.20,
    "banana": 0.55,
    "milk": 2.50,
    "bread": 1.80,
    "eggs": 3.00,
    "rice": 10.00,
    "chicken": 7.50,
    "cheese": 4.05,
    "pasta": 2.25,
    "tomatoes": 1.55,
    "onions": 1.00,
    "carrots": 1.35,
    "butter": 2.80,
    "yogurt": 1.60,
    "coffee": 5.00,
    "tea": 3.20
}

# Cart to store selected items
cart = []

# Function to add an item and its price
def add_item():
    item = entry_item.get().lower()
    try:
        price = float(entry_price.get())
        item_prices[item] = price
        update_item_list()
        messagebox.showinfo("Success", f"{item} has been added with a price of ${price}.")
        entry_item.delete(0, tk.END)
        entry_price.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid price.")

# Function to update the displayed list of items and their prices
def update_item_list():
    listbox_items.delete(0, tk.END)
    for item, price in item_prices.items():
        listbox_items.insert(tk.END, f"{item.capitalize()}: ${price}")

# Function to add items to the cart
def add_to_cart():
    item = entry_cart_item.get().lower()
    if item in item_prices:
        cart.append(item)
        update_cart()
        messagebox.showinfo("Success", f"{item} has been added to the cart.")
    else:
        messagebox.showerror("Error", f"{item} is not available.")
    entry_cart_item.delete(0, tk.END)

# Function to update the displayed cart
def update_cart():
    listbox_cart.delete(0, tk.END)
    total = 0
    for item in cart:
        price = item_prices[item]
        listbox_cart.insert(tk.END, f"{item.capitalize()}: ${price}")
        total += price
    label_total.config(text=f"Total: ${total:.2f}")

# Function to generate receipt
def generate_receipt():
    if not cart:
        messagebox.showerror("Error", "The cart is empty.")
        return

    receipt = "Receipt:\n"
    total = 0
    for item in cart:
        price = item_prices[item]
        receipt += f"{item.capitalize()}: ${price}\n"
        total += price
    receipt += f"\nTotal: ${total:.2f}"

    # Display the receipt in a new window
    receipt_window = tk.Toplevel(root)
    receipt_window.title("Receipt")
    receipt_label = tk.Label(receipt_window, text=receipt, justify=tk.LEFT)
    receipt_label.pack(padx=10, pady=10)

# Create the main window
root = tk.Tk()
root.title("Cashier System")

# Create two frames for side-by-side layout
frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# ----- Left side: Add items and Cart -----

# Add Item Section
frame_add = tk.Frame(frame_left)
frame_add.pack(pady=10)

label_item = tk.Label(frame_add, text="Item Name:")
label_item.grid(row=0, column=0, padx=5)

entry_item = tk.Entry(frame_add)
entry_item.grid(row=0, column=1, padx=5)

label_price = tk.Label(frame_add, text="Item Price:")
label_price.grid(row=1, column=0, padx=5)

entry_price = tk.Entry(frame_add)
entry_price.grid(row=1, column=1, padx=5)

button_add = tk.Button(frame_add, text="Add Item", command=add_item)
button_add.grid(row=2, columnspan=2, pady=5)

# Add to Cart Section
frame_cart = tk.Frame(frame_left)
frame_cart.pack(pady=10)

label_cart_item = tk.Label(frame_cart, text="Add Item to Cart:")
label_cart_item.grid(row=0, column=0, padx=5)

entry_cart_item = tk.Entry(frame_cart)
entry_cart_item.grid(row=0, column=1, padx=5)

button_cart_add = tk.Button(frame_cart, text="Add to Cart", command=add_to_cart)
button_cart_add.grid(row=1, columnspan=2, pady=5)

# Cart and Total Price
frame_cart_list = tk.Frame(frame_left)
frame_cart_list.pack(pady=10)

label_cart = tk.Label(frame_cart_list, text="Cart:")
label_cart.grid(row=0, column=0)

listbox_cart = tk.Listbox(frame_cart_list, width=30, height=10)
listbox_cart.grid(row=1, column=0)

label_total = tk.Label(frame_cart_list, text="Total: $0.00")
label_total.grid(row=2, column=0, pady=5)

# Button to Generate Receipt
button_receipt = tk.Button(frame_cart_list, text="Generate Receipt", command=generate_receipt)
button_receipt.grid(row=3, column=0, pady=5)

# ----- Right side: List of Items and Prices -----

frame_list = tk.Frame(frame_right)
frame_list.pack(pady=10)

label_list = tk.Label(frame_list, text="Items and Prices:")
label_list.pack()

listbox_items = tk.Listbox(frame_list, width=30, height=20)
listbox_items.pack()

update_item_list()  # Display the initial list of items

# Start the GUI event loop
root.mainloop()