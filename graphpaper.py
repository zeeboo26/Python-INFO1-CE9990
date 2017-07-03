'''
graphpaper.py
 
This program prints out a grid based on user input.
 
'''

import sys

rows = int(input("How many rows of boxes? "))
columns = int(input("How many columns of boxes? "))
rspace = int(input("How many rows of spaces in each box (e.g., 1)? "))
cspace = int(input("How many columns of spaces in each box (e.g., 3)? "))

outerow = 1
while outerow <= rows:
    innerow = 1
    while innerow <= columns:
        print("+", cspace * "_", sep = "", end = "")
        innerow +=1
    print()
    outercols = 1
    while outercols <= rspace:

        innercols = 1
        while innercols <= columns:
            print("|", cspace * " ", sep ="", end = "")
            innercols += 1

        print()
        outercols +=1
    outerow += 1

sys.exit(0)
