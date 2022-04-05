# Program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author: Nikolay Sezonov
# 


import matplotlib.pyplot as plt
import numpy as np

lower = int(input('Please enter lower value: '))
# This variables 'lower value' is going to allow the user to set the lower part of the range.

upper = int(input('Please enter upper value: '))
# This variables 'upper value' is going to allow the user to set the upper part of the range.

x = np.arange(lower, upper)
# x creates the range for lower and upper values

plt.plot(x, x)
# Line displays x

plt.plot(x, x ** float(2))
# Line 2 displays x2

plt.plot(x, x ** float(3))
# Line 3 displays x3

# Graph labelling
My_title = f'Functions x, x2 and x3 in the range [{lower},{upper}]'

# Title is set us as a readable string.
plt.title(My_title, fontweight="bold")

plt.xlabel('x - axis')
# X axis is labelled

plt.ylabel('y - axis')
# X axis is labelled

# Allocating labels for x and y axises
plt.xlabel("Number X axis")
plt.ylabel("Number Y axis")
plt.show()