'''
graphpaper.py
 
This program prints out a closed grid based on user input.
 
'''

import sys

row = int(input('How many rows of boxes? '))
col = int(input('How many columns of boxes? '))
width = int(input('How many columns of spaces in each box? '))
height = int(input('How many rows of spaces in each box? '))
 
a = "+" + (width * "-" + "+") * col
b = "|" + (width * " " + "|") * col


for i in range (row):
    print(a)
    
    for y in range(height):
        print(b)
       
print(a)  #closes out the bottom

sys.exit(0)
