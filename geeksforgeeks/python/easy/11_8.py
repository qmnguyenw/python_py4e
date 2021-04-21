Python datetime module with examples



In Python, date and time are not a data type of its own, but a module named
**datetime** can be imported to work with the date as well as time.
**Datetime module** comes built into Python, so there is no need to install it
externally.

Datetime module supplies classes to work with date and time. These classes
provide a number of functions to deal with dates, times and time intervals.
Date and datetime are an object in Python, so when you manipulate them, you
are actually manipulating objects and not string or timestamps.

The datetime classes are categorize into 6 main classes –

  *  **date** – An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. Its attributes are year, month and day.
  *  **time** – An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds. Its attributes are hour, minute, second, microsecond, and tzinfo.
  *  **datetime** – Its a combination of date and time along with the attributes year, month, day, hour, minute, second, microsecond, and tzinfo.
  *  **timedelta** – A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.
  *  **tzinfo** – It provides time zone information objects.
  *  **timezone** – A class that implements the tzinfo abstract base class as a fixed offset from the UTC (New in version 3.2).

## Date class

When an object of this class is instantiated, it represents a date in the
format YYYY-MM-DD. Constructor of this class needs three mandatory arguments
year, month and date.

 **Constructor syntax:**

  

  

    
    
    class datetime.date(year, month, day)
    

The arguments must be in the following range –

  * MINYEAR <= year <= MAXYEAR
  * 1 <= month <= 12
  * 1 <= day <= number of days in the given month and year

 **Note** – If the argument is not an integer it will raise a TypeError and
if it is outside the range a ValueError will be raised.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# demonstrate date class

 

# import the date class

from datetime import date

 

# initializing constructor

# and passing arguments in the 

# format year, month, date

my_date = date(1996, 12, 11)

 

print("Date passed as argument is", my_date)

 

# Uncommenting my_date = date(1996, 12, 39)

# will raise an ValueError as it is

# outside range

 

# uncommenting my_date = date('1996', 12, 11)

# will raise a TypeError as a string is 

# passed instead of interger  
  
---  
  
 __

 __

 **Output:**

    
    
    Date passed as argument is 1996-12-11
    
    
    
    Traceback (most recent call last):
      File "/home/ccabfb570d9bd1dcd11dc4fe55fd6ba2.py", line 14, in 
        my_date = date(1996, 12, 39)
    ValueError: day is out of range for month
    
    Traceback (most recent call last):
      File "/home/53b974e10651f1853eee3c004b48c481.py", line 18, in 
        my_date = date('1996', 12, 11)
    TypeError: an integer is required (got type str)
    

#### Current date

To return the current local date today() function of date class is used.
today() function comes with several attributes (year, month and day). These
can be printed individually.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# print current date

 

from datetime import date

 

# calling the today

# function of date class

today = date.today()

 

print("Today's date is", today)

 

# Printing date's components

print("Date components", today.year, today.month, today.day)  
  
---  
  
 __

 __

 **Output:**

    
    
    Today's date is 2019-10-25
    Date components 2019 10 25
    

Different functions available in date class are –Function name| Description|
fromtimestamp(timestamp)| Return the local date corresponding to the POSIX
timestamp| fromordinal(ordinal)| Return the date corresponding to the
proleptic Gregorian ordinal, where January 1 of year 1 has ordinal 1.|
fromisoformat(date_string)| Return a date corresponding to a date_string given
in the format YYYY-MM-DD:| fromisocalendar(year, week, day)| Return a date
corresponding to the ISO calendar date specified by year, week and day.  
---|---  
  
## Time class

Time object represents local time, independent of any day.  
 **Constructor Syntax:**

    
    
    class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

All the arguments are optional. tzinfo can be None otherwise all the
attributes must be integer in the following range –

  

  

  * 0 <= hour < 24
  * 0 <= minute < 60
  * 0 <= second < 60
  * 0 <= microsecond < 1000000
  * fold in [0, 1]

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# demonstrate time class

 

from datetime import time

 

# calling the constructor

my_time = time(13, 24, 56)

 

print("Entered time", my_time)

 

# calling constructor with 1 

# argument

my_time = time(minute = 12)

print("\nTime with one argument", my_time)

 

# Calling constructor with 

# 0 argument

my_time = time()

print("\nTime without argument", my_time)

 

# Uncommenting time(hour = 26)

# will rase an ValueError as 

# it is out of range

 

# uncommenting time(hour ='23')

# will raise TypeError as

# string is passed instead of int  
  
---  
  
 __

 __

 **Output:**

    
    
    Entered time 13:24:56
    
    Time with one argument 00:12:00
    
    Time without argument 00:00:00
    
    
    
    Traceback (most recent call last):
      File "/home/95ff83138a1b3e67731e57ec6dddef25.py", line 21, in 
        print(time(hour=26))
    ValueError: hour must be in 0..23
    
    Traceback (most recent call last):
      File "/home/fcee9ba5615b0b74fc3ba39ec9a789fd.py", line 21, in 
        print(time(hour='23'))
    TypeError: an integer is required (got type str)
    

After creating a time object, its attributes can also be printed separately.

 __

 __  
 __

 __

 __  
 __  
 __

from datetime import time

 

Time = time(11, 34, 56)

 

print("hour =", Time.hour)

print("minute =", Time.minute)

print("second =", Time.second)

print("microsecond =", Time.microsecond)  
  
---  
  
 __

 __

 **Output:**

    
    
    hour = 11
    minute = 34
    second = 56
    microsecond = 0
    

## Datetime class

Information on both date and time is contained in this class. Like a date
object, datetime assumes the current Gregorian calendar extended in both
directions; like a time object, datetime assumes there are exactly 3600*24
seconds in every day.

 **Constructor Syntax:**

> class datetime.datetime(year, month, day, hour=0, minute=0, second=0,
> microsecond=0, tzinfo=None, *, fold=0)

The year, month and day arguments are mandatory. tzinfo can be None, rest
all the attributes must be an integer in the following range –

  * MINYEAR <= year <= MAXYEAR
  * 1 <= month <= 12
  * 1 <= day <= number of days in the given month and year
  * 0 <= hour < 24
  * 0 <= minute < 60
  * 0 <= second < 60
  * 0 <= microsecond < 1000000
  * fold in [0, 1]

 **Note** – Passing an argument other than integer will raise a TypeError
and passign arguments outside the range will raise ValueError.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# demonstrate datetime object

 

from datetime import datetime

 

# Initializing constructor

a = datetime(1999, 12, 12)

print(a)

 

# Initializing constructor 

# with time parameters as well

a = datetime(1999, 12, 12, 12, 12, 12,
342380)

print(a)  
  
---  
  
 __

 __

 **Output:**

    
    
    1999-12-12 00:00:00
    1999-12-12 12:12:12.342380
    

After creating a datetime object, its attributes can also be printed
separately.

 __

 __  
 __

 __

 __  
 __  
 __

from datetime import datetime

 

a = datetime(1999, 12, 12, 12, 12, 12)

 

print("year =", a.year)

print("month =", a.month)

print("hour =", a.hour)

print("minute =", a.minute)

print("timestamp =", a.timestamp())  
  
---  
  
 __

 __

 **Output:**

    
    
    year = 1999
    month = 12
    hour = 12
    minute = 12
    timestamp = 945000732.0
    

#### Current date and time

You can print the current date and time using the now() function. now()
function returns the current local date and time.

 __

 __  
 __

 __

 __  
 __  
 __

from datetime import datetime

 

# Calling now() function

today = datetime.now()

 

print("Current date and time is", today)  
  
---  
  
 __

 __

 **Output:**

    
    
    Current date and time is 2019-10-25 11:12:11.289834
    

Other fucntions of datetime class are –Fucntion name| Description| utcnow()|
Return the current UTC date and time, with tzinfo None.|
fromtimestamp(timestamp, tz=None)| Return the local date and time
corresponding to the POSIX timestamp.| utcfromtimestamp(timestamp)| Return the
UTC datetime corresponding to the POSIX timestamp, with tzinfo None.|
fromordinal(ordinal)| Return the datetime corresponding to the proleptic
Gregorian ordinal, where January 1 of year 1 has ordinal 1.| combine(date,
time, tzinfo=self.tzinfo)| Return a new datetime object whose date components
are equal to the given date object’s, and whose time components are equal to
the given time object’s.| fromisoformat(date_string)| Return a datetime
corresponding to a date_string in one of the formats emitted by
date.isoformat() and datetime.isoformat().| strptime(date_string, format)|
Return a datetime corresponding to date_string, parsed according to format.  
---|---  
  
## Timedelta class

Python timedelta() function is present under datetime library which is
generally used for calculating differences in dates and also can be used for
date manipulations in Python. It is one of the easiest ways to perform date
manipulations.

 **Constructor syntax:**

> class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0,
> minutes=0, hours=0, weeks=0)
>
> Returns : Date

 __

 __  
 __

 __

 __  
 __  
 __

# Timedelta function demonstration

 

from datetime import datetime, timedelta 

 

 

# Using current time 

ini_time_for_now = datetime.now() 

 

# printing initial_date 

print ("initial_date", str(ini_time_for_now)) 

 

# Calculating future dates 

# for two years 

future_date_after_2yrs = ini_time_for_now + timedelta(days =
730) 

 

future_date_after_2days = ini_time_for_now + timedelta(days =
2) 

 

# printing calculated future_dates 

print('future_date_after_2yrs:', str(future_date_after_2yrs)) 

print('future_date_after_2days:', str(future_date_after_2days))   
  
---  
  
__

__

**Output:**

    
    
    initial_date 2019-10-25 12:01:01.227848
    future_date_after_2yrs: 2021-10-24 12:01:01.227848
    future_date_after_2days: 2019-10-27 12:01:01.227848
    

Time difference can also be found using this class.

 __

 __  
 __

 __

 __  
 __  
 __

# Timedelta function demonstration

from datetime import datetime, timedelta 

 

# Using current time 

ini_time_for_now = datetime.now() 

 

# printing initial_date 

print ("initial_date", str(ini_time_for_now)) 

 

# Some another datetime 

new_final_time = ini_time_for_now + \ 

 timedelta(days = 2) 

 

# printing new final_date 

print ("new_final_time", str(new_final_time)) 

 

 

# printing calculated past_dates 

print('Time difference:', str(new_final_time - \ 

 ini_time_for_now))   
  
---  
  
__

__

**Output:**

    
    
    initial_date 2019-10-25 12:02:32.799814
    new_final_time 2019-10-27 12:02:32.799814
    Time difference: 2 days, 0:00:00
    

## Tzinfo class

This is an abstract base class, meaning that this class should not be
instantiated directly. An instance of (a concrete subclass of) tzinfo can be
passed to the constructors for datetime and time objects. The latter objects
view their attributes as being in local time, and the tzinfo object supports
methods revealing offset of local time from UTC, the name of the time zone,
and DST offset, all relative to a date or time object passed to them. To know
more about this class click here.

## Timezone class

The timezone class is a subclass of tzinfo, each instance of which represents
a timezone defined by a fixed offset from UTC.

 **Constructor syntax:**

    
    
    class datetime.timezone(offset, name=None)
    

The offset argument must be specified as a timedelta object representing the
difference between the local time and UTC.

 **Note** – ValueError will be raised if the offset is not in between
-timedelta(hours=24) and timedelta(hours=24).

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

