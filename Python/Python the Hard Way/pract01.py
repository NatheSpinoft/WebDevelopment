#Practice of everyone I know
from sys import argv

script, file_in = argv

print "This is the way!"
print "The file %r will be assessed" % file_in

target = open(file_in)

print target.read()
