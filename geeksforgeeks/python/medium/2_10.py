How to Extract Weather Data from Google in Python?



In this article, we will see how to extract weather data from google. Google
does not have its own weather API, it fetches data from weather.com and shows
it when you search on Google. So, we will scrape the data from Google.

 **Module needed:**

 **Requests:** Requests allows you to send HTTP/1.1 requests extremely easily.
This module also does not comes built-in with Python. To install this type the
below command in the terminal.

    
    
    pip install requests

 **bs4:** Beautiful Soup is a library that makes it easy to scrape information
from web pages. Whether it be an HTML or XML page, that can later be used for
iterating, searching, and modifying the data within it.

 **Approach:**

  

  

  * Import the module
  * Enter the city name with the URL

    
    
    "https://www.google.com/search?q="+"weather"+{cityname}

  * Make requests instance and pass the URL
  * Get the raw data.
  * Extract the required data from the soup.
  * Finally, print the required data.

 **Step-wise implementation of code:**

Step 1: Import the requests and bs4 library

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the library

import requests

from bs4 import BeautifulSoup  
  
---  
  
 __

 __

 **Step 2:** Create a URL with the entered city name in it and pass it to the
get function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# enter city name

city = "lucknow"

 

# create url

url = "https://www.google.com/search?q="+"weather"+city

 

# requests instance

html = requests.get(url).content

 

# getting raw data

soup = BeautifulSoup(html, 'html.parser')  
  
---  
  
 __

 __

 **Step 3:** Soup will return a heap of data with HTML tags. So, a chunk of
data has been shown below from which we will get all the necessary data with
the help of find function and passing the tag name and class name.

> <div class=”kvKEAb”><div><div><div class=”BNeawe iBp4i AP7Wnd”><div><div
> class=”BNeawe  
> iBp4i AP7Wnd”>13°C</div></div></div></div></div><div><div><div class=”BNeawe
> tAd8D AP7Wnd”>  
> <div><div class=”BNeawe tAd8D AP7Wnd”>Saturday 11:10 am

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# get the temperature

temp = soup.find('div', attrs={'class': 'BNeawe iBp4i
AP7Wnd'}).text

 

# this conatains time and sky description

str = soup.find('div', attrs={'class': 'BNeawe tAd8D
AP7Wnd'}).text

 

# format the data

data = str.split('\n')

time = data[0]

sky = data[1]  
  
---  
  
 __

 __

