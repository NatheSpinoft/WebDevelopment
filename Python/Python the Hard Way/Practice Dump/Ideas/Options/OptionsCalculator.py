#! /usr/bin/python

def Adding (a, b):
    return a + b

def Subtracting (a, b):
    return a - b

def Multiplication (a, b):
    return a * b

def Division (a, b):
    if a != 0:
        return a / b
    else:
        return "Error"

def calculator():
    while True:
        print("\nSelect operation")
        print("1. Add")
        print("2. Subtracting")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        user_input = input("Enter an option (1/2/3/4/5)")

        if user_input == '5':
            print ('Exiting calculator')
            break

        if user_input in ['1', '2', '3', '4']:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if user_input == '1':
                print("The sum of %d and %d is" % (num1, num2))
                print(Adding(num1, num2))
            elif user_input == '2':
                print("The remainder of %d and %d is" % (num1, num2))
                print(Subtracting(num1, num2))
            elif user_input == '3':
                print("The product of %d and %d is" % (num1, num2)) 
                print(Multiplication(num1, num2))
            elif user_input == '4':
                print("The quotient of %d and %d" % (num1, num2)) 
                print(Division(num1, num2))
            else:
                print ('Choose another number')

if __name__ == "__main__":
    calculator()