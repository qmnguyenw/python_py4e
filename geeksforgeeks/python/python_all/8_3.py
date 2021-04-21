Python – Maximum Scoring word



Given a String, the task is to write a Python program to compute maximum
scoring words i.e words made of characters with a maximum positional
summation.

 **Examples:**

>  **Input :** test_str = ‘geeks must use geeksforgeeks for cs knowledge’
>
>  **Output :** geeksforgeeks
>
>  **Explanation :** Sum of characters positional values for “geeksforgeeks”
> word is maximum, hence result.
>
>  
>
>
>  
>
>
>  **Input :** test_str = ‘geeks love geeksforgeeks’
>
>  **Output :** geeksforgeeks
>
>  **Explanation :** Sum of characters positional values for “geeksforgeeks”
> word is maximum, hence result.

 **Method #1 : Using** **split()** **\+ loop +** **ord()** **+**
**ascii_lowercase**

In this, we initially split each word using split(), get positional magnitude
using ord(), ascii_lowercase checks for correct pool of characters chosen for
evaluation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum Scoring word

# Using split() + loop + ord() + ascii_lowercase

import string

 

# initializing string

test_str = 'geeks must use geeksforgeeks for cs knowledge'

 

# printing original string

print("The original string is : " + str(test_str))

 

score = 0

max_sc = 0

res = ''

for wrd in test_str.split():

 score = 0

 # computing score

 for lttr in wrd:

 if lttr in string.ascii_lowercase:

 score += ord(lttr) - 96

 

 # updating maximum

 if score > max_sc:

 max_sc = score

 res = wrd

 

# printing result

print("Maximum scoring word : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeks must use geeksforgeeks for cs knowledge
    Maximum scoring word : geeksforgeeks

 **Method #2 : Using** **sum()** **\+ loop + ord()**

Similar to above method, only difference here being sum() is used for task of
summation rather than internal loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum Scoring word

# Using sum() + loop + ord()

import string

 

# initializing string

test_str = 'geeks must use geeksforgeeks for cs knowledge'

 

# printing original string

print("The original string is : " + str(test_str))

 

score = 0

max_sc = 0

res = ''

for wrd in test_str.split():

 

 # computing score

 # sum for cummulation

 score = sum(ord(lttr) - 96 for lttr in wrd if
lttr in string.ascii_lowercase)

 

 # updating maximum

 if score > max_sc:

 max_sc = score

 res = wrd

 

# printing result

print("Maximum scoring word : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeks must use geeksforgeeks for cs knowledge
    Maximum scoring word : geeksforgeeks

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

