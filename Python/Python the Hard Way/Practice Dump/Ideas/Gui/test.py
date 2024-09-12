import tkinter as tk

# Function to add items to the receipt
def add_to_receipt(item, price):
    receipt.insert(tk.END, f"{item}: ${price:.2f}\n")

# Create the main window
root = tk.Tk()
root.title("Simple Menu")

# Left Frame for buttons
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Right Frame for receipt text box
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Buttons for Hamburger, Fries, and Pop
btn_hamburger = tk.Button(left_frame, text="Hamburger", width=15, command=lambda: add_to_receipt("Hamburger", 2.00))
btn_hamburger.pack(pady=5)

btn_fries = tk.Button(left_frame, text="Fries", width=15, command=lambda: add_to_receipt("Fries", 1.50))
btn_fries.pack(pady=5)

btn_pop = tk.Button(left_frame, text="Pop", width=15, command=lambda: add_to_receipt("Pop", 1.00))
btn_pop.pack(pady=5)

# Text box for receipt printout
receipt = tk.Text(right_frame, width=30, height=10, borderwidth=2, relief="solid")
receipt.pack()

# Run the application
root.mainloop()