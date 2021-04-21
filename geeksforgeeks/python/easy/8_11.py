Getting Instagram profile details using Python



Instagram is a photo and video-sharing social networking service owned by
Facebook. In this article, we will learn how can we get Instagram profile
details using web scraping. Python provides powerful tools for web scraping,
we will be using BeautifulSoup here.

 **Modules required and Installation:**

 **Requests :**  
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no
need to manually add query strings to your URLs.

    
    
    pip install requests

 **Beautiful Soup:**  
Beautiful Soup is a library that makes it easy to scrape information from web
pages. It sits atop an HTML or XML parser, providing Pythonic idioms for
iterating, searching, and modifying the parse tree.

    
    
    pip install beautifulsoup4

  

  

**Explanation –**

For a given user name data scraping will be done then parsing of data will be
done so that output can be readable. The output will be description i.e
followers count, following count, count of posts.

Below is the implementation –

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

from bs4 import BeautifulSoup

import requests

 

# instagram URL

URL = "https://www.instagram.com/{}/"

 

# parse function

def parse_data(s):

 

 # creating a dictionary

 data = {}

 

 # splittting the content 

 # then taking the first part

 s = s.split("-")[0]

 

 # again splitting the content 

 s = s.split(" ")

 

 # assigning the values

 data['Followers'] = s[0]

 data['Following'] = s[2]

 data['Posts'] = s[4]

 

 # returning the dictionary

 return data

 

# scrape function

def scrape_data(username):

 

 # getting the request from url

 r = requests.get(URL.format(username))

 

 # converting the text

 s = BeautifulSoup(r.text, "html.parser")

 

 # finding meta info

 meta = s.find("meta", property ="og:description")

 

 # calling parse method

 return parse_data(meta.attrs['content'])

 

# main function

if __name__=="__main__":

 

 # user name

 username = "geeks_for_geeks"

 

 # calling scrape function

 data = scrape_data(username)

 

 # printing the info

 print(data)  
  
---  
  
 __

 __

 **Output :**

    
    
    {'Followers': '120.2k', 'Following': '0', 'Posts': '702'}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

