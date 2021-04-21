Whatsapp using Python!



Have you ever wished to automatically wish your friends on their birthdays, or
send a set of messages to your friend ( or any Whastapp contact! )
automatically at a pre-set time, or send your friends by sending thousands of
random text on whatsapp! Using **Browser Automation** you can do all of it and
much more!  
First you must install these:-

1) **Python Bindings for Selenium ( Browser Automation software )**

    
    
    pip install selenium

2) **Chrome webdriver**  
Download Chrome driver from here: Chromedriver download page( choose your
specific version )  
Extract it in a known location , as **we need the location later**

If you get stuck somewhere, Refer To the documentation: Documentation link

3) **Chromium Web Browser( Open source version of chrome browser )**

  

  

    
    
    sudo apt-get install chromium-browser

That’s it! You are all set.

Lets dive in right away-

 __

 __  
 __

 __

 __  
 __  
 __

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

import time

 

# Replace below path with the absolute path

# to chromedriver in your computer

driver = webdriver.Chrome('/home/saket/Downloads/chromedriver')

 

driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

 

# Replace 'Friend's Name' with the name of your friend 

# or the name of a group 

target = '"Friend\'s Name"'

 

# Replace the below string with your own message

string = "Message sent using Python!!!"

 

x_arg = '//span[contains(@title,' + target + ')]'

group_title = wait.until(EC.presence_of_element_located((

 By.XPATH, x_arg)))

group_title.click()

inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'

input_box = wait.until(EC.presence_of_element_located((

 By.XPATH, inp_xpath)))

for i in range(100):

 input_box.send_keys(string + Keys.ENTER)

 time.sleep(1)  
  
---  
  
 __

 __

Keep your mobile phone with you. Choose whatsapp web from the top bar in
whatsapp(3 dots)  
![Screenshot2](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot_2016-11-25-14-52-30-483_com.whatsapp-169x300.png)

Then Run the script **( make sure that you have added the absolute path for
chromedriver and have replaced target variable with your friends name ).**
Scan the QR code that appears on the screen and enjoy the power of python!

![Screenshot3](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot_2016-11-25-16-39-51-503_com.whatsapp-169x300.png)

> Please use this script only for educational purposes, i am not responsible
> if your friends ( or even Whatsapp ) block you.

 **Feel free to modify the code. Try to :**

  1. Text Multiple Groups at once
  2. Send the messages from a predefined list of messages randomly or
  3. Send complete random text.

Comment below about your experience!

 **When it comes to browser automation, this is just the tip of the iceberg.**
Will write more articles on browser automation to give you a glimpse of its
power!

 **Related Post :**  
Browser Automation Using Selenium

This article is contributed by **Saket Modi**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

