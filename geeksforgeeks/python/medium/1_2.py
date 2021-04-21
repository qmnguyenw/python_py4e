Python – time.ctime() Method



Python **time.ctime()** method converts a time in seconds since the epoch to a
string in local time. This is equivalent to asctime(localtime(seconds)).
Current time is returned by localtime() is used when the time tuple is not
present.

>  **Syntax:** time.ctime([ sec ])
>
>  **Parameter:**
>
>   *  **sec:** number of seconds to be converted into string representation.
>

 **Example 1:**

Let’s move to the code with an explanation :

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# imort module

import time

 

# here no parameter is passed

print(time.ctime())  
  
---  
  
 __

 __

 **Output:**

    
    
    Thu Mar 18 11:00:19 2021

It prints the standard time equivalent to asctime() method.

**Example 2:**

Let’s Have a look at **asctime()** method:

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

 

# gives local time

a = time.localtime() 

c = time.asctime(a)

print(c)  
  
---  
  
 __

 __

 **Output:**

    
    
    Thu Mar 18 11:01:02 2021

 **Example 3:**

  

  

Let’s move to another example where we will pass seconds as a parameter to
ctime() method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import time module

import time

 

# passing number of seconds as

# parameter to ctime() method

print(time.ctime(1615799665.584516))  
  
---  
  
 __

 __

 **Output:**

    
    
    Mon Mar 15 14:44:25 2021

 **Example 4:**

Here is another example where we pass a parameter to ctime() method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import time module

import time

 

# passing number of seconds as

# parameter to ctime() method

print(time.ctime(1000))  
  
---  
  
 __

 __

 **Output:**

    
    
    Thu Jan  1 05:46:40 1970

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

