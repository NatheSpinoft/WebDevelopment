#!/usr/bin/python

Fruit_list = ['apple', 'banana', 'pear', 'apple', 'banana']


def unique(fruit_list):
    #Create a dictionary
    item_count = {}

    #Count each fruit
    for fruit in fruit_list:
        if fruit in item_count:
            item_count[fruit] += 1
        else:
            item_count[fruit] = 1

    for fruit, count in item_count.items():
        if count == 1:
            print(fruit)

unique(Fruit_list)