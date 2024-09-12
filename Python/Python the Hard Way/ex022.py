#! /usr/bin/python

print "Enter a number that would represent a float"
Float = float(input(">"))

print "Enter a number that would represent an integer"
Integer = int(input(">"))

def add(a, b):
    return a + b

Result = add(Float, Integer)
print """
\t The number for float is %r and the number for integer
is %r. The result is %r. \n
\t\t That is all folks. \b\b 
""" % (Float, Integer, Result)