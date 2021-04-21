Python | Automating Happy Birthday post on Facebook using Selenium



As we know Selenium is a tool used for controlling web browser through a
program. It can be used in all browsers, OS and its program are written in
various programming languages i.e Java, Python (all versions).

Selenium helps us automating any kind of task that we frequently do on our
laptops, PC’s ranging from using facebook messenger for texting and WhatsApp
also, daily tweeting tweets on twitter, wishing friends “Happy birthday” on
Facebook, googling anything we want to learn and many more task. All these
tasks can be automated using selenium in just a small implementation of it.

 **Installation:**

  * Go to command prompt and put this is in:
    
        pip install selenium

  * Once that’s done, download a webdriver for automation. Here, we’ll use chromedriver from http://chromedriver.chromium.org/

Let’s learn how to automate the process of wishing a birthday wish on facebook
friend’s timeline as a post.

The whole process of this automation can be divided as follows :

  

  

  * Logging into Facebook application using credentials like Username and Password.
  * Posting a “Happy Birthday” feed on timeline of those friends whose birthday is today.

 **Below are the steps:**

  * Create a browser object and using the get() function to send a request to the website we want to connect/use.
  * Find the elements like username and password input boxes, login button and using the selenium functions like click(), send_keys() etc to click on buttons and entering username and password respectively.
  * After that using get() function to send a request to /events/birthdays/ page.
  * At the top of this page, there is a card of “Today’s Birthdays” which shows friend’s name whose birthday is today along with an input text box to enter any feed on their timeline.
  * Using the XPATH of these input text boxes we will send our feed i.e., “Happy Birthday” using send_keys() function of selenium.
  * Close the browser.

NOTE: Make a separate test.txt file and put your facebook password in it
before the execution of the below program.

Below is the implementation:

 __

 __  
 __

 __

 __  
 __  
 __

# importing necessary classes

# from different modules

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.keys import Keys

import time

 

chrome_options = webdriver.ChromeOptions()

 

prefs = {"profile.default_content_setting_values.notifications":
2}

chrome_options.add_experimental_option("prefs", prefs)

browser = webdriver.Chrome("chromedriver.exe")

 

# open facebook.com using get() method

browser.get('https://www.facebook.com/')

 

# user_name or e-mail id

username = "agrawal.abhi108@gmail.com"

 

# getting passowrd from text file

with open('test.txt', 'r') as myfile:

 password = myfile.read().replace('\n', '')

 

print("Let's Begin")

 

element = browser.find_elements_by_xpath('//*[@id ="email"]')

element[0].send_keys(username)

 

print("Username Entered")

 

element = browser.find_element_by_xpath('//*[@id ="pass"]')

element.send_keys(password)

 

print("Password Entered")

 

# logging in

log_in = browser.find_elements_by_id('loginbutton')

log_in[0].click()

 

print("Login Successful")

 

browser.get('https://www.facebook.com/events/birthdays/')

 

feed = 'Happy Birthday !'

 

element = browser.find_elements_by_xpath("//*[@class
='enter_submit\

 uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea\

 inlineReplyTextArea mentionsTextarea textInput']")

 

cnt = 0

 

for el in element:

 cnt += 1

 element_id = str(el.get_attribute('id'))

 XPATH = '//*[@id ="' + element_id + '"]'

 post_field = browser.find_element_by_xpath(XPATH)

 post_field.send_keys(feed)

 post_field.send_keys(Keys.RETURN)

 print("Birthday Wish posted for friend" + str(cnt))

 

# Close the browser

browser.close()  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

