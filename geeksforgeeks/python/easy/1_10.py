How to read a JSON response from a link in Python?



There is a huge amount of data available on the web and most of them are in
form of (JavaScript Object Notation) **JSON**. But it is difficult for humans
to directly read and use it. To resolve this problem in python we have
different libraries which help us to read the JSON data fetched from the web.
These libraries have objects and functions which helps to open the URL from
the web and read the data.

To read a JSON response there is a widely used library called ****urllib in
python. This library helps to open the URL and read the JSON response from the
web. To use this library in python and fetch JSON response we have to import
the **json** and **urllib** in our code, The json.loads() method returns JSON
object. Below is the process by which we can read the JSON response from a
link or URL in python.

#### Approach:

  * Import required modules.
  * Assign URL.
  * Get the response of the URL using **urlopen()**.
  * Convert it to a JSON response using **json.loads()**.
  * Display the generated JSON response.

 **Implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import urllib library

from urllib.request import urlopen

 

# import json

import json

# store the URL in url as 

# parameter for urlopen

url = "https://api.github.com"

 

# store the response of URL

response = urlopen(url)

 

# storing the JSON response 

# from url in data

data_json = json.loads(response.read())

 

# print the json response

print(data_json)  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210213161807/output.png)

In this way, one can easily read a JSON response from a given URL by using
**urlopen()** method to get the response and then use **json.loads()** to
convert the response into a JSON object.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

