# Demonstrate the use of function docstrings

def myFunction(arg1, arg2=None):
    """
    myFunction: does not really do anything, just prints

    :parameter:

    :param arg1: the first argument. Whatever you feel like passing.
    :param arg2: second argument. Defaults to None.
    :return:
    """
    print(arg1, arg2)

def main():
    print(myFunction.__doc__)

if __name__ == '__main__':
    main()