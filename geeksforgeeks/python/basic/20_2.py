Calculate distance and duration between two places using google distance
matrix API in Python



Google Map Distance Matrix API is a service that provides travel distance and
time is taken to reach a destination. This API returns the recommended
route(not detailed) between origin and destination, which consists of duration
and distance values for each pair.

To use this API, one must need the _API key_ , which can be get form here.

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

# importing required libraries

import requests, json

 

# enter your api key here

api_key ='Your_api_key'

 

# Take source as input

source = input()

 

# Take destination as input

dest = input()

 

# url variable store url 

url ='https://maps.googleapis.com/maps/api/distancematrix/json?'

 

# Get method of requests module

# return response object

r = requests.get(url + 'origins = ' + source +

 '&destinations; = ' + dest +

 '&key; = ' + api_key)

 

# json method of response object

# return json format result

x = r.json()

 

# by default driving mode considered

 

# print the value of x

print(x)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    dehradun
    haridwar
    
    {'destination_addresses': ['Haridwar, Uttarakhand, India'], 
    'origin_addresses': ['Dehradun, Uttarakhand, India'], 'rows': 
    [{'elements': [{'distance': {'text': '56.3 km', 'value': 56288}, 
    'duration': {'text': '1 hour 40 mins', 'value': 5993},
    'status': 'OK'}]}], 'status': 'OK'}
    

#### Using googlemaps module :

Distance between two places can also be calculated using _googlemaps_ module.

Command to install _googlemaps_ module :

    
    
    pip install googlemaps

 __

 __  
 __

 __

 __  
 __  
 __

# importing googlemaps module

import googlemaps

 

# Requires API key

gmaps = googlemaps.Client(key='Your_API_key')

 

# Requires cities name

my_dist =
gmaps.distance_matrix('Delhi','Mumbai')['rows'][0]['elements'][0]

 

# Printing the result

print(my_dist)  
  
---  
  
 __

 __

 **Output :**

    
    
    {'distance': {'text': '1,415 km', 'value': 1415380}, 'duration': {'text': '23 hours 42 mins', 'value': 85306}, 'status': 'OK'}

Thanks to **aishwarya.27** for contributing this method.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

