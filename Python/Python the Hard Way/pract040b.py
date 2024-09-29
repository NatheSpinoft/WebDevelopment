class boring:
    def __init__(self, title, author):
        self.author = author 
        self.title = title
    
    def Books(self):
        print("The book %s is good! it's by %s" % (self.title, self.author ))

