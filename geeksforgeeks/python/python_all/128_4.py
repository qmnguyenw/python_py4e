Read latest news using newsapi | Python



In this article, we will learn how to create a Python script to read the
latest news. We will fetch news from news API and after that, we will read
news using pyttsx3.

 **Modules required :**

    
    
     **pyttsx3 -** pip install pyttsx3
    **requests -** pip install requests

 **Getting news API :**  
To get a API for news we will use newsapi.org. we will create account and take
API key by clicking on get API button.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190727111935/Screenshot-from-2019-07-27-11-17-15.png)

 **Step #1:** Import modules needed

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import pyttsx3

import requests

import json

import time  
  
---  
  
 __

 __

 **Step #2:** Setting up URL with API key, place your API key here.

 __

 __  
 __

 __

 __  
 __  
 __

url= ('https://newsapi.org/v2/top-headlines?'

 'country = in&'

 'apiKey =')

 

url += 'your_api_key_here'  
  
---  
  
 __

 __

 **Step #3:** Setting an engine for pyttsx3 for reading news.

 __

 __  
 __

 __

 __  
 __  
 __

engine= pyttsx3.init()  
  
---  
  
 __

 __

 **Step #4:** Setting up properties of our engine, means reading rate, volume,
and sound of a voice.

 __

 __  
 __

 __

 __  
 __  
 __

rate= engine.getProperty('rate')

engine.setProperty('rate', rate + 10)

 

volume = engine.getProperty('volume')

engine.setProperty('volume', volume-0.60)

 

sound = engine.getProperty ('voices');

engine.setProperty('voice', 'sound[1].id')  
  
---  
  
 __

 __

 **Step #5:** Trying to send request to get news. Here, **engine.say()**
function is used to read news.

 __

 __  
 __

 __

 __  
 __  
 __

try:

 response = requests.get(url)

except:

 engine.say("can, t access link, plz check you internet ")

 

news = json.loads(response.text)  
  
---  
  
 __

 __

 __

 __  
 __

 __

 __  
 __  
 __

for new in news['articles']:


print("##############################################################\n")

 print(str(new['title']), "\n\n")

 engine.say(str(new['title']))

 print('______________________________________________________\n')

 

 engine.runAndWait()

 

 print(str(new['description']), "\n\n")

 engine.say(str(new['description']))

 engine.runAndWait()


print("..............................................................")

 time.sleep(2)  
  
---  
  
 __

 __

Now, everything is ready build a loop to read new articles.

  
Below is the complete Python implementation :

 __

 __  
 __

 __

 __  
 __  
 __

import pyttsx3

import requests

import json

import time

 

url = ('https://newsapi.org/v2/top-headlines?'

 'country = in&'

 'apiKey =')

 

url +='your_api_key_here'

 

 

engine = pyttsx3.init()

rate = engine.getProperty('rate')

engine.setProperty('rate', rate + 10)

 

volume = engine.getProperty('volume')

engine.setProperty('volume', volume-0.60)

 

sound = engine.getProperty ('voices');

engine.setProperty('voice', 'sound[1].id')

 

 

try:

 response = requests.get(url)

except:

 engine.say("can, t access link, plz check you internet ")

 

news = json.loads(response.text)

 

 

for new in news['articles']:


print("##############################################################\n")

 print(str(new['title']), "\n\n")

 engine.say(str(new['title']))

 print('______________________________________________________\n')

 

 engine.runAndWait()

 

 print(str(new['description']), "\n\n")

 engine.say(str(new['description']))

 engine.runAndWait()


print("..............................................................")

 time.sleep(2)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190727113536/Screenshot-from-2019-07-27-11-34-46.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

