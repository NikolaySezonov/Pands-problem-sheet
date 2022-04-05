# This program takes a positive floating-point number as input and outputs an approximation of its square root
# Author: Nikolay Sezonov

# All the help from stackoverflow.com and https://www.w3schools.com/python/python_try_except.asp

while True: 
    try:
        num = input("Please enter a positive number: ")  
        number = float(num)

    except ValueError:
        print('Can you please try again and enter a positive number?.')
        continue

    if number <= 0:
            print('Please enter a number greater than zero') # ensure that the user inputs a positive number
    break # break from the while loop to the next variable

number_sqrt = (number ** 0.5)
# Formula for the sq.root

print("The square root of %0.1f is approx %0.1f" %(number, number_sqrt))
