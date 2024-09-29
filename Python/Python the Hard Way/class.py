class Dog:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    def bark(self):      # Method
        print("%s says Woof!") % self.name

# Creating an instance (object) of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing attributes and methods
print(my_dog.name)  # Output: Buddy
my_dog.bark()       # Output: Buddy says Woof!
