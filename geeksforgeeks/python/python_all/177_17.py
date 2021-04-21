Implementing Web Scraping in Python with Scrapy



Nowadays data is everything and if someone wants to get data from webpages
then one way to use an API or implement Web Scraping techniques. In Python,
Web scraping can be done easily by using scraping tools like BeautifulSoup.
But what if the user is concerned about performance of scraper or need to
scrape data efficiently.

To overcome this problem, one can make use of MultiThreading/Multiprocessing
with BeautifulSoup module and he/she can create spider, which can help to
crawl over a website and extract data. In order to save the time one use
Scrapy.

    
    
    With the help of Scrapy one can :
    
    1. Fetch millions of data efficiently
    2. Run it on server
    3. Fetching data 
    4. Run spider in multiple processes

Scrapy comes with whole new features of creating spider, running it and then
saving data easily by scraping it. At first it looks quite confusing but it’s
for the best.

Let’s talk about the installation, creating a spider and then testing it.

 **Step 1 : Creating virtual environment**

  

  

It is good to create one virtual environment as it isolates the program and
doesn’t affect any other programs present in the machine. To create virtual
environment first install it by using :

    
    
    sudo apt-get install python3-venv

Create one folder and then activate it :

    
    
    mkdir scrapy-project && cd scrapy-project
    python3 -m venv myvenv 
    

If above command gives Error then try this :

    
    
    python3.5 -m venv myvenv

After creating virtual environment activate it by using :

    
    
    source myvenv/bin/activate

  
**Step 2 : Installing Scrapy module**

Install Scrapy by using :

    
    
    pip install scrapy

To install scrapy for any specific version of python :

    
    
    python3.5 -m pip install scrapy

Replace 3.5 version with some other version like 3.6.  
  
**Step 3 : Creating Scrapy project**

  

  

While working with Scrapy, one needs to create scrapy project.

    
    
    scrapy startproject gfg

![](https://media.geeksforgeeks.org/wp-
content/uploads/scrapy_projecttree-1024x470.png)

In Scrapy, always try to create one spider which helps to fetch data, so to
create one, move to spider folder and create one python file over there.
Create one spider with name gfgfetch.py python file.  
  
**Step 4 : Creating Spider**

Move to the spider folder and create gfgfetch.py. While creating spider,
always create one class with unique name and define requirements. First thing
is to name the spider by assigning it with name variable and then provide the
starting URL through which spider will start crawling. Define some methods
which helps to crawl much deeper into that website. For now, let’s scrap all
the URL present and store all those URL.

 __

 __  
 __

 __

 __  
 __  
 __

import scrapy

 

class ExtractUrls(scrapy.Spider):

 

 # This name must be unique always

 name = "extract"

 

 # Function which will be invoked

 def start_requests(self):

 

 # enter the URL here

 urls = ['https://www.geeksforgeeks.org/', ]

 

 for url in urls:

 yield scrapy.Request(url = url, callback = self.parse)  
  
---  
  
 __

 __

Main motive is to get each url and then request it. Fetch all the urls or
anchor tags from it. To do this, we need to create one more methodparse ,to
fetch data from the given url.  
  
**Step 5 : Fetching data from given page**  
Before writing parse function, test few things like how to fetch any data from
given page. To do this make use of scrapy shell. It is just like python
interpreter but with the ability to scrape data from the given url. In short,
its a python interpreter with Scrapy functionality.

    
    
    scrapy shell _URL_

Note: Make sure to in the same directory where scrapy.cfg is present, else it
will not work.

    
    
    scrapy shell https://www.geeksforgeeks.org/

Now for fetching data from the given page, use _selectors_. These selectors
can be either from CSS or from Xpath. For now, let’s try to fetch all url by
using CSS Selector.

  * To get anchor tag :
    
        response.css('a')

  * To extract the data :
    
        links = response.css('a').extract()

  * For example, links[0] will show something like this :
    
        '<a href="https://www.geeksforgeeks.org/" title="GeeksforGeeks" rel="home">GeeksforGeeks</a>'

  * To get href attribute, use attributes tag.
    
        links = response.css('a::attr(href)').extract()

This will get all the href data which is very useful. Make use of this link
and start requesting it.

Now, let’s create parse method and fetch all the urls and then yield it.
Follow that particular URL and fetch more links from that page and this will
keep on happening again and again. In short, we are fetching all url present
on that page.

Scrapy, by default, filters those url which has already been visited. So it
will not crawl the same url path again. But it’s possible that in two
different pages there are two or more than two similar links. For example, in
each page, the header link will be available which means that this header link
will come in each page request. So try to exclude it by checking it.

 __

 __  
 __

 __

 __  
 __  
 __

# Parse function

def parse(self, response):

 

 # Extra feature to get title

 title = response.css('title::text').extract_first() 

 

 # Get anchor tags

 links = response.css('a::attr(href)').extract() 

 

 for link in links:

 yield

 {

 'title': title,

 'links': link

 }

 

 if 'geeksforgeeks' in link: 

 yield scrapy.Request(url = link, callback = self.parse)  
  
---  
  
 __

 __

  
Below is the implementation of scraper :

 __

 __  
 __

 __

 __  
 __  
 __

# importing the scrapy module

import scrapy

 

class ExtractUrls(scrapy.Spider):

 name = "extract"

 

 # request function

 def start_requests(self):

 urls = [ 'http://www.geeksforgeeks.org', ]

 

 for url in urls:

 yield scrapy.Request(url = url, callback = self.parse)

 

 # Parse function

 def parse(self, response):

 

 # Extra feature to get title

 title = response.css('title::text').extract_first() 

 

 # Get anchor tags

 links = response.css('a::attr(href)').extract() 

 

 for link in links:

 yield

 {

 'title': title,

 'links': link

 }

 

 if 'geeksforgeeks' in link: 

 yield scrapy.Request(url = link, callback = self.parse)  
  
---  
  
 __

 __

  
**Step 6 : In last step, Run the spider and get output in simple json file**

    
    
    scrapy crawl NAME_OF_SPIDER -o links.json

Here, name of spider is “extract” for given example. It will fetch loads of
data within few seconds.

 **Output :**

**Note :** Scraping any web page is not a legal activity. Don’t perform any
scraping operation without permission.

  
Reference : https://doc.scrapy.org/en/.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

