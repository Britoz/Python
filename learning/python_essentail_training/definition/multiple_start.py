

class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"

class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        # TODO: it will looking from A to B, you can swap A and B in class line and can see more
        print(self.name)

c = C()
c.showprops()
# TODO: double check the priority by using
print(C.__mro__)