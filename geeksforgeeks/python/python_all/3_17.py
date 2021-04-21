Python program to calculate Date, Month and Year from Seconds



Given the number of seconds, the task is to write a Python program to
calculate the date, month, and year in the format MM-DD-YYYY that have been
passed from 1 January 1947.

 **Examples:**

    
    
     **Input:** 0
    **Output:** 01-01-1947
    
    **Input:** 123456789
    **Output:** 11-29-1950
    
    **Input:** 9876543210
    **Output:** 12-22-2259

 **Step-by-step Approach:**

  * Create a function to get the number of days in a year.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# function to get number of

# days in the year

# if leap year then 366

# else 365

def dayInYear(year):

 

 if (year % 4) == 0:

 

 if (year % 100) == 0:

 

 if (year % 400) == 0:

 return 366

 else:

 return 365

 

 else:

 return 366

 

 else:

 return 365  
  
---  
  
 __

 __

  * Create a function to count the years after 1947.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# counting the years after 1947

def getYear(days):

 year = 1946

 

 while True:

 year += 1

 dcnt = dayInYear(year)

 

 if days >= dcnt:

 days -= dcnt

 else:

 break

 return year, days  
  
---  
  
 __

 __

