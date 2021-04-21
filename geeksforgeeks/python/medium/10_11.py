Get Current Time in different Timezone using Python



Timezone is defined as a geographical area or region throughout which standard
time is observed. It basically refers to the local time of a region or
country. Most of the time zones are offset from Coordinated Universal Time
(UTC), the world’s standard for time zone.  
In order to get the current time of different time zones, we will be using the
pytz python library.  

### How to get the current time ?

In order to get the local time, we can use the time module. Some important
functions of the time module

  *  ** _localtime()_** – it helps to get the current local time
  *  ** _strftime(“%H:%M:%S”, t)_** – it helps to decide the format of the time to be used to display the time

### How to get current time in different zones ?

In order to get the current time of a particular timezone there is a need to
use the pytz Python library. Some of the important commands of pytz library
are

  *  ** _utc_** – it helps to get the standard UTC time zone
  *  ** _timezone()_** – it helps to get the time zone of a particular location
  *  ** _now()_** – it helps to get the date, time, utc standard in default format
  *  ** _astimezone()_** – it helps to convert the time of a particular time zone into another time zone

 **Examples:**

 __

 __  
 __

 __

 __  
 __  
 __

import time

 

 

curr_time = time.localtime()

curr_clock = time.strftime("%H:%M:%S", curr_time)

 

print(curr_clock)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    11:58:19
    

We will get the local current time of the region and the standard UTC time  
 **Examples:**

 __

 __  
 __

 __

 __  
 __  
 __

from datetime import datetime

import pytz

 

# get the standard UTC time 

UTC = pytz.utc

 

# it will get the time zone 

# of the specified location

IST = pytz.timezone('Asia/Kolkata')

 

# print the date and time in

# standard format

print("UTC in Default Format : ", 

 datetime.now(UTC))

 

print("IST in Default Format : ", 

 datetime.now(IST))

 

# print the date and time in 

# specified format

datetime_utc = datetime.now(UTC)

print("Date & Time in UTC : ",

 datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z %z'))

 

datetime_ist = datetime.now(IST)

print("Date & Time in IST : ", 

 datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z'))  
  
---  
  
 __

 __

    
    
    **Output:**
    UTC in Default Format :  2020-03-31 07:15:59.640418+00:00
    IST in Default Format :  2020-03-31 12:45:59.692642+05:30
    Date & Time in UTC :  2020:03:31 07:15:59 UTC+0000
    Date & Time in IST :  2020:03:31 12:45:59 IST+0530
    

Comparing the UTC and IST format of time zones of different regions  
 **Examples:**

 __

 __  
 __

 __

 __  
 __  
 __

from datetime import datetime

import pytz

 

UTC = pytz.utc

 

timeZ_Kl = pytz.timezone('Asia/Kolkata') 

timeZ_Ny = pytz.timezone('America/New_York')

timeZ_Ma = pytz.timezone('Africa/Maseru')

timeZ_Ce = pytz.timezone('US/Central')

timeZ_At = pytz.timezone('Europe/Athens')

 

dt_Kl = datetime.now(timeZ_Kl)

dt_Ny = datetime.now(timeZ_Ny)

dt_Ma = datetime.now(timeZ_Ma)

dt_Ce = datetime.now(timeZ_Ce)

dt_At = datetime.now(timeZ_At)

 

utc_Kl = dt_Kl.astimezone(UTC)

utc_Ny = dt_Ny.astimezone(UTC)

utc_Ma = dt_Ma.astimezone(UTC)

utc_Ce = dt_Ce.astimezone(UTC)

utc_At = dt_At.astimezone(UTC)

 

print("UTC Format \t\t\t IST Format")

 

print(utc_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z'),

 "\t ",

 dt_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z'))

 

print(utc_Ny.strftime('%Y-%m-%d %H:%M:%S %Z %z'),

 "\t ",

 dt_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z'))

 

print(utc_Ma.strftime('%Y-%m-%d %H:%M:%S %Z %z'),

 "\t ",

 dt_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z'))

 

print(utc_Ce.strftime('%Y-%m-%d %H:%M:%S %Z %z'),

 "\t ",

 dt_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z'))

 

print(utc_At.strftime('%Y-%m-%d %H:%M:%S %Z %z'),

 "\t ",

 dt_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z'))  
  
---  
  
 __

 __

    
    
    **Output:**
    UTC Format               IST Format
    2020-03-31 11:21:13 UTC +0000       2020-03-31 16:51:13 IST +0530
    2020-03-31 11:21:13 UTC +0000       2020-03-31 16:51:13 IST +0530
    2020-03-31 11:21:13 UTC +0000       2020-03-31 16:51:13 IST +0530
    2020-03-31 11:21:13 UTC +0000       2020-03-31 16:51:13 IST +0530
    2020-03-31 11:21:13 UTC +0000       2020-03-31 16:51:13 IST +0530
    

Thus we can conclude that although different regions have different regional
time zones but when converted to the UTC time zone all of them gave same
value. Thus we can say that

  * IST is +0530 hrs ahead of UTC
  * EDT is -0400 hrs before of UTC
  * SAST is +0200 hrs ahead of UTC
  * CDT is -0500 hrs before of UTC
  * EEST is +0300 hrs ahead of UTC

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

