import datetime
import calendar

#set datetime & human readable
now = datetime.datetime.now()
human_readable = now.strftime("%Y-%M-%D %H:%M")

product_list = []

should_continue = 'yes'

while should_continue == "yes":
    print("Enter product details: ")
    
    product_name = raw_input("Enter product name: ")
    model_number = raw_input("Enter model number: ")
    date_returned = raw_input("Enter date returned (YYYY-MM-DD): ")

    product_tuple = product_name, model_number, date_returned

    product_list.append(product_tuple) 

    should_continue = input("Do you want to add another product? (yes, no)")   

print("Product details entered: ")
for product in product_list:
    print(product)