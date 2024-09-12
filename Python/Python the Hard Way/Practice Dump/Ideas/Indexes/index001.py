# Initial dictionary to store items and their prices
item_prices = {
    "apple": 1.2,
    "banana": 0.5,
    "milk": 2.5,
    "bread": 1.8,
    "eggs": 3.0,
    "rice": 10.0,
    "chicken": 7.5,
    "cheese": 4.0,
    "pasta": 2.2,
    "tomatoes": 1.5,
    "onions": 1.0,
    "carrots": 1.3,
    "butter": 2.8,
    "yogurt": 1.6,
    "coffee": 5.0,
    "tea": 3.2
}

# Function to add items and their prices
def add_item():
    item = input("Enter the item name: ").lower()
    price = float(input(f"Enter the price for {item}: $"))
    item_prices[item] = price
    print(f"{item} has been added with a price of ${price}.")

# Function to check the price of an item
def check_price():
    item = input("Enter the item name to check the price: ").lower()
    if item in item_prices:
        print(f"The price of {item} is: ${item_prices[item]}")
    else:
        print(f"{item} is not available in the system.")

# Example usage
while True:
    print("\nChoose an option:")
    print("1. Add a new item")
    print("2. Check the price of an item")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        check_price()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please select again.")