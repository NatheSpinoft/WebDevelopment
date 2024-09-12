from sys import argv 

script, filename = argv

# This section below is a disclaimer
print "We're going to erase %r" % filename
print "if you don't want to CTRL C"
print "if you want to hit enter"

# A distracter for the above mentioned
raw_input("?")

# Opening the file with the write funciton
print "Opening the file..."
target = open(filename,"w")

# Delection of contents
print "Truncating the file. Goodbye"
target.truncate()

# The rest writing into the file
print "Now I'm going to ask you three times"

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And we finally close it."
target.close()