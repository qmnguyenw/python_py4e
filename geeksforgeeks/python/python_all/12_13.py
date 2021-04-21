Python program to print current year, month and day



In this article, the task is to write a Python Program to print the current
year, month, and day.

 **Approach:**

  * In Python, in order to print the current date consisting of a year, month, and day, it has a module named datetime. From the DateTime module, import date class
  * Create an object of the date class
  * Call the today( ) function of date class to fetch todays date.
  * By using the object created, we can print the year, month, day(attribute of date class) of today.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing date class from datetime module

from datetime import date

 

# creating the date object of today's date

todays_date = date.today()

 

# printing todays date

print("Current date: ", todays_date)

 

# fetching the current year, month and day of today

print("Current year:", todays_date.year)

print("Current month:", todays_date.month)

print("Current day:", todays_date.day)  
  
---  
  
 __

 __

 **Output:**

    
    
    Current date:  2020-12-10
    Current year: 2020
    Current month: 12
    Current day: 10

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

