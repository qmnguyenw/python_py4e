Python | Calendar Module



Python defines an inbuilt module **calendar** which handles operations
related to calendar.

 **Calendar module** allows output calendars like the program and provides
additional useful functions related to the calendar. Functions and classes
defined in Calendar module use an idealized calendar, the current Gregorian
calendar extended indefinitely in both directions. By default, these calendars
have Monday as the first day of the week, and Sunday as the last (the European
convention).

 **Example #1:** Display Calendar of given month.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to display calendar of

# given month of the year 

 

# import module 

import calendar 

 

yy = 2017

mm = 11

 

# display the calendar 

print(calendar.month(yy, mm))   
  
---  
  
__

__

**Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/calendar_month1.png)

 **Example #2:** Display calendar of given year.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# calendar() function to print calendar

 

# importing calendar module 

# for calendar operations 

import calendar 

 

# using calender to print calendar of year 

# prints calendar of 2018 

print ("The calender of year 2018 is : ") 

print (calendar.calendar(2018, 2, 1, 6))   
  
---  
  
__

__

**Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/calendar_month2.png)  
  
**class calendar.Calendar :**

