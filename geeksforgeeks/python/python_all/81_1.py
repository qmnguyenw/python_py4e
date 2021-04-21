Python – Evaluate Expression given in String



Sometimes, while working with Python Strings, we can have certain computations
in string format and we need to formulate its result. This can occur in
domains related to Mathematics and data. Lets discuss certain ways in which we
can perform this task.  
 **Method #1 : Using regex + map() + sum()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of computation using sum() and mapping of operator and
operation using map(). This method can be used if the string has only + or -.
Method #2 can be used for other operations as well.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Expression evalution in String

# Using regex + map() + sum()

import re

# initializing string

test_str = "45 + 98-10"

# printing original string

print("The original string is : " + test_str)

# Expression evalution in String

# Using regex + map() + sum()

res = sum(map(int, re.findall(r'[+-]?\d+', test_str)))

# printing result

print("The evaluated result is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : 45+98-10
    The evaluated result is : 133
    
    

  
**Method #2 : Using eval()**  
This is one of the way in which this task can be performed. In this, we
perform computation internally using eval().  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Expression evalution in String

# Using eval()

# initializing string

test_str = "45 + 98-10"

# printing original string

print("The original string is : " + test_str)

# Expression evalution in String

# Using eval()

res = eval(test_str)

# printing result

print("The evaluated result is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : 45+98-10
    The evaluated result is : 133
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

