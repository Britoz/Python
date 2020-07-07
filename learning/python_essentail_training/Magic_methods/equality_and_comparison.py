

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method checks for equality between two objects
    def __eq__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare book to a non-book")
        return (self.title == other.title and
                self.author == other.author and
                self.price == other.price)

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare book to a non-book")

        return self.price >= other.price

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare book to a non-book")

        return self.price < other.price



b1 = Book("Title 1", "Author 1", 1)
b11 = Book("Title 1", "Author 1", 1)
b2 = Book("Title 2", "Author 2", 2)
b3 = Book("Title 3", "Author 3", 3)
b4 = Book("Title 4", "Author 4", 4)


# TODO: Check for equality
# print(b1 == b11) # RESULE: False, __eq__ make it become true
# print(b1 == b2) # false
# print(b1 == 2) # non-book comparation

# TODO: Check for greater and lesser value
print(b2 >= b1)
print(b2 < b1)

# TODO: Now we can sort them too
books = [b1, b3, b2 ,b4]
books.sort()
# print only the title as a list
print([book.title for book in books])