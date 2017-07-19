"""
nycwater.py 

This program creates lists from a csv file, and tell users how much water was consumed by a new yorker in a specific year.
"""
import sys
import urllib.request
import csv

url = "https://data.cityofnewyork.us" \
    "/api/views/ia2d-e54m/rows.csv?accessType=DOWNLOAD"

try:
    infile = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

sequenceOfBytes = infile.read() #Read the entire file into the sequenceOfBytes.
infile.close()

try:
    stringOfCharacters = sequenceOfBytes.decode("utf-8")
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)

listOfLines = stringOfCharacters.splitlines() #listOfLines is a list of strings.
reader = csv.reader(listOfLines[1:])          #Chop off header line.

listOfYears = []
waterUses = []

for line in reader:
    listOfYears.append(line[0])
    waterUses.append(line[3])

Year = input('Enter a year between 1979 and 2016: ')

for i in range(len(listOfYears)):
    if Year == listOfYears[i]:
        print ('In', Year , 'a new yorker used', waterUses[i], 'gallons of water PER DAY.')
    
infile.close()
sys.exit(0)
