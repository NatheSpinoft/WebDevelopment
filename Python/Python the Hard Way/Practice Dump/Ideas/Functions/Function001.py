from sys import argv 

script, a, b = argv

def calculator(a, b):
    a = int(a)
    b = int(b)
    
    print(a + b)

calculator(a, b)