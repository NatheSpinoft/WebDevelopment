# Nested 

list1 = [1, 2, 3]
list2 = [4, 5, 6]

for i in list1:
    for j in list2:
        if (i * j) % 2 == 0:
            print(f"The product of {i} and {j} is even: {i * j}")
        else:
            print(f"The product of {i} and {j} is odd: {i * j}")
