Performing Google Search using Python code



Let’s say you are working on a project that needs to do web scraping but you
don’t know websites on which scraping is to be performed beforehand instead
you are required to perform google search and then proceed according to google
search result to few websites. In that case you need google search result for
your different queries.

  * One way of achieving this is using request and beautiful soup which has been discussed here in Implementing Web Scraping in Python with BeautifulSoup.
  * Instead of putting so much effort for a trivial task google package has been made. Its almost a o **ne liner solution** to find links of all the google search result directly.
  * Using python package **google** we can get result of google search from python script. We can get link of first n search results.

 **Installation**  
google package has one dependency on beautifulsoup which need to be installed
first.

    
    
    pip install beautifulsoup4
    

Then install google package

    
    
    pip install google
    

Required Function and its parameters

    
    
     **search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0)**

  *  **query :** query string that we want to search for.
  *  **tld :** tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
  *  **lang :** lang stands for language.
  *  **num :** Number of results we want.
  *  **start :** First result to retrieve.
  *  **stop :** Last result to retrieve. Use None to keep searching forever.
  *  **pause :** Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
  *  **Return :** Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.

 **Python codes on how to do google search using python script**

  

  

 **Example1: google_search.py**

 __

 __  
 __

 __

 __  
 __  
 __

try:

 from googlesearch import search

except ImportError: 

 print("No module named 'google' found")

 

# to search

query = "Geeksforgeeks"

 

for j in search(query, tld="co.in", num=10, stop=10,
pause=2):

 print(j)  
  
---  
  
 __

 __

Output:

    
    
    ![](https://media.geeksforgeeks.org/wp-content/uploads/google_3.png)
    

Lets perform google search manually and verify our result

![](https://media.geeksforgeeks.org/wp-content/uploads/google_4.png)

![](https://media.geeksforgeeks.org/wp-content/uploads/google_6.png)

 **Example 2: google_search.py**

 __

 __  
 __

 __

 __  
 __  
 __

try:

 from googlesearch import search

except ImportError: 

 print("No module named 'google' found")

 

# to search

query = "A computer science portal"

 

for j in search(query, tld="co.in", num=10, stop=10,
pause=2):

 print(j)  
  
---  
  
 __

 __

Output:

    
    
    ![](https://media.geeksforgeeks.org/wp-content/uploads/google_search_.png)
    

Lets perform google search manually and verify our result

![](https://media.geeksforgeeks.org/wp-content/uploads/google_8.png)

 **Referecne :** Google python package

This article is contributed by **Pratik Chhajer**. If you like GeeksforGeeks
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

