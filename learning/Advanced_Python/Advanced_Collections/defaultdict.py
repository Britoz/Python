# Demonstrate default dictionary
from collections import defaultdict

def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    # fruitCounter = {}
    fruitCounter = defaultdict(int)
    '''
    defaultdict used to create a default value whenever we try to access
    in the not existing key()
    
    by using it, we can ignore the condition to check the existing key()
    
    we can change the default key by defaultdict(lambda: 100)
    and then the default key will start by 100
    '''

    # Count the elements in the list
    for fruit in fruits:
        # TODO: normally we have to check whether the key exists or not
        """if fruit in fruitCounter.keys():
            fruitCounter[fruit] += 1
        else:
            fruitCounter[fruit] = 1"""

        # TODO: instead of using condition to check existing key(), we use defaultdict
        fruitCounter[fruit] += 1

    # print the result
    for (k, x) in fruitCounter.items():
        print(k + ': ' + str(x))

if __name__ == '__main__':
    main()