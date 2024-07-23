import datetime

# Current datetime
now = datetime.datetime.now()
print("Current Datetime:", now)

# Convert datetime to timestamp
timestamp = now.timestamp()
print("Timestamp:", timestamp)

# Convert timestamp back to datetime
dt_from_timestamp = datetime.datetime.fromtimestamp(timestamp)
print("Datetime from Timestamp:", dt_from_timestamp)
