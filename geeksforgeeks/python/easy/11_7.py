Automate linkedin connections using Python



LinkedIn connections are a very important thing for an IT professional, so we
need to send connection requests to a lot of people who can be useful to us.
But sometimes sending connection requests one at a time can be a little
annoying and hectic. It would be nice to automate this work but How?  
Python to rescue!

In this article, we will learn how to automate the accepting of LinkedIn
connections using Python.

 **Modules required** –

  *  **Selenium** – Selenium does not comes built-in with python. To install selenium type the below command in the terminal.
    
    
    pip install selenium
    

  * **Pyautogui** – Pyautogui also does not comes built-in with python. To install pyautogui type the below command in the terminal.
    
    
    pip install pyautogui
    

  * **Chrome web driver** – To download chrome web driver click here.

Below is the implementation.

First of all, let’s import all the important stuff.

  

  

    
    
    # connect python with webbrowser-chrome
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import pyautogui as pag
    

Now, let’s write the main function-

    
    
    
    def main():
        # url of LinkedIn
        url = “http://linkedin.com/"  
        # url of LinkedIn network page
        network_url = “http://linkedin.com / mynetwork/" 
        # path to browser web driver
        driver = webdriver.Chrome('C:\\Program Files\\Web Driver\\chromedriver.exe'')
        driver.get(url)
    
    # Driver's code
    if __name__ == __main__:
        main()
    
    

We need to go to the authentication page and then we need to login. Here is
the code-

    
    
    
    def login():
        # Getting the login element
        username = driver.find_element_by_id(“login-email”)  
        # Sending the keys for username     
        username.send_keys(“username”)       
        # Getting the password element                            
        password = driver.find_element_by_id(“login-password”) 
        # Sending the keys for password   
        password.send_keys(“password”)               
        # Getting the tag for submit button           
        driver.find_element_by_id(“login-submit”).click()         
    

find_element_by_id is used to find the HTML tag ‘login-email’ and ‘login-
password’ then we sent the keys of those.

Next, we go to the network section-

    
    
    def goto_network():
        driver.find_element_by_id(“mynetwork-tab-icon”).click()
    

Now, LinkedIn tries to prevent scraping so finding the connection button can
be a little tricky. So you need to try hard and find the connection button
position somehow(You can use some techniques like Xpath).

Code for sending requests-

    
    
    def send_requests():
        # Number of requests you want to send
        n = input(“Number of requsts: ”)   
    
        for i in range(0, n):
            # position(in px) of connection button 
            # will be different for different user
            pag.click(880, 770)  
        print(“Done !”)
    

To click on the required position, we use pyautogui i.e. pag.click(, ). So
this is how we can automate sending LinkedIn connections.

Here is the full code-

 __

 __  
 __

 __

 __  
 __  
 __

# connect python with webbrowser-chrome

from selenium import webdriver 

from selenium.webdriver.common.keys import Keys

import pyautogui as pag

 

 

def login():

 

 # Getting the login element

 username = driver.find_element_by_id("login-email") 

 

 # Sending the keys for username 

 username.send_keys("username")

 

 # Getting the password element 

 password = driver.find_element_by_id("login-password")

 

 # Sending the keys for password 

 password.send_keys("password") 

 

 # Getting the tag for submit button 

 driver.find_element_by_id("login-submit").click() 

 

def goto_network():

 driver.find_element_by_id("mynetwork-tab-icon").click()

 

def send_requests():

 

 # Number of requests you want to send

 n = input("Number of requsts: ") 

 

 for i in range(0, n):

 # position(in px) of connection button

 pag.click(880, 770) 

 print("Done !")

 

def main():

 

 # url of LinkedIn

 url = "http://linkedin.com/"

 

 # url of LinkedIn network page

 network_url = "http://linkedin.com / mynetwork/"

 

 # path to browser web driver

 driver = webdriver.Chrome('C:\\Program Files\\Web
Driver\\chromedriver.exe') 

 driver.get(url)

 

# Driver's code 

if __name__ == __main__:

 main()  
  
---  
  
 __

 __

 **Output screen:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/20190801202300/sel.jpg)  
All, the connections are sent!

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

