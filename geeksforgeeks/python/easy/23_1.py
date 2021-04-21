Movie recommendation based on emotion in Python



 **Introduction** One of the underlying targets of movies is to evoke emotions
in their viewers. IMDb offers all the movies for all genre. Therefore the
movie titles can be scraped from the IMDb list to recommend to the user.IMDb
does not have an API, for accessing information on movies and TV Series.
Therefore we have to perform scraping. Scraping is used for accessing
information from a website which is usually done with APIs.  
 **Installation**

Install **BeautifulSoup** and **lxml** ,  
Open terminal and write

    
    
    pip install beautifulsoup4
    pip install lxml

The scraper is written in Python and uses lxml for parsing the webpages.
BeautifulSoup is used for pulling data out of HTML and XML files.

 **Emotion associated with Genre of Movie**

There are 8 classes of emotion that would be effective to classify a text.
These are: _‘Anger’, ‘Anticipation’, ‘Disgust’, ‘Fear’, ‘Joy’, ‘Sad’,
‘Surprise’, ‘Trust’_. Here these are taken as input and the corresponding
movies would be displayed for the emotion.  
The correspondence of every emotion with genre of movies is listed below:

  

  

Sad – Drama  
Disgust – Musical  
Anger – Family  
Anticipation – Thriller  
Fear – Sport  
Enjoyment – Thriller  
Trust – Western  
Surprise – Film-Noir

Based on the input emotion, the corresponding genre would be selected and all
the top 5 movies of that genre would be recommended to the user.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code for movie

# recommendation based on

# emotion

 

# Import library for web

# scrapping

from bs4 import BeautifulSoup as SOUP

import re

import requests as HTTP

 

# Main Function for scraping

def main(emotion):

 

 # IMDb Url for Drama genre of

 # movie against emotion Sad

 if(emotion == "Sad"):

 urlhere =
'http://www.imdb.com/search/title?genres=drama&title;_type=feature&sort;=moviemeter,
asc'

 

 # IMDb Url for Musical genre of

 # movie against emotion Disgust

 elif(emotion == "Disgust"):

 urlhere =
'http://www.imdb.com/search/title?genres=musical&title;_type=feature&sort;=moviemeter,
asc'

 

 # IMDb Url for Family genre of

 # movie against emotion Anger

 elif(emotion == "Anger"):

 urlhere =
'http://www.imdb.com/search/title?genres=family&title;_type=feature&sort;=moviemeter,
asc'

 

 # IMDb Url for Thriller genre of

 # movie against emotion Anticipation

 elif(emotion == "Anticipation"):

 urlhere =
'http://www.imdb.com/search/title?genres=thriller&title;_type=feature&sort;=moviemeter,
asc'

 

 # IMDb Url for Sport genre of

 # movie against emotion Fear

 elif(emotion == "Fear"):

 urlhere =
'http://www.imdb.com/search/title?genres=sport&title;_type=feature&sort;=moviemeter,
asc'

 

 # IMDb Url for Thriller genre of

 # movie against emotion Enjoyment

 elif(emotion == "Enjoyment"):

 urlhere =
'http://www.imdb.com/search/title?genres=thriller&title;_type=feature&sort;=moviemeter,
asc'

 

 # IMDb Url for Western genre of

 # movie against emotion Trust

 elif(emotion == "Trust"):

 urlhere =
'http://www.imdb.com/search/title?genres=western&title;_type=feature&sort;=moviemeter,
asc'

 

 # IMDb Url for Film_noir genre of

 # movie against emotion Surprise

 elif(emotion == "Surprise"):

 urlhere =
'http://www.imdb.com/search/title?genres=film_noir&title;_type=feature&sort;=moviemeter,
asc'

 

 # HTTP request to get the data of

 # the whole page

 response = HTTP.get(urlhere)

 data = response.text

 

 # Parsing the data using

 # BeautifulSoup

 soup = SOUP(data, "lxml")

 

 # Extract movie titles from the

 # data using regex

 title = soup.find_all("a", attrs = {"href" :
re.compile(r'\/title\/tt+\d*\/')})

 return title

 

# Driver Function

if __name__ == '__main__':

 

 emotion = input("Enter the emotion: ")

 a = main(emotion)

 count = 0

 

 if(emotion == "Disgust" or emotion == "Anger"

 or emotion=="Surprise"):

 

 for i in a:

 

 # Splitting each line of the

 # IMDb data to scrape movies

 tmp = str(i).split('>;')

 

 if(len(tmp) == 3):

 print(tmp[1][:-3])

 

 if(count > 13):

 break

 count += 1

 else:

 for i in a:

 tmp = str(i).split('>')

 

 if(len(tmp) == 3):

 print(tmp[1][:-3])

 

 if(count > 11):

 break

 count+=1  
  
---  
  
 __

 __

This script would scrape all the movie titles of the genre corresponding to
the input emotion and list to the user.

Web Scraping is highly beneficial in extracting the data and doing analysis on
it. Without web scraping, the Internet as you know it really wouldn’t exist.
That’s because Google and other major search engines rely upon a sophisticated
web scraper to pull the content that will get included in their index. These
tools are what makes search engines possible.

Applications of Crawling

  * Article extraction for websites that curate content.
  * Business listings extraction for companies that build databases of leads.
  * Many different types of data extraction, sometimes called data mining. For example, one popular and sometimes controversial use of a web scraper is for pulling prices off of airlines to publish on airfare comparison sites.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

