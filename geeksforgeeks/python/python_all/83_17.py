Python program to get Current Time



In this article, we will know the approaches to get the current time in
Python. There are multiple ways to get it. The most preferably date-time
module is used in Python to create the object containing date and time.  
 **1: Current time of a timezone –** Using pytZ module

 __

 __  
 __

 __

 __  
 __  
 __

from datetime import *

import pytz

 

 

tz_INDIA = pytz.timezone('Asia/Kolkata') 

datetime_INDIA = datetime.now(tz_INDIA)

print("INDIA time:", datetime_INDIA.strftime("%H:%M:%S"))  
  
---  
  
 __

 __

 **Output:**

    
    
    INDIA time: 19:29:53

 **2 : Current time –** Using date time object

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

from datetime import datetime

 

# now() method is used to

# get object containing 

# current date & time.

now_method = datetime.now()

 

# strftime() method used to

# create a string representing

# the current time.

currentTime = now_method.strftime("%H:%M:%S")

print("Current Time =", currentTime)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Current Time = 19:31:51
    

**Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

from datetime import datetime

 

# Time object containing 

# the current time.

time = datetime.now().time() 

 

print("Current Time =", time)  
  
---  
  
 __

 __

 **Output:**

    
    
    Current Time = 19:33:29.087840

 **3\. Getting Time –** using Time module.

 __

 __  
 __

 __

 __  
 __  
 __

import time

 

 

# localtime() method used to

# get the object containing

# the local time.

Time = time.localtime()

 

# strftime() method used to

# create a string representing

# the current time.

currentTime = time.strftime("%H:%M:%S", Time)

print(currentTime)  
  
---  
  
 __

 __

 **Output:**

    
    
    19:35:17

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

