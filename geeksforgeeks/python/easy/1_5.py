BeautifulSoup – Find tags by CSS class with CSS Selectors



 **Prerequisites** : Beautifulsoup

Beautifulsoup is a Python library used for web scraping. BeautifulSoup object
is provided by Beautiful Soup which is a web scraping framework for Python.
Web scraping is the process of extracting data from the website using
automated tools to make the process faster. The BeautifulSoup object
represents the parsed document as a whole. This powerful python tool can also
be used to modify HTML webpages. This article depicts how beautifulsoup can be
employed to find tag by CSS class with CSS Selectors. For this, **find_all()**
method of the module is used.

 **Syntax:**

> find_all(class_=”class_name”)
>
> Retruns tags having a particular CSS class.
>
>  
>
>
>  
>

 **Approach:**

  * Import module
  * Scrap data from a webpage.
  * Parse the string scraped to HTML.
  * Use find_all() function to get a list of tag with the given class name.
  * Print tags.

 **Example 1:** Finding all tags of a particular CSS class from an HTML file.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing module

from bs4 import BeautifulSoup

 

markup = """

 

<!DOCTYPE>

<html>

 <head><title>Example</title></head>

 <body>

 <div class="first"> Div with Class first

 </div> 

 <p class="first"> Para with Class first

 </p>

 

 <div class="second"> Div with Class second

 </div>

 <span class="first"> Span with Class first

 </span> 

 </body>

</html>

"""

 

# parsering string to HTML

soup = BeautifulSoup(markup, 'html.parser')

 

# printing tags with given class name

for i in soup.find_all(class_="first"):

 print(i.name)  
  
---  
  
 __

 __

 **Output:**

    
    
    div
    p
    span

 **Example 2:** Finding all tags of a particular CSS class from a URL.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing module

from bs4 import BeautifulSoup

import requests

 

URL = "https://www.geeksforgeeks.org/"

html = requests.get(URL)

 

# parsering string to HTML

soup = BeautifulSoup(html.content, "html5lib")

 

# printing tags with given class name

for i in soup.find_all(class_="article--container_content"):

 print(i.name)  
  
---  
  
 __

 __

 **Output:**

    
    
    div

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

