Python Program to Split joined consecutive similar characters



Given a String, our task is to write a Python program to split on the
occurrence of a non-similar character.

> **Input :** test_str = ‘ggggffggisssbbbeessssstt’
>
>  **Output :** [‘gggg’, ‘ff’, ‘gg’, ‘i’, ‘sss’, ‘bbb’, ‘ee’, ‘sssss’, ‘tt’]
>
>  **Explanation :** All similar consecutive characters are converted to
> separate strings.
>
>  **Input :** test_str = ‘ggggffgg’
>
>  
>
>
>  
>
>
>  **Output :** [‘gggg’, ‘ff’, ‘gg’]
>
>  **Explanation :** All similar consecutive characters are converted to
> separate strings.

 **Method #1 : Using** **join()** **+** **list comprehension** **+**
**groupby()**

In this, the characters are grouped on similarity using groupby(), join() is
used to reform strings list. List comprehension performs task of iterating
constructed groups.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split joined consecutive similar characters

# Using join() + list comprehension + groupby()

from itertools import groupby

 

# initializing string

test_str = 'ggggffggisssbbbeessssstt'

 

# printing original string

print("The original string is : " + str(test_str))

 

# groupby groups the elements, join joining Consecutive groups

res = ["".join(grup) for ele, grup in groupby(test_str)]

 

# printing result

print("Consecutive split string is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : ggggffggisssbbbeessssstt
>
> Consecutive split string is : [‘gggg’, ‘ff’, ‘gg’, ‘i’, ‘sss’, ‘bbb’, ‘ee’,
> ‘sssss’, ‘tt’]

 **Method #2 : Using finditer() +** **regex** **\+ list comprehension**

In this, regex is used to check for consecutive equal sequences. The
finditer() performs the task of finding the matching regex in a string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split joined consecutive similar characters

# Using finditer() + regex + list comprehension

import re

 

# initializing string

test_str = 'ggggffggisssbbbeessssstt'

 

# printing original string

print("The original string is : " + str(test_str))

 

# list comprehension iterates for all the formed groups found by regex

# if consecutive numbers need to search "d" can be used.

res = [iters.group(0) for iters in
re.finditer(r"(\D)\1*", test_str)]

 

# printing result

print("Consecutive split string is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : ggggffggisssbbbeessssstt
>
> Consecutive split string is : [‘gggg’, ‘ff’, ‘gg’, ‘i’, ‘sss’, ‘bbb’, ‘ee’,
> ‘sssss’, ‘tt’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

