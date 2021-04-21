Scraping Javascript Enabled Websites using Scrapy-Selenium



Scrapy-selenium is a middleware that is used in web scraping. scrapy do not
support scraping modern sites that uses javascript frameworks and this is the
reason that this middleware is used with scrapy to scrape those modern
sites.Scrapy-selenium provide the functionalities of selenium that help in
working with javascript websites. Other advantages provided by this is driver
by which we can also see what is happening behind the scenes. As selenium is
automated tool it also provides us to how to deal with input tags and scrape
according to what you pass in input field. Passing inputs in input fields
became easier by using selenium.First time scrapy-selenium was introduced in
2018 and its an opensource. The alternative to this can be scrapy-splash

  *  **Install and Setup Scrapy –**
    * Install scrapy
    * Run
        
                scrapy startproject projectname  (projectname is name of project)

    * Now, let’s Run,
        
                scrapy genspider spidername example.com

(replace spidername with your preferred spider name and example.com with
website that you want to scrape). Note: Later also url can be changed, inside
your scrapy spider.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200719174045/startproject_final.png)

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200719174110/genspider_final.png)

  

  

 **scrapy spider:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200719174158/scrapespider_final.png)

  *  **Integrating scrapy-selenium in scrapy project:**
    * Install scrapy-selenium and add this in your settings.py file

 __

 __  
 __

 __

 __  
 __  
 __

# for firefox

from shutil import which

 

SELENIUM_DRIVER_NAME = 'firefox'

SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')

SELENIUM_DRIVER_ARGUMENTS=['-headless'] 

 

# for chrome driver 

from shutil import which

 

SELENIUM_DRIVER_NAME = 'chrome'

SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')

SELENIUM_DRIVER_ARGUMENTS=['--headless'] 

 

DOWNLOADER_MIDDLEWARES = {

 'scrapy_selenium.SeleniumMiddleware': 800

 }  
  
---  
  
 __

 __

    * In this project chrome driver is used.Chrome driver is to be downloaded according to version of chrome browser. Go to help section in your chrome browser then click about Google chrome and check your version.Download chrome driver from website as referred hereTo download chrome driver
    *  **Where to add chromedriver:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200719174224/chromedriver_final.png)

    *  **Addition in settings.py file:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200719174248/adding_Code_in_settings.py_file_final.png)

    *  **Change to be made in spider file:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/20200719174313/scrapy-
selenium-spider_final.png)

    *  **To run project:**
        
                command- scrapy crawl spidername (scrapy crawl integratedspider in this project)
        

    * **spider code before scrapy-selenium:**

 __

 __  
 __

 __

 __  
 __  
 __

import scrapy

 

class IntegratedspiderSpider(scrapy.Spider):

 name = 'integratedspider' # name of spider

 allowed_domains = ['example.com']

 start_urls = ['http://example.com/']

 

 def parse(self, response):

 pass  
  
---  
  
 __

 __

  *  **Important fields in scrapy-selenium:**
    1.  **name-** name is a variable where name of spider is written and each spider is recognized  
by this name. The command to run spider is, scrapy crawl spidername (Here
spidername is  
referred to that name which is defined in the spider).

    2.  **function start_requests-** The first requests to perform are obtained by calling the start_requests() method which generates Request for the URL specified in the url field in yield SeleniumRequest and the parse method as callback function for the Requests
    3.  **url-** Here url of the site is provided.
    4.  **screenshot-** You can take a screenshot of a web page with the method get_screenshot_as_file() with as parameter the filename and screenshot will save in project.
    5.  **callback-** The function that will be called with the response of this request as its first parameter.
    6.  **dont_filter-** indicates that this request should not be filtered by the scheduler. if same url is send to parse it will not give exception of same url already accessed. What it means is same url can be accessed more then once.default value is false.
    7.  **wait_time-** Scrapy doesn’t wait a fixed amount of time between requests. But by this field we can assign it during callback.
  *  **General structure of scrapy-selenium spider:**

 __

 __  
 __

 __

 __  
 __  
 __

import scrapy

from scrapy_selenium import SeleniumRequest

 

class IntegratedspiderSpider(scrapy.Spider):

 name = 'integratedspider'

 def start_requests(self):

 yield SeleniumRequest(

 url ="https://www.geeksforgeeks.org/",

 wait_time = 3,

 screenshot = True,

 callback = self.parse, 

 dont_filter = True

 )

 

 def parse(self, response):

 pass  
  
---  
  
 __

 __

  *  **Project of Scraping with scrapy-selenium:**  
scraping online courses names from geeksforgeeks site using scrapy-selenium

 **Getting X-path of element we need to scrap –**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200719174402/course_card_xpath_final.png)

 **Code to scrap Courses Data from Geeksforgeeks –**

 __

 __  
 __

 __

 __  
 __  
 __

import scrapy

from scrapy_selenium import SeleniumRequest

 

class IntegratedspiderSpider(scrapy.Spider):

 name = 'integratedspider'

 def start_requests(self):

 yield SeleniumRequest(

 url = "https://practice.geeksforgeeks.org/courses/online",

 wait_time = 3,

 screenshot = True,

 callback = self.parse,

 dont_filter = True

 )

 

 def parse(self, response):

 # courses make list of all items that came in this xpath

 # this xpath is of cards containing courses details

 courses = response.xpath('//*[@id ="active-courses-
content"]/div/div/div')

 

 # course is each course in the courses list

 for course in courses:

 # xpath of course name is added in the course path

 # text() will scrape text from h4 tag that contains course name

 course_name =
course.xpath('.//a/div[2]/div/div[2]/h4/text()').get()

 

 # course_name is a string containing \n and extra spaces

 # these \n and extra spaces are removed

 

 course_name = course_name.split('\n')[1]

 course_name = course_name.strip()

 

 

 yield {

 'course Name':course_name

 }  
  
---  
  
 __

 __

 **Output –**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200719174503/courses_final.png)

 **Official link** github repo  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

