# Program that reads in a text file moby-dick.txt and outputs the number of e's it contains.
# Author Nikolay Sezonov
# Reference http://book.pythontips.com/en/latest/open_function.html
# Refernence:https://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/

with open('moby-dick.txt', 'r') as text_file:
# this opens the text document from the command line

# 'r' imports the readline function

    count = 0
    # The count is set at zero for the for loop
    for line in text_file:
    #the for loop goes through each line in the text file
    # The count is looking at the line and adding 1 every time it runs through the for loop.
        count (a)
        # If the count is even and has no remainders then the if statement is true.
        if count % 2 == 0:
            # If the if statement is true it will print the line.
            print(line)