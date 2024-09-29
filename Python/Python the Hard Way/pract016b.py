from sys import argv

# creating a file to open and write into a text

script, filename = argv

target = open(filename,"w")

input_var = raw_input("> ")

target.write(input_var)

target.close()
