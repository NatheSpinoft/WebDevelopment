import sys

if len(sys.argv) < 2:
    print "Usage: script.py arg1"
    sys.exit(1)

script = sys.argv[0]
var1 = sys.argv[1]

print "There is something called", var1

