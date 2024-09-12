import tkinter as tk
import csv
from datetime import datetime

#initialize the list to store transaction data
items = []
accumulated_total = 0.00
csv_filename = "accumulated_transactions.csv"

#function to add items to the receipt
def add_to_receipt(item, price):
    receipt.insert(tk.END, f'{item:<15} ${price:>5.2f}\n')
    items.append((item, price))


#function to update the total amount in the receipt
def show_total():
    total_amount = sum(price for _, price in items)

    #show total in the receipt
    receipt.insert(tk.END, "-" * 25 +"\n")
    receipt.insert(tk.END, f"{'Total':<15} ${total_amount:>5.2f}\nHave a good day!\n")

def save_and_clear():
    global accumulated_total

    total_amount = sum(price for _, price in items)
    accumulated_total += total_amount

    #appending to file
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        #Write current transaction
        writer.writerow([f"Transaction on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"])
        writer.writerow(["Item", "Price"])
        for item, price in items:
            writer.writerow([item, f"${price:.2}"])
        writer.writerow(["Total", f"${sum(price for _, price in items):.2f}"])
        writer.writerow([])

    #clear the receipt and reset total
    items.clear()
    receipt.delete(1.0, tk.END)
    
#Function to accumulated total
def show_accumulated_total():
    receipt.insert(tk.END, "-" * 25 + "\n")
    receipt.insert(tk.END, f"{'Accumulated Total':<15} ${accumulated_total:>5.2}\n")

    #Save the accumulated total to the CSV
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f"Accumulated total as of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"])
        writer.writerow([f"${accumulated_total:.2f}"])
        writer.writerow([])

#Create the main window
root = tk.Tk()
root.title("Simple Window")

#Layout setup
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

left_frame = tk.Frame(main_frame)
left_frame.pack(side=tk.LEFT, padx=10)

right_frame = tk.Frame(main_frame)
right_frame.pack(side=tk.RIGHT, padx=10)

#Buttons for Hamburger, Fries and Pop
btn_hamburger = tk.Button(left_frame, text = "Hamburger", width=13, command=lambda: add_to_receipt("Hamburger", 2.00))
btn_hamburger.pack(pady=5)

btn_fries = tk.Button(left_frame, text = "Fries", width=13, command=lambda: add_to_receipt("Fries", 1.50))
btn_fries.pack(pady=5)

btn_pop = tk.Button(left_frame, text = "Pop", width=13, command=lambda: add_to_receipt("Pop", 1.00))
btn_pop.pack(pady=5)

#button to show the total
btn_total = tk.Button(left_frame, text="Total", width=10, command=show_total)
btn_total.pack(pady=10)

#button to save transaction and clear the receipt
btn_save_clear = tk.Button(left_frame, text="Save and Clear", width=15, command=save_and_clear)
btn_save_clear.pack(pady=10)

#button to show accumulated total
btn_accumulated_total = tk.Button(left_frame, text="Accumulated Total", width=15, command=show_accumulated_total, bg="red")
btn_accumulated_total.pack(pady=10)

# Text box for receipt printout
receipt = tk.Text(right_frame, width=40, height=15, borderwidth=2, relief="solid")
receipt.pack()

#Create the csv file with headers
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Accumulated total transaction log"])
    writer.writerow([]) #spacing

root.mainloop()