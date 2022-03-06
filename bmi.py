# This program will calculate BMI 
# Author: Nikolay Sezonov

number = int(input(' Please enter your weight in Kg: '))
number2 = int(input(' Please enter your height in cm: '))

number3 = 0.01

newNumber = number / ((number2*number3)*(number2*number3))

print ('Your BMI is (kg/m2): {}'.format(newNumber))