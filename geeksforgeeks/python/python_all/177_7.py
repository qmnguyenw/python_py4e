Find current weather of any city using OpenWeathermap API in Python



 **openweathermap**is a service that provides weather data, including
current weather data, forecasts, and historical data to the developers of web
services and mobile applications.

It provides an API with JSON, XML and HTML endpoints and a limited free usage
tier. Making more than 60 calls per minute requires a paid subscription
starting at _USD 40_ per month. Access to historical data requires a
subscription starting at _150 USD_ per month. Users can request current
weather information, extended forecasts and graphical maps (showing cloud
cover, wind speed, pressure and precipitation).

To use this current weather data API, one must need the API key, which can be
get form here.

 **Note:** User need to create an account on openweathermap.org then only can
use the APIs.

 **Modules Needed :**

  

  

    
    
    requests
    json
    

  
Below is the implementation :

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find current

# weather details of any city

# using openweathermap api

 

# import required modules

import requests, json

 

# Enter your API key here

api_key = "Your_API_Key"

 

# base_url variable to store url

base_url = "http://api.openweathermap.org/data/2.5/weather?"

 

# Give city name

city_name = input("Enter city name : ")

 

# complete_url variable to store

# complete url address

complete_url = base_url + "appid=" + api_key + "&q;=" +
city_name

 

# get method of requests module

# return response object

response = requests.get(complete_url)

 

# json method of response object 

# convert json format data into

# python format data

x = response.json()

 

# Now x contains list of nested dictionaries

# Check the value of "cod" key is equal to

# "404", means city is found otherwise,

# city is not found

if x["cod"] != "404":

 

 # store the value of "main"

 # key in variable y

 y = x["main"]

 

 # store the value corresponding

 # to the "temp" key of y

 current_temperature = y["temp"]

 

 # store the value corresponding

 # to the "pressure" key of y

 current_pressure = y["pressure"]

 

 # store the value corresponding

 # to the "humidity" key of y

 current_humidiy = y["humidity"]

 

 # store the value of "weather"

 # key in variable z

 z = x["weather"]

 

 # store the value corresponding 

 # to the "description" key at 

 # the 0th index of z

 weather_description = z[0]["description"]

 

 # print following values

 print(" Temperature (in kelvin unit) = " +

 str(current_temperature) +

 "\n atmospheric pressure (in hPa unit) = " +

 str(current_pressure) +

 "\n humidity (in percentage) = " +

 str(current_humidiy) +

 "\n description = " +

 str(weather_description))

 

else:

 print(" City Not Found ")  
  
---  
  
 __

 __

 **Output :**

    
    
     Enter city name : Delhi
     Temperature (in kelvin unit) = 312.15
     atmospheric pressure (in hPa unit) = 996
     humidity (in percentage) = 40
     description = haze
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

