How to find longitude and latitude for a list of Regions or Country using
Python



 **Geopy** is a Python 2 and 3 client for several popular geocoding web
services. Geocoding is the process to identify geographic coordinates like
latitude and longitude of a given city/country/address. This is very useful
during marking position on the map in data visualization. We use geopy.exec,
geocodertimedout, geolocators, geopy.geocoder in the below code to fetch
the results

### Installation

This module does not come built-in with Python. To install it type the below
command in the terminal.

    
    
    pip install geopy 
    

**Example: Let’s create a pandas dataframe containing a list of regions or
countries.**

 __

 __  
 __

 __

 __  
 __  
 __

# Import pandas package

import pandas as pd 

import numpy as np

 

# Define a dictionary containing data 

data = {'City':['Bangalore', 'Mumbai', 'Chennai',
'Delhi']} 

 

# Convert the dictionary into DataFrame 

df = pd.DataFrame(data) 

 

# Observe the result 

df   
  
---  
  
__

__

**Output:**

![ find longitude and latitude for a list of
regions/country](https://media.geeksforgeeks.org/wp-
content/uploads/20200330130108/Screenshot_2020-03-30-gfg.png)

  

  

 **Now Let’s find the latitude and longitude of the following regions or
countries.**

 __

 __  
 __

 __

 __  
 __  
 __

from geopy.exc import GeocoderTimedOut

from geopy.geocoders import Nominatim

 

# declare an empty list to store

# latitude and longitude of values 

# of city column

longitude = []

latitude = []

 

# function to find the coordinate

# of a given city 

def findGeocode(city):

 

 # try and catch is used to overcome

 # the exception thrown by geolocator

 # using geocodertimedout 

 try:

 

 # Specify the user_agent as your

 # app name it should not be none

 geolocator = Nominatim(user_agent="your_app_name")

 

 return geolocator.geocode(city)

 

 except GeocoderTimedOut:

 

 return findGeocode(city) 

 

# each value from city column

# will be fetched and sent to

# function find_geocode 

for i in (df["City"]):

 

 if findGeocode(i) != None:

 

 loc = findGeocode(i)

 

 # coordinates returned from 

 # function is stored into

 # two separate list

 latitude.append(loc.latitude)

 longitude.append(loc.longitude)

 

 # if coordinate for a city not

 # found, insert "NaN" indicating 

 # missing value 

 else:

 latitude.append(np.nan)

 longitude.append(np.nan)  
  
---  
  
 __

 __

 **Showing the output produced as dataframe.**

 __

 __  
 __

 __

 __  
 __  
 __

# now add this column to dataframe

df["Longitude"] = longitude

df["Latitude"] = latitude

 

df  
  
---  
  
 __

 __

 **Output:**

![ find longitude and latitude for a list of
regions/country](https://media.geeksforgeeks.org/wp-
content/uploads/20200330130240/Screenshot_2020-03-30-gfg1.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

