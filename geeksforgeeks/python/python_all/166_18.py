Python program to find day of the week for a given date



Write a Python program to find the day of the week for any particular date in
the past or future. Let the input be in the format “dd mm yyyy”.

 **Examples:**

    
    
    **Input :** 03 02 1997 
    **Output :** Monday
    
    **Input :** 31 01 2019
    **Output :** Thursday
    

The already discussed approach to find the day of the week for a given date is
the Naive approach. Now, let’s discuss the pythonic approaches.

 **Approach #1 :** Using weekday() provided by datetime module.

The weekday() function of date class in datetime module, returns an integer
corresponding to the day of the week.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to Find day of

# the week for a given date

import datetime

import calendar

 

def findDay(date):

 born = datetime.datetime.strptime(date, '%d %m %Y').weekday()

 return (calendar.day_name[born])

 

# Driver program

date = '03 02 2019'

print(findDay(date))  
  
---  
  
 __

 __

 **Output:**

    
    
    Sunday
    

  
**Approach #2 :** Using strftime() method

The strftime() method takes one or more format codes as an argument and
returns a formatted string based on it. Here we will pass the directive “%A”
in the method which provides Full weekday name for the given date.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to Find day of

# the week for a given date

import datetime 

from datetime import date

import calendar

 

def findDay(date):

 day, month, year = (int(i) for i in date.split(' ')) 

 born = datetime.date(year, month, day)

 return born.strftime("%A")

 

# Driver program

date = '03 02 2019'

print(findDay(date))  
  
---  
  
 __

 __

 **Output:**

    
    
    Sunday
    

  
**Approach #3 :** By finding day number

In this approach, we find the day number using calender module and then find
the correspoding week day.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to Find day of

# the week for a given date

import calendar

 

def findDay(date):

 day, month, year = (int(i) for i in date.split(' ')) 

 dayNumber = calendar.weekday(year, month, day)

 days =["Monday", "Tuesday", "Wednesday", "Thursday",

 "Friday", "Saturday", "Sunday"]

 return (days[dayNumber])

 

# Driver program

date = '03 02 2019'

print(findDay(date))  
  
---  
  
 __

 __

 **Output:**

    
    
    Sunday
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

