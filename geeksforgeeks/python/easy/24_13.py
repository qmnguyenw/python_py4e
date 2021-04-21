Selenium Python Tricks



 **Selenium** : Selenium Python bindings provide a convenient API to access
Selenium Web Driver like Firefox, Chrome, etc.

 **What is webdriver?**  
Selenium WebDriver is an automation testing tool. When I say automation, it
means it automates test scripts written in Selenium.

 **Webdriver Install**

    
    
    Chrome:    https://sites.google.com/a/chromium.org/chromedriver/downloads
    

**Library Imported**

    
    
    from selenium import webdriver
    import time
    

(i) Selenium library:  
– Used for Automation  
– Control Webdriver  
– Perform actions like – element clicks, refresh page, goto website link, etc

  

  

(ii) Time library:  
-For using sleep function because selenium works only when all the elements of the page is loaded.

 **Trick1: How to increase view count on a website?**  
#Note: This will not work on all websites, like youtube.  
What we would be learning is to refresh the webpage again and again after a
particular interval of time.

 __

 __  
 __

 __

 __  
 __  
 __

#!/usr / bin / env python

from selenium import webdriver

import time

 

# set webdriver path here it may vary

brower = webdriver.Chrome(executable_path ="C:\Program Files
(x86)\Google\Chrome\chromedriver.exe")

 

website_URL ="https://www.google.co.in/"

brower.get(website_URL)

 

# After how many seconds you want to refresh the webpage

# Few website count view if you stay there

# for a particular time

# you have to figure that out

refreshrate = int(15)

 

# This would keep running until you stop the compiler.

while True:

 time.sleep(refreshrate)

 brower.refresh()  
  
---  
  
 __

 __

 **Trick2: How to login on a website, here we take example of Zomato**

 __

 __  
 __

 __

 __  
 __  
 __

from selenium import webdriver

# For using sleep function because selenium

# works only when all the elements of the

# page is loaded.

import time

# webdriver path set

browser = webdriver.Chrome("C:\Program Files
(x86)\Google\Chrome\chromedriver.exe")

 

# To maximize the browser window

browser.maximize_window()

 

# zomato link set

browser.get('https://www.zomato.com / ncr')

 

time.sleep(3)

# Enter your user name and password here.

username = "test"

password = "test"

 

 

# signin element clicked

browser.find_element_by_xpath("//a[@id ='signin-link']").click()

time.sleep(2)

 

# Login clicked

browser.find_element_by_xpath("//a[@id ='login-email']").click()

 

# username send

a = browser.find_element_by_xpath("//input[@id ='ld-email']")

a.send_keys(username)

 

# password send

b = browser.find_element_by_xpath("//input[@id ='ld-password']")

b.send_keys(password)

 

# submit button clicked

browser.find_element_by_xpath("//input[@id ='ld-submit-
global']").click()

 

print('Login Successful')

browser.close()  
  
---  
  
 __

 __

 **Trick3: Instagram Login automation script.**

We know that Instagram is discontinuing its Legacy API from 29 June, 2020.  
So it’s probably a better idea to learn automation scripting.

 __

 __  
 __

 __

 __  
 __  
 __

from selenium import webdriver

# sleep() function is required because

# selenium needs a page to be fully loaded first

# otherwise errors may occur

from time import sleep

# Usage sleep(x) Where x is time in seconds and

# may vary according to your connection

 

# I have made class so that extra methods can be added later on

# if required

class instagramBot:

 def __init__(self, username, password):

 # these lines will help if someone faces issues like

 # chrome closes after execution

 self.opts = webdriver.ChromeOptions()

 self.opts.add_experimental_option("detach", True)

 self.driver = webdriver.Chrome(options=self.opts)

 

 # Username and password

 self.username = username

 self.password = password

 

 # Opens Instagram login page

 self.driver.get("https://instagram.com")

 sleep(2) # 1 Second Wait

 

 # Automatically enters your username and 

 # password to instagram's username field

 self.driver.find_element_by_xpath("//input[@name =
'username']").send_keys(self.username)

 self.driver.find_element_by_xpath("//input[@name =
'password']").send_keys(self.password)

 

 # Clicks on Log In Button

 self.driver.find_element_by_xpath("//div[contains(text(), 'Log
In')]").click()

 sleep(2)

 

 # Bonus: Automatically clicks on 'Not Now' 

 # when Instagram asks to show notifications

 self.driver.find_element_by_xpath("//button[contains(text(), 'Not
Now')]").click()

 

# Testing Your Code

instagramBot('Sample Username','Sample Password')  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

