Python | Segregate Positive and Negative Integers from mixed string



Sometimes, while working with Python strings of data, we can have a problem in
which we need to separate positive and negative integers in a string. This can
occur in many domains that include data handling. Lets discuss certain way in
which we can solve this problem.

 **Method : Using regex**  
This problem can be solved using appropriate regex. In this, we match the
matching regex with string and separate the positive integers and negative
integers from the string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Segregate Positive and Negative Integers

# Using regex

import re

 

# initializing string

test_str = "gfg + 4-1is + 5best-8"

 

# printing original string

print("The original string is : " + test_str)

 

# Segregate Positive and Negative Integers

# Using regex

res = re.findall('[-+]?\d+', test_str)

 

# printing result 

print("The split string is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg+4-1is+5best-8
    The split string is : ['+4', '-1', '+5', '-8']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

