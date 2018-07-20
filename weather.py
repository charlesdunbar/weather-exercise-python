#!/usr/bin/env python3

import json
import os
import re
import requests
import sys

"""
Author: Charles Dunbar
"""

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.getenv("WEATHER_API_KEY", "abc123")


def parse_json(response):
    """ Parse the json response and return the temperature

    Args:
        response (str): A string variable of json data
    
    Returns:
        The ['main']['temp'] value from the json data
    """
    parsed_json = json.loads(response)
    return parsed_json['main']['temp']


def generate_url(city):
    """ Generate the url based on either a 5 digit zip code or the name of a city
    
    Args:
      city (str): Either a string value from the user representing a city name
                  or a 5 numeric ZIP code

    Returns:
      The url to be used for the api call
    """
    if city.isdigit():
        # Make sure the zip code is 5 numbers long
        if re.match(r'^\d{5}$', city) == None:
            sys.exit("ZIP code should be 5 numbers")
        url = BASE_URL + "zip=" + city
    else:
        # Check that a city name is only alphabetical characters
        if re.match(r'^[a-zA-Z ]+$', city) == None:
            sys.exit("City name should only be alphabetical characters")
        # Default to US if only city name given
        if len(city.split()) == 1:
            country = "us"
        elif len(city.split()) == 2:
            country = city.split()[1]
            city = city.split()[0]
        else:
            sys.exit("Please enter in the format of City or City Country")
        url = BASE_URL + "q=" + city + "," + country

    url += "&units=imperial&APPID=" + API_KEY
    return url

def main():
    city = input("Where are you?\nChoose a format of Des Moines (optional 2 letter country code) or ZIP code: ")
    url = generate_url(city)
    request = requests.get(url)
    if request.status_code == 200:
        temperature = parse_json(request.text)
    else:
        sys.exit("Failed to get the temperature, please try again later")

    print("{} weather:\n{} degrees Fahrenheit".format(str(city), str(temperature)))

if __name__ == '__main__':
    main()