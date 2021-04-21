Python program to Extract string till first Non-Alphanumeric character



Given a string, extract all the alphanumerics before 1st occurrence of non-
alphanumeric.

>  **Input** : test_str = ‘geek$s4g!!!eeks’  
> **Output** : geek  
> **Explanation** : Stopped at $ occurrence.
>
>  **Input** : test_str = ‘ge)eks4g!!!eeks’  
> **Output** : ge  
> **Explanation** : Stopped at ) occurrence.

 **Method #1 : Using regex + search()**

In this, search() is used to search appropriate regex() for alphanumerics,
then the result is sliced till 1st occurrence of a non-alphanumeric character

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract string till first Non-Alphanumeric character

# Using regex + search()

import re

 

# initializing string

test_str = 'geeks4g!!!eeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# using start() to get 1st substring

res = re.search(r'\W+', test_str).start()

res = test_str[0 : res]

 

# printing result 

print("The resultant string : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : geeks4g!!!eeks
    The resultant string : geeks4g
    

**Method #2 : Using findall()**

This is yet another regex way to solve this problem. In this, we extract the
1st substring before non-alnum character by accessing the 0th index.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract string till first Non-Alphanumeric character

# Using findall()

import re

 

# initializing string

test_str = 'geeks4g!!!eeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# using findall() to get all substrings 

# 0th index gives 1st substring

res = re.findall("[\dA-Za-z]*", test_str)[0]

 

# printing result 

print("The resultant string : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : geeks4g!!!eeks
    The resultant string : geeks4g
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

