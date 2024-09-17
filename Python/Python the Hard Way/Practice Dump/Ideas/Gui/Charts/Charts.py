import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Simulate minute-by-minute data for the past hour
now = datetime.now()
minutes = pd.date_range(end=now, periods=60, freq='T')
usage = [random.randint(100, 500) for _ in range(len(minutes))]  # Random data for example

# Convert simulated data to pandas DataFrame
df = pd.DataFrame({'Time': minutes, 'Usage': usage})
df.set_index('Time', inplace=True)

# Function to plot the data
def plot_data():
    fig, ax = plt.subplots()
    df.plot(ax=ax)
    ax.set_title('Internet Usage Over Time')
    ax.set_xlabel('Time')
    ax.set_ylabel('Usage (MB)')
    plt.xticks(rotation=45)
    return fig

# Function to update the plot in the GUI
def update_plot():
    # Simulate new data point
    new_time = df.index[-1] + timedelta(minutes=1)
    new_usage = random.randint(100, 500)
    global df
    new_data = pd.DataFrame({'Time': [new_time], 'Usage': [new_usage]})
    new_data.set_index('Time', inplace=True)
    df = pd.concat([df, new_data])
    df = df.tail(60)  # Keep only the last 60 minutes of data

    fig = plot_data()
    canvas.figure = fig
    canvas.draw()
    root.after(60000, update_plot)  # Schedule to update every minute

# Create the main application window
root = tk.Tk()
root.title("Minute-by-Minute Internet Usage Tracker")

# Create a frame for the plot
plot_frame = ttk.Frame(root)
plot_frame.pack(fill=tk.BOTH, expand=True)

# Create the plot and add it to the frame
fig = plot_data()
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Start the update loop
root.after(60000, update_plot)  # Initial call to start updating every minute

# Run the application
root.mainloop()
