Python | Convert string to DateTime and vice-versa



Write a Python program to convert a given string to datetime and vice-versa.

 **Program to convert string to DateTime usingstrptime() function.**

 **Examples:**

    
    
    **Input :** Dec 4 2018 10:07AM 
    **Output :** 2018-12-04 10:07:00
    
    **Input :** Jun 12 2013 5:30PM 
    **Output :** 2013-06-12 17:30:00
    

strptime() is available in datetime and time modules and is used for Date-
Time Conversion. This function changes the given string of datetime into the
desired format.

 **Syntax:**

  

  

    
    
    datetime.strptime(date_string, format)

The arguments date_string and _format_ should be of string type.

 __

 __  
 __

 __

 __  
 __  
 __

import datetime

 

# Function to convert string to datetime

def convert(date_time):

 format = '%b %d %Y %I:%M%p' # The format

 datetime_str = datetime.datetime.strptime(date_time, format)

 

 return datetime_str

 

# Driver code

date_time = 'Dec 4 2018 10:07AM'

print(convert(date_time))  
  
---  
  
 __

 __

 **Output:**

    
    
    2018-12-04 10:07:00

  
**Program to convert DateTime to string**  
 **Examples:**

    
    
    **Input :** 2018-12-04 10:07:00  
    **Output :** Dec 4 2018 10:07:00AM 
    
    **Input :** 2013-06-12 17:30:00Jun 12 2013 5:30PM 
    **Output :** Jun 12 2013 5:30:00PM 
    

Python strftime() function is present in datetime and time modules to create
a string representation based on the specified format string.

 **Syntax:**

    
    
    datetime_object.strftime(format_str)

Another similar function is available in time module which converts a tuple or
struct_time object to a string as specified by the format argument.

 __

 __  
 __

 __

 __  
 __  
 __

import time

 

# Function to convert string to datetime

def convert(datetime_str):

 datetime_str = time.mktime(datetime_str)

 

 format = "%b %d %Y %r" # The format

 dateTime = time.strftime(format, time.gmtime(datetime_str))

 return dateTime

 

# Driver code

date_time = (2018, 12, 4, 10, 7, 00, 1,
48, 0)

print(convert(date_time))  
  
---  
  
 __

 __

 **Output:**

    
    
    Dec 04 2018 10:07:00 AM

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

