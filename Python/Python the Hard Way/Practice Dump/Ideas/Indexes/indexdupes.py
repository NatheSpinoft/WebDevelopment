#!/user/bin/python3

Fruit_list = ["apple", 'apple', 'banana', 'pear', 'pear']

def duplicates(fruit_list):
    item_count = {}
    for fruit in fruit_list:
        if fruit in item_count:
            item_count[fruit] += 1
        else:
            item_count[fruit] = 1
    
    for fruit, count in item_count.items():
        if count == 1:
            print("%s unique item" % fruit)


duplicates(Fruit_list)