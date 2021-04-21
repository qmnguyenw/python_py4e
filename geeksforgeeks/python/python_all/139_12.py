Python | Difference between two dates (in minutes) using datetime.timedelta()
method



To find the difference between two dates in Python, one can use the
**timedelta** class which is present in the **datetime** library. The
timedelta class stores the difference between two datetime objects.  
To find the difference between two dates in form of minutes, the attribute
**seconds** of timedelta object can be used which can be further divided by 60
to convert to minutes.  
 **Example 1:**  
The following program takes two datetime objects and finds the difference
between them in minutes.

__

__  
__

__

__  
__  
__

import datetime

 

# datetime(year, month, day, hour, minute, second)

a = datetime.datetime(2017, 6, 21, 18, 25, 30)

b = datetime.datetime(2017, 5, 16, 8, 21, 10)

 

# returns a timedelta object

c = a-b 

print('Difference: ', c)

 

minutes = c.total_seconds() / 60

print('Total difference in minutes: ', minutes)

 

# returns the difference of the time of the day

minutes = c.seconds / 60

print('Difference in minutes: ', minutes)  
  
---  
  
 __

 __

 **Output:**

    
    
    Difference:  36 days, 10:04:20
    Difference in minutes:  604.3333333333334

 **Example 2:**  
To get a more appropriate answer divmod() can be used which will return the
fractional part of the minutes in terms of seconds:

__

__  
__

__

__  
__  
__

import datetime

 

# datetime(year, month, day, hour, minute, second)

a = datetime.datetime(2017, 6, 21, 18, 25, 30)

b = datetime.datetime(2017, 5, 16, 8, 21, 10)

 

# returns a timedelta object

c = a-b 

print('Difference: ', c)

 

# returns (minutes, seconds)

minutes = divmod(c.total_seconds(), 60) 

print('Total difference in minutes: ', minutes[0], 'minutes',

 minutes[1], 'seconds')

 

# returns the difference of the time of the day (minutes, seconds)

minutes = divmod(c.seconds, 60) 

print('Total difference in minutes: ', minutes[0], 'minutes',

 minutes[1], 'seconds')  
  
---  
  
 __

 __

 **Output:**

    
    
    Difference:  36 days, 10:04:20
    Difference in minutes:  604 minutes 20 seconds

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

