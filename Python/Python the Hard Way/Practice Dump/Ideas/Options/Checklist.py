from datetime import datetime

product_list = []

should_continue = "yes"

while should_continue == "yes":
    print("Enter product details")
    
    Product_name = input("Enter product name: ")
    Model_number = input("Enter model number: ")

    while True:
        Date_returned = input("Enter date returned (YYYY-MM-DD): ")
        try: # try to parse the date string 
            valid_date = datetime.strptime(Date_returned, "%Y-%m-%d")
            break #exit if the date is valid
        except ValueError:
            print("Invalid date Enter (YYYY-MM_DD)")
    product_tuple = Product_name, Model_number, Date_returned

    product_list.append(product_tuple)

    should_continue = input("Do you want to add another? (yes,no)").strip().lower()

    if should_continue == "no":
        break
    

print("Product details entered: ")   
for product in product_list:
    print(product)