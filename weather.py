import requests # lib to make HTTP req (talks to API)
from dotenv import load_dotenv # best practice to store sensitive info in .env
import os
from dataclasses import dataclass


load_dotenv()
api_key = os.getenv('API_KEY') # grab api key from the file and load into variable "api_key"

@dataclass # stores weather info to be shown to user
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int


# function to get lat&lon 
def get_lat_lon(city_name, country_code, api_key): # accpet these 3 argument
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={api_key}').json()
    
    # check that resp is a list with at least one item
    if not isinstance(resp, list) or len(resp) == 0: # If the API didnt give a list or the list is empty, so dont continue
        return None, None # why 2? bcoz it return 2 values

    lat = resp[0].get('lat') # pick the first match (most relevant) --below too
    lon = resp[0].get('lon')
    return lat, lon


# function to get current weather condition (using coordinates)
def get_current_weather(lat, lon, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json() # "&units=metric" this part returns celcius instead of kelvin
    
    weather = resp.get('weather')
    main_data = resp.get('main')

    if not weather or not isinstance(weather, list) or not main_data: # if weather list is missing/empty or temperature data is missing, dont continue
        return None
    
    data = WeatherData(
        main = weather[0].get('main'),
        description = weather[0].get('description'),
        icon = weather[0].get('icon'),
        temperature = round(main_data.get('temp')) # round the temperature
    )
    return data


# function that combine them
# this is the function that Flask calls (from weather import main as get_weather)
def main(city_name, country_code):
    lat, lon = get_lat_lon(city_name, country_code, api_key) # get coordinates

    if lat is None or lon is None: 
        return None # if the coordinates invalid, return none (and trigger error message)

    return get_current_weather(lat, lon, api_key) # Otherwise, fetch actual weather (get_current_weather)
