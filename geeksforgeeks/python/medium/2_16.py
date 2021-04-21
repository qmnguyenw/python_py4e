How to get Geolocation in Python?



In this article we will discuss on how to get Geolocation when you enter any
location name and its gives all the useful information such as postal code,
city, state, country etc. with the latitudes and the longitudes (the specific
coordinates) and vice-versa in which we provide the coordinates to get the
location name.

This can be done using the GeoPy library in python. This library isn’t built
into python and hence needs to installed explicitly.

### Installation

In your terminal, simply run the given command:

> pip install geopy

###  **Method 1: Getting coordinates from location name**

With provided location it is possible using geopy to extract the coordinates
meaning its latitude and longitude. Therefore, it can be used ot express the
location in terms of coordinates.

  

  

 **Approach**

  * Import module
  * Import Nominatim from geopy- Nominatim is a free service or tool or can be called as API with no keys that provides you with the data after providing it with name and address and vice versa.
  * On calling Nomination tool which accepts an argument of **user_agent** you can give any name as it considers it to be the name of the app to which it is providing its services. 
  * The **geocode()** function accepts the location name and returns a geodataframe that has all the details and since it’s a dataframe we can get the address, latitude and longitude by simply calling it with the given syntax 

**Syntax:**

> variablename.address
>
> variablename.latitude
>
> variablename.longitude.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing geopy library

from geopy.geocoders import Nominatim

 

# calling the Nominatim tool

loc = Nominatim(user_agent="GetLoc")

 

# entering the location name

getLoc = loc.geocode("Gosainganj Lucknow")

 

# printing address

print(getLoc.address)

 

# printing latitude and longitude

print("Latitude = ", location.latitude, "\n")

print("Longitude = ", location.longitude)  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210114172730/op1-660x91.JPG)

###  **Method 2: Getting location name from latitude and longitude**

In this method all the things are same as the above, the only difference is
instead of using the geocode function we will now use the **reverse()** method
which accepts the coordinates (latitude and longitude) as the argument, this
method gives the address after providing it with the coordinates.

 **Syntax:**

> reverse(latitude,longitude)

 **Approach**

  * Import module
  * Call nominatim tool
  * Pass latitude and longitude to reverse()
  * Print location name

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing modules

from geopy.geocoders import Nominatim

 

# calling the nominatim tool

geoLoc = Nominatim(user_agent="GetLoc")

 

# passing the coordinates

locname = geoLoc.reverse("26.7674446, 81.109758")

 

# printing the address/location name

print(locname.address)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210114173037/op2-660x83.JPG)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

