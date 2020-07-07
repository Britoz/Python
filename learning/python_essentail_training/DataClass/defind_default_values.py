
from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20, 40))

@dataclass
class Book:
    # you can define dafault values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func) # can using default for normal default value



b1 = Book("title 1", "author 1", 12)
b2 = Book("title 2", "author 2", 23)

print(b1)
print(b2)