"""
json.py

This programs downloads information from a website and converts it into a dictionnary in
JSON format.
See:  http://date.jsontest.com
"""
import datetime 
import sys
import urllib.request
import json

url = "http://date.jsontest.com"

try:
    infile = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

sequenceOfBytes = infile.read()         #Read the entire input file.
infile.close()

try:
    s = sequenceOfBytes.decode("utf-8") #s is a string.
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)

print(s)
print()

try:
    dictionary = json.loads(s)          #dictionary is a dictionary.
except json.JSONDecodeError as jSONDecodeError:
    print(jSONDecodeError)
    sys.exit(1)
    
millisec = int(dictionary["milliseconds_since_epoch"])
seconds = millisec/1000

localDateAndTime = datetime.datetime.fromtimestamp(seconds)
print("Eastern Daylight Time:")
print(localDateAndTime.strftime("%c"))
print()

sys.exit(0)
