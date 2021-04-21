Twitter Automation using Selenium Python



If you are someone like me who considers Twitter to be far better than
Instagram, then I might be having something for you. We all know gaining
followers on twitter can be pretty tough but sometimes retweeting quality
content can gain you followers too. Obviously, you are a busy person and you
don’t have time to sit around on your phone or laptop to read and retweet
contents. Pretty boring task right? Let’s make our smart friend do it. This
article revolves around how to automate twitter using selenium Python.

First, you will be needing **Python**. You download python from here. Now,
let’s begin coding. First, create a folder named **Twitter Automation** and
then change directory to the newly created folder. Now, create a file named
_requirements.txt_ and add just this one line to it.

    
    
    selenium==3.141.0

Next, open up your terminal and type

    
    
    pip install -r requirements.txt

Next, you will need _chrome driver_. You can download it from here. After the
download is complete, move downloaded driver to your newly created folder
_Twitter Automation_.  
Now all the requirements are taken care of. Now let’s begin with the coding.  
  
Now, create a file called _credentials.txt_ and add the following lines to it.

    
    
    email: {your twitter email}
    password: {your twitter password}
    

Replace the email and password placeholder with your original credentials of
twitter. I am using a text file. One could also use a _.env_ file but here for
simplicity I am using a _.txt_ file.

  

  

Next, create another file called **secrets.py** and add the following lines of
code to it.

 __

 __  
 __

 __

 __  
 __  
 __

"""

 Add your twitter handle's email and password

 in the credentials.txt file.

 This will be used to automate the login.

"""

 

def get_credentials() -> dict:

 # dictionary for storing credentials

 credentials = dict()

 # reading the text file 

 # for credentials

 with open('credentials.txt') as f:

 # interating over the lines

 for line in f.readlines():

 try:

 # fetching email and password

 key, value = line.split(": ")

 except ValueError:

 # raises error when email and password not supplied

 print('Add your email and password in credentials file')

 exit(0)

 # removing trailing 

 # white space and new line

 credentials[key] = value.rstrip(" \n")

 # returning the dictionary containing the credentials

 return credentials  
  
---  
  
 __

 __

I have added detailed code explaination in the inline comments for better
understanding. Now, lets create the most important file, the one which does
all the magic. Create a new file called **twitterbot.py** and add the
following lines to it.

 __

 __  
 __

 __

 __  
 __  
 __

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.options import Options

'''Uncomment the below line when running in linux'''

# from pyvirtualdisplay import Display

import time, os

 

class Twitterbot:

 

 def __init__(self, email, password):

 

 """Constructor

 

 Arguments:

 email {string} -- registered twitter email

 password {string} -- password for the twitter account

 """

 

 self.email = email

 self.password = password

 # initializing chrome options

 chrome_options = Options()

 

 # adding the path to the chrome driver and 

 # integrating chrome_options with the bot

 self.bot = webdriver.Chrome(

 executable_path = os.path.join(os.getcwd(), 'chromedriver'),

 options = chrome_options

 )

 

 def login(self):

 """

 Method for signing in the user 

 with the provided email and password.

 """

 

 bot = self.bot

 # fetches the login page

 bot.get('https://twitter.com / login')

 # adjust the sleep time according to your internet speed

 time.sleep(3)

 

 email = bot.find_element_by_xpath(

 '//*[@id ="react-root"]/div / div / div[2]/main / div / div / form / div /
div[1]/label / div / div[2]/div / input'

 )

 password = bot.find_element_by_xpath(

 '//*[@id ="react-root"]/div / div / div[2]/main / div / div / form / div /
div[2]/label / div / div[2]/div / input'

 )

 

 # sends the email to the email input

 email.send_keys(self.email)

 # sends the password to the password input

 password.send_keys(self.password)

 # executes RETURN key action

 password.send_keys(Keys.RETURN)

 

 time.sleep(2)

 

 def like_retweet(self, hashtag):

 

 """

 This function automatically retrieves

 the tweets and then likes and retweets them

 

 Arguments:

 hashtag {string} -- twitter hashtag

 """

 

 bot = self.bot

 

 # fetches the latest tweets with the provided hashtag

 bot.get(

 'https://twitter.com / search?q =% 23' + \

 hashtag+'&src; = typed_query&f; = live'

 )

 

 time.sleep(3)

 

 # using set so that only unique links

 # are present and to avoid unnecessary repetition

 links = set() 

 

 # obtaining the links of the tweets

 for _ in range(100):

 # executing javascript code 

 # to scroll the webpage

 bot.execute_script(

 'window.scrollTo(0, document.body.scrollHeight)'

 )

 

 time.sleep(4)

 

 # using list comprehension 

 # for adding all the tweets link to the set

 # this particular piece of code might

 # look very complicated but the only reason

 # I opted for list comprehension because is

 # lot faster than traditional loops

 [

 links.add(elem.get_attribute('href'))\

 for elem in bot.find_elements_by_xpath("//a[@dir ='auto']")

 ]

 

 # traversing through the generated links

 for link in links:

 # opens individual links

 bot.get(link)

 time.sleep(4)

 

 try:

 # retweet button selector

 bot.find_element_by_css_selector(

 '.css-18t94o4[data-testid ="retweet"]'

 ).click()

 # initializes action chain

 actions = ActionChains(bot)

 # sends RETURN key to retweet without comment

 actions.send_keys(Keys.RETURN).perform()

 

 # like button selector

 bot.find_element_by_css_selector(

 '.css-18t94o4[data-testid ="like"]'

 ).click()

 # adding higher sleep time to avoid

 # getting detected as bot by twitter

 time.sleep(10)

 except:

 time.sleep(2)

 

 # fetches the main homepage

 bot.get('https://twitter.com/')  
  
---  
  
 __

 __

Now, it’s time to code our driver script. To do that, create a file called
**main.py** and add the following lines to it.

 __

 __  
 __

 __

 __  
 __  
 __

import twitterbot as tb

import secrets, sys

 

# fetches the hashtag from command line argument

hashtag = sys.argv[1]

# fetches the credentials dictionary

# using get_credentials function

credentials = secrets.get_credentials()

# initialize the bot with your credentials

bot = tb.Twitterbot(credentials['email'],
credentials['password'])

# loging in

bot.login()

# calling like_retweet function

bot.like_retweet(hashtag)  
  
---  
  
 __

 __

Now, we are done with the code. Let’s call our driver script by running the
following command in your terminal.

    
    
    python main.py {hashtag}
    

Just in place of the hashtag placeholder replace it with any trending hashtag,
for example, you can try

    
    
    python main.py python3

This will like and retweet 100 tweets with the hashtag _python_. You can check
out how it would perform in the video below.

So, there you have it. Go ahead and try it out and do not increase the number
of tweets because twitter has a daily limit of tweets.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

