
# TODO: create new class Book with 4 detail

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    '''
    
    :parameter
    title :  title of the book - should be string
    
    
    '''

    # TODO: get price of the object
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    # TODO: discount the money
    def setdiscount(self, amount):
        self._discount = amount

# TODO: create instances of the class
b1 = Book("Hello world", "vinh", 12, 12)
b2 = Book("War and peace","Lee", 1, 3)

print(b1.getprice())

print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())