URL Shorteners and its API in Python | Set-1



URL Shortener, as the name suggests, is a service to help to reduce the length
of the URL so that it can be shared easily on platforms like Twitter, where
number of characters is an issue.  
There are so many URL Shorteners available in the market today, that will
definitely help you out to solve the purpose. We will be discussing API
implementation of Bitly URL Shortener and implementation of a Python module
pyshorteners. This is basically a library in Python that provides
implementation of few popular URL Shorteners.

 **Bitly** : Bitly provides a platform to shorten URL’s, share them and keep a
track of the activity on the shortened URL. Before starting using Bitly API,
you first need to signup on the site to get an API Key. This is very important
to get access to the API to use it for programming.

  * Signup using: Bitly Signup.
  * Once the signup procedure is completed you will see the name on the right hand side with a 4 lines icon.
  * Select **Settings** from the drop down.
  * Go to **ADVANCE SETTINGS** and there you will find the first option as **API SUPPORT**.
  * On selecting this option you will get your username and API Key. To reset your API key, select **Reset API Key** located below your API Key in ‘API Support’.

![](https://media.geeksforgeeks.org/wp-content/uploads/Bitly_api.png)  
Note: API keys are being deprecated, we recommend you use OAuth.

So we will be discussing Bitly API application using both API Keys and OAuth.

Before proceeding further let’s first discuss what is an API Key. Application
Programming Interface Key is a code that is passed by the computer calling an
API that is used to identify the user, computer or we can say the calling
program. This is basically used to control malicious activity in using an API.  
  
**Bitly API Python Module Installation:**

  

  

  1. Following link shows the list of Bitly API code libraries that are available : Bitly API Code Libraries  
In this post we will be using bitly-api-python library which is also official
Python client.

  2. One way to install the python module is to use the **pip** command
    
        pip install bitly_api

  3. In case the installation using pip command is showing error, uninstall bitly_api using the following command:
    
        pip unsinstall bitly_api

  4. Download Bitly API Module using the following link bitly_api
  5. Unzip the downloaded folder and then navigate to the folder bitly-api-python-master, using the command:
    
        cd bitly-api-python-master

  6. Now install bitly_api module using the following command:
    
        python setup.py install

  7. On the command prompt type following set of commands to check whether module is successfully installed or not
    
        python
    import bitly_api

If no error shows, this means module is successfully installed.  
![](https://media.geeksforgeeks.org/wp-content/uploads/import_bitly.png)

  8. Alternatively, you can execute test_bitly_api.py file using the command
    
        python test_bitly_api.py

Absence of error means module is successfully installed.

 **Bitly API Implementation using API Key:**

 __

 __  
 __

 __

 __  
 __  
 __

import bitly_api 

 

API_USER = "username"

API_KEY = "API_Key"

bitly = bitly_api.Connection(API_USER, API_KEY) 

 

response = bitly.shorten('http://google.com/') 

 

# Now let us print the Bitly URL 

print(response)  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/bitly_output.png)  
  
**Bitly API Implementaion using OAuth:**

First we need to Generate OAuth token for the program. Note that only verified
email id can be used to generate OAuth Token.

  * Click on the option **OAuth**
  * You will get a menu like this

![](https://media.geeksforgeeks.org/wp-content/uploads/OAuth.png)

  * Click on **Generic Access Token** option, enter password and you will get the Access Token.

 __

 __  
 __

 __

 __  
 __  
 __

import bitly_api

 

BITLY_ACCESS_TOKEN ="ACCESS_TOKEN"

 

b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)

 

response = b.shorten('http://google.com/')

print(response)   
  
---  
  
__

__

![](https://media.geeksforgeeks.org/wp-content/uploads/GFG_BITLY.png)

**Pyshortner:** **Pyshortner** is a Python module that provides
implementation for various URL Shortening services that are available in the
market.  
Use **pip** command to install the module:

    
    
    pip install pyshorteners

  
Now let’s discuss code implementation and output of Google URL shortening
service.

 **Google URL Shortener:** Before starting using Google URL Shortener we first
need to signup, create a project and get an API Key for using the API.  
Steps to create an API Key are as follows:

  

  

  * Navigate to Google Developers homepage and Click on **Sign In** in the upper rightmost corner of the page. Sign In using the credentials of the valid Google Account. If you don’t have a google account, setup a account first and then use the details to Sign In on the Google Developers Homepage.
  * Now navigate to the Developer Dashboard and Click on **Enable API** option.
  * In the search field, search for **URL Shortener** and select the **URL Shortener API** option that comes in the drop down list.

![](https://media.geeksforgeeks.org/wp-content/uploads/GFG_GURL_2.png)

  * You will be redirected to a screen that says information about the URL Shortener API, along with two options : **MANAGE** and **TRY API**
  * Click on **MANAGE** option and create a project to get started with the API.
  * You’ll be redirected to the search page again. Click **Enable** above the search bar.
  * You will see a bar showing the message **To use this API, you may need credentials. Click ‘Create Credentials’ to get started.**

![](https://media.geeksforgeeks.org/wp-content/uploads/GFG_GURL_3.png)

  * Click on **Create Credentials** in the top right corner.
  * You will be redirected to the page to add credentials.
  * For **Which API are you using?** select **URL Shortener API** if not already selected.
  * For **Where will you be calling the API from?** select **Other UI(eg. Windows, CLI Tool)**
  * For **What data you will be accessing?** select **Public Data**

![](https://media.geeksforgeeks.org/wp-content/uploads/GFG_GURL_4-300x191.png)

  * Click on **What Credentials do I need?**. You will be redirected to a page that says **Add Credentials to your project**. This page will also give you **API Key.**

 __

 __  
 __

 __

 __  
 __  
 __

from pyshorteners import Shortener

 

long_url = 'http://www.google.com'

 

API_Key = 'AIzaSyBBS...jXKIGh1fNU'

 

url_shortener = Shortener('Google', api_key = API_Key)

print ("Short URL is {}".format(url_shortener.short(long_url)))  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/GFG_GURL_5.png)

 **Code to Expand the Shortened URL:**

 __

 __  
 __

 __

 __  
 __  
 __

from pyshorteners import Shortener

 

short_url ='https://goo.gl/fbsS'

 

API_Key = 'AIzaSyBBSL...jXKIGh1fNU'

 

url_expander = Shortener('Google', api_key = API_Key)

 

print ("Long URL is {}".format(url_expander.expand(short_url)))  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/GFG_GURL_6.png)

