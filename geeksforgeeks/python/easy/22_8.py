now() function in Python



Python library defines a function that can be primarily used to get current
time and date. **_now()_** function Return the current local date and time,
which is defined under datetime module.

> Syntax : **datetime.now(tz)**
>
>  **Parameters :**  
>  **tz :** Specified time zone of which current time and date is required.
> (Uses Greenwich Meridian time by default.)
>
>  **Returns :** Returns the current date and time in time format.

  
**Code #1 :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Getting current time using 

# now().

 

# importing datetime module for now()

import datetime

 

# using now() to get current time

current_time = datetime.datetime.now()

 

# Printing value of now.

print ("Time now at greenwich meridian is : "

 , end = "")

print (current_time)  
  
---  
  
 __

 __

Output :

    
    
    Time now at greenwich meridian is : 2018-03-29 10:26:23.473031
    

#### Attributes of now() :

now() has different attributes, same as attributes of time such as year,
month, date, hour, minute, second.

 **Code #2 :** Demonstrate attributes of now().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# attributes of now()

 

# importing datetime module for now()

import datetime

 

# using now() to get current time

current_time = datetime.datetime.now()

 

# Printing attributes of now().

print ("The attributes of now() are : ")

 

print ("Year : ", end = "")

print (current_time.year)

 

print ("Month : ", end = "")

print (current_time.month)

 

print ("Day : ", end = "")

print (current_time.day)

 

print ("Hour : ", end = "")

print (current_time.hour)

 

print ("Minute : ", end = "")

print (current_time.minute)

 

print ("Second : ", end = "")

print (current_time.second)

 

print ("Microsecond : ", end = "")

print (current_time.microsecond)  
  
---  
  
 __

 __

    
    
    The attributes of now() are : 
    Year : 2018
    Month : 3
    Day : 26
    Hour : 20
    Minute : 9
    Second : 4
    Microsecond : 499806

#### Getting time of particular timezone :

Sometimes, the need is just to get the current time of a particular timezone.
now() takes timezone as input to give timezone oriented output time. But these
time zones are defined in **pytz** library.

 **Code #3 :** Use of now() to handle specific timezone.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# attributes of now() for timezone

 

# for now()

import datetime

 

# for timezone()

import pytz

 

# using now() to get current time

current_time = datetime.datetime.now(pytz.timezone('Asia /
Calcutta'))

 

# printing current time in india

print ("The current time in india is : ")

print (current_time)   
  
---  
  
__

__

Output:

    
    
    The current time in india is : 
    2018-03-29 03:09:33.878000+05:30
    

**Note :** Above code won’t work on online IDE due to absence of _pytz_
module.  
  
**Application :**  
While developing any real world application, we might need to show real time
of any timezone. now() function can do the work here very efficiently and
easily.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

