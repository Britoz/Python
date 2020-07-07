

def main():
    # use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]

    # TODO: any will return true if any of the sequence values are true
    print(any(list1))
    '''
    using any(array) to check if any element in the array difference than false
    '''

    # TODO: all will return true only if all values are true
    print(all(list1))
    '''
    all(array) used to check whether all of the elements in array are true (!=0)
    '''

    # TODO: min and max will return minimum and maximum values in a sequence
    print("min: ", min(list1))
    print("max: ", max(list1))

    # TODO: use sum() to sum up all of the values in a sequence
    print("sum: ", sum(list1))


if __name__ == '__main__':
    main()