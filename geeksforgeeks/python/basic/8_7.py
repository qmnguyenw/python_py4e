response.text – Python requests



 **response.text** returns the content of the response, in unicode. Basically,
it refers to Binary Response content. Python requests are generally used to
fetch the content from a particular resource URI. Whenever we make a request
to a specified URI through Python, it returns a response object. Now, this
response object would be used to access certain features such as content,
headers, etc. This article revolves around how to check the **response.text**
out of a response object.

#### How to use response.text using Python requests?

To illustrate use of response.text, let’s ping API of Github. To run this
script, you need to have Python and requests installed on your PC.

##### Prerequisites –

  * Download and Install Python 3 Latest Version
  * How to install requests in Python – For windows, linux, mac

##### Example code –

 __

 __  
 __

 __

 __  
 __  
 __

import requests

 

# Making a get request

response = requests.get('https://api.github.com')

 

# prinitng request text

print(response.text)  
  
---  
  
 __

 __

##### Example Implementation –

Save above file as request.py and run using

    
    
    Python request.py
    

##### Output –

![response.text-Python-requests](https://media.geeksforgeeks.org/wp-
content/uploads/20200228135432/response.text-Python-requests.png)  
Check the **content** at the start of output, it shows the entire content in
unicode.

#### Advanced Concepts

There are many libraries to make an HTTP request in Python, which are httplib,
urllib, httplib2 , treq, etc., but requests is the one of the best with cool
features. If any attribute of requests shows NULL, check the status code using
below attribute.

  

  

    
    
    requests.status_code

If status_code doesn’t lie in range of 200-29. You probably need to check
method begin used for making a request + the url you are requesting for
resources.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

