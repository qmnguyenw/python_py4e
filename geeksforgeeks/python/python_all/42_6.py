Python – Divide String into Equal K chunks



Given a String perform division into K equal chunks.

>  **Input** : test_str = ‘geeksforgeek’, K = 4  
>  **Output** : [‘gee’, ‘ksf’, ‘org’, ‘eek’]  
>  **Explanation** : 12/4 = 3, length of each string extracted.
>
>  **Input** : test_str = ‘geeksforgeek’, K = 1  
>  **Output** : [‘geeksforgeek’]  
>  **Explanation** : 12/1 = 12, whole string is single chunk.

 **Method #1 : Using len() + loop**

In this, we first perform task of computation of length of each chunk required
from K and string length, post that, string is splitted on desired indices to
extract chunks using slicing.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Divide String into Equal K chunks

# Using len() + loop

 

# initializing strings

test_str = 'geeksforgeeks 1'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 5

 

# compute chunk length 

chnk_len = len(test_str) // K

 

res = []

for idx in range(0, len(test_str), chnk_len):

 

 # appending sliced string

 res.append(test_str[idx : idx + chnk_len])

 

 

# printing result 

print("The K chunked list : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks 1
    The K chunked list : ['gee', 'ksf', 'org', 'eek', 's 1']
    

**Method #2 : Using list comprehension**

The method similar to above, difference being that last process is
encapsulated to one – liner list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Divide String into Equal K chunks

# Using list comprehension

 

# initializing strings

test_str = 'geeksforgeeks 1'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 5

 

# compute chunk length 

chnk_len = len(test_str) // K

 

# one-liner to perform the task 

res = [test_str[idx : idx + chnk_len] for idx in
range(0, len(test_str), chnk_len)]

 

# printing result 

print("The K len chunked list : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks 1
    The K len chunked list : ['gee', 'ksf', 'org', 'eek', 's 1']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

