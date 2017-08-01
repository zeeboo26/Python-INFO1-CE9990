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

print()

try:
    dictionary = json.loads(s)          #dictionary is a dictionary.
except json.JSONDecodeError as jSONDecodeError:
    print(jSONDecodeError)
    sys.exit(1)
    
for key in sorted(dictionary):
    value = dictionary[key]
    print("{:25} {:<14}".format(key + ":", value), end = "")

    #Two of the keys require additional printing:
    if key == "milliseconds_since_epoch":
        seconds = value / 1000
        d = datetime.datetime.fromtimestamp(seconds)
        print(d.strftime("(local %a %b %d %I:%M:%S.%f %p %Y)"), end = "")
    elif key == "time":
        s = dictionary["date"] + " " + value
        d = datetime.datetime.strptime(s, "%m-%d-%Y %I:%M:%S %p")
        d = d.replace(tzinfo = datetime.timezone.utc)
        d = d.astimezone(tz = None)
        print(d.strftime("(local %a %b %d %I:%M:%S %p %Y)"), end = "")

    print()


sys.exit(0)
