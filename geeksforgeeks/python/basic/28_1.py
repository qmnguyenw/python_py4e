Time Functions in Python | Set 1 (time(), ctime(), sleep()…)



Python has defined a module, “time” which allows us to handle various
operations regarding time, its conversions and representations, which find its
use in various applications in life. The beginning of time is started
measuring from **1 January, 12:00 am, 1970** and this very time is termed as “
**epoch** ” in Python.

 **Operations on Time :**

 **1\. time()** :- This function is used to count the number of **seconds
elapsed since the epoch**.

**2\. gmtime(sec)** :- This function returns a **structure with 9 values**
each representing a time attribute in sequence. It converts **seconds into
time attributes(days, years, months etc.)** till specified seconds from epoch.
If no seconds are mentioned, time is calculated till present. The structure
attribute table is given below.

  

  

    
    
    Index   Attributes   Values
     0        tm_year     2008
     1        tm_mon      1 to 12
     2        tm_mday     1 to 31
     3        tm_hour     0 to 23
     4        tm_min      0 to 59
     5        tm_sec      0 to 61 (60 or 61 are leap-seconds)
     6        tm_wday     0 to 6 
     7        tm_yday     1 to 366
     8        tm_isdst    -1, 0, 1 where -1 means 
                                   Library determines DST
    

__

__  
__

__

__  
__  
__

# Python code to demonstrate the working of

# time() and gmtime()

 

# importing "time" module for time operations

import time

 

# using time() to display time since epoch

print ("Seconds elapsed since the epoch are : ",end="")

print (time.time())

 

 

# using gmtime() to return the time attribute structure

print ("Time calculated acc. to given seconds is : ")

print (time.gmtime())  
  
---  
  
 __

 __

Output:

    
    
    Seconds elapsed since the epoch are : 1470121951.9536893
    Time calculated acc. to given seconds is : 
    time.struct_time(tm_year=2016, tm_mon=8, tm_mday=2,
    tm_hour=7, tm_min=12, tm_sec=31, tm_wday=1, 
    tm_yday=215, tm_isdst=0)
    

**3\. asctime(“time”)** :- This function takes a time attributed string
produced by gmtime() and returns a **24 character string denoting time**.

**4\. ctime(sec)** :- This function returns a **24 character time string** but
takes seconds as argument and **computes time till mentioned seconds**. If no
argument is passed, time is calculated till present.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# asctime() and ctime()

 

# importing "time" module for time operations

import time

 

# initializing time using gmtime()

ti = time.gmtime()

 

# using asctime() to display time acc. to time mentioned

print ("Time calculated using asctime() is : ",end="")

print (time.asctime(ti))

 

 

# using ctime() to diplay time string using seconds 

print ("Time calculated using ctime() is : ", end="")

print (time.ctime())  
  
---  
  
 __

 __

Output:

    
    
    Time calculated using asctime() is : Tue Aug  2 07:47:02 2016
    Time calculated using ctime() is : Tue Aug  2 07:47:02 2016
    

**5\. sleep(sec)** :- This method is used to **hault the program execution**
for the time specified in the arguments.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# sleep()

 

# importing "time" module for time operations

import time

 

# using ctime() to show present time

print ("Start Execution : ",end="")

print (time.ctime())

 

# using sleep() to hault execution

time.sleep(4)

 

# using ctime() to show present time

print ("Stop Execution : ",end="")

print (time.ctime())  
  
---  
  
 __

 __

Output:

    
    
    Start Execution : Tue Aug  2 07:59:03 2016
    Stop Execution : Tue Aug  2 07:59:07 2016
    

This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

