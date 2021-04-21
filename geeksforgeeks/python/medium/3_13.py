How to add and subtract days using DateTime in Python?



As we know date and time are used in programs where we have to keep track of
date and time, so it is necessary to have a module to manipulate date and
time. In python, a **DateTime** module deals with dates and times.
**Datetime** module is built into Python standard library.

Datetime module consists of the following classes: |

**Name**|

 **Description**|  1.|  **date**|  It shows the date according to the Georgian
calendar with attributes are year, month and day.| 2.|  **time**|  It shows
time, independent of any particular day with attributes are hour, minute,
second, microsecond, and tzinfo.| 3.|  **datetime**|  It is a collection of
date and time with the attributes year, month, day, hour, minute, second,
microsecond, and tzinfo.| 4.|  **timedelta**|  It is used to manipulate date.|
5.|  **tzinfo**|  It provides information about time zone.  
---|---|---  
  
##  **Add and subtract days using DateTime in Python**

For adding or subtracting date, we use something called **timedelta()**
function which can be found under **datetime** class. It is used to manipulate
date, and we can perform an arithmetic operations on date like adding or
subtract. **timedelta** is very easy and useful to implement.

  

  

>  **Syntax:** class datetime.timedelta(days=10, seconds=40, microseconds=10,
> milliseconds=60, minutes=10, hours=4, weeks=8)
>
>  **Returns :** Date
>
>  **Note :** if we doesn’t specify bydefault it takes interger as an day.

**Example 1.** Adding Days

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# MANIPULATING DATETIME

from datetime import date, timedelta

today_date = date.today()

print("CURRENT DAY : ", today_date)

# as said earlier it takes argument as day by default

td = timedelta(5)

print("AFTER 5 DAYS DATE WILL BE : ", today_date + td)  
  
---  
  
 __

 __

**Output:**

    
    
    CURRENT DAY :  2020-12-27
    AFTER 5 DAYS DATE WILL BE :  2021-01-01

 **Example 2.** Subtract Days

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# MANIPULATING DATETIME

from datetime import date, timedelta

current_date = date.today()

print("CURRENT DAY : ",current_date)

print("OLD Date : ",current_date - timedelta(17))  
  
---  
  
 __

 __

