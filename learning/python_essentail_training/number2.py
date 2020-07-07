#this library is used to import more math function in python
from math import *

A = 10
B = 3
C = -100

print(A%B)
#print number as string
print("Result  of A+ B is : " + str(A+B))
#getting absolute value
print("Absolute value of C is : " + str(abs(C)))
#power of a number, 3 power 2
print("3 power 2 is: " + str(pow(3,2)))
#we can finding the maximum number by using max
print("maximum: " + str(max(A,max(B,abs(C)))))
#we can round up the number by using round(number) or ceil(number)
print("rouding number: " + str(round(3,7)))
#we also able to round down the number by using floor(number) of the math library
print("Round down number 3.8: " + str(floor(3.8)))
#we can handle the squarute of the number by using sqrt(number)
print("square root of 144 is : " + str(sqrt(144)))