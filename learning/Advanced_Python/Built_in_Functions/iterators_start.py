
# use iterator functions like enumerate, zip, iter, next

def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Web", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection
    """i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))"""

    # TODO: iterate using a function and a sentinel
    """with open("testfile.txt", "r") as fb:
        # TODO: using loop to read each line in the file and print it out
        for line in iter(fb.readline, ''):
            print(line)"""

    # TODO: use regular interation over the days
    # for m in range(len(days)):
    #    print(m+ 1, days[m])


    # TODO: using enumerate reduces code and provides a counter
    # for i, m in enumerate(days, start=1):
    #     print(i, m)

    # TODO: use zip to combine sequences
    # for m in zip(days, daysFr):
    #    print(m)
    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], "=", m[1], "in French")

    '''
    by using enumerate(array, start index) you will have the start index with 
    difference than 0
    
    zip(array1, array2) will used to combine 2 sequences
    
    i is the index
    m is the array value -> m[0] is the first element of array input
    '''

if __name__ == '__main__':
    main()