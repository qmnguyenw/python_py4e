Web Scraping using lxml and XPath in Python



 **Prerequisites:**Introduction to Web Scrapping

In this article, we will discuss the lxml python library to scrape data from a
webpage, which is built on top of the _libxml2_ XML parsing library written in
C. When compared to other python web scraping libraries like _BeautifulSoup_
and _Selenium_ , the _lxml_ package gives an advantage in terms of
performance. Reading and writing large XML files takes an indiscernible amount
of time, making data processing easier & much faster.

We will be using the **lxml** library for Web Scraping and the **requests**
library for making _HTTP_ requests in Python. These can be installed in the
command line using the pip package installer for Python.

Getting data from an element on the webpage using _lxml_ requires the usage of
_Xpaths_.

## Using XPath

 _XPath_ works very much like a traditional file system

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201001193629/Tree1.png)

Diagram of a File System

To access file 1,

    
    
    C:/File1
    

Similarly, To access file 2,

    
    
    C:/Documents/User1/File2
    

Now consider a simple web page,

## HTML

 __

 __  
 __

 __

 __  
 __  
 __

<html>

 <head>

 <title>My page</title>

 </head>

 <body>

 <h2>Welcome to my page<h2>

 <a href="www.example.com">page</a>

 

<p>This is the first paragraph</p>

 

 <h2>Hello World</h2>

 </body>

</html>  
  
---  
  
 __

 __

This can be represented as an XML Tree as follows,

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201001193756/tree2.png)

XML Tree of the Webpage

For getting the text inside the < _p >_ tag,

    
    
    XPath : html/body/p/text()
    
    
    
    Result : This is the first paragraph
    

For getting a value inside the < _href >_ attribute in the _anchor_ or < _a >_
tag,

    
    
    XPath : html/body/a/@href
    
    
    
    Result: www.example.com
    

For getting the value inside the second < _h2 >_ tag,

    
    
    XPath : html/body/h2[2]/text()
    
    
    
    Result: Hello World
    

#### To find the XPath for a particular element on a page:

  * Right-click the element in the page and click on _Inspect._
  * Right click on the element in the _Elements_ Tab.
  * Click on copy _XPath_.

##  **Using LXML**

#### Step-by-step Approach

  * We will use requests.get to retrieve the web page with our data.
  * We use html.fromstring to parse the content using the _lxml_ parser.
  * We create the correct _XPath_ query and use the _lxml xpath_ function to get the required element.

 **Example 1:**

  

  

Below is a program based on the above approach which uses a particular URL.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Import required modules

from lxml import html

import requests

 

# Request the page

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')

 

# Parsing the page

# (We need to use page.content rather than 

# page.text because html.fromstring implicitly

# expects bytes as input.)

tree = html.fromstring(page.content) 

 

# Get element using XPath

buyers = tree.xpath('//div[@title="buyer-name"]/text()')

print(buyers)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201007100603/ex1-300x79.png)

 **Example 2:**

Another example for an E-commerce website, URL.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Import required modules

from lxml import html

import requests

 

# Request the page

page = requests.get('https://webscraper.io/test-
sites/e-commerce/allinone')

 

# Parsing the page

tree = html.fromstring(page.content)

 

# Get element using XPath

prices = tree.xpath(

 '//div[@class="col-sm-4 col-lg-4 col-md-4"]/div/div[1]/h4[1]/text()')

print(prices)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201007100533/ex2-300x47.png)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

