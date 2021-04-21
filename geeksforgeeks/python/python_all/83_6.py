Python | Frequency of numbers in String



Sometimes, while working with Strings, we can have a problem in which we need
to check how many of numerics are present in strings. This is a common problem
and have application across many domains like day-day programming and data
science. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Usingre.findall() + len()**  
The combination of above functions can be used to perform this task. In this,
we check for all numbers and put in list using findall() and the count is
extracted using len().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Frequency of numbers in String

# Using re.findall() + len()

import re

 

# initializing string

test_str = "geeks4feeks is No. 1 4 geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Frequency of numbers in String

# Using re.findall() + len()

res = len(re.findall(r'\d+', test_str))

 

# printing result 

print("Count of numerics in string : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeks4feeks is No. 1 4 geeks
    Count of numerics in string : 3
    

**Method #2 : Usingsum() + findall()**  
The combination of above functions can also be used to solve this problem. In
this, we cumulate the sum using sum(). The task of findall() is to find all
the numerics.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Frequency of numbers in String

# Using re.findall() + sum()

import re

 

# initializing string

test_str = "geeks4feeks is No. 1 4 geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Frequency of numbers in String

# Using re.findall() + sum()

res = sum(1 for _ in re.finditer(r'\d+', test_str)) 

 

# printing result 

print("Count of numerics in string : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeks4feeks is No. 1 4 geeks
    Count of numerics in string : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

