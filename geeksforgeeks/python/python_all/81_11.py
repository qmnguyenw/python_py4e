Python | Split by repeating substring



Sometimes, while working with Python strings, we can have a problem in which
we need to perform splitting. This can be of custom nature. In this, we can
have a split in which we need to split by all the repetitions. This can have
application in many domains. Lets discuss certain ways in which this task can
be performed.

 **Method #1 : Using * operator + len()**  
This is one of the way in this we can perform this task. In this, we compute
the length of repeated string and then divide the list to obtain root and
construct new list using * operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split by repeating substring

# Using * operator + len()

 

# initializing string

test_str = "gfggfggfggfggfggfggfggfg"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing target

K = 'gfg'

 

# Split by repeating substring

# Using * operator + len()

temp = len(test_str) // len(str(K))

res = [K] * temp

 

# printing result 

print("The split string is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfggfggfggfggfggfggfggfg
    The split string is : ['gfg', 'gfg', 'gfg', 'gfg', 'gfg', 'gfg', 'gfg', 'gfg']
    

**Method #2 : Usingre.findall()**  
This is yet another way in which this problem can be solved. In this, we use
findall() to get all the substrings and split is also performed internally.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split by repeating substring

# Using re.findall()

import re

 

# initializing string

test_str = "gfggfggfggfggfggfggfggfg"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing target

K = 'gfg'

 

# Split by repeating substring

# Using re.findall()

res = re.findall(K, test_str)

 

# printing result 

print("The split string is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfggfggfggfggfggfggfggfg
    The split string is : ['gfg', 'gfg', 'gfg', 'gfg', 'gfg', 'gfg', 'gfg', 'gfg']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

