Python – Uppercase Half String



Given a String, perform uppercase of later part of string.

> **Input** : test_str = ‘geeksforgeek’  
>  **Output** : geeksfORGEEK  
>  **Explanation** : Latter half of string is uppercased.
>
>  **Input** : test_str = ‘apples’  
>  **Output** : appLES  
>  **Explanation** : Latter half of string is uppercased.

 **Method #1 : Using upper() + loop + len()**

In this, we compute the half index, and then perform upper() to only those
characters which lie in other half of string.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Uppercase Half String

# Using upper() + loop + len()

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# computing half index

hlf_idx = len(test_str) // 2

 

res = ''

for idx in range(len(test_str)):

 

 # uppercasing later half

 if idx >= hlf_idx:

 res += test_str[idx].upper()

 else :

 res += test_str[idx]

 

# printing result 

print("The resultant string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks
    The resultant string : geeksfORGEEKS
    

**Method #2 : Using list comprehension + join() + upper()**

This is similar to above method, just the task is performed in shorthand
manner using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Uppercase Half String

# Using list comprehension + join() + upper()

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# computing half index

hlf_idx = len(test_str) // 2

 

# join() used to create result string 

res = ''.join([test_str[idx].upper() if idx >= hlf_idx else
test_str[idx]

 for idx in range(len(test_str)) ])

 

# printing result 

print("The resultant string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks
    The resultant string : geeksfORGEEKS
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

