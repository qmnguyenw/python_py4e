Python Program to Check Overlapping Prefix – Suffix in Two Lists



Given 2 Strings, our task is to check overlapping of one string’s suffix with
prefix of other string.

    
    
    Input : test_str1 = "Gfgisbest", test_str2 = "bestforall"
    Output : best
    
    Explanation : best overlaps as suffix of first string and prefix of next.
    
    Input : test_str1 = "Gfgisbest", test_str2 = "restforall"
    Output : ''
    
    Explanation : No overlapping.

 **Method : Using** **loop** **+** **slicing** **+** **startswith()**

In this, we increment the first list and slice till list end and keep
comparing with the prefix substring of other string using startswith(). In
this, the word that occurs at end of string is compared with once with prefix
of 2nd string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Overlapping Prefix - Suffix in Two Lists

# Using loop + slicing + startswith()

import re

 

# initializing strings

test_str1 = "Gfgisbest"

test_str2 = "bestforall"

 

# printing original strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

res = ''

for char in range(len(test_str1)):

 

 # using startswith() to get prefix

 if test_str2.startswith(test_str1[char:]):

 res = test_str1[char:]

 break

 

# printing result

print("Overlapped String : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string 1 is : Gfgisbest
    The original string 2 is : bestforall
    Overlapped String  : best

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

