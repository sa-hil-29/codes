class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")

book = Book('Python Rocks','Jose',200)
print(str(book))
print(len(book))
del book
print(str(book))
        
