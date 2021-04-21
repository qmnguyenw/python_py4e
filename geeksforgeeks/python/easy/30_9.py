Twitter Sentiment Analysis using Python



This article covers the sentiment analysis of any topic by parsing the tweets
fetched from Twitter using Python.

![sentiment-
analysis](https://indianpythonista.files.wordpress.com/2017/01/sentiment-
analysis.jpg)

 **What is sentiment analysis?  
** Sentiment Analysis is the process of ‘computationally’ determining whether
a piece of writing is positive, negative or neutral. It’s also known as
**opinion mining** , deriving the opinion or attitude of a speaker.

 **Why sentiment analysis?**

  *  **Business:** In marketing field companies use it to develop their strategies, to understand customers’ feelings towards products or brand, how people respond to their campaigns or product launches and why consumers don’t buy some  
products.

  *  **Politics:** In political field, it is used to keep track of political view, to detect consistency and inconsistency between statements and actions at the government level. It can be used to predict election results as well!
  *  **Public Actions:** Sentiment analysis also is used to monitor and analyse social phenomena, for the spotting of potentially dangerous situations and determining the general mood of the blogosphere.

 **Installation:**

  

  

  *  **Tweepy:**tweepy is the python client for the official Twitter API.  
Install it using following pip command:

    
        pip install tweepy

  *  **TextBlob:**textblob is the python library for processing textual data.  
Install it using following pip command:

    
        pip install textblob

Also, we need to install some NLTK corpora using following command:

    
        python -m textblob.download_corpora

(Corpora is nothing but a large and structured set of texts.)

 **Authentication:  
** In order to fetch tweets through Twitter API, one needs to register an App
through their twitter account. Follow these steps for the same:

  * Open this link and click the button: ‘Create New App’
  * Fill the application details. You can leave the callback url field empty.
  * Once the app is created, you will be redirected to the app page.
  * Open the ‘Keys and Access Tokens’ tab.
  * Copy ‘Consumer Key’, ‘Consumer Secret’, ‘Access token’ and ‘Access Token Secret’.

 **Implementation:**

 __

 __  
 __

 __

 __  
 __  
 __

import re

import tweepy

from tweepy import OAuthHandler

from textblob import TextBlob

 

class TwitterClient(object):

 '''

 Generic Twitter Class for sentiment analysis.

 '''

 def __init__(self):

 '''

 Class constructor or initialization method.

 '''

 # keys and tokens from the Twitter Dev Console

 consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXX'

 consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'

 access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'

 access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

 

 # attempt authentication

 try:

 # create OAuthHandler object

 self.auth = OAuthHandler(consumer_key, consumer_secret)

 # set access token and secret

 self.auth.set_access_token(access_token, access_token_secret)

 # create tweepy API object to fetch tweets

 self.api = tweepy.API(self.auth)

 except:

 print("Error: Authentication Failed")

 

 def clean_tweet(self, tweet):

 '''

 Utility function to clean tweet text by removing links, special
characters

 using simple regex statements.

 '''

 return '
'.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z
\t])

 |(\w+:\/\/\S+)", " ", tweet).split())

 

 def get_tweet_sentiment(self, tweet):

 '''

 Utility function to classify sentiment of passed tweet

 using textblob's sentiment method

 '''

 # create TextBlob object of passed tweet text

 analysis = TextBlob(self.clean_tweet(tweet))

 # set sentiment

 if analysis.sentiment.polarity > 0:

 return 'positive'

 elif analysis.sentiment.polarity == 0:

 return 'neutral'

 else:

 return 'negative'

 

 def get_tweets(self, query, count = 10):

 '''

 Main function to fetch tweets and parse them.

 '''

 # empty list to store parsed tweets

 tweets = []

 

 try:

 # call twitter api to fetch tweets

 fetched_tweets = self.api.search(q = query, count = count)

 

 # parsing tweets one by one

 for tweet in fetched_tweets:

 # empty dictionary to store required params of a tweet

 parsed_tweet = {}

 

 # saving text of tweet

 parsed_tweet['text'] = tweet.text

 # saving sentiment of tweet

 parsed_tweet['sentiment'] =
self.get_tweet_sentiment(tweet.text)

 

 # appending parsed tweet to tweets list

 if tweet.retweet_count > 0:

 # if tweet has retweets, ensure that it is appended only once

 if parsed_tweet not in tweets:

 tweets.append(parsed_tweet)

 else:

 tweets.append(parsed_tweet)

 

 # return parsed tweets

 return tweets

 

 except tweepy.TweepError as e:

 # print error (if any)

 print("Error : " + str(e))

 

def main():

 # creating object of TwitterClient Class

 api = TwitterClient()

 # calling function to get tweets

 tweets = api.get_tweets(query = 'Donald Trump', count =
200)

 

 # picking positive tweets from tweets

 ptweets = [tweet for tweet in tweets if
tweet['sentiment'] == 'positive']

 # percentage of positive tweets

 print("Positive tweets percentage: {}
%".format(100*len(ptweets)/len(tweets)))

 # picking negative tweets from tweets

 ntweets = [tweet for tweet in tweets if
tweet['sentiment'] == 'negative']

 # percentage of negative tweets

 print("Negative tweets percentage: {}
%".format(100*len(ntweets)/len(tweets)))

 # percentage of neutral tweets

 print("Neutral tweets percentage: {} % \

 ".format(100*(len(tweets) -(len( ntweets
)+len( ptweets)))/len(tweets)))

 

 # printing first 5 positive tweets

 print("\n\nPositive tweets:")

 for tweet in ptweets[:10]:

 print(tweet['text'])

 

 # printing first 5 negative tweets

 print("\n\nNegative tweets:")

 for tweet in ntweets[:10]:

 print(tweet['text'])

 

if __name__ == "__main__":

 # calling main function

 main()  
  
---  
  
 __

 __

Here is how a sample output looks like when above program is run:

    
    
    Positive tweets percentage: 22 %
    Negative tweets percentage: 15 %
    
    
    Positive tweets:
    RT @JohnGGalt: Amazing—after years of attacking Donald Trump the media managed
    to turn #InaugurationDay into all about themselves.
    #MakeAme…
    RT @vooda1: CNN Declines to Air White House Press Conference Live YES! 
    THANK YOU @CNN FOR NOT LEGITIMI…
    RT @Muheeb_Shawwa: Donald J. Trump's speech sounded eerily familiar...
    POTUS plans new deal for UK as Theresa May to be first foreign leader to meet new 
    president since inauguration 
    .@realdonaldtrump #Syria #Mexico #Russia & now #Afghanistan. 
    Another #DearDonaldTrump Letter worth a read @AJEnglish 
    
    
    Negative tweets:
    RT @Slate: Donald Trump’s administration: “Government by the worst men.” 
    RT @RVAwonk: Trump, Sean Spicer, et al. lie for a reason. 
    Their lies are not just lies. Their lies are authoritarian propaganda.  
    RT @KomptonMusic: Me: I hate corn 
    Donald Trump: I hate corn too
    Me: https://t.co/GPgy8R8HB5
    It's ridiculous that people are more annoyed at this than Donald Trump's sexism.
    RT @tony_broach: Chris Wallace on Fox news right now talking crap 
    about Donald Trump news conference it seems he can't face the truth eithe…
    RT @fravel: With False Claims, Donald Trump Attacks Media on Crowd Turnout 
    Aziz Ansari Just Hit Donald Trump Hard In An Epic Saturday NIght Live Monologue

We follow these 3 major steps in our program:

  * Authorize twitter API client.
  * Make a GET request to Twitter API to fetch tweets for a particular query.
  * Parse the tweets. Classify each tweet as positive, negative or neutral.

Now, let us try to understand the above piece of code:

  

  

  * First of all, we create a **TwitterClient** class. This class contains all the methods to interact with Twitter API and parsing tweets. We use **__init__** function to handle the authentication of API client.
  * In **get_tweets** function, we use:
    
        fetched_tweets = self.api.search(q = query, count = count)

to call the Twitter API to fetch tweets.

  * In **get_tweet_sentiment** we use textblob module.
    
        analysis = TextBlob(self.clean_tweet(tweet))

TextBlob is actually a high level library built over top of NLTK library.
First we call **clean_tweet** method to remove links, special characters, etc.
from the tweet using some simple regex.  
Then, as we pass **tweet** to create a **TextBlob** object, following
processing is done over text by textblob library:

    * Tokenize the tweet ,i.e split words from body of text.
    * Remove stopwords from the tokens.(stopwords are the commonly used words which are irrelevant in text analysis like I, am, you, are, etc.)
    * Do POS( part of speech) tagging of the tokens and select only significant features/tokens like adjectives, adverbs, etc.
    * Pass the tokens to a **sentiment classifier** which classifies the tweet sentiment as positive, negative or neutral by assigning it a polarity between -1.0 to 1.0 .

Here is how **sentiment classifier** is created:

    *  **TextBlob** uses a Movies Reviews dataset in which reviews have already been labelled as positive or negative.
    * Positive and negative features are extracted from each positive and negative review respectively.
    * Training data now consists of labelled positive and negative features. This data is trained on a Naive Bayes Classifier.

Then, we use **sentiment.polarity** method of **TextBlob** class to get the
polarity of tweet between -1 to 1.  
Then, we classify polarity as:

    
    
    if analysis.sentiment.polarity > 0:
           return 'positive'
    elif analysis.sentiment.polarity == 0:
           return 'neutral'
    else:
           return 'negative'

  * Finally, parsed tweets are returned. Then, we can do various type of statistical analysis on the tweets. For example, in above program, we tried to find the percentage of positive, negative and neutral tweets about a query.

 **References:**

  * http://www.ijcaonline.org/research/volume125/number3/dandrea-2015-ijca-905866.pdf
  * https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis
  * textblob.readthedocs.io/en/dev/_modules/textblob/en/sentiments.html

This article is contributed by **Nikhil Kumar**. If you like GeeksforGeeks and
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

