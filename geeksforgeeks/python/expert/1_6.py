Click button by text using Python and Selenium



Selenium is a tool that provides APIs to automate a web application to aid in
its testing. In this article, we discuss the use of Selenium Python API
bindings to access the Selenium WebDrivers to click a button by text present
in the button. In the following example, we take the help of Chrome. The
method used is the **find_element_by_link_text()** which scrapes the element
using the text present. In case there is no such element with the given text
attribute, **NoSuchElementException** is returned.

### Installation:

Make sure you have Selenium installed using

    
    
    pip3 install Selenium

And also download the WebDriver for your web browser :

    
    
    Chrome : https://chromedriver.chromium.org/downloads
    Firefox : https://github.com/mozilla/geckodriver/releases
    Safari : https://webkit.org/blog/6900/webdriver-support-in-safari-10/

Once Selenium is installed along with the desired WebDriver, we create a file
script.py and using our code editor write the python script below which opens
up the geeksforgeeks website using the Selenium WebDriver and clicks the Sign
In button using the link text.

 **Syntax:**

  

  

    
    
    driver.find_element_by_link_text("sample text")

 **Steps by step Approach:**

  * Import required modules.
  * Create webdriver object.
  * Assign URL.
  * Use **maximize_window()** method to maximize the browser window. And then wait 10 seconds using **sleep()** method.
  * Use **find_element_by_link_text()** method to click button by text.

Below is the implementation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

from selenium import webdriver

import time

 

# Create the webdriver object. Here the 

# chromedriver is present in the driver 

# folder of the root directory.

driver = webdriver.Chrome(r"./driver/chromedriver")

 

# get https://www.geeksforgeeks.org/

driver.get("https://www.geeksforgeeks.org/")

 

# Maximize the window and let code stall 

# for 10s to properly maximise the window.

driver.maximize_window()

time.sleep(10)

 

# Obtain button by link text and click.

button = driver.find_element_by_link_text("Sign In")

button.click()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210222231422/output_FTOFsx0Z_Tx7e.mp4

First, the WebDriver opens up the window with geeksforgeeks, maximizes it, and
waits for 10 seconds. Then it clicks the Sign In button and opens up the sign-
up panel.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

