import datetime
import calendar

# Get the current datetime
now = datetime.datetime.now()

# Format the datetime object into a human-readable string
human_readable = now.strftime("%Y-%m-%d %H:%M:%S.%f")
print("Current Timestamp", human_readable)
