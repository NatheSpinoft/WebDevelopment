import datetime
import calendar

# Get the current datetime
now = datetime.datetime.now()

# Format the datetime object into a human-readable string
human_readable = now.strftime("%Y-%m-%d %H:%M:%S.%f")
print("Current Timestamp", human_readable)

import platform
import subprocess

def get_system_profiler_data(data_type):
    try:
        output = subprocess.check_output(["system_profiler", data_type])
        return output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return str(e)
    
# Function to print system profiler output with each key-value pair on a new line
def print_system_profiler_output(data_type):
    data = get_system_profiler_data(data_type)
    lines = data.strip().split("\n")
    for line in lines:
        print(line)

# Basic OS information using platform module
os_name = platform.system()
os_version = platform.version()
os_release = platform.release()
os_full = platform.platform()

print("Operating System:", os_name)
print("OS Version:", os_version)
print("OS Release:", os_release)
print("Full OS Description:", os_full)

# Detailed information using system_profiler
print("\nFetching detailed system information...\n")

# Example usage:
print("System Overview:")
print_system_profiler_output("SPSoftwareDataType")

print("\nHardware Information:")
print_system_profiler_output("SPHardwareDataType")

print("\nOS Information:")
print_system_profiler_output("SPSoftwareDataType")
