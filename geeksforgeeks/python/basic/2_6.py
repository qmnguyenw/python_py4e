How to extract youtube data in Python?



 **Prerequisites:** Beautifulsoup

YouTube statistics of a YouTube channel can be used for analysis and it can
also be extracted using python code. A lot of data like viewCount,
subscriberCount, and videoCount can be retrieved. This article discusses 2
ways in which can be done.

###  **Method 1: Using YouTube API**

First we need to generate an API key. You need a Google Account to access the
Google API Console, request an API key, and register your application. You can
use Google APIs page to do so.

To extract data we need the channel id of the YouTube channel whose stats we
want to view. To get the channel id visit that particular YouTube channel and
copy the last part of the URL (In the examples given below channel id of
GeeksForGeeks channel are used).

**Approach**

  

  

  * First create youtube_statistics.py 
  * In this file extract data using YTstats class and generate a json file will all the data extracted.
  * Now create main.py
  * In main import youtube_statistics.py
  * Add API key and channel id
  * Now using the first file data corresponding to the key given will be retrieved and saved to json file.

 **Example :**

Code for main.py file :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from youtube_statistics import YTstats

 

# paste the API key generated by you here

API_KEY = "AIzaSyA-0KfpLK04NpQN1XghxhSlzG-WkC3DHLs"

 

 # paste the channel id here

channel_id = "UC0RhatS1pyxInC00YKjjBqQ"

 

yt = YTstats(API_KEY, channel_id)

yt.get_channel_statistics()

yt.dump()  
  
---  
  
 __

 __

 **Code for youtube_statistics.py file :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import requests

import json

 

 

class YTstats:

 

 def __init__(self, api_key, channel_id):

 self.api_key = api_key

 self.channel_id = channel_id

 self.channel_statistics = None

 

 def get_channel_statistics(self):

 url =
f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id;={self.channel_id}&key;={self.api_key}'

 

 json_url = requests.get(url)

 data = json.loads(json_url.text)

 

 try:

 data = data["items"][0]["statistics"]

 except:

 data = None

 

 self.channel_statistics = data

 return data

 

 def dump(self):

 if self.channel_statistics is None:

 return

 

 channel_title = "GeeksForGeeks"

 channel_title = channel_title.replace(" ", "_").lower()

 

 # generate a json file with all the statistics data of the youtube
channel

 file_name = channel_title + '.json'

 with open(file_name, 'w') as f:

 json.dump(self.channel_statistics, f, indent=4)

 print('file dumped')  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201228202017/Screenshot688.png)

###  **Method 2: Using BeautifulSoup**

Beautiful Soup is a Python library for pulling data out of HTML and XML files.
In this approach we will use BeautifulSoup and Selenium to scrape data from
YouTube channels. This program will tell the views, time since posted, title
and urls of the videos and print them using Python’s formatting.

  

  

 **Approach**

  * Import module
  * Provide url of the channel whose data is to be fetched
  * Extract data
  * Display data fetched.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import required packages

from selenium import webdriver

from bs4 import BeautifulSoup

 

# provide the url of the channel whose data you want to fetch

urls = [

 'https://www.youtube.com/channel/UC0RhatS1pyxInC00YKjjBqQ'

]

 

 

def main():

 driver = webdriver.Chrome()

 for url in urls:

 driver.get('{}/videos?view=0&sort;=p&flow;=grid'.format(url))

 content = driver.page_source.encode('utf-8').strip()

 soup = BeautifulSoup(content, 'lxml')

 titles = soup.findAll('a', id='video-title')

 views = soup.findAll(

 'span', class_='style-scope ytd-grid-video-renderer')

 video_urls = soup.findAll('a', id='video-title')

 print('Channel: {}'.format(url))

 i = 0 # views and time

 j = 0 # urls

 for title in titles[:10]:


print('\n{}\t{}\t{}\thttps://www.youtube.com{}'.format(title.text,

 views[i].text, views[i+1].text, video_urls[j].get('href')))

 i += 2

 j += 1

 

 

main()  
  
---  
  
 __

 __

 **Output**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201228211036/Screenshot684.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save
