Python program to crawl a web page and get most frequent words



The task is to count the most frequent words, which extracts data from dynamic
sources.  
First, create a web-crawler or scraper with the help of _requests_ module and
_beautiful soup_ module, which will extract data from the web-pages and store
them in a list. There might be some undesired words or symbols (like special
symbols, blank spaces), which can be filtered in order to ease the counts and
get the desired results.

After counting each word, we also can have the count of most (say 10 or 20)
frequent words.

 **Modules and Library functions used :**  

> **requests :** Will allow you to send HTTP/1.1 requests and many more.  
> **beautifulsoup4 :** Used for parsing HTML/XML to extract data out of HTML
> and XML files.  
> **operator :** Exports a set of efficient functions corresponding to the
> intrinsic operators.  
> **collections :** Implements high-performance container datatypes.

Below is a implementation of the idea discussed above :  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for a word frequency

# counter after crawling/scraping a web-page

import requests

from bs4 import BeautifulSoup

import operator

from collections import Counter

'''Function defining the web-crawler/core

spider, which will fetch information from

a given website, and push the contents to

the second function clean_wordlist()'''

def start(url):

 # empty list to store the contents of

 # the website fetched from our web-crawler

 wordlist = []

 source_code = requests.get(url).text

 # BeautifulSoup object which will

 # ping the requested url for data

 soup = BeautifulSoup(source_code, 'html.parser')

 # Text in given web-page is stored under

 # the <div> tags with class <entry-content>

 for each_text in soup.findAll('div', {'class': 'entry-
content'}):

 content = each_text.text

 # use split() to break the sentence into

 # words and convert them into lowercase

 words = content.lower().split()

 for each_word in words:

 wordlist.append(each_word)

 clean_wordlist(wordlist)

# Function removes any unwanted symbols

def clean_wordlist(wordlist):

 clean_list = []

 for word in wordlist:

 symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "

 for i in range(len(symbols)):

 word = word.replace(symbols[i], '')

 if len(word) > 0:

 clean_list.append(word)

 create_dictionary(clean_list)

# Creates a dictionary conatining each word's

# count and top_20 ocuuring words

def create_dictionary(clean_list):

 word_count = {}

 for word in clean_list:

 if word in word_count:

 word_count[word] += 1

 else:

 word_count[word] = 1

 ''' To get the count of each word in

 the crawled page -->

 # operator.itemgetter() takes one

 # parameter either 1(denotes keys)

 # or 0 (denotes corresponding values)

 for key, value in sorted(word_count.items(),

 key = operator.itemgetter(1)):

 print ("% s : % s " % (key, value))

 <-- '''

 c = Counter(word_count)

 # returns the most occurring elements

 top = c.most_common(10)

 print(top)

# Driver code

if __name__ == '__main__':

 url = "https://www.geeksforgeeks.org/programming-language-choose/"

 # starts crawling and prints output

 start(url)  
  
---  
  
 __

 __

    
    
    [('to', 10), ('in', 7), ('is', 6), ('language', 6), ('the', 5),
     ('programming', 5), ('a', 5), ('c', 5), ('you', 5), ('of', 4)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

