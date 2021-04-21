Python | Test if number is valid Excel column



Sometimes, while working with Python strings, we can have a problem in which
we need to test for string if its a valid excel column. This has application
in many domains including day-day programming, web development and Data
Science. Lets discuss certain way in which this task can be performed.

 **Method : Usingre.match() + group()**  
The combination of above functions can be used to perform this task. In this,
we perform regex match() to match with the potential updated excel version
which have A-XDF, and starts with 0-9 followed by 0-6 characters not exceeding
1048576. The groupby() is used to group the elements on that basis.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if number is valid Excel column

# Using re.match() + groupby()

import re

 

# initializing string

test_str = "C101"

 

# printing original string

print("The original string is : " + test_str)

 

# Test if number is valid Excel column

# Using re.match() + groupby()

temp = re.match(r'^([A-Z]{1,
2}|[A-W][A-Z]{2}|X[A-E][A-Z]|XF[A-D])([1-9]\d{0, 6})$', test_str)

res = bool(temp) and int(temp.group(2)) < 1048577

 

# printing result 

print("Is string valid excel column : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : C101
    Is string valid excel column : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

