'''
graphpaper2.py
 
This program prints out a perfect grid based on user input.
 
'''

import sys
 
row = int(input('How many rows of boxes? '))
col = int(input('How many columns of boxes? '))
width = int(input('How many columns of spaces in each box? '))
height = int(input('How many rows of spaces in each box? '))
 

a = "+" + (width * "-" + "+") * col
b = "|" + (width * " " + "|") * col

outer = 0 #for the outside of the box
while outer < row:
    print(a)
    inner = 0 #for the inside of the box
    while inner < height:
        print(b)
        inner += 1
    outer += 1


print(a) #closing the box at the bottom

sys.exit(0)
