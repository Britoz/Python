# Demonstrate the using of 'deck' which is called as Deque objects

import collections
import string

def main():
    # TODO: initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)
    '''
    string.ascii_lowercase will give  a lower case letters (from a->z)
    '''

    # TODO: deques support the len() function
    print("Item count: ", str(len(d)))

    # TODO: deques can be iterated over
    '''for elem in d:
        # TODO: add comma for each end of element
        print(elem.upper(), end=',')'''


    # TODO: manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)

    # TODO: rotate the deque
    print(d)
    d.rotate(10)
    print(d)


if __name__ == '__main__':
    main()