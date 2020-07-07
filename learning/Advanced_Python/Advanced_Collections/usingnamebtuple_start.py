# Demonstrate the usage of namdtuple objects
import collections

def main():
    # TODO: create a Point namedtuple
    Point = collections.namedtuple("Point", "x y z d")
    '''
    collections.namedtuple(name, value)
    value can have various variable "x y"
    '''
    p1 = Point(10, 20, 30, 10)
    p2 = Point(30, 40, 30, 10)
    print(p1, p2)
    print(p1.x, p2.y)

    # TODO: use _replace to create a new instance
    p1 = p1._replace(x=100)
    print(p1)
    '''
    _replace used to change the value on the top variable
    '''

if __name__ == '__main__':
    main()