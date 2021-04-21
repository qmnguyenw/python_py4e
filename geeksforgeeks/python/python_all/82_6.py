Python | First alphabet index



Sometimes, while working with Python strings we can have a problem in which we
need to extract the first index of alpha character from string. This can have
application in day-day programming. Lets discuss certain ways in which this
task can be performed.

 **Method #1 : Using loop + regex**  
The combination of above functionalities can be used to perform this task. In
this, we employ loop to loop through the string and regex is used to filter
out for alphabets in characters.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# First alphabet index

# Using loop + regex

import re

 

# initializing string

test_str = "34#$g67fg"

 

# printing original string

print("The original string is : " + test_str)

 

# First alphabet index

# Using loop + regex

res = None

temp = re.search(r'[a-z]', test_str, re.I)

if temp is not None:

 res = temp.start()

 

# printing result 

print("Index of first character : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : 34#$g67fg
    Index of first character : 4
    

**Method #2 : Usingfind() + next() + filter() + isalpha()**  
The combination of above methods can also be used to perform this task. In
this, we check for alphabets using isalpha(). The task of finding element is
done by find(). The next() returns the 1st occurrence.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# First alphabet index

# Using find() + next() + filter() + isalpha()

import re

 

# initializing string

test_str = "34#$g67fg"

 

# printing original string

print("The original string is : " + test_str)

 

# First alphabet index

# Using find() + next() + filter() + isalpha()

res = test_str.find(next(filter(str.isalpha, test_str)))

 

# printing result 

print("Index of first character : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : 34#$g67fg
    Index of first character : 4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

