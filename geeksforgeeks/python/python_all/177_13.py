Python | Get a google map image of specified location using Google Static Maps
API



 **Google Static Maps API** lets embed a Google Maps image on the web page
without requiring JavaScript or any dynamic page loading. The Google Static
Maps API service creates the map based on URL parameters sent through a
standard HTTP request and returns the map as an image one can display on the
web page.

To use this service, one must need an API key, get it form here .

 **Note:** One need to create billing account on google then only can use
Google APIs.

 **Modules needed :**

    
    
    import requests

Below is the implementation :

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to get a google map

# image of specified location using 

# Google Static Maps API

 

# importing required modules

import requests

 

# Enter your api key here

api_key = "_your_api_key_"

 

# url variable store url

url = "https://maps.googleapis.com/maps/api/staticmap?"

 

# center defines the center of the map,

# equidistant from all edges of the map. 

center = "Dehradun"

 

# zoom defines the zoom

# level of the map

zoom = 10

 

# get method of requests module

# return response object

r = requests.get(url + "center =" + center + "&zoom; =" +

 str(zoom) + "&size; = 400x400&key; =" +

 api_key + "sensor = false")

 

# wb mode is stand for write binary mode

f = open('address of the file location ', 'wb')

 

# r.content gives content,

# in this case gives image

f.write(r.content)

 

# close method of file object

# save and close the file

f.close()  
  
---  
  
 __

 __

 **Output :**  
![Output](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-132.png)

 **Note :** For checking whether the API key is properly working or not, store
r.content in .txt file, inspite of saving as .png file. If the API key
is invalid, API will return this error message instead of image “The Google
Maps API server rejected your request. The provided API key is invalid “.  

Following list shows the approximate level of detail one can expect to see at
each zoom level :

    
    
    1 : World
    5 : Landmass/continent
    10 : City
    15 : Streets
    20 : Buildings
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

