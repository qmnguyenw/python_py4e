Basic DateTime Operations in Python



Python has an in-built module named DateTime to deal with dates and times in
numerous ways. In this article, we are going to see basic DateTime operations
in Python.

There are six main object classes with their respective components in the
datetime module mentioned below:

  1. datetime.date
  2. datetime.time
  3. datetime.datetime
  4. datetime.tzinfo
  5. datetime.timedelta
  6. datetime.timezone

Now we will see the program for each of the functions under datetime module
mentioned above.

### datetime.date():

We can generate date objects from the date class. A date object represents a
date having a year, month, and day.

>  **Syntax:** datetime.date( year, month, day)
>
>  
>
>
>  
>

 **strftime to print day, month, and year in various formats. Here are some of
them are:**

  *  **current.strftime(“%m/%d/%y”)** that prints in **month(Numeric)/date/year** format
  *  **current.strftime(“%b-%d-%Y”)** that prints in **month(abbreviation)-date-year** format
  *  **current.strftime(“%d/%m/%Y”)** that prints in **date/month/year** format
  *  **current.strftime(“%B %d, %Y”)** that prints in **month(words) date, year** format

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from datetime import date

 

# You can create a date object containing 

# the current date 

# by using a classmethod named today()

current = date.today() 

 

# print current year, month, and year individually

print("Current Day is :", current.day)

print("Current Month is :", current.month)

print("Current Year is :", current.year)

 

# strftime() creates string representing date in 

# various formats

print("\n")

print("Let's print date, month and year in different-different ways")

format1 = current.strftime("%m/%d/%y")

 

# prints in month/date/year format

print("format1 =", format1)

 

format2 = current.strftime("%b-%d-%Y")

# prints in month(abbreviation)-date-year format

print("format2 =", format2)

 

format3 = current.strftime("%d/%m/%Y")

 

# prints in date/month/year format

print("format3 =", format3)

 

format4 = current.strftime("%B %d, %Y")

 

# prints in month(words) date, year format

print("format4 =", format4)  
  
---  
  
 __

 __

 **Output:**

    
    
    Current Day is : 23
    Current Month is : 3
    Current Year is : 2021
    
    
    Let's print date, month and year in different-different ways
    format1 = 03/23/21
    format2 = Mar-23-2021
    format3 = 23/03/2021
    format4 = March 23, 2021

### datetime.time():

A time object generated from the time class represents the local time.

 **Components:**

  * hour
  * minute
  * second
  * microsecond
  * tzinfo

>  **Syntax:** datetime.time(hour, minute, second, microsecond)

 **Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from datetime import time

 

# time() takes hour, minutes, second,

# microsecond respectively in order 

# if no parameter is passed in time() by default

# it takes 0 

defaultTime = time()

 

print("default_hour =", defaultTime.hour)

print("default_minute =", defaultTime.minute)

print("default_second =", defaultTime.second)

print("default_microsecond =", defaultTime.microsecond)

 

# passing parameter in different-different ways

# hour, minute and second respectively is a default

# order

time1= time(10, 5, 25)

print("time_1 =", time1)

 

# assigning hour, minute and second to respective

# variables

time2= time(hour = 10, minute = 5, second = 25)

print("time_2 =", time2)

 

# assigning hour, minute, second and microsecond to

# respective variables

time3= time(hour=10, minute= 5, second=25,
microsecond=55)

print("time_3 =", time3)  
  
---  
  
 __

 __

Output:

    
    
    default_hour = 0
    default_minute = 0
    default_second = 0
    default_microsecond = 0
    time_1 = 10:05:25
    time_2 = 10:05:25
    time_3 = 10:05:25.000055

### datetime.datetime():

datetime.datetime() module shows the combination of a date and a time.

  

  

 **Components:**

  * year
  * month
  * day
  * hour
  * minute
  * second,
  * microsecond
  * tzinfo

>  **Syntax:** datetime.datetime( year, month, day )
>
> or
>
> datetime.datetime(year, month, day, hour, minute, second, microsecond)

 **Current date and time using the strftime() method in different ways:**

  *  **strftime(“%d”)** gives current day
  *  **strftime(“%m”)** gives current month
  *  **strftime(“%Y”)** gives current year
  *  **strftime(“%H:%M:%S”)** gives current time in an hour, minute, and second format
  *  **strftime(“%m/%d/%Y, %H:%M:%S”)** gives date and time together

 **Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from datetime import datetime

 

# now() gives current date and time

current = datetime.now()

 

# print combinedly

print(current)

print("\n")

print("print each term individually")

 

day = current.strftime("%d")

 

# print day

print("day:", day)

 

month = current.strftime("%m")

 

# print month

print("month:", month)

 

year = current.strftime("%Y")

 

# print year

print("year:", year)

 

time = current.strftime("%H:%M:%S")

 

# time in hour, minute and second

print("time:", time)

 

print("\n")

print("printing date and time together")

date_time = current.strftime("%m/%d/%Y, %H:%M:%S")

print("date and time:", date_time)

print("\n")

 

# fetching details from timestamp

timestamp = 1615797322

date_time = datetime.fromtimestamp(timestamp)

 

# %c, %x and %X are used for locale's proper date and time representation

time_1 = date_time.strftime("%c")

print("first_output:", time_1)

 

time_2 = date_time.strftime("%x")

print("second_output:", time_2)

 

time_3 = date_time.strftime("%X")

print("third_output:", time_3)

 

print("\n")

 

# assigning each term manually

manual = datetime(2021, 3, 28, 23, 55, 59,
342380)

print("year =", manual.year)

print("month =", manual.month)

print("hour =", manual.hour)

print("minute =", manual.minute)

print("timestamp =", manual.timestamp())  
  
---  
  
 __

 __

Output:

    
    
    2021-03-23 19:00:20.726833
    
    
    print each term individually
    day: 23
    month: 03
    year: 2021
    time: 19:00:20
    
    
    printing date and time together
    date and time: 03/23/2021, 19:00:20
    
    
    first_output: Mon Mar 15 14:05:22 2021
    second_output: 03/15/21
    third_output: 14:05:22
    
    
    year = 2021
    month = 3
    hour = 23
    minute = 55
    timestamp = 1616955959.34238

### datetime.timedelta():

It shows a duration that expresses the difference between two date, time, or
datetime instances to microsecond resolution.

Here we implemented some basic functions and printed past and future days.
Also, we will print some other attributes of timedelta max, min, and
resolution that show maximum days and time, minimum date and time, and the
smallest possible difference between non-equal timedelta objects respectively.
Here we will also apply some arithmetic operations on two different dates and
times.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from datetime import timedelta, datetime

 

present_date_with_time = datetime.now() 

 

print("Present Date :", present_date_with_time)

 

# coming date after 10 days

ten_days_after= present_date_with_time + timedelta(days = 10)

print('Date after 10 days :',ten_days_after)

 

# date before 10 days

ten_days_before= present_date_with_time - timedelta(days = 10)

print('Date before 10 days :',ten_days_before)

 

# date before one year ago

one_year_before_today= present_date_with_time + timedelta(days =
365)

print('One year before present Date :', one_year_before_today)

 

#date before one year ago

one_year_after_today= present_date_with_time - timedelta(days =
365)

print('One year before present Date :', one_year_after_today)

 

print("\n")

print("print some other attributes of timedelta\n")

 

# maximum days and time

print("Max : ",timedelta.max)

 

# miniimum days and time

print("Min : ",timedelta.min)

 

# The smallest possible difference between non-equal

# timedelta objects, timedelta(microseconds=1)

print("Resolution: ",timedelta.resolution)

 

print('Total number of seconds in an year :', 

 timedelta(days = 365).total_seconds())

 

print("\nApply some operations on timedelta function\n")

time_after_one_min = present_date_with_time +
timedelta(seconds=10) * 6

print('Time after one minute :', time_after_one_min)

 

print('Timedelta absolute value :', abs(timedelta(days =
+20)))

 

print('Timedelta string representation :', str(timedelta(days =
5,

 seconds = 40, hours = 20, milliseconds = 355)))

 

print('Timedelta object representation :', repr(timedelta(days =
5, 

 seconds = 40, hours = 20, milliseconds = 355)))  
  
---  
  
 __

 __

Output:

> Present Date : 2021-03-25 22:34:27.651128
>
> Date after 10 days : 2021-04-04 22:34:27.651128
>
> Date before 10 days : 2021-03-15 22:34:27.651128
>
> One year before present Date : 2022-03-25 22:34:27.651128
>
> One year before present Date : 2020-03-25 22:34:27.651128
>
> print some other attributes of timedelta
>
> Max : 999999999 days, 23:59:59.999999
>
> Min : -999999999 days, 0:00:00
>
> Resolution: 0:00:00.000001
>
> Total number of seconds in an year : 31536000.0
>
> Apply some operations on timedelta function
>
> Time after one minute : 2021-03-25 22:35:27.651128
>
> Timedelta absolute value : 20 days, 0:00:00
>
> Timedelta string representation : 5 days, 20:00:40.355000
>
> Timedelta object representation : datetime.timedelta(days=5, seconds=72040,
> microseconds=355000)

### datetime.tzinfo():

It is an abstract base class for time zone information objects. They are used
by the datetime and time classes to provide a customizable notion of time
adjustment.

There are the following four methods available for tzinfo base class:

  *  **utcoffset(self, dt):** returns the offset of the datetime instance passed as an argument
  *  **dst(self, dt):** dst stands for Daylight Saving Time. dst denotes advancing the clock 1 hour in summer so that darkness falls later according to the clock. It is set to on or off. It is checked on the basis of the following elements:

> (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.weekday(), 0,
> 0)

  *  **tzname(self, dt):** It returns a Python String object. It is used to find the time zone name of the datetime object passed.
  *  **fromutc(self, dt) :** This function returns the equivalent local time and takes up the date and time of the object in UTC. It is mostly used to adjust the date and time. It is called from default datetime.astimezone() implementation. The dt.tzinfo will be passed as self, dst date and time data will be returned as an equivalent local time.

 **Note:** It raises ValueError if dt.tzinfo is not self or/and dst() is None.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

from datetime import datetime, timedelta

from pytz import timezone

import pytz

 

time_zone = timezone('Asia/Calcutta')

 

normal = datetime(2021, 3, 16)

ambiguous = datetime(2021, 4, 16, 23, 30)

 

# is_dst parameter is ignored for most of the

# timstamps.It is only used during DST

# transition ambiguous periods to resolve that

# ambiguity

print("Operations on normal datetime")

print(time_zone.utcoffset(normal, is_dst=True))

print(time_zone.dst(normal, is_dst=True))

print(time_zone.tzname(normal, is_dst=True))

 

# put is_dst=False

print(time_zone.utcoffset(normal, is_dst=False))

print(time_zone.dst(normal, is_dst=False))

print(time_zone.tzname(normal, is_dst=False))

 

print("\n")

print("Opeartions on ambiguous datetime")

print(time_zone.utcoffset(ambiguous, is_dst=True))

print(time_zone.dst(ambiguous, is_dst=True))

print(time_zone.tzname(ambiguous, is_dst=True))

 

# is_dst=False

print(time_zone.utcoffset(ambiguous, is_dst=False))

print(time_zone.dst(ambiguous, is_dst=False))

print(time_zone.tzname(ambiguous, is_dst=False))  
  
---  
  
 __

 __

Output:

    
    
    Operations on normal datetime
    5:30:00
    0:00:00
    IST
    5:30:00
    0:00:00
    IST
    
    
    Opeartions on ambiguous datetime
    5:30:00
    0:00:00
    IST
    5:30:00
    0:00:00
    IST

### datetime.timezone():

Description: It is a class that implements the tzinfo abstract base class as a
fixed offset from the UTC.

>  **Syntax:** datetime.timezone()

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from datetime import datetime, timedelta

from pytz import timezone

import pytz

 

utc = pytz.utc

print(utc.zone)

 

india = timezone('Asia/Calcutta')

print(india.zone)

 

eastern = timezone('US/Eastern')

print(eastern.zone)

 

time_format = '%Y-%m-%d %H:%M:%S %Z%z'

 

# localize() is used to localize

# datetime with no timezone information

loc_dt = india.localize(datetime(2021, 3, 16, 6, 0,
0))

loc_dt = india.localize(datetime(2021, 3, 16, 6, 0,
0))

print(loc_dt.strftime(time_format))

 

# another way of building a localized time is by converting

# an existing localized time 

# using the standard astimezone() method

eastern_dt = loc_dt.astimezone(eastern)

print(eastern_dt.strftime(time_format))

 

print(datetime(2021, 3, 16, 12, 0, 0,
tzinfo=pytz.utc).strftime(time_format))

 

# 10 minutes before

before_dt = loc_dt - timedelta(minutes=10)

print(before_dt.strftime(time_format))

print(india.normalize(before_dt).strftime(time_format))

 

# 20 mins later

after_dt = india.normalize(before_dt + timedelta(minutes=20))

print(after_dt.strftime(time_format))  
  
---  
  
 __

 __

Output:

    
    
    UTC
    Asia/Calcutta
    US/Eastern
    2021-03-16 06:00:00 IST+0530
    2021-03-15 20:30:00 EDT-0400
    2021-03-16 12:00:00 UTC+0000
    2021-03-16 05:50:00 IST+0530
    2021-03-16 05:50:00 IST+0530
    2021-03-16 06:10:00 IST+0530

### Let’s see different Functions with description under time module :-

###  Function

|

###  Description

|  time( ) |  Returns the time in floating point number in seconds |  ctime(
)|  Returns the current date and time|  sleep( )|  Stops execution of a thread
for the given duration |  localtime( ) |  Returns the date and time in
time.struct_time format |  gmtime( )|  Returns time.struct_time in UTC format|
mktime( )|  Returns the seconds passed since epochs are output|  asctime( )|
Returns a string representing the same  
---|---  
  
 **Now we will see the program and output for each of the above-mentioned
functions in the table.**

 **1: time( ) method:** The time() method returns the time as a floating-point
number expressed in seconds since the epoch, in UTC.

>  **Syntax:** time.time([ ])
>
> NOTE: It does not have any parameter

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import time

import time

 

#prints total number of seconds passed since epoch

print(time.time())  
  
---  
  
 __

 __

Output:

    
    
    1616692391.3081982

 **2: ctime( ) method**

ctime() method converts a time expressed in seconds since the epoch to a
string representing local time. The current time as returned by time() is used
If secs is not provided or None. This method is equivalent to
asctime(localtime(secs)). Locale information is not used by ctime() method.

>  **Syntax:** time.ctime([ sec ])
>
> Where sec passed as an argument is the number of seconds to be converted
> Into string representation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import time

 

number_of_seconds=1625925769.9618232

 

# function takes seconds passed since epoch as an argument and returns

# a string representing local time

print(time.ctime(number_of_seconds))  
  
---  
  
 __

 __

Output

    
    
    Sat Jul 10 14:02:49 2021

 **3: sleep( ) method**

Python time method sleep() stops execution for the given number of seconds.
The floating-point the number can be passed as an argument to get more precise
sleep time.

>  **Syntax:** time.sleep([ sec ])
>
> where sec passed as an argument is the number of seconds for which
>
> the process is to be stopped.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import time

 

# prints GEEKSFORGEEKS immediately

print("GEEKSFORGEEKS")

 

time.sleep(1.23)

 

# prints GEEKSFORGEEKS after 1.23 seconds

# as it stops execution for that time interval

print("GEEKSFORGEEKS")  
  
---  
  
 __

 __

Output

    
    
    GEEKSFORGEEKS
    GEEKSFORGEEKS

 **4: localtime( ) method**

localtime() method converts number of seconds to local time. If secs is not
provided or None, the current time as returned by time() is used. The dst flag
is set to 1 when DST applies to the given time.

>  **Syntax:** time.localtime([ sec ])
>
> Where sec passed as an argument is the number of seconds to be converted
> into struct_time representation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import time

 

# returns a time.struct_time

# object with a named tuple interface

print(time.localtime())  
  
---  
  
 __

 __

Output

> time.struct_time(tm_year=2021, tm_mon=3, tm_mday=30, tm_hour=8, tm_min=48,
> tm_sec=58, tm_wday=1, tm_yday=89, tm_isdst=0)

 **5: gmtime( ) method.**

gmtime() method converts a time expressed in seconds since the Epoch to a
struct_time in UTC in which the dst flag is always zero. If secs is not
provided or None, the current time as returned by time() is used.

>  **Syntax:** time.gmtime([ sec ])
>
> Where sec passed as an argument is the number of seconds to be converted
> into structure struct_time representation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

import time

# returns a time.struct_time object with a named tuple interface

# If secs is not provided or None,

# the current time as returned by time() is used

print(time.gmtime())  
  
---  
  
 __

 __

Output:

> time.struct_time(tm_year=2021, tm_mon=3, tm_mday=30, tm_hour=8, tm_min=49,
> tm_sec=18, tm_wday=1, tm_yday=89, tm_isdst=0)

 **6: mktime( ) method**

It is the inverse function of localtime() method. It takes an argument as
struct_time or full 9-tuple and it returns a floating-point number. If the
input value is not represented as a valid time, then either OverflowError or
ValueError is raised.

>  **Syntax:** time.mktime([t])
>
> Where t passed as an argument is a time.struct_time object or a tuple
> containing 9 elements corresponding to time.struct_time object

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

import time

 

# method mktime() is the inverse function of localtime()

# Its argument is the struct_time or full 9-tuple and 

# it returns a floating point number, for compatibility with time().

 

t = (2016, 2, 15, 10, 13, 38, 1, 48,
0)

d = time.mktime(t)

print ("time.mktime(t) : %f" % d)

print ("asctime(localtime(secs)): %s" %
time.asctime(time.localtime(d)))  
  
---  
  
 __

 __

Output

    
    
    time.mktime(t) : 1455531218.000000
    asctime(localtime(secs)): Mon Feb 15 10:13:38 2016

 **7: asctime( ) method**

Python time method asctime() converts a struct_time representing a time as
returned by gmtime() or localtime() to a 24-character string of the following
form: ‘Tue Mar 23 23:21:05 2021’.

>  **Syntax:** time.asctime([t])
>
> Where t passed as an argument is a tuple of 9 elements or struct_time
> representing a time as returned by gmtime() or localtime() function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import time

# method returns 24-character string of 

# the following form − 'Mon March 15 23:21:05 2021'

 

local_time = time.localtime()

print ("asctime : ",time.asctime(local_time))  
  
---  
  
 __

 __

Output

    
    
    asctime :  Tue Mar 16 06:02:42 2021

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

