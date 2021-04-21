Fetching top news using News API



News API is a simple JSON-based REST API for searching and retrieving news
articles from all over the web. Using this, one can fetch the top stories
running on a news website or can search top news on a specific topic (or
keyword).

News can be retrieved based on some criteria. Say the topic (keyword) to be
searched is ‘Geeksforgeeks’ or might be concerned to a specific channel. All
can be done, but the API key is needed to get started.  

    
    
    **Steps :**
    
    1. Visit https://newsapi.org/ to get your own API key.
    
    2. Install _requests_ package.

  
Below is the implementation of the above idea :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing requests package

import requests 

def NewsFromBBC():

 

 # BBC news api

 # following query parameters are used

 # source, sortBy and apiKey

 query_params = {

 "source": "bbc-news",

 "sortBy": "top",

 "apiKey": "4dbc17e007ab436fb66416009dfb59a8"

 }

 main_url = " https://newsapi.org/v1/articles"

 # fetching data in json format

 res = requests.get(main_url, params=query_params)

 open_bbc_page = res.json()

 # getting all articles in a string article

 article = open_bbc_page["articles"]

 # empty list which will

 # contain all trending news

 results = []

 

 for ar in article:

 results.append(ar["title"])

 

 for i in range(len(results)):

 

 # printing all trending news

 print(i + 1, results[i])

 #to read the news out loud for us

 from win32com.client import Dispatch

 speak = Dispatch("SAPI.Spvoice")

 speak.Speak(results) 

# Driver Code

if __name__ == '__main__':

 

 # function call

 NewsFromBBC()  
  
---  
  
 __

 __

 **Output :**  

  

  

    
    
    1 Italy to lift coronavirus travel restrictions
    2 White House 'Operation Warp Speed' to look for Covid jab
    3 Two Americas in the nation's capital
    4 Kobe Bryant helicopter crash post-mortem released
    5 Little things people are doing while socially distanced
    6 The last 'normal' photo on your phone
    7 'They came to kill the mothers'
    8 EU-UK Brexit trade talks in trouble
    9 Trial starts to see if dogs can 'sniff out' virus
    10 Beatles photographer Astrid Kirchherr dies aged 81

 **Note:** Output may change based on the top articles at the time.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

