How to Scrape Multiple Pages of a Website Using Python?



Web Scraping is a method of extracting useful data from a website using
computer programs without having to manually do it. This data can then be
exported and categorically organized for various purposes. Some common places
where Web Scraping finds its use are Market research & Analysis Websites,
Price Comparison Tools, Search Engines, Data Collection for AI/ML projects,
etc.

Let’s dive deep and scrape a website. In this article, we are going to take
the GeeksforGeeks website and extract the titles of all the articles available
on the Homepage using a Python script.

If you notice, there are thousands of articles on the website and to extract
all of them, we will have to scrape through all pages so that we don’t miss
out on any!

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210225001509/image20210225001509-660x449.png)

GeeksforGeeks Homepage

## Scraping multiple Pages of a website Using Python

Now, there may arise various instances where you may want to get data from
multiple pages from the same website or multiple different URLs as well, and
manually writing code for each webpage is a time-consuming and tedious task.
Plus, it defies all basic principles of automation. Duh!

To solve this exact problem, we will see two main techniques that will help us
extract data from multiple webpages:

  

  

  * The same website
  * Different website URLs

 **Approach:**

The approach of the program will be fairly simple, and it will be easier to
understand it in a POINT format:

  * We’ll import all the **necessary libraries**.
  * Set up our URL strings for making a connection using the **requests** library.
  * Parsing the available data from the target page using the **BeautifulSoup** library’s parser.
  * From the target page, **Identify** and **Extract** the classes and tags which contain the information that is valuable to us.
  *  **Prototype** it for one page using a loop and then apply it to all the pages.

 **Example 1: Looping through the page numbers**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210224143314/image20210224143314-660x68.png)

page numbers at the bottom of the GeeksforGeeks website

Most websites have pages labeled from 1 to N. This makes it really simple for
us to loop through these pages and extract data from them as these pages have
similar structures. For example:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210224142442/image20210224142442-660x32.png)

notice the last section of the URL – page/4/

Here, we can see the page details at the end of the URL. Using this
information we can easily create a _**for loop**_ iterating over as many pages
as we want (by putting _**page/(i)/**_ in the URL string and iterating “ _i_ ”
_till N_ ) and scrape all the useful data from them. The following code will
give you more clarity over how to scrape data by using a **For Loop** in
Python.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import requests

from bs4 import BeautifulSoup as bs

 

URL = 'https://www.geeksforgeeks.org/page/1/'

 

req = requests.get(URL)

soup = bs(req.text, 'html.parser')

 

titles = soup.find_all('div',attrs = {'class','head'})

 

print(titles[4].text)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210224230221/13-660x179.PNG)

Output for the above code

Now, using the above code, we can get the titles of all the articles by just
sandwiching those lines with a loop.

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import requests

from bs4 import BeautifulSoup as bs

 

URL = 'https://www.geeksforgeeks.org/page/'

 

for page in range(1,10):

 # pls note that the total number of

 # pages in the website is more than 5000 so i'm only taking the

 # first 10 as this is just an example

 

 req = requests.get(URL + str(page) + '/')

 soup = bs(req.text, 'html.parser')

 

 titles = soup.find_all('div',attrs={'class','head'})

 

 for i in range(4,19):

 if page>1:

 print(f"{(i-3)+page*15}" + titles[i].text)

 else:

 print(f"{i-3}" + titles[i].text)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210227182552/image20210227182552-660x303.png)

Output for the above code

 **Note:** The above code will fetch the first 10 pages from the website and
scrape all the 150 titles of the articles that fall under those pages.

**Example 2: Looping through a list of different URLs.**

The above technique is absolutely wonderful, but what if you need to scrape
different pages, and you don’t know their page numbers? You’ll need to scrape
those different URLs one by one and manually code a script for every such
webpage.

Instead, you could just make a list of these URLs and loop through them. By
simply iterating the items in the list i.e. the URLs, we will be able to
extract the titles of those pages without having to write code for each page.
Here’s an example code of how you can do it.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import requests

from bs4 import BeautifulSoup as bs

URL =
['https://www.geeksforgeeks.org','https://www.geeksforgeeks.org/page/10/']

 

for url in range(0,2):

 req = requests.get(URL[url])

 soup = bs(req.text, 'html.parser')

 

 titles = soup.find_all('div',attrs={'class','head'})

 for i in range(4, 19):

 if url+1 > 1:

 print(f"{(i - 3) + url * 15}" + titles[i].text)

 else:

 print(f"{i - 3}" + titles[i].text)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210227183111/image20210227183110-660x359.png)

Output for the above code

## How to avoid getting your IP address banned?

Controlling the crawl rate is the most important thing to keep in mind when
carrying out a very large extraction. Bombarding the server with multiple
requests within a very short amount of time will most likely result in getting
your IP address blacklisted. To avoid this, we can simply carry out our
crawling in short _**random**_ bursts of time. In other words, we add pauses
or little breaks between crawling periods, which help us look like actual
humans as websites can easily identify a crawler because of the speed it
possesses compared to a human trying to visit the website. This helps avoid
unnecessary traffic and overloading of the website servers. Win-Win!

Now, how do we control the crawling rate? It’s simple. By using two functions,
_**randint()** and **sleep()**_ from python modules _‘random’ and ‘time’_
respectively.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from random import randint

from time import sleep 

 

print(randint(1,10))  
  
---  
  
 __

 __

 **Output**

    
    
    1

The _**randint()**_ function will choose a random integer between the given
upper and lower limits, in this case, 10 and 1 respectively, for every
iteration of the loop. Using the _**randint()**_ function in combination with
the _**sleep()**_ function will help in adding short and random breaks in the
crawling rate of the program. The _**sleep()**_ function will basically cease
the execution of the program for the given number of seconds. Here, the number
of seconds will randomly be fed into the sleep function by using the
_**randint()**_ function. Use the code given below for reference.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from time import *

from random import randint

 

for i in range(0,3):

 # selects random integer in given range

 x = randint(2,5)

 print(x)

 sleep(x)

 print(f'I waited {x} seconds')  
  
---  
  
 __

 __

 **Output**

    
    
    5
    I waited 5 seconds
    4
    I waited 4 seconds
    5
    I waited 5 seconds

To get you a clear idea of this function in action, refer to the code given
below.

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

from random import randint

from time import sleep

 

URL = 'https://www.geeksforgeeks.org/page/'

 

for page in range(1,10): 

 # pls note that the total number of

 # pages in the website is more than 5000 so i'm only taking the

 # first 10 as this is just an example

 

 req = requests.get(URL + str(page) + '/')

 soup = bs(req.text, 'html.parser')

 

 titles = soup.find_all('div',attrs={'class','head'})

 

 for i in range(4,19):

 if page>1:

 print(f"{(i-3)+page*15}" + titles[i].text)

 else:

 print(f"{i-3}" + titles[i].text)

 

 sleep(randint(2,10))  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210228141438/19-660x288.PNG)

The program has paused its execution and is waiting to resume

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210228141610/20-660x324.PNG)

The output of the above code

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

