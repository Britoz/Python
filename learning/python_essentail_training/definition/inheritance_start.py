class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.pages = pages
        self.author = author

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)

class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)

b1 = Book("first one", "Vinh", 1, 2)
n1 = Newspaper("newspaper 1", "Lee",12, "daily")
m1 = Magazine("magazine 1", "V", 32, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, n1.price, m1.price)