# Weather
[![Build Status](https://travis-ci.org/charlesdunbar/weather-exercise-python.svg?branch=master)](https://travis-ci.org/charlesdunbar/weather-exercise-python)

## Challenge
Using the OpenWeatherMap API at http://openweathermap.org/current, create a 
program that prompts for a city name and returns the current temperature for 
the city. 

Example Output:

Where are you? Chicago IL
Chicago weather:
65 degrees Fahrenheit 

Brian P. Hogan. Exercises for Programmers, P1.0 The Pragmatic Bookshelf, LLC.


## Use
Set up a virtualenv: 
`virtualenv .virtual -p /usr/bin/python3`

`source .virtual/bin/activate`

`pip install -r requirements.txt`

Set your API key for openweathermap as an environment variable

`export WEATHER_API_KEY=YOUR_API_KEY_HERE`

`python ./weather.py`

You can currently enter city names in the format of "City" or "City Country"

## Known issues
The API doesn't allow a nice way to look up a US state.  To work around this, I added ZIP code functionality.
