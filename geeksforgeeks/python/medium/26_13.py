Tweet using Python



Twitter is an online news and social networking service where users post and
interact with messages. These posts are known as “tweets”. Twitter is known as
the social media site for robots. We can use Python for posting the tweets
without even opening the website. There is a Python library which is used for
accessing the Python API, known as tweepy. Here, we are going to use tweepy
for doing the same.  
Tweepy is not the native library. You need to install it before using it.
Installation is easy when you have pip. In the Terminal or Command Prompt,
type the following command to install tweepy.

    
    
    sudo install pip tweepy
    

In case you don’t have pip, install it as an external library.  
Don’t forget to change the change the application type from “Read only” to
“Read and write” in the settings. This given the permission to tweet as well.  
After this, go to https://apps.twitter.com/. This is used to create a link
between your script and Twitter. In “Keys and Access Tokens” tab, get the
Consumer Key (API Key), Consumer Secret (API secret), Access Token and Access
Token Secret.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

### Posting a simple tweet

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import tweepy

 

# personal details

consumer_key ="xxxxxxxxxxxxxxxx"

consumer_secret ="xxxxxxxxxxxxxxxx"

access_token ="xxxxxxxxxxxxxxxx"

access_token_secret ="xxxxxxxxxxxxxxxx"

 

# authentication of consumer key and secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

 

# authentication of access token and secret

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

 

# update the status

api.update_status(status ="Hello Everyone !")  
  
---  
  
 __

 __

This is the simple method which will set the tweet “Hello Everyone!”. This is
an easy process and doesn’t hold much any importance in real life. It is
integrated into bigger programs for some useful work. We can use for loop to
tweet a large number of tweets. For maintaining the time period between any
two tweets in the loop, we can use sleep() function from the time module as
shown.

 __

 __  
 __

 __

 __  
 __  
 __

time.sleep(600) # waits for 600 seconds  
  
---  
  
 __

 __

This was all about posting a text tweet. What if we want to post a tweet with
a media file, there is a separate method for that.

  

  

### Posting a tweet with a media file

Sometimes, a user wants to post a tweet with a media file which is quite
simple if we use the website interface. Posting with the help of Python takes
some effort. It is same as posting the text-only tweet with just two lines of
code addition.

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import tweepy

 

# personal information

consumer_key ="xxxxxxxxxxxxxxxx"

consumer_secret ="xxxxxxxxxxxxxxxx"

access_token ="xxxxxxxxxxxxxxxx"

access_token_secret ="xxxxxxxxxxxxxxxx"

 

# authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

 

api = tweepy.API(auth)

tweet ="Text part of the tweet" # toDo

image_path ="path of the image" # toDo

 

# to attach the media file

status = api.update_with_media(image_path, tweet) 

api.update_status(status = tweet)  
  
---  
  
 __

 __

Please don’t forget to change the Application type as stated above. Without
changing it, we can’t have the access to post.

This article is contributed by **Rishabh Bansal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

