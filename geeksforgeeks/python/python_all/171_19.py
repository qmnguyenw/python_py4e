Python program to find number of days between two given dates



Given two dates, Write a Python program to find the total number of days
between them.  
**Examples:**  

    
    
    **Input :** dt1 = 13/12/2018, dt2 = 25/2/2019
    **Output :** 74 days
    
    **Input :** dt1 = 01/01/2004, dt2 = 01/01/2005
    **Output :** 365 days
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** One Naive Solution is to start from _dt1_ and keep
counting days till _dt2_ is reached. This solution requires more than O(1)
time.  
A Better and Simple solution is to count the total number of days before dt1
from i.e., total days from 00/00/0000 to _dt1_ , then count the total number
of days before _dt2_. Finally, return the difference between the two counts.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program two find number of

# days between two given dates

# A date has day 'd', month 'm' and year 'y'

class Date:

 def __init__(self, d, m, y):

 self.d = d

 self.m = m

 self.y = y

# To store number of days in all months from

# January to Dec.

monthDays = [31, 28, 31, 30, 31, 30,

 31, 31, 30, 31, 30, 31]

# This function counts number of leap years

# before the given date

def countLeapYears(d):

 years = d.y

 # Check if the current year needs to be considered

 # for the count of leap years or not

 if (d.m <= 2):

 years -= 1

 # An year is a leap year if it is a multiple of 4,

 # multiple of 400 and not a multiple of 100.

 return int(years / 4) - int(years / 100) +
int(years / 400)

# This function returns number of days between two

# given dates

def getDifference(dt1, dt2):

 # COUNT TOTAL NUMBER OF DAYS BEFORE FIRST DATE 'dt1'

 # initialize count using years and day

 n1 = dt1.y * 365 + dt1.d

 # Add days for months in given date

 for i in range(0, dt1.m - 1):

 n1 += monthDays[i]

 # Since every leap year is of 366 days,

 # Add a day for every leap year

 n1 += countLeapYears(dt1)

 # SIMILARLY, COUNT TOTAL NUMBER OF DAYS BEFORE 'dt2'

 n2 = dt2.y * 365 + dt2.d

 for i in range(0, dt2.m - 1):

 n2 += monthDays[i]

 n2 += countLeapYears(dt2)

 # return difference between two counts

 return (n2 - n1)

# Driver program

dt1 = Date(13, 12, 2018)

dt2 = Date(25, 2, 2019)

print(getDifference(dt1, dt2), "days")  
  
---  
  
 __

 __

 **Output:**

    
    
    74 days
    
    
    
    

  
**Using Python datetime module** :  
Python comes with an inbuilt _datetime_ module which helps us to solve various
datetime related problems. In order to find the difference between two dates
we simply input the two dates with date type and subtract them, which in turn
provides us the number of days between the two dates.  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find number of days

# between two given dates

from datetime import date

def numOfDays(date1, date2):

 return (date2-date1).days

 

# Driver program

date1 = date(2018, 12, 13)

date2 = date(2019, 2, 25)

print(numOfDays(date1, date2), "days")  
  
---  
  
 __

 __

 **Output:**

    
    
    74 days
    
    
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

