Python calendar module : yeardayscalendar() method



Calendar module allows to output calendars like program, and provides
additional useful functions related to the calendar. Functions and classes
defined in Calendar module use an idealized calendar, the current Gregorian
calendar extended indefinitely in both directions.

 **yeardayscalendar()** method in Python is used to get the data for
specified year. Entries in the week lists are day numbers. Day numbers outside
this month are zero.

    
    
     **Syntax:** yeardayscalendar(year, width)
    
    **Parameter:** 
    **year:** year of the calendar
    **width:** _[Default: 3]_ number of months in each row. 
    
    **Returns:** list of day numbers.

 **Code #1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate working

# of yeardayscalendar() method

 

# importing calendar module

import calendar

 

obj = calendar.Calendar()

 

year = 2016

# default value of width is 3

 

# priting with yeardayscalendar

print(obj.yeardayscalendar(year))  
  
---  
  
 __

 __

 **Output:**

> [[[[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16,
> 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31]], [[1, 2, 3,
> 4, 5, 6, 7]…  
> …  
> [[0, 0, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17,
> 18], [19, 20, 21, 22, 23, 24, 25], [26, 27, 28, 29, 30, 31, 0]]]]
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

# of yeardayscalendar() method

 

# importing calendar module

import calendar

 

obj = calendar.Calendar()

 

# iteratign with yeardayscalendar

for day in obj.yeardayscalendar(2018, 1):

 print(day)  
  
---  
  
 __

 __

 **Output:**

> [[[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19,
> 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 0, 0, 0, 0]]]  
> [[[0, 0, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17,
> 18], [19, 20, 21, 22, 23, 24, 25], [26, 27, 28, 0, 0, 0, 0]]]  
> …  
> [[[0, 0, 0, 0, 0, 1, 2], [3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15,
> 16], [17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30], [31, 0, 0,
> 0, 0, 0, 0]]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

