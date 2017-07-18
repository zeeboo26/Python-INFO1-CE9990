"""
song.py

This program uses nested loops and a list of strings to output the lyrics of a song whose verses get longer and longer.
"""

import sys

lyrics = [
    "is our God on earth and Heaven",
    "are the tablets of the covenant",
    "are the Fathers",
    "are the mothers",
    "are the books of the Torah",
    "are the books of the Mishnah",
    "are the days of the week",
    "are the days of the circumcision",
    "are the months of the pregnant",
    "are the commandments",
    "are the stars of Joseph's dream",
    "are the tribes of Israel",
    "are the attributes of God"
    ]
    
n = [
    'One',
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten',
    'Eleven',
    'Twelve',
    'Thirteen'
    ]
     
for i in range(len(lyrics)):
    print ("Who knows ", n[i],"?, sep ="")
    print("I know ", n[i],"." sep ="")
    for j in range(i, 0, -1):
        print(n[j], lyrics[j])                  #print lines in inverse order from i to 0
    print()                                     #to separate the paragraphs
    
sys.exit(0)
