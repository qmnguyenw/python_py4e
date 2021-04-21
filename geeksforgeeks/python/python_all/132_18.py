Python program to find the first day of given year



Given a year as input, write a Python to find the starting day of the given
year. We will use Python datetime library in order to solve this problem.

 **Example:**

    
    
     **Input :** 2010
    **Output :** Friday
    
    **Input :** 2019
    **Output :** Tuesday
    

Below is the implementation:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find the first day of given year

 

# import datetime library

import datetime

 

def Startingday(year):

 

 # Creating an object for 1st January of that particular year

 # For that we are passing three argument (1) year (2) month

 # i.e 1 for january (3) date i.e 1 for starting day of 

 # that particular year

 a = datetime.datetime(year, 1, 1)

 

 # for printing Startingday of a particular year 

 # we are using a.strftime("% A")

 print("Starting day of year ", year, " is ",
a.strftime("%A"))

 

# Driver Code

year = 2010

Startingday(year)  
  
---  
  
 __

 __

 **Output:**

    
    
    Starting day of year  2010  is  Friday
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

