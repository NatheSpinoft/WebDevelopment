#

class History():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

        print("The title is %s, author %s and year %s") % (title, author, year)  

class Math():
    def __init__(self):
        self.num1 = float(input("Enter first number: "))
        self.num2 = float(input("Enter second number: "))
        self.operation = raw_input("Enter in an operation (+) (-) (*) (/): ")
    
    def calculate(self):
        try:
            if self.operation == "+":
                result = self.num1 + self.num2
                print(result)
            elif self.operation == "-":
                result =  self.num1 - self.num2
                print(result)
            elif self.operation == "*":
                result = self.num1 * self.num2
                print(result)
            elif self.operation == "/":
                result = self.num1 / self.num2
                print(result)
            else:
                print("no good choice?")
        except ZeroDivisionError:
            print("Error cannot divide by zero")

def print_books(books):
    for category, book_list in books.items():
        print("\nCategory: {}".format(category))
        for book in book_list:
            print("Title: {}, Author: {}, Year: {} ".format(book['title'], book['author'], book['year']) )


books = {
    'History': [
        {
            'title': '1984',
            'author': 'George Orwell',
            'year': 1949
        },
        {
            'title': 'Sapiens',
            'author': 'Yuval Noah Harari',
            'year': 2011
        }
    ],
    'Math': [
        {
            'title': 'The Joy of x',
            'author': 'Steven Strogatz',
            'year': 2012
        },
        {
            'title': 'Godel, Escher, Bach',
            'author': 'Douglas Hofstadter',
            'year': 1979
        }
    ]
}
History_instance = History("1984", "George Orwell", "1949")

math_instance = Math()
math_instance.calculate()

print_books(books)
