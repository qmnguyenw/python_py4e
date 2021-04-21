Find number of times every day occurs in a Year



Given a year .Your task is to find the number of every day in a year ie.number
of Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday, Sunday in that
given year.

 **Examples:**

    
    
    Input: 2019
    Output: Monday-52
            Tuesday-53
            Wednesday-52
            Thrusday-52
            Friday-52
            Saturday-52
            Sunday-52
    
    Input: 2024
    Output: Monday-53
            Tuesday-53
            Wednesday-52
            Thrusday-52
            Friday-52
            Saturday-52
            Sunday-52
    

**Observations:** We have to make some key observations. The first one will be
that there are at least 52 weeks in a year, so every day will occur at least
52 times in a year. As 52*7 is 364 so the day occurring on the 1st January of
any year will occur 53 times and if the year is a leap year then the day on
the 2nd January will also occur 53 times.

 **Approach:** Create a list with size 7 and having an initial value of 52 as
the minimum number of occurrences will be 52. Find the index of the first day.
Calculate the number of days whose occurrence will be 53.

Below is the implementation.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# python program Find number of

# times every day occurs in a Year 

 

 

import datetime 

import calendar

 

def day_occur_time(year):

 

 # stores days in a week 

 days = [ "Monday", "Tuesday", "Wednesday", 

 "Thursday", "Friday", "Saturday", 

 "Sunday" ]

 

 # Initialize all counts as 52

 L = [52 for i in range(7)]

 

 # Find the index of the first day

 # of the year

 pos = -1

 day = datetime.datetime(year, month = 1, day =
1).strftime("%A")

 for i in range(7):

 if day == days[i]:

 pos = i

 

 # mark the occurrence to be 53 of 1st day

 # and 2nd day if the year is leap year

 if calendar.isleap(year):

 L[pos] += 1

 L[(pos+1)%7] += 1

 

 else:

 L[pos] += 1

 

 

 # Print the days

 for i in range(7):

 print(days[i], L[i])

 

 

# Driver Code 

year = 2019

day_occur_time(year)  
  
---  
  
 __

 __

 **Output:**

    
    
    Monday 52
    Tuesday 52
    Wednesday 52
    Thursday 52
    Friday 53
    Saturday 53
    Sunday 52
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

