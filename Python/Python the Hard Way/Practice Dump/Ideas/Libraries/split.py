# This file is to understand the use of strip

array = input("Enter a phrase > ")
print("This is what was written '%s'" % array)
print(array.strip().lower())

for arr in array.split():
    print(arr)
