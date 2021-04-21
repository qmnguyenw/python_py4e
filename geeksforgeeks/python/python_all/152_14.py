Python | Print number of leap years from given list of years



The problem of finding leap year is quite generic and we might face the issue
of finding the number of leap years in given list of years. Let’s discuss
certain ways in which this can be performed.

 **Method #1: Using Iteration**

Check whether year is a multiple of 4 and not multiple of 100 or year is
multiple of 400.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to finding number of

# leap years in list of years.

 

# Input list initialization

Input = [2001, 2002, 2003, 2004, 2005, 2006,

 2007, 2008, 2009, 2010, 2011, 2012]

 

# Find whether it is leap year or not

def checkYear(year):

 return (((year % 4 == 0) and

 (year % 100 != 0)) or

 (year % 400 == 0)) 

 

# Answer Initialization

Answer = 0

 

for elem in Input:

 if checkYear(elem):

 Answer = Answer + 1

 

# Printing

print("No of leap years are:", Answer)  
  
---  
  
 __

 __

 **Output:**

    
    
    No of leap years are: 3
    

  
**Method #2: Usingcalender**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to finding number of

# leap years in list of years.

 

# Importing calender

import calendar

 

# Input list initialization

Input = [2001, 2002, 2003, 2004, 2005,

 2006, 2007, 2008, 2009, 2010]

 

# Using calender to find leap year

def FindLeapYear(Input):

 ans = 0

 for elem in Input:

 if calendar.isleap(int(elem)):

 ans = ans + 1

 return ans

 

Output = FindLeapYear(Input)

 

# Printing

print("No of leap years are:", Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    No of leap years are: 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

