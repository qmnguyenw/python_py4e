Python Program to Print the Incremented Date if valid



In this article, we will write a python program to input a date and check
whether it is a valid date or not. If it is valid, output the incremented
date. Otherwise, print “Invalid date”.

 **Examples:**

    
    
     **Input :** 1/2/2000
    **Output:** 2/2/2000
    
    **Input :** 29/2/2002
    **Output:** Invalid date
    
    **Input :** 31/12/2015
    **Output:** 1/1/2016 
    

The first step is to check whether the entered date is valid or not. For this
step, we need to first obtain the maximum possible day number for the month
entered. Then we need to see whether the day lies between 1 and the obtained
maximum day number and whether the month lies between 1 and 12. If both these
conditions get satisfied, that means it is a valid date, and we need to
increment it. To increment the date, we need to handle the following cases:

  1. If the entered date is the last day of the year.
  2. If the entered date is the last day of the month.
  3. If the entered date is not the last day of the month.

For the first case, increment the year and set both the day and the month to
1. For the second case, increment the month and set the day to 1. For the
third case, just increment the day. If even one of the two conditions did not
get satisfied, then it is an invalid date.

Below is the implementation.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# input the date and split it to day, month and year

day, month, year = map(int, input().split('/'))

 

if month == 2:

 

 # check for February

 if year % 4 != 0:

 d_max = 28

 else:

 d_max = 29

 

elif month in [4, 6, 9, 11]:

 

 # check the months with 30 days

 d_max = 30

 

else:

 d_max = 31

 

if 1 <= day <= d_max and 1 <= month <= 12:

 

 # increment the date since it is a

 # valid date

 if day == d_max:

 day = 1

 if month == 12:

 

 # If this block is enterred,

 # then it is the last day of

 # the year

 month = 1

 year += 1

 else:

 

 # If this block is enterred, 

 # then it is the last day of 

 # the month

 month += 1

 else:

 

 # If this block is enterred, then it

 # is NOT the last day of the month

 day += 1

 print(str(day) + "/" + str(month) + "/" +
str(year))

else:

 print("Invalid date")  
  
---  
  
 __

 __

 **Output:**

    
    
    31/12/2015
    1/1/2016
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

