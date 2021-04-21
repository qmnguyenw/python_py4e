Subdomain in Flask | Python



Prerequisite: Introduction to Flask

In this article, we will learn how to setup subdomains in Flask. But first,
let’s go through the basic like what is DNS and subdomains.

 **Domain Name System (DNS):**  
The Domain Name System (DNS) is a hierarchical and decentralized naming system
for computers, services, or other resources connected to the Internet or a
private network. Most prominently, it translates more readily memorized domain
names to the numerical IP addresses needed for locating and identifying
computer services and devices with the underlying network protocols.  
DNS is basically using words (Domain Names) in place of numbers (IP addresses)
to locate something. For example, 127.0.0.1 is used to point the local
computer address, _localhost_.

 **Subdomain:**  
A subdomain is a domain that is part of a larger domain. Basically, it’s a
sort of child domain which means it is a part of some parent domain. For
example, practice.geeksforgeeks.org and contribute.geeksforgeeks.org are
subdomains of the geeksforgeeks.org domain, which in turn is a subdomain of
the org top-level domain (TLD).  
These are different from the path defined after TLD as in
geeksforgeeks.org/basic/.

Further, we will discuss how to set endpoints in your web application using
Python’s micro-framework, Flask.

  

  

 **Adding alternate domain name for local IP –**  
Prior to the coding part, we got to setup _hosts_ file in order to provide
alternate names to local IP so that we are able to test our app locally. Edit
this file with root privileges.

    
    
     **Linux:** /etc/hosts 
    **Windows:** C:\Windows\System32\Drivers\etc\hosts

Add these lines to set up alternate domain names.

    
    
    127.0.0.1       vibhu.gfg
    127.0.0.1       practice.vibhu.gfg

In this example, we’re considering vibhu.gfg as our domain name, with gfg
being the TLD. practice would be a subdomain we’re targeting to set in our
web app.

 **Setting up the Server –**  
In the app’s configuration SERVER_NAME is set to the domain name, along with
the port number we intend to run our app on. The default port, flask uses is
5000, so we take it as it is.

 __

 __  
 __

 __

 __  
 __  
 __

from flask import Flask

 

app = Flask(__name__)

 

 

@app.route('/')

def home():

 return "Welcome to GeeksForGeeks !"

 

 

if __name__ == "__main__":

 website_url = 'vibhu.gfg:5000'

 app.config['SERVER_NAME'] = website_url

 app.run()  
  
---  
  
 __

 __

 **Output:**  
Run the app and notice the link on which the app is running.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190417001639/flask0.png)  
Test the link on your browser.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190417002030/flask1.png)

 **Adding Several Endpoints –**

  1.  **basic:** An endpoint with extension to the path on the main domain.
  2.  **practice:** An endpoint serving on the practice subdomain.
  3.  **courses:** An endpoint with extension on to the path on the practice subdomain.

Subdomains in Flask are set using the subdomain parameter in the app.route
decorator.

 __

 __  
 __

 __

 __  
 __  
 __

from flask import Flask

 

app = Flask(__name__)

 

 

@app.route('/')

def home():

 return "Welcome to GeeksForGeeks !"

 

 

@app.route('/basic/')

def basic():

 return "Basic Category Articles " \

 "listed on this page."

 

 

@app.route('/', subdomain ='practice')

def practice():

 return "Coding Practice Page"

 

 

@app.route('/courses/', subdomain ='practice')

def courses():

 return "Courses listed " \

 "under practice subdomain."

 

 

if __name__ == "__main__":

 website_url = 'vibhu.gfg:5000'

 app.config['SERVER_NAME'] = website_url

 app.run()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190417013011/flask4.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

