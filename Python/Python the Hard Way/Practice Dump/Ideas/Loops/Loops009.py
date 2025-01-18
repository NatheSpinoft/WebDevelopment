# Example: Checking for even numbers that are either multiples of 4 or 6
for i in range(1, 21):
    if i % 2 == 0 and (i % 4 == 0 or i % 6 == 0):
        print(f"{i} is even and is also a multiple of 4 or 6")
