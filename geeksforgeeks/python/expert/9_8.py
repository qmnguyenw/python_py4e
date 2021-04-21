Get emotions of images using Microsoft emotion API in Python



The emotions of images like happy, sad, neutral, surprise, etc. can be
extracted using Microsoft emotion API for any development purpose.

It is very simple to use and can be called via API through terminal or any of
languages like Python or PHP. Microsoft provides free subscription of 30 days
for making total of 30,000 requests.  
The details of the end points and parameters can be found in the
documentation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python script to analyze

# emotion of image

import http.client, urllib.request

import urllib.parse, urllib.error

import base64, sys

import simplejson as json

 

# replace with subscription_key

# you obtained after registration

subscription_key = '12f29133caf4406493e81b6a31c47c1a'

 

headers = {

 

 # Request headers. Replace

 # the placeholder key

 # below with your

 # subscription key.

 'Content-Type': 'application/json',

 'Ocp-Apim-Subscription-Key': subscription_key,

}

 

params = urllib.parse.urlencode({

})

 

# Replace the URL

# below with the

# URL of the image

# you want to analyze.

url1 = 'IMAGE URL TO BE ADDED HERE'

body = { 'url': url1 }

newbody =str(body)

 

try:

 # NOTE: You must use the same region in your REST call as you used to
obtain your subscription keys.

 # For example, if you obtained your subscription keys from westcentralus,
replace "westus" in the

 # URL below with "westcentralus".

 conn =
http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')

 conn.request("POST", "/emotion/v1.0/recognize?%s" % params,
newbody, headers)

 response = conn.getresponse()

 data = response.read()

 

 parsed = json.loads(data)

 print ("Response:")

 print (json.dumps(parsed, sort_keys=True, indent=2))

 

 # the emotion of image

 # will the max value of

 # any emotion obtained

 # from the different

 # scores of each emotion

 val = parsed[0]["scores"]

 res = max(val, key = val.get)

 print ("\nEmotion :: ",res)

 

 conn.close()

except Exception as e:

 print(e.args)  
  
---  
  
 __

 __

The sample project using this api is available on **SnapLook**

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

  
  

  

My Personal Notes _arrow_drop_up_

Save

