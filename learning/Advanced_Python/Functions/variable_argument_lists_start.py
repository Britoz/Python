# Demonstrate the use of variable argument lists

# TODO: define a function that takes variable arguments
def addition(*args):
    """
    addition(*args) : sum of all input argument with unknown number of arguments
    and it is only has 1 list param rather than (base, *args)
    if (base, *args), first param will be missing because it is replace by 'base'

    :param args: list of arguments
    :return: sum of arg
    """
    result = 0
    for arg in args:
        result += arg
    return result

def main():
    # TODO: pass different arguments
    print(addition(5, 10, 15, 20))
    print(addition(25, 10))


    # TODO: pass an existing list
    myNums = [5, 10, 14, 12]

    print(addition(*myNums))
    """
    *myNums: we have addition(*arg) hence we need *arg as param
    """


if __name__ == '__main__':
    main()