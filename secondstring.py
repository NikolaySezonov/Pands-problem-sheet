# This program asks the user to input string and outputs every second letter in reverse order
# Author: Nikolay Sezonov
# Help provided from stackoverflow.com

rawString = input ("Please input a sentence: ")
secondchar = -2
# reads second letter from reverse

splitString = rawString[::secondchar]

print(splitString)
