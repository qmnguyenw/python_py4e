Python – Subscript Dictionary



Sometimes, while working with data in Python, we can have a problem in which
we need to use subscripted version of numbers rather than normal ones. For
this, having a dictionary which maps the number with its subscript version has
good utility. Let’s discuss certain ways in which this task can be performed.

>  **Input :** test_str = “012345”  
>  **Output :** {‘0’: ‘?’, ‘1’: ‘?’, ‘2’: ‘?’, ‘3’: ‘?’, ‘4’: ‘?’, ‘5’: ‘?’}
>
>  **Input :** test_str = “0”  
>  **Output :** {‘0’: ‘?’}

 **Method #1 : Using loop + ord()**  
This is brute force way in which we perform this task. In this, we iterate
through the numbers that we require to subscript and construct subscript value
using ord() and its binary value. Works in Python 3.7 +.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Subscript Dictionary

# Using loop + ord()

 

# initializing string

test_str = "0123456789"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing Subscript number value

K = u'\u2080'

 

# Subscript Dictionary

# Using loop + ord()

res = {}

for ele in test_str:

 res[ele] = K

 K = chr(ord(K) + 1)

 

# printing result 

print("The split string is : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original string is : 0123456789  
> The split string is : {‘7’: ‘?’, ‘4’: ‘?’, ‘2’: ‘?’, ‘3’: ‘?’, ‘5’: ‘?’,
> ‘8’: ‘?’, ‘1’: ‘?’, ‘6’: ‘?’, ‘0’: ‘?’, ‘9’: ‘?’}

