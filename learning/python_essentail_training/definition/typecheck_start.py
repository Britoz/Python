class Book:
    def __init__(self, title):
        self.title = title

class Newspaper:
    def __init__(self, name):
        self.name = name

b1 = Book("Book 1")
b2 = Book("Book 2")

n1 = Newspaper("Vinh newspaper 1")
n2 = Newspaper("Vinh newspaper 2")

# TODO: use type() to known type of book
print(type(b1))
print(type(b2))


# TODO: use type() to known type of newspaper
print(type(n1))
print(type(n2))

# TODO: use isinstance to compare a specific instance to a known type
print(isinstance(b1, Book))
print(isinstance(b2, Book))

print(isinstance(n2, object))
