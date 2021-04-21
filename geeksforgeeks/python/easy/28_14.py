Python Desktop News Notifier in 20 lines



To get started with the Desktop News Notifier, we require two libraries:
feedparser and notify2.  
Give following command to to install feedparser:

    
    
    sudo pip3 install feedparser

For installing notify2 in your terminal:

    
    
    sudo pip3 install notify2

Feedparser wil parse the feed that we will get from the URL. We will use
notify2 for the desktop notification purpose. Other than these two libararies,
we will use OS and time lib. Once you are done with the installation import
both libraries in the program. Here, in this example i have parsed the news
from the BBC UK, you can use any news feedparser URL. Let’s have a look at the
program:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# desktop news notifier

import feedparser

import notify2

import os

import time

def parseFeed():

 f = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")

 ICON_PATH = os.getcwd() + "/icon.ico"

 notify2.init('News Notify')

 for newsitem in f['items']: 

 n = notify2.Notification(newsitem['title'], 

 newsitem['summary'], 

 icon=ICON_PATH 

 )

 n.set_urgency(notify2.URGENCY_NORMAL)

 n.show()

 n.set_timeout(15000)

 time.sleep(1200)

 

if __name__ == '__main__':

 parseFeed()  
  
---  
  
 __

 __

 **Screenshot of the news notification popup**

![Python Desktop News Notifier in 20
lines](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2017-04-24-10_00_06.png)

  

  

 **Step by step Explanation of Code:  
**

  1.     f = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")

Here feedparser will parse the news data from the feed URL. The parsed data
will be in the form of dictionary.

  2.     ICON_PATH = os.getcwd() + "/icon.ico"

If you want to set any icon in the notification then here we are setting the
Icon path. This is optional.

  3.     notify2.init('News Notify')

Here we are initializing the notify2 using the init method of notify2.
Initialize the D-Bus connection. Must be called before you send any
notifications, or retrieve server info or capabilities.

  4.      for newsitem in f['items']: 
            n = notify2.Notification(newsitem['title'], 
                                     newsitem['summary'], 
                                     icon=ICON_PATH 
                                     )

Looping from the parsed data to get the relevant information like news title,
short summary and setting the notification icon using the Notification method
of the notify2 lib.

  5.     n.set_urgency(notify2.URGENCY_NORMAL)

Set the urgency level to one of URGENCY_LOW, URGENCY_NORMAL or
URGENCY_CRITICAL

  6.     n.show()

This method will show the notification on the Desktop

  7.     n.set_timeout(15000)

Setting the time to keep the notification on the desktop (in milliseconds). I
have set here as 15 seconds.

  8.     time.sleep(1200)

This will usually display the news notification every 20 mins. You can set the
time as per your requirement. You can find the full source code that is hosted
on GitHub

This article is contributed by **Srce Cde**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

