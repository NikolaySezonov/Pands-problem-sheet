# This program asks the user to input string and outputs every second letter in reverse order
# Author: Nikolay Sezonov

rawString = input ("Please input a sentence: ")
secondchar = -2

splitString = rawString[::secondchar]

print(splitString)
