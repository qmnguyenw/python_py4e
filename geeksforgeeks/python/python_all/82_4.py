Python | Extract Numbers in Brackets in String



Sometimes, while working with Python strings, we can have a problem in which
we have to perform the task of extracting numbers in string that are enclosed
in brackets. Lets discuss certain way in which this task can be performed.

 **Method : Using regex**  
The way to solve this task is to construct a regex string that can return in
all the numbers in a string that have brackets around them.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Numbers in Brackets in String

# Using regex

import re

 

# initializing string

test_str = "gfg is [1] [4] all geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Extract Numbers in Brackets in String

# Using regex

res = re.findall(r"\[\s*\+?(-?\d+)\s*\]", test_str)

 

# printing result 

print("Extracted number list : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg is [1] [4] all geeks
    Extracted number list : ['1', '4']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

