Facebook Login using Python



Python scripting is one of the most intriguing and fascinating things to do
meanwhile learning Python. Automation and controlling the browser is one of
them.

In this particular article, we will see how to log in to the Facebook account
using Python and the power of selenium.

Selenium automates and controls browsers and it’s activity. We can code in our
way to control browser tasks with the help of selenium. Primarily, it is for
automating web applications for testing purposes, but is certainly not limited
to just that. Boring web-based administration tasks can be automated as well.
As you learn more it’s so much fun to see things happening automatically and
saving time in doing useless tasks again and again.

We use selenium here to open the site of our requirement (in this case
Facebook) and there we inspect elements across email box, password box, and
login button to find the id of them.

  * Using **find_element_by_id()** function provided by selenium module, we can find the required element (username box, password box, login button)
  * Using **send_keys()** function, provided by selenium module, we will send the data into the box.

  1.  **Installing third party modules required**
    
    
    Selenium 
    getpass
    Additional Requirement : geckodriver for firefox and 
                             chromedriver for chrome
    

  2. **Importing necessary modules**
    * Selenium : to automate browser
    * Time : to pause running of script for some seconds as browsers try to detect automation stuff if we input too fast
  3.  **Taking username and password as input from user**  
Using **input()** function and passing prompt message as argument.

  4.  **Opening browser and required website**  
 **webdriver.Chrome()** will open new window of chrome. We will save it’s
object in variable named driver.  
Now using get function we will open up the Facebook website.

  5.  **Finding element for sending data and Sending input**  
Use inspect element tool on the element of browser of which you want to find
id. In this case we will inspect username box, password box, login button to
find their id. And then use this id combining with selenium function
**find_element_by_id()** to find it across web page and save it in variables
for later use. Then by using **send_keys()** we will send data across the
elements found previously.

  6.  **Closing the browser**  
After all of the above steps we have to quit the session and will be achieved
by using driver.quit().  
 **Note:** Here **driver** is the name of variable you chose for
webdriver.Chrome().

 **Complete Code:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from selenium import webdriver

from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options 

 

usr=input('Enter Email Id:') 

pwd=input('Enter Password:') 

 

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.facebook.com/')

print ("Opened facebook")

sleep(1)

 

username_box = driver.find_element_by_id('email')

username_box.send_keys(usr)

print ("Email Id entered")

sleep(1)

 

password_box = driver.find_element_by_id('pass')

password_box.send_keys(pwd)

print ("Password entered")

 

login_box = driver.find_element_by_id('loginbutton')

login_box.click()

 

print ("Done")

input('Press anything to quit')

driver.quit()

print("Finished")  
  
---  
  
 __

 __

See how such a concise piece of code can automate things for you.

 **Bonus:**  
We can also **enter the password without displaying it on screen** , for
security purpose. For that we have to include one more module called
**getpass**. Now with just one change in input statement of the password we
can input password without displaying it on screen.

 __

 __  
 __

 __

 __  
 __  
 __

from getpass import getpass

pwd = getpass('Enter Password:')   
  
---  
  
__

__

Getpass prompts the user for a password without echoing. Basically it lets you
enter the password without showing it on the screen.

Similarly you can also automate many other things like twitter login,
tweeting, Facebook logout, and much more.

 **In case of any queries, post them below in the comments section. If you
liked this article and want to see any more of the similar stuff, let me know
in the comments section below.**

This article is contributed by **Umang Ahuja**. If you like GeeksforGeeks and
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

