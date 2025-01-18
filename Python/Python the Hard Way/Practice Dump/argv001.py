import sys

#Calculation
def celsius_to_fahrenheit(celsius):
    return (celsius * 5/9) + 32

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Usage: python script_name.py <celsius>")
        sys.exit(1)

    try:
        celsius = float(sys.argv[1])
    except ValueError:
        print("Please enter a valid number for celsius.")
        sys.exit(1)

Fahrenheit = celsius_to_fahrenheit(celsius)

print('The conversion is: ', Fahrenheit)