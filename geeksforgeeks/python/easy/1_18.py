BeautifulSoup – Scraping Paragraphs from HTML



In this article, we will discuss how to scrap paragraphs from HTML using
Beautiful Soup

 **Method 1: using bs4 and urllib.**

 **Module Needed:**

  *  **bs4:** Beautiful Soup(bs4) is a Python library for pulling data out of HTML and XML files. For installing the module-

    
    
    pip install bs4.

  *  **urllib:** urllib is a package that collects several modules for working with URLs. It can also be installed the same way, it is most of the in-built in the environment itself.

    
    
    pip install urllib

The html file contains several tags and like the anchor tag <a>, span tag
<span>, paragraph tag <p> etc. So, the beautiful soup helps us to parse the
html file and get our desired output such as getting the paragraphs from a
particular url/html file.

 **Explanation:**

  

  

After importing the modules **urllib** and **bs4** we will provide a variable
with a url which is to be read, the **urllib.request.urlopen()** function
forwards the requests to the server for opening the url. **BeautifulSoup()**
function helps us to parse the html file or you say the encoding in html. The
loop used here with **find_all()** finds all the tags containing paragraph tag
<p></p> and the text between them are collected by the **get_text()** method.

 **Below is the implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing modules

import urllib.request 

from bs4 import BeautifulSoup

 

# providing url

url = "https://www.geeksforgeeks.org/how-to-automate-an-excel-sheet-in-
python/?ref=feed"

 

# opening the url for reading

html = urllib.request.urlopen(url)

 

# parsing the html file

htmlParse = BeautifulSoup(html, 'html.parser')

 

# getting all the paragraphs

for para in htmlParse.find_all("p"):

 print(para.get_text())  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210115200513/bop1.jpg)

 **Methods 2: using requests and bs4**

 **Module Needed:**

  *  **bs4:** Beautiful Soup(bs4) is a Python library for pulling data out of HTML and XML files. This module does not come built-in with Python. To install this type the below command in the terminal.

    
    
    pip install bs4

  *  **requests:** Requests allows you to send HTTP/1.1 requests extremely easily. This module also does not comes built-in with Python. To install this type the below command in the terminal.

    
    
    pip install requests

 **Approach:**

  * Import module
  * Create an HTML document and specify the ‘<p>’ tag into the code
  * Pass the HTML document into the Beautifulsoup() function
  * Use the ‘P’ tag to extract paragraphs from the Beautifulsoup object
  * Get text from the HTML document with get_text().

 **Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import requests 

import pandas as pd 

from bs4 import BeautifulSoup 

 

# link for extract html data 

def getdata(url): 

 r = requests.get(url) 

 return r.text 

 

htmldata = getdata("https://www.geeksforgeeks.org/how-to-automate-an-
excel-sheet-in-python/?ref=feed") 

soup = BeautifulSoup(htmldata, 'html.parser') 

data = '' 

for data in soup.find_all("p"): 

 print(data.get_text())   
  
---  
  
__

__

**Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210115200513/bop1.jpg)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

