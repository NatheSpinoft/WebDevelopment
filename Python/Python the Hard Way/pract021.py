import sys

# Celsius calculation
def Conversion (Celsius):
    return (Celsius * 9 / 5 ) + 32

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Usage: python script_name.py <celsius>")
        sys.exit(1)

    try:
        celsius = float(sys.argv[1])
    except ValueError:
        print("Please enter a valid number for celsius.")
        sys.exit(1)

Fahrenheit = Conversion(celsius)

print 'The conversion is: ', Fahrenheit
