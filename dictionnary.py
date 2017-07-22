"""
dictionnary.py
HW for July 27

This program allows users to request the zipcodes of Manhattan's neighborood by using a dictionnary.
"""

import sys

manhattan = {
    "central harlem": (10026, 10027, 10030, 10037, 10039),
    "chelsea": (10001, 10011, 10018, 10019, 10020, 10036),
    "east harlem": (10029, 10035),
    "gramercy park": (10010, 10016, 10017, 10022),
    "murray hill": (10010, 10016, 10017, 10022),
    "greenwich village": (10012, 10013, 10014),
    "soho": (10012, 10013, 10014),
    "lower manhattan": (10004, 10005, 10006, 10007, 10038, 10280),
    "lower east side": (10002, 10003, 10009),
    "upper east side":(10021, 10028, 10044, 10065, 10075, 10128),
    "upper west side":(10023, 10024, 10025),
    "inwood":(10031, 10032, 10033, 10034, 10040),
    "washington heights":(10031, 10032, 10033, 10034, 10040)
}

while True:
    try:
        borough = input("Please enter a borough of Manhattan (e.g., soho): ")
        print()
    except EOFError:
        sys.exit(0)

    try:
        definition = manhattan[borough]
    except KeyError:
        print("Sorry, \"", borough, "\" is not a borough of Manhattan.", sep = "")
        print()
        continue   #Go back up to the word "while".
    
    print("The ZIP Codes associated with ",borough.capitalize()," are: ", definition, ".", sep = "")
    print()
   

sys.exit(0)
