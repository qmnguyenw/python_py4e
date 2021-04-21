Python – Test if String contains any Uppercase character



Given a String, Test if it contains any uppercase character.

>  **Input** : test_str = ‘geeksforgeeks’  
> **Output** : False  
> **Explanation** : No uppercase character in String.
>
>  **Input** : test_str = ‘geeksforgEeks’  
> **Output** : True  
> **Explanation** : E is uppercase in String.

**Method #1 : Using loop + isupper()**

In this, we iterate for each character in String, check for uppercase using
_isupper()_ , if found, String is flagged as True.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if String contains any Uppercase character

# Using isupper() + loop

 

# initializing string

test_str = 'geeksforGeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

res = False

for ele in test_str:

 

 # checking for uppercase character and flagging

 if ele.isupper():

 res = True

 break

 

# printing result

print("Does String contain uppercase character : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeksforGeeks
    Does String contain uppercase character : True
    

**Method #2 : Using any() + isupper()**

In this, we use _any()_ to check for any character if it is a uppercase
character.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if String contains any Uppercase character

# Using any() + isupper()

 

# initializing string

test_str = 'geeksforGeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Using any() to check for any element to be uppercase

res = any(ele.isupper() for ele in test_str)

 

# printing result

print("Does String contain uppercase character : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeksforGeeks
    Does String contain uppercase character : True
    

**Method #3 : Using regex()**

Appropriate regex can be used to perform this task. This checks for any
uppercase in the String.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if String contains any Uppercase character

# Using re()

import re

 

# initializing string

test_str = 'geeksforGeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Using regex to check for any element to be uppercase

res = bool(re.match(r'\w*[A-Z]\w*', test_str))

 

# printing result

print("Does String contain uppercase character : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeksforGeeks
    Does String contain uppercase character : True
    

**Method #4 : Using any() + ASCII values**

Checks for each character to be in pool of capital case of ASCII values.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if String contains any Uppercase character

# Using any() + ASCII values

 

# initializing string

test_str = 'geeksforGeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Using ascii values check for any element to be uppercase

res = any(ord(ele) != 32 and ord(ele) <=

 64 or ord(ele) >= 91 for ele in test_str)

 

# printing result

print("Does String contain uppercase character : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeksforGeeks
    Does String contain uppercase character : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

