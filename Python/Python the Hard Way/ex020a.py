from sys import argv 
import sys

script, inputfile = argv

def print_all(foo):
    print(foo.read())

def print_seek(foo):
    user_input = input("Enter a number of bytes> ")
    foo.seek(user_input)

with open(inputfile) as current_file:
    print_seek (current_file)
    print_all(current_file)