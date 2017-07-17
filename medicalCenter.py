"""
medicalCenter.py

This program output the phone number of Montefiore Medical center institutions
"""
import sys
import csv  

filename = "Mental_Health_Service_Finder_Data.csv"

try:
    csvfile = open(filename, encoding = "utf-8", newline = "")
except FileNotFoundError:
    print("Sorry, could not find file \"", filename, "\".", sep = "")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open file \"", filename, "\".", sep = "")
    sys.exit(1)

lines = csv.reader(csvfile)

f = """\
Institution Name: {}: {}
Phone number:     {}
"""
for line in lines:
        print(f.format(line[0], line[1], line[6])) #names and phone number
        
csvfile.close()
sys.exit(0)
