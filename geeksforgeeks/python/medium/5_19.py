How to convert timestamp string to datetime object in Python?



Python has a module named DateTime to work with dates and times. We did not
need to install it separately. It is pre-installed with the python package
itself. A UNIX timestamp is several seconds between a particular date and
January 1, 1970, at UTC.

## Timestamp to DateTime object

You can simply use the **fromtimestamp** function from the DateTime module to
get a date from a UNIX timestamp. This function takes the timestamp as input
and returns the corresponding DateTime object to timestamp.

 **Syntax:**

    
    
    fromtimestamp(timestamp, tz=None)

 **Example:** Python timestamp to DateTime

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from datetime import datetime

 

 

timestamp = 1545730073

dt_obj = datetime.fromtimestamp(1140825600)

 

print("date_time:",dt_obj)

print("type of dt:",type(dt_obj))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    date_time: 2006-02-25 05:30:00
    type of dt_obj: <class 'datetime.datetime'>
    

Here, we have imported the DateTime class from DateTime module. Then we have
used _datetime.fromtimestamp()_ class method which returns the local DateTime.

To get a DateTime in a particular form in you can use **strftime** function.
The strftime() function is used to convert date and time objects to their
string representation. It takes one or more input of formatted code and
returns the string representation.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from datetime import datetime

 

 

timestamp = 1553367060

dt_obj = datetime.fromtimestamp(timestamp).strftime('%d-%m-%y')

 

print("date:",dt_obj)  
  
---  
  
 __

 __

 **Output:**

    
    
    date: 24-03-19
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

