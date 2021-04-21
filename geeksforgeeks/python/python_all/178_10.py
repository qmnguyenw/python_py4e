Python | Calculate geographic coordinates of places using google geocoding API



Geocoding is the process of converting addresses into geographic coordinates
like latitude and longitude, which can be used to mark position on map.

To use the Google Maps Geocoding API, one must need an API key, which can be
get form here.  
  
**Modules needed :**

    
    
    import requests
    import json 

Below is the implementation :

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to calculate geographic

# coordinates of places using google

# geocoding API

 

# importing required modules

import requests, json

 

# enter your api key here

api_key = 'Your_api_key'

 

# url variable store url

url = 'https://maps.googleapis.com/maps/api/geocode/json?'

 

# take place as input

place = input()

 

# get method of requests module

# return response object

res_ob = requests.get(url + 'address =' +

 place + '&key; =' + api_key)

 

# json method of response object

# convert json format data 

# into python format data.

x = res_ob.json()

 

# print the vale of x

print(x)  
  
---  
  
 __

 __

 **Output :**

    
    
    _Dehradun_
    
    {'results': [{'address_components': [{'long_name': 'Dehradun', 'short_name': 'Dehradun', 'types': ['locality', 'political']}, {'long_name': 'Dehradun', 'short_name': 'Dehradun', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Uttarakhand', 'short_name': 'UK', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'India', 'short_name': 'IN', 'types': ['country', 'political']}], 'formatted_address': 'Dehradun, Uttarakhand, India', 'geometry': {'bounds': {'northeast': {'lat': 30.4041936, 'lng': 78.1089305}, 'southwest': {'lat': 30.2466633, 'lng': 77.92533879999999}}, 'location': {'lat': 30.3164945, 'lng': 78.03219179999999}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 30.4041936, 'lng': 78.1089305}, 'southwest': {'lat': 30.2466633, 'lng': 77.92533879999999}}}, 'place_id': 'ChIJr4jIVsMpCTkRmYdRMsBiNUw', 'types': ['locality', 'political']}], 'status': 'OK'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

