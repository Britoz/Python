# use transform functions like sorted, filter and map

def filterFunc(x):
    if x % 2 == 0:
        return False
    return True

def filterFunc2(x):
    if x.isupper():
        return False
    return True

def squareFunc(x):
    return x**2

def toGrade(x):
    if x >= 90:
        return "A"
    elif (x >= 80 and x <90):
        return "B"
    elif x >= 70 and x < 80:
        return "C"
    elif x >= 65 and x < 70:
        return "D"
    return "F"

def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: use filter to remove items from a list
    # odds = list(filter(filterFunc, nums))
    # print(odds)
    '''
    used to filter the value from sequence
    filter(func, iterable)
    func: is filterFunc() used to make fomular to filter out the even number
    
    in this sample, filter will used to filter the even number and keep odds
    '''

    # TODO: use filter on nonm-numeric sequence
    # lowers = list(filter(filterFunc2, chars))
    # print(lowers)
    '''
    filterFunc2 is used to filter out all the upper case char
    '''

    # TODO: use map to create a new sequence of values
    # squares = list(map(squareFunc, nums))
    # print(squares)
    '''
    map() is used to map 1 value to another
    '''

    # TODO: use sorted and map to change numbers to grades
    # TODO: sort the array
    grades = sorted(grades)
    letters = list(map(toGrade, grades))
    print(letters)


if __name__ == '__main__':
    main()