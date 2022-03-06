# program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, 
#   if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

# Author Nikolay Sezonov

from itertools import count


def collatz(number):

    if number % 2 == 0:
        # number even

        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        # number odd
     
        result = 3 * number + 1
        print(result)
        return result

n = input("Please enter a positive integer : ")
while n != 1:
    n = collatz(int(n))
