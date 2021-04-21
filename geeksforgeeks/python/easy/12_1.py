Like instagram pictures using Selenium | Python



In this article, we will learn how can we like all the pictures of a profile
on Instagram without scrolling and manually clicking the buttons. We will be
using Selenium to do this task.  

**Packages/Software needed:**  

> 1\. Python 3  
> 2\. Chromedriver compatible with the existing chrome version (download
> chromedriver)  
> 3\. Google chrome  
> 4\. Selenium package (pip install selenium), bs4 package(pip install bs4)

 **Step #1:** Importing modules and entering the login information along with
the URL of the page.  

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from bs4 import BeautifulSoup as bs

import selenium.common.exceptions

from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys

print("enter username")

username = input()

print("enter password")

password = input()

print("enter the url")

url = input()  
  
---  
  
 __

 __

