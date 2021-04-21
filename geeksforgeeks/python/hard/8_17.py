Google Geo-coding Web Service (JSON response)



Prerequisite : JSON Formatting in Python  
Google has an excellent web service that allows us to make use of their large
database of geographic information. Here, we are going to be working with the
Google Maps API. In the old days, this Maps API was free and did 2, 500
requests per day but now they’ve made it so that parts of it are behind API
keys and you start having to use OAuth and stuff. We can submit a geographical
search string like “Ann Arbor, MI” to their geocoding API and have Google
return its best guess as to where on a map we might find our search string and
tell us about the landmarks nearby.

The geocoding service is free but rate limited so you cannot make unlimited
use of the API in a commercial application. But if you have some survey data
where an end user has entered a location in a free-format input box, you can
use this API to clean up your data quite nicely.

 _When you are using a free API like Google’s geocoding API, you need to be
respectful in your use of these resources. If too many people abuse the
service, Google might drop or significantly curtail its free service._

You can read the online documentation for this service, but it is quite simple
and you can even test it using a browser by typing the following URL into your
browser:  
http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI

Make sure to unwrap the URL and remove any spaces from the URL before pasting
it into your browser.

The following is a simple application to prompt the user for a search string,
call the Google geocoding API, and extract information from the returned JSON.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Libraries used to grab the URL web stuff and import json

import urllib.request, urllib.parse, urllib.error

import json

 

# Note that Google is increasingly requiring keys

# for this API

# service URL for Google Maps API

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

 

while True:

 address = input('Enter location: ')

 if len(address) < 1: break

 

 # Concatenate the serviceurl and urllib.parse.urlencode

 # which give a dictonary of address equal and this bit 

 # right here

 url = serviceurl + urllib.parse.urlencode(

 {'address': address})

 

 print('Retrieving', url)

 

 # urlopen() to get a handle

 uh = urllib.request.urlopen(url)

 # Read the whole document in UTF-8

 data = uh.read().decode()

 print('Retrieved', len(data), 'characters')

 

 # Load internal strings

 try:

 js = json.loads(data)

 except:

 js = None

 # If false then quit and print data

 if not js or 'status' not in js or js['status']
!= 'OK':

 print('==== Failure To Retrieve ====')

 print(data)

 continue

 

 # Call json dump and print it with an indent of four

 print(json.dumps(js, indent = 4))

 

 # Parsing and printing

 lat =
js["results"][0]["geometry"]["location"]["lat"]

 lng =
js["results"][0]["geometry"]["location"]["lng"]

 print('lat', lat, 'lng', lng)

 location = js['results'][0]['formatted_address']

 print(location)  
  
---  
  
 __

 __

Output :

    
    
    
    Enter location: Dehradun
    Retrieving http://maps.googleapis.com/maps/api/geocode/json?address=dehradun
    Retrieved 1743 characters
    {
        "results": [
            {
                "address_components": [
                    {
                        "long_name": "Dehradun",
                        "short_name": "Dehradun",
                        "types": [
                            "locality",
                            "political"
                        ]
                    },
                    {
                        "long_name": "Dehradun",
                        "short_name": "Dehradun",
                        "types": [
                            "administrative_area_level_2",
                            "political"
                        ]
                    },
                    {
                        "long_name": "Uttarakhand",
                        "short_name": "UK",
                        "types": [
                            "administrative_area_level_1",
                            "political"
                        ]
                    },
                    {
                        "long_name": "India",
                        "short_name": "IN",
                        "types": [
                            "country",
                            "political"
                        ]
                    }
                ],
                "formatted_address": "Dehradun, Uttarakhand, India",
                "geometry": {
                    "bounds": {
                        "northeast": {
                            "lat": 30.4041936,
                            "lng": 78.1089305
                        },
                        "southwest": {
                            "lat": 30.2466633,
                            "lng": 77.92533879999999
                        }
                    },
                    "location": {
                        "lat": 30.3164945,
                        "lng": 78.03219179999999
                    },
                    "location_type": "APPROXIMATE",
                    "viewport": {
                        "northeast": {
                            "lat": 30.4041936,
                            "lng": 78.1089305
                        },
                        "southwest": {
                            "lat": 30.2466633,
                            "lng": 77.92533879999999
                        }
                    }
                },
                "place_id": "ChIJr4jIVsMpCTkRmYdRMsBiNUw",
                "types": [
                    "locality",
                    "political"
                ]
            }
        ],
        "status": "OK"
    }
    lat 30.3164945 lng 78.03219179999999
    Dehradun, Uttarakhand, India
    

The program takes the search string and constructs a URL with the search
string as a properly encoded parameter and then uses urllib to retrieve the
text from the Google geocoding API. Unlike a fixed web page, the data we get
depends on the parameters we send and the geographical data stored in Google’s
servers.  
Once we retrieve the JSON data, we parse it with the json library and do a few
checks to make sure that we received good data, then extract the information
that we are looking for.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

