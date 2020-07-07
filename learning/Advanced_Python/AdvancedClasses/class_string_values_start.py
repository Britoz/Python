# Demonstrate using of class string values

class Person():
    def __init__(self):
        self.fname = "vinh"
        self.lname = "Lee"
        self.age = 25

    def __repr__(self):
        return "<Person Class - fname:{0}, lname{1}, age:{2}>".format(self.fname, self.lname, self.age)

    def __str__(self):
        return "Person ({0} {1} is {2})".format(self.fname, self.lname, self.age)

    # TODO: function used to hole the
    def __bytes__(self):
        val = "Persom: {0},{1},{2}".format(self.fname, self.lname, self.age)

def main():
    # create a new person objects
    cls1 = Person()


    # use different Python function to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    print("Formatted: {0}".format(cls1))

if __name__ == '__main__':
    main()