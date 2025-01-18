fruit = ['apple', 'orange', 'peach', 'tangerine', 'banana']
vegetables = ['tomato', 'lettuce', 'cucumber', 'pickles', 'raddish']

print("1. first position")
print("\t {}".format(fruit[0]))
print("2. Last position")
print("\t {}".format(fruit[-1]))
print("3. Join lists ")
perishables = fruit + vegetables
print("\t {}".format(perishables))
print("4. String with list")
print(" You should eat " + ", ".join(fruit))
