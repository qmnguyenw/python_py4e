Convert HTML source code to JSON Object using Python



In this post, we will see how we can convert an HTML source code into a JSON
object. JSON objects can be easily transferred, and they are supported by most
of the modern programming languages. We can read JSON from Javascript and
parse it as a Javascript object easily. Javascript can be used to make HTML
for your web pages.

We will use **xmltojson** module in this post. The parse function of this
module takes the HTML as the input and returns the parsed JSON string.

>  **Syntax:** xmltojson.parse(xml_input, xml_attribs=True, item_depth=0,
> item_callback)
>
>  **Parameters:**
>
>   *  **xml_input** can be either a file or a string.
>   *  **xml_attribs** will include attributes if set to True. Otherwise,
> ignore them if set to False.
>   *  **item_depth** is the depth of children for which item_callback
> function is called when found.
>   *  **item_callback** is a callback function
>

 **Environment Setup:**

  

  

Install the required **** modules :

    
    
    pip install xmltojson
    pip install requests

 **Steps:**

  * Import the libraries

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import xmltojson

import json

import requests  
  
---  
  
 __

 __

  * Fetch the HTML code and save it into a file.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Sample URL to fetch the html page

url = "https://geeksforgeeks-example.surge.sh"

 

# Headers to mimic the browser

headers = {

 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)
AppleWebKit/537.36 \

 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'

}

 

# Get the page through get() method

html_response = requests.get(url=url, headers = headers)

 

# Save the page content as sample.html

with open("sample.html", "w") as html_file:

 html_file.write(html_response.text)  
  
---  
  
 __

 __

  * Use the parse function to convert this HTML into JSON. Open the HTML file and use the parse function of **xmltojson** module.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

withopen("sample.html", "r") as html_file:

 html = html_file.read()

 json_ = xmltojson.parse(html)  
  
---  
  
 __

 __

  * The **json_** variable contains a JSON string that we can print or dump into a file.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

withopen("data.json", "w") as file:

 json.dump(json_, file)  
  
---  
  
 __

 __

  * Print the output.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

print(json_)  
  
---  
  
 __

 __

 **Complete Code:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import xmltojson

import json

import requests

 

 

# Sample URL to fetch the html page

url = "https://geeksforgeeks-example.surge.sh"

 

# Headers to mimic the browser

headers = {

 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)
AppleWebKit/537.36 \

 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'

}

 

# Get the page through get() method

html_response = requests.get(url=url, headers = headers)

 

# Save the page content as sample.html

with open("sample.html", "w") as html_file:

 html_file.write(html_response.text)

 

with open("sample.html", "r") as html_file:

 html = html_file.read()

 json_ = xmltojson.parse(html)

 

with open("data.json", "w") as file:

 json.dump(json_, file)

 

print(json_)  
  
---  
  
 __

 __

 **Output:**

> {“html”: {“@lang”: “en”, “head”: {“title”: “Document”}, “body”: {“div”:
> {“h1”: “Geeks For Geeks”, “p”:
>
> “Welcome to the world of programming geeks!”, “input”: [{“@type”: “text”,
> “@placeholder”: “Enter your name”},
>
> {“@type”: “button”, “@value”: “submit”}]}}}}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

