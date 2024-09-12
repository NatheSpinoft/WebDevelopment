import tkinter as tk
import time
import math

def update_clock():
    # Get the current time
    now = time.localtime()
    seconds = now.tm_sec
    minutes = now.tm_min
    hours = now.tm_hour % 12  # Convert to 12-hour format

    # Calculate angles for the clock hands
    sec_angle = math.radians((seconds / 60) * 360)
    min_angle = math.radians((minutes / 60) * 360 + (seconds / 60) * 6)
    hour_angle = math.radians((hours / 12) * 360 + (minutes / 60) * 30)

    # Update second hand
    canvas.coords(sec_hand, 200, 200, 
                  200 + 100 * math.sin(sec_angle), 
                  200 - 100 * math.cos(sec_angle))

    # Update minute hand
    canvas.coords(min_hand, 200, 200, 
                  200 + 80 * math.sin(min_angle), 
                  200 - 80 * math.cos(min_angle))

    # Update hour hand
    canvas.coords(hour_hand, 200, 200, 
                  200 + 60 * math.sin(hour_angle), 
                  200 - 60 * math.cos(hour_angle))

    # Schedule the update_clock function to be called again after 1000ms (1 second)
    root.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.title("Analog Clock")

# Create a canvas to draw the clock
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Draw the clock face (circle)
canvas.create_oval(50, 50, 350, 350, outline="black", width=2)

# Draw hour markers
for i in range(12):
    angle = math.radians(i * 30)
    x = 200 + 140 * math.sin(angle)
    y = 200 - 140 * math.cos(angle)
    canvas.create_text(x, y, text=str(i if i != 0 else 12), font=('Helvetica', 16))

# Initialize clock hands
sec_hand = canvas.create_line(200, 200, 200, 100, fill='red', width=1)
min_hand = canvas.create_line(200, 200, 200, 120, fill='blue', width=2)
hour_hand = canvas.create_line(200, 200, 200, 140, fill='black', width=4)

# Start the clock
update_clock()

# Run the main event loop
root.mainloop()
