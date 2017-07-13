"""
poème.py

This program inputs all the lines of a text file from the web and does something not very interesting with them 
(i.e sort lines in order of decreasing length)
"""

import sys
import urllib.request

# read the url 
url = "https://raw.githubusercontent.com/zeldasalfati/Python-INFO1-CE9990/master/ChansonDautomne"

try:                                                                      
    filename = urllib.request.urlopen(url) # we were successful
except urllib.error.URLError as error: 
    print("The url", url, "does not exist") # we weren't successful
    sys.exit(1)

# read the filename
lines = filename.readlines()

#sort lines in order of decreasing length
lines.sort(reverse = True) 

# use decode to onverts a sequence of bytes into a string of characters. 
for line in lines:
    # s = line.decode("utf-8")
    # print(s, end = "")
    print(line.decode("utf-8"), end = "")
    
lines.close()
sys.exit(0)
