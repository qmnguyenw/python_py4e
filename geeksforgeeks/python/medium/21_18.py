Python calendar module : yeardays2calendar() method



Calendar module allows to output calendars like program, and provides
additional useful functions related to the calendar. Functions and classes
defined in Calendar module use an idealized calendar, the current Gregorian
calendar extended indefinitely in both directions.

 **yeardays2calendar()** method in Python is used to get the data for
specified year. Entries in the week lists are tuples of day numbers and
weekday numbers. Day numbers outside this month are zero.

    
    
     **Syntax:** yeardays2calendar(year, width)
    
    **Parameter:** 
    **year:** year of the calendar
    **width:** _[Default: 3]_ number of months in each row. 
    
    **Returns:** tuples of day numbers and weekday numbers.

 **Code #1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate working

# of yeardays2calendar() method

 

# importing calendar module

import calendar

 

obj = calendar.Calendar()

 

year = 2016

# default value of width is 3

 

# priting with yeardays2calendar

print(obj.yeardays2calendar(year))  
  
---  
  
 __

 __

 **Output:**

> [[[[(0, 0), (0, 1), (0, 2), (0, 3), (1, 4), (2, 5), (3, 6)], [(4, 0), (5,
> 1), (6, 2), (7, 3), (8, 4), (9, 5), (10, 6)], [(11, 0), (12, 1), (13, 2),
> (14, 3), (15, 4), (16, 5), (17, 6)], [(18, 0), (19, 1), (20, 2), (21, 3),
> (22, 4), (23, 5), (24, 6)], [(25, 0), (26, 1), (27, 2), (28, 3), (29, 4),
> (30, 5), (31, 6)]]  
> …  
> [[(0, 0), (0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 6)], [(5, 0), (6, 1),
> (7, 2), (8, 3), (9, 4), (10, 5), (11, 6)], [(12, 0), (13, 1), (14, 2), (15,
> 3), (16, 4), (17, 5), (18, 6)], [(19, 0), (20, 1), (21, 2), (22, 3), (23,
> 4), (24, 5), (25, 6)], [(26, 0), (27, 1), (28, 2), (29, 3), (30, 4), (31,
> 5), (0, 6)]]]]
>
>  
>
>
>  
>

**Code #2:** iterating the list of weeks

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate working

# of yeardays2calendar() method

 

# importing calendar module

import calendar

 

obj = calendar.Calendar()

 

# iteratign with yeardays2calendar

for day in obj.yeardays2calendar(2018, 1):

 print(day)  
  
---  
  
 __

 __

 **Output:**

> [[[(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)], [(8, 0), (9, 1),
> (10, 2), (11, 3), (12, 4), (13, 5), (14, 6)], [(15, 0), (16, 1), (17, 2),
> (18, 3), (19, 4), (20, 5), (21, 6)], [(22, 0), (23, 1), (24, 2), (25, 3),
> (26, 4), (27, 5), (28, 6)], [(29, 0), (30, 1), (31, 2), (0, 3), (0, 4), (0,
> 5), (0, 6)]]]  
> …  
> [[[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (2, 6)], [(3, 0), (4, 1),
> (5, 2), (6, 3), (7, 4), (8, 5), (9, 6)], [(10, 0), (11, 1), (12, 2), (13,
> 3), (14, 4), (15, 5), (16, 6)], [(17, 0), (18, 1), (19, 2), (20, 3), (21,
> 4), (22, 5), (23, 6)], [(24, 0), (25, 1), (26, 2), (27, 3), (28, 4), (29,
> 5), (30, 6)], [(31, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

