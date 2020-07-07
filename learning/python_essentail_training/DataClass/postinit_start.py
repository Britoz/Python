

# TODO:only work on 3.7 or later

from dataclasses import dataclass

@dataclass
class Book:
    title : str
    author : str
    pages : int
    price : float

    # TODO: the __post_init__
    # after the object has been init
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"

# create some instances
b1 = Book("title 1", "author 1", 12, 1.0)
b2 = Book("title 2", "author 2", 23, 2.0)

print(b1.description)
print(b2.description)