"""
listoflists.py

This program uses lists of lists to output the information of an experiment in rows and columns
"""

import sys

lines = [
    [['1.63', 8 * ' ', '2,02'], ['1.1',  9 * ' ', '2,3']],
    [['2.1',  9 * ' ', '3,9'],  ['4.1', 10 * ' ', '5,9']],
    [['1.09', 9 * ' ','6,04'],  ['6.3',  9 * ' ', '2,1']]
]


f = """
 Type:               {}                               {}
 Location:  {}                 {}          {}                 {}
 Average:   {}           {}
"""

for line in lines:
    print(f.format("Control", "Experimental", "Cilia", "Nucleus",
        "Cilia", "Nucleus", line[0], line[1]))

sys.exit(0)
