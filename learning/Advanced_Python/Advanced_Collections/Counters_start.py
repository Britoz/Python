# Demonstrate the using of Counters

from collections import Counter

def main():
    # list of students in class 1
    class1 = ["student 1", "James", "student 3", "student 4",
              "student 5", "student 6", "Lee", "Yes", "Yes"]

    # list of students in class 2
    class2 = ['Bill', 'Gate', 'student 1', 'Blood', 'Fire', 'wall',
              'Hello', 'Lee', 'Fucking', 'Yes']

    # TODO: Create a Counter for class1 and class2
    c1 = Counter(class1)
    c2 = Counter(class2)
    '''
    Counter is a dictionary
    hence, we need key to get value in the list
    '''

    # TODO: How many students in class 1 named James?
    print(c1["student 1"])


    # TODO: how many student are in class 1?
    print(sum(c1.values()), "student in class 1")


    # TODO: Combine the two classes
    c1.update(class2)
    print(sum(c1.values()), "student in class 1")
    '''
    update() will be used to include the new value to the dictionary
    '''

    # TODO: What's the most common name in the two classes?
    print(c1.most_common(3))

    # TODO: separate class again
    c1.subtract(class2)
    print(c1.most_common(3))
    '''
    substract will take out the value that similar to arg inside the ()
    
    '''
    # TODO: what's common between 2 classes
    print(c1 & c2)

if __name__ == '__main__':
    main()