#!/usr/bin/python3

import pytest
import weather

def test_parse_json():
    json_blob = '{"coord":{"lon":145.77,"lat":-16.92},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"base":"cmc stations","main":{"temp":293.25,"pressure":1019,"humidity":83,"temp_min":289.82,"temp_max":295.37},"wind":{"speed":5.1,"deg":150},"clouds":{"all":75},"rain":{"3h":3},"dt":1435658272,"sys":{"type":1,"id":8166,"message":0.0166,"country":"AU","sunrise":1435610796,"sunset":1435650870},"id":2172797,"name":"Cairns","cod":200}'
    parsed_temperature = weather.parse_json(json_blob)
    assert parsed_temperature == 293.25

def test_url_zip_code_invalid():
    zip_code = "123456"
    # From https://medium.com/python-pandemonium/testing-sys-exit-with-pytest-10c6e5f7726f
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        weather.generate_url(zip_code)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == "ZIP code should be 5 numbers"

def test_url_zip_code_valid():
    zip_code = "50315"
    url = weather.generate_url(zip_code)
    assert url == "http://api.openweathermap.org/data/2.5/weather?zip=50315&units=imperial&APPID=abc123"

def test_url_city_invalid():
    city = "D3s M0in3$"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        weather.generate_url(city)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == "City name should only be alphabetical characters"
    
def test_url_city_valid():
    city = "Ames"
    url = weather.generate_url(city)
    assert url == "http://api.openweathermap.org/data/2.5/weather?q=Ames,us&units=imperial&APPID=abc123"