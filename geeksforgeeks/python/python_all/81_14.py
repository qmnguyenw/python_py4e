Python | Extract substrings between brackets



Sometimes, while working with Python strings, we can have a problem in which
we need to extract the substrings between certain characters and can be
brackets. This can have application in cases we have tuples embedded in
string. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using regex**  
One way to solve this problem is by using regex. In this we employ suitable
regex and perform the task of extraction of required elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract substrings between brackets

# Using regex

import re

 

# initializing string

test_str = "geeks(for)geeks is (best)"

 

# printing original string

print("The original string is : " + test_str)

 

# Extract substrings between brackets

# Using regex

res = re.findall(r'\(.*?\)', test_str)

 

# printing result 

print("The element between brackets : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeks(for)geeks is (best)
    The element between brackets : ['(for)', '(best)']
    

**Method #2 : Using list comprehension +isintance() + eval()**  
The combination of above methods can also be used to solve this problem. In
this eval() assume the brackets to be tuples and helps the extraction of
strings within them.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract substrings between brackets

# Using list comprehension + eval() + isinstance()

 

# initializing string

test_str = "[(234, ), 4, (432, )]"

 

# printing original string

print("The original string is : " + test_str)

 

# Extract substrings between brackets

# Using list comprehension + eval() + isinstance()

res = [str(idx) for idx in eval(test_str) if
isinstance(idx, tuple)]

 

# printing result 

print("The element between brackets : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : [(234, ), 4, (432, )]
    The element between brackets : ['(234, )', '(432, )']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

