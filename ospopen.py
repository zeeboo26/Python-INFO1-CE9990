"""
ospopen.py

This programs lists your outdated Python packages and the latest version available.
"""
import sys
import os

infile = os.popen("/Library/Frameworks/Python.framework/Versions/3.6/bin"
                  "/pip3 list -o")              #Create a child process and a pipe.               
                                     
lines = infile.readlines()                      #lines is a list of lines.
status = infile.close()

if status != None:                              #status is supposed to be None.
    print("\"pip3 list -o\" produced exit status", status)
    sys.exit(1)

lines = [line.rstrip() for line in lines]       #Remove trailing newline.

for i, line in enumerate(lines, start = 1):
    print("{} {}".format(i, line))

print()
print("You have", i , "outdated Python librairies.")

sys.exit(0)
