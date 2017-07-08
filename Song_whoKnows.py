"""
Song_whoKnows.py

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
     
for i in range(0,13):
    print ("Who knows", n[i],"?\nI know", n[i]) #print the first lines of the song.
    print(n[i], lyrics[i])                      #print n associated to its lyrics
    for j in range (i):
        print(n[i-1], lyrics[i-1])
        i -=1                                   #print lines in inverse order from i to 0
    print()                                     #to separate the paragraphs
    
sys.exit(0)
