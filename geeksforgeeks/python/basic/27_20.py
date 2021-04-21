Time Functions in Python | Set-2 (Date Manipulations)



Some of Time Functions are discussed in Set 1

Date manipulation can also be performed using Python using “datetime” module
and using “date” class in it.

 **Operations on Date :**

 **1\. MINYEAR** :- It displays the **minimum year** that can be represented
using date class.

 **2\. MAXYEAR** :- It displays the **maximum year** that can be represented
using date class.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# MINYEAR and MAXYEAR

 

# importing built in module datetime

import datetime

from datetime import date

 

# using MINYEAR to print minimum representable year

print ("Minimum representable year is : ",end="")

print (datetime.MINYEAR)

 

# using MAXYEAR to print maximum representable year

print ("Maximum representable year is : ",end="")

print (datetime.MAXYEAR)  
  
---  
  
 __

 __

Output:

    
    
    Minimum representable year is : 1
    Maximum representable year is : 9999
    

**3\. date(yyyy-mm-dd)** :- This function returns a string with passed
arguments in order of year, months and date.

 **4\. today()** :- Returns the **date of present day** in the format yyyy-mm-
dd.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# date() and today()

 

# importing built in module datetime

import datetime

from datetime import date

 

# using date() to represent date

print ("The represented date is : ",end="")

print (datetime.date(1997,4,1))

 

# using today() to print present date

print ("Present date is : ",end="")

print (date.today())  
  
---  
  
 __

 __

Output:

    
    
    The represented date is : 1997-04-01
    Present date is : 2016-08-02
    

**5\. fromtimestamp(sec)** :- It returns the **date calculated from the
seconds** elapsed since epoch mentioned in arguments.

 **6\. min()** :- This returns the **minimum date** that can be represented by
date class.

 **7\. max()** :- This returns the **maximum date** that can be represented by
date class.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# fromtimestamp(), min() and max()

 

# importing built in module datetime

import datetime

from datetime import date

 

# using fromtimestamp() to calculate date

print ("The calculated date from seconds is : ",end="")

print (date.fromtimestamp(3452435))

 

# using min() to print minimum representable date

print ("Minimum representable date is : ",end="")

print (date.min)

 

# using max() to print minimum representable date

print ("Maximum representable date is : ",end="")

print (date.max)  
  
---  
  
 __

 __

Output:

    
    
    The calculated date from seconds is : 1970-02-09
    Minimum representable date is : 0001-01-01
    Maximum representable date is : 9999-12-31
    

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

