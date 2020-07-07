class Book:
    # TODO: properties defined at the class level are shared by all instance
    BOOK_TYPES = ("novel", "horro", "comedy")

    # TODO: private variable is declare by double underscore
    __booklist = None

    # TODO: create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # TODO: using static method to access the private variable
    @staticmethod
    def getBooklist():
        if Book.__booklist == None:
            # TODO: if the booklist is None, we create a new one
            Book.__booklist = []
        return Book.__booklist

    def setTitle(self, newTitle):
        self.title = newTitle

    def __init__(self, title, booktype):
        self.title = title

        if not booktype in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not a valid booktype")
        else:
            self.booktype = booktype

# TODO: access the class attribute
print("Book types: ", Book.getbooktypes())

# TODO: Create some book instances
b1 = Book("Title 1", "novel")
b2 = Book("Title 2", "horro")

# TODO: use the static method to acces a singleton object
thebook = Book.getBooklist()
thebook.append(b1)
thebook.append(b2)
print(thebook)