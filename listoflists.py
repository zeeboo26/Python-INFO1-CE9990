"""
listoflists.py

This program uses lists of lists to output the information of an experiment in rows and columns
"""

import sys

CellsA19 = [
    "Control", "Experimental", "Cilia", "Nucleus", ['1.63','        ', '2,02'], ['1.1','         ', '2,3']
]


CellsRPE1 = [
    "Control", "Experimental", "Cilia", "Nucleus", ['2.1','         ', '3,9'], ['4.1','          ', '5,9']
]

CellsMDCK = [
     "Control", "Experimental", "Cilia", "Nucleus", ['1.09','         ','6,04'], ['6.3','         ', '2,1']
]


f = """
 Type:               {}                               {}
 Location:  {}                 {}          {}                 {}
 Average:   {}           {}
""" 

print(f.format(CellsA19[0], CellsA19[1], CellsA19[2], CellsA19[3], CellsA19[2], CellsA19[3], CellsA19[4], CellsA19[5]))
print(f.format(CellsRPE1[0], CellsRPE1[1], CellsRPE1[2], CellsRPE1[3], CellsRPE1[2], CellsRPE1[3], CellsRPE1[4], CellsRPE1[5]))
print(f.format(CellsMDCK[0], CellsMDCK[1], CellsMDCK[2], CellsMDCK[3], CellsMDCK[2], CellsMDCK[3],CellsMDCK[4],CellsMDCK[5]))

sys.exit(0)
