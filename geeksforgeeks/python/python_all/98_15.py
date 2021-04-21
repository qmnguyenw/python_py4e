Python – Convert JSON to string



Data in transmitted accross platforms using API calls. Data is mostly retrived
in JSON format. We can convert the obtained JSON data into String data for the
ease of storing and working with it.

Let’s see how to convert JSON to String.

 **Method #1:** Json to String on dummy data using “json.dumps”

 __

 __  
 __

 __

 __  
 __  
 __

import json

 

# create a sample json

 

a = {"name" : "GeeksforGeeks", "Topic" : "Json to
String", "Method": 1}

 

# Convert JSON to String

 

y = json.dumps(a)

 

print(y)

print(type(y))  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200129135419/Screenshot-from-2020-01-29-13-53-41.png)

 **Method #2:** Json to String using an API using requests and “json.dumps”

 __

 __  
 __

 __

 __  
 __  
 __

import json 

import requests 

 

# Get dummy data using an API

res =
requests.get("http://dummy.restapiexample.com/api/v1/employees")

 

# Convert data to dict

data = json.loads(res.text)

 

# Convert dict to string

data = json.dumps(data)

 

print(data)

print(type(data))  
  
---  
  
 __

 __

 **Output: **

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200129135517/Screenshot-from-2020-01-29-13-54-51.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

****

