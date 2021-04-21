Scraping websites with Newspaper3k in Python



Web Scraping is a powerful tool to gather information from a website. To
scrape multiple URLs, we can use a Python library called _Newspaper3k_. The
_Newspaper3k_ package is a Python library used for Web Scraping articles, It
is built on top of requests and for parsing _lxml_. This module is a modified
and better version of the _Newspaper_ module which is also used for the same
purpose.

### Installation:

To install this module type the below command in the terminal.

    
    
    pip install newspaper3k
    

### **Step-by-step Approach:**

  1. First we will define a list containing the URLs or assign a single URL. 
  2. We will create an _Article_ object passing in the parameters such as the name of the URL and optional parameters like language=’en’, for English
  3. We will then download and parse the file.
  4. Finally, display the data extracted.

 **Below are some examples based on the above approach:**

 **Example 1**

Below is a program to scarp data from a given URL.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import required module

import newspaper

 

# Assingn url

url = 'https://www.geeksforgeeks.org/top-5-open-source-online-machine-
learning-environments/'

 

# Extract web data

url_i = newspaper.Article(url="%s" % (url), language='en')

url_i.download()

url_i.parse()

 

# Display scrapped data

print(url_i.text)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201026173524/Screenshot587.png)

 **Example 2**

Here, we scrap data from multiple URLs and then display it.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import required modules

import newspaper

 

# Define list of urls

list_of_urls = ['https://www.geeksforgeeks.org/how-to-get-the-
magnitude-of-a-vector-in-numpy/',

 'https://www.geeksforgeeks.org/3d-wireframe-plotting-in-python-using-
matplotlib/',

 'https://www.geeksforgeeks.org/difference-between-small-data-and-big-
data/']

 

# Parse through each url and display its content

for url in list_of_urls:

 url_i = newspaper.Article(url="%s" % (url),
language='en')

 url_i.download()

 url_i.parse()

 print(url_i.text)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201026175226/Screenshot588.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

