Python | Exceptional Split in String



Sometimes, while working with Strings, we may need to perform the split
operation. The straight forward split is easy. But sometimes, we may have a
problem in which we need to perform split on certain character but have
exceptions. This discusses split on comma, with exception that comma should
not be enclosed by brackets. Lets discuss certain ways in which this task can
be performed.

 **Method #1 : Using loop + strip()**  
This is brute force way in which we perform this task. In this we construct
the each element of list as words in String accounting for brackets and comma
to perform split.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Exceptional Split in String

# Using loop + split()

 

# initializing string

test_str = "gfg, is, (best, for), geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Exceptional Split in String

# Using loop + split()

temp = ''

res = []

check = 0

for ele in test_str:

 if ele == '(':

 check += 1

 elif ele == ')':

 check -= 1

 if ele == ', ' and check == 0:

 if temp.strip():

 res.append(temp)

 temp = ''

 else:

 temp += ele

if temp.strip():

 res.append(temp)

 

# printing result 

print("The string after exceptional split : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg, is, (best, for), geeks
    The string after exceptional split : ['gfg', ' is', ' (best, for)', ' geeks']
    

**Method #2 : Usingregex()**  
This is yet another way in which this task can be performed. In this, we use a
regex instead of manual brute force logic for brackets comma and omit that
from getting split.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Exceptional Split in String

# Using regex()

import re

 

# initializing string

test_str = "gfg, is, (best, for), geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Exceptional Split in String

# Using regex()

res = re.split(r', (?!\S\)|\()', test_str)

 

# printing result 

print("The string after exceptional split : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg, is, (best, for), geeks
    The string after exceptional split : ['gfg', ' is', ' (best, for)', ' geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

