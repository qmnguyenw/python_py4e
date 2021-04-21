Load testing using LOCUST



Locust is an open source load testing tool. Load testing is a type of software
testing that is conducted to check the tolerance/behavior of the system under
a specific expected load. The target of locust is load-testing web sites and
checking number of concurrent users a system can handle.  
During a locust test, a swarm of locusts will attack the target i.e website.
The behavior of each locust is configurable and the swarming process is
monitored from a web UI in real-time.

 **Speciality of locust:**

  * Test scenarios can be written in Python
  * Distributed and scalable
  * Web-based UI
  * Any system can be tested using this tool

 **Installation:**

Locust can be installed with pip.

    
    
    pip install locust

Once the locust is successfully installed, a locust command should be
available in your shell.  
To see more available options:

  

  

    
    
    locust --help

 **Getting started:**

 __

 __  
 __

 __

 __  
 __  
 __

from locust import HttpLocust, TaskSet, task

from locust import ResponseError

import json

 

 

class UserBehavior(TaskSet):

 

 def __init__(self, parent):

 super(UserBehavior, self).__init__(parent)

 self.token = ""

 self.headers = {}

 

 def on_start(self):

 # The on_start method is called 

 # when a simulated user starts 

 # executing that TaskSet class

 self.token = self.login()

 self.headers = {'Authorization': 'Bearer
{}'.format(self.token)}

 self.login()

 

 def login(self):

 # admin login and retrieving it's access token

 response = self.client.post("/login/",

 data = {'username': 'admin',

 'password': 'ZYT5nsg3565!'})

 

 return json.loads(response._content)['access']

 

 

 

class WebsiteUser(HttpLocust):

 # The task_set attribute should point

 # to a TaskSet class which defines 

 # the behaviour of the user

 task_set = UserBehavior

 min_wait = 5000

 max_wait = 9000  
  
---  
  
 __

 __

 **Start locust:**  
To run the above code, create a Python file named locustfile.py, and open
the terminal in the directory of the above created file. Then write the
following command in the terminal.

    
    
    locust

 **Note:** By default locust searches for locustfile.py.

After the successful execution of the above command, you should open a browser
and hit **http://127.0.0.1:8089**

The Locust UI will appear like below:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200210224427/locust_UI.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

