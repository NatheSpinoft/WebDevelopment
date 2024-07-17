import sys

# Ensure that at least four arguments are provided (including the script name itself)
if len(sys.argv) < 4:
    print("Usage: python script.py <first_variable> <second_variable> <third_variable>")
    sys.exit(1)

# Assign command-line arguments to variables
script = sys.argv[0]
first = sys.argv[1]
second = sys.argv[2]
third = sys.argv[3]

# Print out the values
print "The first script is called", script
print "Your first variable is", first
print "Your second variable is", second
print "Your third variable is", third
