# This program will tell whether today is a weekday or the weekend
# Author: Nikolay Sezonov

# Part of the code obtained from stackoverflow.com

import datetime

weekno = datetime.datetime.today().weekday()

if weekno < 5:
    print ("Unfortunately today is a working day, so go and crack some codes!")
else:  # 5 Sat, 6 Sun
    print ("Yes, it is a weekend, Hooray !")