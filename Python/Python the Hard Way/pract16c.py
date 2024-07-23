from sys import argv
import datetime
import calendar

#Opening

script, filename = argv

now = datetime.datetime.now()
dt_from_timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")

line1 = raw_input("Enter: ")

print ("Opening file")
target = open(filename,"a")


target.write(dt_from_timestamp)
target.write(line1)