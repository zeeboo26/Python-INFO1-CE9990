"""
poèmeChansonDautomne.py

This program inputs all the lines of a text file from the web and does something not very interesting with them 
(i.e sort lines in order of decreasing length)
"""

import sys
import urllib.request

# read the url 
url = "https://raw.githubusercontent.com/zeldasalfati/Python-INFO1-CE9990/master/ChansonDautomne"

try:                                                                      
    inputFile = urllib.request.urlopen(url) # we were successful
except urllib.error.URLError as error: 
    print("The url", url, "does not exist") # we weren't successful
    sys.exit(1)
    
# read the filename
lines = inputFile.readlines()
inputFile.close()

try:
    stringOfCharacters = sequenceOfBytes.decode("utf-8")
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)
    
lines = stringOfCharacters.splitlines() #lines is a list of strings
#sort lines in order of decreasing number of characters
lines.sort(key = len, reverse = True)

for line in lines:
print(line)
