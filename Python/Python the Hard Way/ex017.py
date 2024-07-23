from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do this in two files in one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit enter to return, or CTRL C to abort"
raw_input()

out_file = open(to_file,"w")
out_file.write(indata)

print "Alright, done"

out_file.close()
in_file.close()