# Program that reads in a text file moby-dick.txt and outputs the number of e's each line contains.
# Author Nikolay Sezonov
# Reference http://book.pythontips.com/en/latest/open_function.html
# Refernence:https://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/

total = 0
line_nr = 0
counter = 0

# variables required for total number and letter count
letr = input ('Please enter the letter you want to count:')
# this prompt user to enter the required letter to count

with open('moby-dick.txt', 'r') as text_file:
# this opens the text document from the command line and 'r' imports the readline function

    for line in text_file:
        line_nr += 1
        # add 1 to every line in the loop

        print ('Number of letters in Line No - ',line_nr)
        for letter in line:
        # It will look for the specific letter in the line. 
        # It will add 1 every time it found the letter until the counted line is ended
            if letter == letr:
                counter += 1
                total +=1
                # two counts run simulanuesly 
        print (counter)
        counter = 0
    print ('Total number of required letter:',(total))
    

    # the for loop goes through each line in the text file
    # The count is looking at the line and adding 1 every time it runs through the for loop.
        
        
        # If the count is even and has no remainders then the if statement is true.
        
               # If the if statement is true it will count number of "e" in each line, but i cannot get the total :(
        