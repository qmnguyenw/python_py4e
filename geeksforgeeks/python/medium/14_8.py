Download Instagram profile pic using Python



Instagram is a photo and video-sharing social networking service owned by
Facebook, Python provides powerful tools for web scraping of Instagram.  
 **Modules required and Installation:**  
 **requests –**  

    
    
    pip install requests
    

**concept –**  
For a given user profile, open _view-source_ and find _“profile_pic_url_hd”_ .
To find press ctrl+f and type _“profile_pic_url_hd”_ the link with it is our
data or profile pic.  
link will look link :  

    
    
    https://scontent-bom1-1.cdninstagram.com/vp/d2df9b2d162969e87200984ee763cc27/5DC590F2/t51.2885-19/s320x320/61851740_845288152518430_7068999703693623296_n.jpg?_nc_ht=scontent-bom1-1.cdninstagram.com
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190809214848/Screenshot-from-2019-08-09-16-51-572.png)

Below is the stepwise implementation of the project –  
**Step 1:** import all dependence  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import requests

from bs4 import BeautifulSoup as bs

import json

import random

import os.path  
  
---  
  
 __

 __

 **Step 2:** Ask for username and send a response to Instagram.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

insta_url='https://www.instagram.com'

inta_username= input('enter username of instagram : ')

response = requests.get(f"{insta_url}/{inta_username}/")  
  
---  
  
 __

 __

 **Step 3:** if the response is ok, find profile photo link

( **Note:** replace ‘\\\u0026’ with ‘&’ in the string_url to remove bad URL
timestamp or bad URL hash error)  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

if response.ok:

 html=response.text

 bs_html=bs(html, features="lxml")

 bs_html=bs_html.text

 index=bs_html.find('profile_pic_url_hd')+21

 remaining_text=bs_html[index:]


remaining_text_index=remaining_text.find('requested_by_viewer')-3


string_url=remaining_text[:remaining_text_index].replace("\\u0026","&")

 print(string_url, "\n \n downloading..........")  
  
---  
  
 __

 __

 **Step 4:** Now, create a loop and download photo.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

while True:

 filename='pic'+str(random.randint(1,
100000))+'.jpg'

 file_exists = os.path.isfile(filename)

 if not file_exists:

 with open(filename, 'wb+') as handle:

 response = requests.get(string_url, stream=True)

 if not response.ok:

 print(response)

 for block in response.iter_content(1024):

 if not block:

 break

 handle.write(block)

 else:

 continue

 break

print("\n downloading completed ..............")  
  
---  
  
 __

 __

 **Complete code :**  

Python3″ 1=”=

    
    
    import requests
    from bs4 import BeautifulSoup as bs
    import json
    import random
    import os.path
    
    insta_url = 'https://www.instagram.com'
    inta_username = input('enter username of instagram : ')
    
    response = requests.get(f"{insta_url}/{inta_username}/")
    
    if response.ok:
        html = response.text
        bs_html = bs(html, features="lxml")
        bs_html = bs_html.text
        index = bs_html.find('profile_pic_url_hd')+21
        remaining_text = bs_html[index:]
        remaining_text_index = remaining_text.find('requested_by_viewer')-3
        string_url = remaining_text[:remaining_text_index].replace("\\u0026", "&")
    
        print(string_url, "\n \n downloading..........")
    
    
    while True:
        filename = 'pic'+str(random.randint(1, 100000))+'.jpg'
        file_exists = os.path.isfile(filename)
    
        if not file_exists:
            with open(filename, 'wb+') as handle:
                response = requests.get(string_url, stream=True)
                if not response.ok:
                    print(response)
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
        else:
            continue
        break
    print("\n                downloading completed ..............")
    

