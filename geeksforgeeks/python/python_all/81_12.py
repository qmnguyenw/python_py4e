Python | Consecutive characters frequency



Sometimes, while working with Python, we can have a problem in which we need
to compute the frequency of consecutive characters till character changes.
This can have application in many domains. Lets discuss certain ways in which
this task can be performed.

 **Method #1 : Using list comprehension + groupby()**  
This is one of the shorthand with the help of which this task can be
performed. In this, we employ groupby() to group consecutives together to
perform frequency calculations.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive characters frequency

# Using list comprehension + groupby()

from itertools import groupby

 

# initializing string

test_str = "geekksforgggeeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Consecutive characters frequency

# Using list comprehension + groupby()

res = [len(list(j)) for _, j in groupby(test_str)]

 

# printing result 

print("The Consecutive characters frequency : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geekksforgggeeks
    The Consecutive characters frequency : [1, 2, 2, 1, 1, 1, 1, 3, 2, 1, 1]
    

**Method #2 : Using regex**  
Another way to solve this problem is using regex. In this we employ regex
character finding technique and find count using len().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive characters frequency

# Using regex

import re

 

# initializing string

test_str = "geekksforgggeeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Consecutive characters frequency

# Using regex

res = [len(sub.group()) for sub in re.finditer(r'(.)\1*',
test_str)]

 

# printing result 

print("The Consecutive characters frequency : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geekksforgggeeks
    The Consecutive characters frequency : [1, 2, 2, 1, 1, 1, 1, 3, 2, 1, 1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

