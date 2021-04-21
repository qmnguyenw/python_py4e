Send Direct Message On Instagram using Selenium in Python



In this article, we will learn how we can send a direct message to users on
Instagram without any manual action. We will be using the selenium module to
do this task.

### Requirements:

  1. Chrome Driver for Chrome Browser (https://chromedriver.chromium.org/) or Gecko Driver for Firefox(https://github.com/mozilla/geckodriver/releases)
  2. Selenium Package. To install this type the below command in the terminal.

    
    
    pip install selenium
    
    

**Note:** For more information, refer How to install Selenium in Python

**Approach:**

 **Step 1:** Importing modules and entering the login information along with
the username of the user whom you want to send a message.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import selenium.common.exceptions

import time

import random

# Login Credentials

username = input('Enter your Username ')

password = input('Enter your Password ')

url = 'https://instagram.com/' + input('Enter username of user
whome you want to send message')  
  
---  
  
 __

 __

