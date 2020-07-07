# advanced iteration functions in the itertools package
import itertools

def testFunction(x):
    return x < 40

def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    '''
    itertools.cycle(array) like an infinitive loop, 
    every time it printed, a next value will be print out and jump to next value,
    when index = n - 1, the next value will come back to index = 0
    '''


    # TODO: use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    '''
    using itertools.count(beginning number, increase number)
    the number will start by the beginning number and increase by the increase number
    '''


    # TODO: accumulate creates an iterator that accumulates values
    vals = [10, 20, 10, 40, 50 ,40 , 30]
    # acc = itertools.accumulate(vals, max)
    # print(list(acc))
    '''
    itertools.accumulate(array) is used to calculate with the fomular of
    next value equals to sum of all element before it include itself
    
    itertools.accumulate(array, max) is used to generate the array again with
    whenever index move to the maximum value, if next value is not bigger than current
    it will keep the max value
    '''

    # TODO: use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x))
    '''
    like mix both array to 1 big array
    '''

    # TODO: dropwhile and takewhile will return values until

    # a certain condition is met that stops them
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))
    '''
    dropwhile() drop value from the sequence while testFunction return true, then 
    return all the value after that
    
    takewhile returns value from the sequence while the predicate function returns true,
    and then it will stop giving you values
    '''


if __name__ == '__main__':
    main()