"""
location.py

This is a Python module that has been imported in the script: uselocation.py
This Python module gives the corresponding zipcode of a location by using latitude and longitude,
by importing info from the website in a JSON format.
This program can also be run on its own, it prompts the user to chose a latitude
and a longitude in order to output the zipcode.
"""
import sys
import urllib.request
import json

class Location(object):
    """
    Class Location demonstrates class and instance attributes, class and instance methods.
    """

    def __init__(self, latitude, longitude):
        if not (isinstance (latitude, int) or isinstance(latitude, float)):
            raise TypeError("latitude must be int or float.")
        if not (isinstance (longitude, int) or isinstance(longitude, float)):
            raise TypeError("longitude must be int or float.")
        if abs(latitude) > 90:
            raise ValueError("latitude must be between -90 to 90 inclusive")
        if abs(longitude) > 180:
            raise ValueError("longitude must be between -180 to 180 inclusive")
        
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        "Return a string that looks like the content of myself."
        if self.latitude >= 0:
            latitudeDirection = "N"
        else:
            latitudeDirection = "S"
        if self.longitude >= 0:
            longitudeDirection = "E"
        else:
            longitudeDirection = "W"

        return "{}\u00B0{} {}\u00B0{}".\
                format(abs(self.latitude), latitudeDirection,
                       abs(self.longitude), longitudeDirection)

    def getLatitude(self):
        "Return my latitude."
        return self.latitude
    
    def setLatitude(self, newLatitude):
        "Set my latitude to a new value."
        if not (isinstance (newLatitude, int) or isinstance(newLatitude, float)):
            raise TypeError("Latitude must be int or float.")
        if abs(newLatitude) > 90:
            raise ValueError("Latitude must be between -90 to 90 inclusive")
        self.latitude = newLatitude
    
    def getLongitude(self):
        "Return my longitude."
        return self.longitude

    def setLongitude(self, newLongitude):
        "Set my longitude to a new value."
        if not (isinstance (newLongitude, int) or isinstance(newLongitude, float)):
            raise TypeError("Longitude must be int or float.")
        if abs(newLongitude > 180):
            raise ValueError("Longitude must be between -180 to 180 inclusive")
        self.longitude = newLongitude

    def getZipcode(self):
        "Returns zipcode"  
        url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}".format(self.latitude, self.longitude)

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

        try:
            dictionary = json.loads(s)          #dictionary is a dictionary.
        except json.JSONDecodeError as jSONDecodeError:
            print(jSONDecodeError)
            sys.exit(1)

        if "results" in dictionary:                             #check if dictionary has no results key
            results = dictionary["results"]                     #results is a list of dictionaries
            if len(results) == 0:
                return 0
        else:
            print("dictionary has no results key")
            sys.exit(1)

        firstResult = results[0]  
        if "address_components" not in firstResult:           #check if firstResult has no address_components key
            print("firstResult has no Address_components key")
            sys.exit(1)
        else:
            address_components = firstResult["address_components"] #address_components is a list of dictionarie
            for component in address_components:                   #component is a dictionary
                if "postal_code" in component["types"]:            #component["types"] is a list of string
                    if "long_name" in component:                   #check if component has no long name key
                        return component["long_name"]                   #component["long_name"] is a string that looks like a zipcode
                    else:
                        print("Component does not have a long_name")
                        sys.exit(1)
        return 0


    #The definition of classLocation ends here.

if __name__ == '__main__':
    loc = Location(-34.074678, 120.46583998282)
    print("The zipcode of {} is {}.".format(loc, loc.getZipcode()))
    print()
    print("Your turn to chose a latitude and a longitude:\n")
    loc.setLatitude = float(input("Please enter a latitude between -90 and 90 inclusive: "))
    loc.setLongitude = float(input("Please enter a longitude between -180 and 180 inclusive: "))
    loc = Location(loc.setLatitude, loc.setLongitude)
    print("The zipcode of {} is {}.".format(loc, loc.getZipcode()))
    sys.exit(0)
