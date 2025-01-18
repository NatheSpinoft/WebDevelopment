import tkinter as tk

def button_click(button_text):
    current = display_var.get()
    if button_text == "=":
        try:
            result = eval(current)
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif button_text == "C":
        display_var.set("")
    else:
        display_var.set(current + button_text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Variable to store display value
display_var = tk.StringVar()
display_var.set("")

# Display
display = tk.Entry(root, textvariable=display_var, justify="right", font=("Arial", 18))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row = 1
col = 0
for button_text in buttons:
    tk.Button(root, text=button_text, width=5, height=2, command=lambda text=button_text: button_click(text)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
