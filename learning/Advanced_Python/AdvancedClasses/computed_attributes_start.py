# demonstrate Computed attributes

class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100


    # TODO: use getattr to dynamically return a value
    def __getattr__(self, item):
        if item == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif item == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(
                self.red,
                self.green,
                self.blue
            )
        else:
            raise AttributeError
    '''
    used whenever called as 
    myColor.rgbcolor -> work as an attribute of class
    
    :02x -> 2 characters hex string
    0: 1: 2: are the index of format value
    '''

    # TODO: use setattr to dynamically return a value
    def __setattr__(self, key, value):
        if key == "rbgcolor":
            self.red = value[0]
            self.green = value[1]
            self.blue = value[2]
        else:
            super().__setattr__(key,value)

    # TODO: use dir to list the available properties
    def __dir__(self):
        return ("red", "green", "blue","rgbcolor", "hexcolor")


def main():
    # create an instance of myColor
    cls1 = myColor()


    # TODO: print the value of a computed attribute
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    # TODO: set the value of a computed attribute
    print("after set new value")
    cls1.rgbcolor = (255, 200, 111)
    print(cls1.rgbcolor)

    # TODO: access a regular attribute
    print(cls1.red)

    # TODO: list the available attributes
    print(dir(cls1))


if __name__ == '__main__':
    main()