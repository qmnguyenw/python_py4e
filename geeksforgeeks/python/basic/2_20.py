Scrape Google Search Results using Python BeautifulSoup



In this article, we are going to see how to Scrape Google Search Results using
Python BeautifulSoup.

###  **Module Needed:**

  *  **bs4:** Beautiful Soup(bs4) is a Python library for pulling data out of HTML and XML files. This module does not come built-in with Python. To install this type the below command in the terminal.

    
    
    pip install bs4
    

  * **requests:** Requests allows you to send HTTP/1.1 requests extremely easily. This module also does not come built-in with Python. To install this type the below command in the terminal.

    
    
    pip install requests
    

### **Approach:**

  * Import the beautifulsoup and request libraries.
  * Make two strings with the default Google search URL, **‘https://google.com/search?q=’** and our customized search keyword.
  * Concatenate these two strings to get our search URL.
  * Fetch the URL data using **requests.get(url),** store it in a variable, **request_result**.
  * Create a string and store the result of our fetched request, using **request_result.text.**
  * Now we use BeautifulSoup to analyze the extracted page. We can simply create an object to perform those operations but beautifulsoup comes with a lot of in-built features to scrape the web. We have created a soup object first using beautifulsoup from the request-response
  *  **** We can do **soup.find.all(h3)** to grab all major headings of our search result, Iterate through the object and print it as a string.

 **Example 1:** Below is the implementation of the above approach.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import the beautifulsoup

# and request libraries of python.

import requests

import bs4

 

# Make two strings with default google search URL

# 'https://google.com/search?q=' and

# our customized search keyword.

# Concatenate them

text= "geeksforgeeks"

url = 'https://google.com/search?q=' + text

 

# Fetch the URL data using requests.get(url),

# store it in a variable, request_result.

request_result=requests.get( url )

 

# Creating soup from the fetched request

soup = bs4.BeautifulSoup(request_result.text,

 "html.parser")

print(soup)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201124131944/Capture-660x214.PNG)

  

  

Let’s We can do **soup.find.all(h3)** to grab all major headings of our search
result, Iterate through the object and print it as a string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# soup.find.all( h3 ) to grab

# all major headings of our search result,

heading_object=soup.find_all( 'h3' )

 

# Iterate through the object 

# and print it as a string.

for info in heading_object:

 print(info.getText())

 print("------")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201124132133/Capture.PNG)

 **Example 2:** Below is the implementation. In the form of extracting the
city temperature using Google search:

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import requests 

import bs4 

 

# Taking thecity name as an input from the user

city = "Imphal"

 

# Generating the url 

url = "https://google.com/search?q=weather+in+" + city

 

# Sending HTTP request 

request_result = requests.get( url )

 

# Pulling HTTP data from internet 

soup = bs4.BeautifulSoup( request_result.text 

 , "html.parser" )

 

# Finding temperature in Celsius.

# The temperature is stored inside the class "BNeawe". 

temp = soup.find( "div" , class_='BNeawe' ).text 

 

print( temp )   
  
---  
  
__

__

**Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201120074706/Screenshot162.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

