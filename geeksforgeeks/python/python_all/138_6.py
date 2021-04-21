Python | Splitting operators in String



Sometimes we have a source string to have certain mathematical statement for
computations and we need to split both the numbers and operators as a list of
individual elements. Let’s discuss certain ways in which this problem can be
performed.

 **Method #1 : Usingre.split()**  
This task can be solved using the split functionality provided by Python regex
library which has power to split the string according to certain conditions
and in this case all numbers and operators.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Splitting operators in String

# Using re.split()

import re

 

# initializing string 

test_str = "15 + 22 * 3-4 / 2"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using re.split()

# Splitting operators in String

res = re.split(r'(\D)', test_str)

 

# printing result 

print("The list after performing split functionality : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

> The original string is : 15+22*3-4/2  
> The list after performing split functionality : [’15’, ‘+’, ’22’, ‘*’, ‘3’,
> ‘-‘, ‘4’, ‘/’, ‘2’]

  

  

**Method #2 : Usingre.findall()**  
This Python regex library function also can perform the similar task as the
above function. It can also support decimal numbers as additional
functionality.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Splitting operators in String

# Using re.findall()

import re

 

# initializing string 

test_str = "15 + 22.6 * 3-4 / 2"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using re.findall()

# Splitting operators in String

res = re.findall(r'[0-9\.]+|[^0-9\.]+', test_str)

 

# printing result 

print("The list after performing split functionality : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

> The original string is : 15+22.6*3-4/2  
> The list after performing split functionality : [’15’, ‘+’, ‘22.6’, ‘*’,
> ‘3’, ‘-‘, ‘4’, ‘/’, ‘2’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

