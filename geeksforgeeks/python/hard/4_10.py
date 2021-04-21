Scraping COVID-19 statistics using Python and Selenium



Selenium is an open source web testing tool that allows users to test web
applications across different browsers and platforms. It includes a plethora
of software that developers can use to automate web applications including
IDE, RC, webdriver and Selenium grid, which all serve different purposes.
Moreover, it serves the purpose of scraping dynamic web pages, something which
Beautiful Soup can’t.

**1.A _Selenium Bindings in Python_**

Selenium Python bindings provide a simple API to write functional tests using
it’s WebDriver. Through the API you can access all functionalities of Selenium
WebDriver without hassle.

    
    
    pip install Selenium
    

**1.B _Web Drivers_**

Selenium requires a web driver to interface and interact with the chosen
browser, i.e. Chrome, Safari, Firefox, etc. A web driver is a package to set
up interactivity with the user’s web browser. It interacts through a wire
protocol which is common to all.

  

  

You can easily install the web drivers compatible with your browser. The
following links will help you with that: **Chrome** :|
https://sites.google.com/a/chromium.org/chromedriver/downloads|  **Edge** :|
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/|
**Firefox** :| https://github.com/mozilla/geckodriver/releases|  **Safari** :|
https://webkit.org/blog/6900/webdriver-support-in-safari-10/  
---|---  
  
**2.A _Using Python Bindings_**

If you have installed Selenium Python bindings, you can start using it from
Python like this:

    
    
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from time import sleep
    

The sleep module waits until the browser URL has completely loaded. Now we
create a browser webdriver instance (here, Chrome) as follows:

    
    
    driver=webdriver.Chrome("C:/chromedriver.exe")
    driver.get("https://www.covid19india.org/")
    sleep(2) //Waits for 2 seconds after navigating to the URL
    

The **driver.get()** method navigates to the page given by the URL and
subsequently the chromedriver waits until the page has been fully loaded
before returning control to the script.

 **2.B _Web Scraping_**

There are various strategies to locate elements in a page. In this case, we
use the **find_element_by_xpath()** method to navigate to the desired HTML-
rendered values on _**https://www.covid19india.org/.**_ The above script
extracts seven different values from the desired URL, namely:

  

  

  *  _Total Cases_
  *  _Total Active Cases_
  *  _Total Recovered Cases_
  *  _Total Deaths_
  *  _New Positive Cases_
  *  _New Recovered Cases_
  *  _Additional Deaths yet_

These extracted values of COVID-19 statistics are displayed on the user’s
console in real-time using Python using the **print()** statement as follows:

    
    
     _ **def extractor():**_
    
    _**TCases = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]/div[1]/h1/span")**_
    _**TActive = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]/div[2]/h1/span")**_
    _**TRecov = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]/div[3]/h1/span")**_
    _**TDeath = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]/div[4]/h1/span")**_
    _**New_Cases = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]/div[1]/h4/span")**_
    _**New_Rcov = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]/div[3]/h4/span")**_
    _**New_Death = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]/div[4]/h4/span")**_
            _****_    _**print("Total Cases:", TCases.text)**_
    _****_    _**print("Total Active Cases:", TActive.text)**_
    _****_    _**print("Total Recovered Cases:", TRecov.text)**_
    _****_    _**print("Total Deaths:", TDeath.text)**_
    _****_    _**print("New Cases:", New_Cases.text[1:len(New_Cases.text)-1])**_
    _****_    _**print("New Recovered Cases:", New_Rcov.text[1:len(New_Rcov.text)-1])**_
    _****_    _**print("Additional Deaths yet:", New_Death.text[1:len(New_Death.text)-1])**_
    
    
    

The entire script can be automated to execute after a given interval using the
**sleep()** module as follows:

    
    
     _ **while True:**_
    _**extractor()**_
    _**sleep(60*60)   // The loop executes after every hour in this case**_
    
    
    

The while loop executes indefinitely and runs the **extractor()** function
after every hour.

Here’s the entire web scraping program:

__

__  
__

__

__  
__  
__

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from time import sleep

 

driver = webdriver.Chrome("C:/chromedriver.exe")

driver.get("https://www.covid19india.org/")

sleep(2)

 

 

def extractor():

 TCases = driver.find_element_by_xpath(

 "/html / body / div / div / div[2]/div[1]/div[2]/div[1]/h1 / span")

 TActive = driver.find_element_by_xpath(

 "/html / body / div / div / div[2]/div[1]/div[2]/div[2]/h1 / span")

 TRecov = driver.find_element_by_xpath(

 "/html / body / div / div / div[2]/div[1]/div[2]/div[3]/h1 / span")

 TDeath = driver.find_element_by_xpath(

 "/html / body / div / div / div[2]/div[1]/div[2]/div[4]/h1 / span")

 New_Cases = driver.find_element_by_xpath(

 "/html / body / div / div / div[2]/div[1]/div[2]/div[1]/h4 / span")

 New_Rcov = driver.find_element_by_xpath(

 "/html / body / div / div / div[2]/div[1]/div[2]/div[3]/h4 / span")

 New_Death = driver.find_element_by_xpath(

 "/html / body / div / div / div[2]/div[1]/div[2]/div[4]/h4 / span")

 

 print("Total Cases:", TCases.text)

 print("Total Active Cases:", TActive.text)

 print("Total Recovered Cases:", TRecov.text)

 print("Total Deaths:", TDeath.text)

 print("New Cases:",
New_Cases.text[1:len(New_Cases.text)-1])

 print("New Recovered Cases:",
New_Rcov.text[1:len(New_Rcov.text)-1])

 print("Additional Deaths yet:",
New_Death.text[1:len(New_Death.text)-1])

 

 

while True:

 extractor()

 sleep(60 * 60)  
  
---  
  
 __

 __

The output of the above program on the user’s console is as follows:

    
    
     _ **Total Cases: 2, 17, 187**_
    _**Total Active Cases: 1, 07, 017**_
    _**Total Recovered Cases: 1, 04, 071**_
    _**Total Deaths: 6, 088**_
    _**New Cases: +2561**_
    _**New Recovered Cases: +543**_
    _**Additional Deaths yet: +23**_
    //The above COVID-19 values differ with time. Your output may differ. 

The above script thus automates web scraping using Selenium and prints the
updated statistics on the user’s console on an hourly basis.

Using this you can create a custom automated script for every single website
which automates all your actions. Honestly, there’s no limit to web scraping
and automation and the above is just an example to get you going.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

