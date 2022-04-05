# This program will calculate person BMI 
# Author: Nikolay Sezonov

number = int(input(' Please enter your weight in Kg: '))
# Integer number as an input

number2 = int(input(' Please enter your height in cm: '))
# Integer number as an input

number3 = 0.01

newNumber = number / ((number2*number3)*(number2*number3))
# formula to calculate BMI

print ('Your BMI is (kg/m2): {}'.format(newNumber))