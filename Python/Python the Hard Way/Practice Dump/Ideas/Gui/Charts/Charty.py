import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

# Initialize lists to store data
cpu_data = []
net_data = []
time_data = []

# Function to update CPU and Network data
def update_data(i):
    # Get CPU usage
    cpu = psutil.cpu_percent(interval=1)
    # Get network usage (in bytes)
    net_info = psutil.net_io_counters()
    net_sent = net_info.bytes_sent / 1024  # Convert to KB
    net_recv = net_info.bytes_recv / 1024  # Convert to KB
    
    # Append new data to the lists
    cpu_data.append(cpu)
    net_data.append(net_sent + net_recv)
    time_data.append(datetime.now().strftime('%H:%M:%S'))
    
    # Keep only the last 60 data points (for 1 minute of monitoring)
    if len(cpu_data) > 60:
        cpu_data.pop(0)
        net_data.pop(0)
        time_data.pop(0)
    
    # Clear the plots and plot new data
    ax1.clear()
    ax2.clear()

    # Set black background and green text/lines
    ax1.set_facecolor('black')
    ax2.set_facecolor('black')
    fig.patch.set_facecolor('black')

    ax1.spines['bottom'].set_color('green')
    ax1.spines['top'].set_color('green') 
    ax1.spines['right'].set_color('green')
    ax1.spines['left'].set_color('green')

    ax2.spines['bottom'].set_color('green')
    ax2.spines['top'].set_color('green') 
    ax2.spines['right'].set_color('green')
    ax2.spines['left'].set_color('green')

    ax1.tick_params(axis='x', colors='green')
    ax1.tick_params(axis='y', colors='green')
    ax2.tick_params(axis='x', colors='green')
    ax2.tick_params(axis='y', colors='green')

    # Plot CPU usage
    ax1.plot(time_data, cpu_data, label='CPU Usage (%)', color='green')
    ax1.set_ylim(0, 100)  # CPU usage is from 0 to 100%
    ax1.set_ylabel('CPU Usage (%)', color='green')
    ax1.legend(loc="upper left", fontsize=8, facecolor='black', edgecolor='green')

    # Plot Internet usage (sum of bytes sent and received)
    ax2.plot(time_data, net_data, label='Internet Usage (KB)', color='green')
    ax2.set_ylabel('Internet Usage (KB)', color='green')
    ax2.legend(loc="upper left", fontsize=8, facecolor='black', edgecolor='green')

    # Rotate X-axis labels for readability
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha="right", color='green')
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha="right", color='green')

    # Display only the first and last time on the X-axis
    if len(time_data) > 1:
        ax1.set_xticks([0, len(time_data) - 1])
        ax1.set_xticklabels([time_data[0], time_data[-1]], color='green')

        ax2.set_xticks([0, len(time_data) - 1])
        ax2.set_xticklabels([time_data[0], time_data[-1]], color='green')

# Set up the figure and two subplots (one for CPU, one for network)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(4, 3), dpi=100)  # Smaller screen size

# Add more space between the charts
plt.subplots_adjust(hspace=2.5)  # Adjust vertical space between charts

# Animate the plot, updating every second
ani = animation.FuncAnimation(fig, update_data, interval=1000)  # 1 second intervals

# Display the plot
plt.show()
