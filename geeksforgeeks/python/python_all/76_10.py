Python – Maximum Consecutive Substring Occurrence



Sometimes, while working with python, we can have a problem in which we need
to check for substrings occurring in consecutive repetition. This can have
application in data domains. Lets discuss a way in which this task can be
performed.

 **Method : Usingmax() + re.findall()**  
The combination of above methods can be used to perform this task. In this, we
extract the substrings repetitions using using findall() and extract the
maximum of them using max().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum Consecutive Substring Occurrence

# Using max() + re.findall()

import re

 

# initializing string

test_str = 'geeksgeeks are geeks for all geeksgeeksgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing subs 

sub_str = 'geeks'

 

# Maximum Consecutive Substring Occurrence

# Using max() + re.findall()

res = max(re.findall('((?:' + re.escape(sub_str) + ')*)',
test_str), key = len)

 

# printing result 

print("The maximum run of Substring : " + res)   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksgeeks are geeks for all geeksgeeksgeeks
    The maximum run of Substring : geeksgeeksgeeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

