# TODO:only work on 3.7 or later

from dataclasses import dataclass

# TODO: using new dataclass (new version 3.7 and later using)
@dataclass
class Book:
    title : str
    author : str
    pages : int
    price : float

    # TODO: print out
    def bookinfo(self):
        return f"{self.title}, by {self.author}, pages {self.pages}, costs {self.price}"

@dataclass
class Notebook(Book):
    id : int



print(s1 == s2)

"""

# create some instances
b1 = Book("title 1", "author 1", 12, 1.0)
b2 = Book("title 2", "author 2", 23, 2.0)
b3 = Book("title 3", "author 3", 43, 3.0)

# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__
# print(b1)


# TODO: comparing two classes - they implement __eq__
# print(b1 == b3)

# TODO: change some fields
b1.title = "Vinh"
b1.pages = 67
print(b1.bookinfo())"""