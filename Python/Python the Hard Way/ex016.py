from sys import argv 

script, filename = argv

print "We're going to erase %r" % filename
print "if you don't want to CTRL C"
print "if you want to hit enter"

raw_input("?")

print "Opening the file..."
target = open(filename,"w")

print "Truncating the file. Goodbye"
target.truncate()

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