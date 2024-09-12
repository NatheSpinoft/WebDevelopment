def Pounds_to_kilograms(a):
    return a * 2.2

def Kilograms_to_pounds(a):
    return a / 2.2

def Pounds_to_stones(a):
    return a * 14

def Stones_to_pounds(a):
    return a / 14

def Grams_to_ounces(a):
    return a / 28.35

def Ounces_to_grams(a):
    return a * 28.35

def Weighing():
    while True:
        print ("\nSelect an option")
        print ("1. Pounds to kilograms")
        print ("2. Kilograms to pounds")
        print ("3. Pounds to stones")
        print ("4. Stones to pounds")
        print ("5. Grams to ounces")
        print ("6. Ounces to grams")
        print ("7. Quit")

        User_input = raw_input("Choose [1] [2] [3] [4] [5] [6] [7]>")

        if User_input == "7":
            print ("Application closed")
            break
        
        if User_input in ["1", "2", "3", "4", "5", "6"]:
            num1 = float(input("Pounds: "))

            if User_input == "1":
                print ("%d pounds into kilograms is %d") % (num1, Pounds_to_kilograms(num1))
            elif User_input == "2":
                print ("%d Kilograms to pounds is %d") % (num1, Kilograms_to_pounds(num1))
            elif User_input == "3":
                print ("%d Pounds to stones is %d") % (num1, Pounds_to_stones(num1))
            elif User_input == "4":
                print ("%d Stones to pounds is %d") % (num1, Stones_to_pounds(num1))
            elif User_input == "5":
                print ("%d Grams to ounces is %d") % (num1, Grams_to_ounces(num1))
            elif User_input == "6":
                print ("%d Ounces to grams is %d") % (num1, Ounces_to_grams(num1))
            else:
                print("Choose another number")

if __name__ == "__main__":
    Weighing()