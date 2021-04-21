Python | Get a set of places according to search query using Google Places API



 **Google Places API Web Service** allow the user to query for place
information on a variety of categories, such as establishments, prominent
points of interest, geographic locations, and more. One can search for places
either by proximity or a text string. A Place Search returns a list of places
along with summary information about each place; additional information is
available via a Place Details query.

Text Search Service of Google Places Api is used here, which is a web service
that returns information about a set of places based on a string. For example
“Hotels in Delhi” or “shoe stores near Oshawa”. The service responds with a
list of places matching the text string and any location bias that has been
set.

To use this service, the user must need an API key, which one can get form
here.

Let’s try to use this API service using Python. The modules which will be used
are requests and json.

Below is the implementation :

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to get a set of

# places according to your search 

# query using Google Places API

 

# importing required modules

import requests, json

 

# enter your api key here

api_key = 'Your_API_key'

 

# url variable store url

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

 

# The text string on which to search

query = input('Search query: ')

 

# get method of requests module

# return response object

r = requests.get(url + 'query=' + query +

 '&key;=' + api_key)

 

# json method of response object convert

# json format data into python format data

x = r.json()

 

# now x contains list of nested dictionaries

# we know dictionary contain key value pair

# store the value of result key in variable y

y = x['results']

 

# keep looping upto length of y

for i in range(len(y)):

 

 # Print value corresponding to the

 # 'name' key at the ith index of y

 print(y[i]['name'])  
  
---  
  
 __

 __

 **Output :**

    
    
    Search query: Hotels in delhi
    
    ITC Maurya
    Le Meridien New Delhi
    The Imperial New Delhi
    Radisson Blu Hotel New Delhi Paschim Vihar
    The Lalit New Delhi
    Crowne Plaza New Delhi Rohini
    Shangri-La's Eros Hotel, New Delhi
    Pride Plaza Hotel Aerocity, New Delhi
    The Claridges
    The Leela Ambience Convention Hotel, Delhi
    Radisson Blu Plaza Delhi Airport
    Hotel City Park
    Radisson Blu New Delhi Dwarka
    The Ashok Hotel
    Novotel New Delhi Aerocity
    Mapple Emerald
    The Metropolitan Hotel and Spa
    The Umrao
    Pullman New Delhi Aerocity
    Welcome Hotel Dwarka
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

