import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <arg1> <arg2>")
    sys.exit(1)

script_name = sys.argv[0]
arg1 = sys.argv[1]
arg2 = sys.argv[2]

print("Script name: {}".format(script_name))
print("Argument 1: {}".format(arg1))
print("Argument 2: {}".format(arg2))
