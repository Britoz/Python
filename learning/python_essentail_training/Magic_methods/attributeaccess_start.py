

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1


    # The __str__ function is used to return a user_friendly string
    # representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: __getattribute__ called when an attr is retrieved. Don't
    # directly access the attr name otherwise a recursive loop is created
    """def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p*d)
        return super().__getattribute__(name)"""
    # TODO: __setattr__ called when an attribute value is set. Don't set
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("The price attr must be a float")
        return super().__setattr__(name, value)
    # TODO: __getattr__ called when __getattribute__ lookup fails
    def __getattr__(self, item):
        return item + " is not here"

b1 = Book("title 1", "author 1", 1.0)
b2 = Book("title 2", "author 2", 2.0)

"""b1.price = float(50)
print(b1)"""
print(b1.randomprop)