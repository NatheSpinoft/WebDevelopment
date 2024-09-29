def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # Yield the current count
        count += 1   # Increment count

val = input("> ")

# Using the generator
for number in count_up_to(val):
    print(number)
