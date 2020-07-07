

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: the __call__ method can be used to call the object like a function
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

b1 = Book("title 1", "author 1", 1.0)
b2 = Book("title 2", "author 2", 2.0)

# TODO: call the object as if it were a function
print(b1)
b1("title new 1", "author 1", 3.0)
print(b1)