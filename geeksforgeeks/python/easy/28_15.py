Extraction of Tweets using Tweepy



 **Introduction:** Twitter is a popular social network where users share
messages called tweets. Twitter allows us to mine the data of any user using
Twitter API or Tweepy. The data will be tweets extracted from the user. The
first thing to do is get the consumer key, consumer secret, access key and
access secret from twitter developer available easily for each user. These
keys will help the API for authentication.

 **Steps to obtain keys:**  
– Login to twitter developer section  
– Go to “Create an App”  
– Fill the details of the application.  
– Click on Create your Twitter Application  
– Details of your new app will be shown along with consumer key and consumer
secret.  
– For access token, click ” Create my access token”. The page will refresh and
generate access token.

Tweepy is one of the library that should be installed using pip. Now in order
to authorize our app to access Twitter on our behalf, we need to use the OAuth
Interface. Tweepy provides the convenient Cursor interface to iterate through
different types of objects. Twitter allows a maximum of 3200 tweets for
extraction.

These all are the prerequisite that have to be used before getting tweets of a
user.

 **Code(with explanation) :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import tweepy

 

# Fill the X's with the credentials obtained by 

# following the above mentioned procedure.

consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

access_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

access_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

 

# Function to extract tweets

def get_tweets(username):

 

 # Authorization to consumer key and consumer secret

 auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

 

 # Access to user's access key and access secret

 auth.set_access_token(access_key, access_secret)

 

 # Calling api

 api = tweepy.API(auth)

 

 # 200 tweets to be extracted

 number_of_tweets=200

 tweets = api.user_timeline(screen_name=username)

 

 # Empty Array

 tmp=[] 

 

 # create array of tweet information: username, 

 # tweet id, date/time, text

 tweets_for_csv = [tweet.text for tweet in tweets] # CSV file
created 

 for j in tweets_for_csv:

 

 # Appending tweets to the empty array tmp

 tmp.append(j) 

 

 # Printing the tweets

 print(tmp)

 

 

# Driver code

if __name__ == '__main__':

 

 # Here goes the twitter handle for the user

 # whose tweets are to be extracted.

 get_tweets("twitter-handle")   
  
---  
  
__

__

**Conclusion :**  
The above script would generate all the tweets of the particular user and
would be appended to the empty array tmp. Here Tweepy is introduced as a tool
to access Twitter data in a fairly easy way with Python. There are different
types of data we can collect, with the obvious focus on the “tweet” object.
Once we have collected some data, the possibilities in terms of analytics
applications are endless.

One such application of extracting tweets is sentiment or emotion analysis.
The emotion of the user can be obtained from the tweets by tokenizing each
word and applying machine learning algorithms on that data. Such emotion or
sentiment detection is used worldwide and will be broadly used in the future.

This article is contributed by **Ayush Govil**. If you like GeeksforGeeks and
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

