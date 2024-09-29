class Dog:
    # __init__ is the constructor that initializes an object
    def __init__(self, name, breed):
        # These are instance variables (attributes)
        self.name = name
        self.breed = breed

    # Method that outputs the dog's name and breed
    def describe(self):
        print("This dog's name is %s and it is a %s.") % (self.name, self.breed)

# Creating an object of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")

# Accessing the object's attributes and methods
print(my_dog.name)  # Output: Buddy (object attribute)
print(my_dog.breed)  # Output: Golden Retriever (object attribute)

# Calling the describe method of the object
my_dog.describe()  # Output: This dog's name is Buddy and it is a Golden Retriever.
