def add(a, b):
    print "ADDING %d and %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d and %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d and %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d and %d" % (a, b)
    return a / b


print "Let's do some math!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "age %d, height %d, weight %d, iq %d" %(age, height, weight, iq)


#more of a puzzle
print "Here is a puzzle"

what = add(age,subtract(height, multiply(weight, divide(iq,2))))

print "That becomes", what, "Can you do this" 