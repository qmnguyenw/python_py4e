Browser Automation Using Selenium



Selenium is a powerful tool for controlling a web browser through the program.
It is functional for all browsers, works on all major OS and its scripts are
written in various languages i.e Python, Java, C#, etc, we will be working
with Python.

Mastering Selenium will help you automate your day to day tasks like
controlling your tweets, Whatsapp texting, and even just googling without
actually opening a browser in just 15-30 lines of python code. The limits of
automation are endless with selenium.

 **Installation**

 **1.1 Selenium Bindings in Python**  
Selenium Python bindings provide a convenient API to access Selenium Web
Driver like Firefox,Chrome,etc.

    
    
    Pip install Selenium 
    

**1.2 Web Drivers**  
Selenium requires a web driver to interface with the chosen browser. Web
drivers is a package to interact with a web browser. It interacts with the web
browser or a remote web server through a wire protocol which is common to all.
You can check out and install the web drivers of your browser choice.

  

  

    
    
    Chrome:    https://sites.google.com/a/chromium.org/chromedriver/downloads
    Firefox: https://github.com/mozilla/geckodriver/releases
    Safari:    https://webkit.org/blog/6900/webdriver-support-in-safari-10/
    

**Getting Started**

 __

 __  
 __

 __

 __  
 __  
 __

from selenium import webdriver 

 

# For using sleep function because selenium 

# works only when the all the elements of the 

# page is loaded.

import time 

 

from selenium.webdriver.common.keys import Keys 

 

# Creating an instance webdriver

browser = webdriver.Firefox() 

browser.get('https://www.twitter.com')

 

# Let's the user see and also load the element 

time.sleep(2)

 

login =
browser.find_elements_by_xpath('//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]')

 

# using the click function which is similar to a click in the mouse.

login[0].click()

 

print("Login in Twitter")

 

user = browser.find_elements_by_xpath('//*[@id="login-dialog-
dialog"]/div[2]/div[2]/div[2]/form/div[1]/input')

 

# Enter User Name

user[0].send_keys('USER-NAME')

 

user = browser.find_element_by_xpath('//*[@id="login-dialog-
dialog"]/div[2]/div[2]/div[2]/form/div[2]/input')

 

# Reads password from a text file because

# saving the password in a script is just silly.

with open('test.txt', 'r') as myfile: 

 Password = myfile.read().replace('\n', '')

user.send_keys(Password)

 

LOG = browser.find_elements_by_xpath('//*[@id="login-dialog-
dialog"]/div[2]/div[2]/div[2]/form/input[1]')

LOG[0].click()

print("Login Successful")

time.sleep(5)

 

elem = browser.find_element_by_name("q")

elem.click()

elem.clear()

 

elem.send_keys("Geeks for geeks ")

 

# using keys to send special KEYS 

elem.send_keys(Keys.RETURN) 

 

print("Search Successful")

 

# closing the browser

browser.close()   
  
---  
  
__

__

**Dissecting the code**

The above script is for logging into twitter and searching for geeks for geeks
handle.  
So let’s see how it works:  
1\. Opening the browser  
2\. Creating a browser instance and using the .get function to connect the
website.  
3\. Finding the element this can be anything finding the input box or a button
and using the selenium function like click(), send_keys(), etc to interact
with the element.  
4\. Closing the browser

As of now you must have realized this automation script works in an
**iterative** manner of finding an element and interacting with it. There are
various ways of finding an element in the web page, you just right click and
inspect element and copy element either by name, css selector or xpath.

![Screenshot_20170419_203546](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot_20170419_203546.png)

Well that’s basically it using this you can create a custom automated script
for every single website or a universal one for all your social media which
automates all your actions.  
There is no limit to automation and the above is just an example to get you
guys started.So happy coding !

 **Related Post :**  
Whatsapp using Python!

This article is contributed by **Pradhvan Bisht**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
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

