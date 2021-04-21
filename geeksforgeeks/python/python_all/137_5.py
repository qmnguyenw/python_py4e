Python | Get numeric prefix of given string



Sometimes, while working with strings, we might be in a situation in which we
require to get the numeric prefix of a string. This kind of application can
come in various domains such as web application development. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Usingre.findall()**  
The regex can be used to perform this particular task. In this, we use findall
function which we use to get all the occurrences of numbers and then return
the initial occurrence.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get numeric prefix of string 

# Using re.findall()

import re

 

# initializing string 

test_str = "1234Geeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# Using re.findall()

# Get numeric prefix of string 

res = re.findall('\d+', test_str)

 

# printing result 

print("The prefix number at string : " + str(res[0]))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : 1234Geeks
    The prefix number at string : 1234
    

**Method #2 : Usingitertools.takewhile()**  
The inbuilt function of takewhile can be used to perform this particular task
of extracting all the numbers till a character occurs.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get numeric prefix of string 

# Using itertools.takewhile()

from itertools import takewhile

 

# initializing string 

test_str = "1234Geeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# Using itertools.takewhile()

# Get numeric prefix of string 

res = ''.join(takewhile(str.isdigit, test_str))

 

# printing result 

print("The prefix number at string : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : 1234Geeks
    The prefix number at string : 1234
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

