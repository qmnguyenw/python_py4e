Python – Mid occurrence of K in string



Given a String, the task is to write a Python program to extract the mid
occurrence of a character.

> **Input :** test_str = “geeksforgeeks is best for all geeks”, K = ‘e’
>
>  **Output :** 10
>
>  **Explanation :** 7 occurrences of e. The 4th occurrence [mid] is at 10th
> index.
>
>  **Input :** test_str = “geeksforgeeks is best for all geeks”, K = ‘g’
>
>  
>
>
>  
>
>
>  **Output :** 8
>
>  **Explanation :** 3 occurrences of g. The 2nd occurrence [mid] is at 8th
> index.

 **Method #1 : Using** **enumerate()** **+** **list comprehension**

In this, we perform the task of getting all occurrences using list
comprehension and enumerate gets all indices. Post that the middle element of
the list is printed to get mid occurrence of a character.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mid occurrence of K in string

# Using find() + max() + slice

 

# initializing string

test_str = "geeksforgeeks is best for all geeks"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = 'e'

 

# getting all the indices of K

indices = [idx for idx, ele in enumerate(test_str) if ele
== K]

 

# getting mid index

res = indices[len(indices) // 2]

 

# printing result

print("Mid occurrence of K : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeksforgeeks is best for all geeks
    Mid occurrence of K : 10

 **Method #2 : Using finditer() +** **list comprehension** **+** **regex**

In this, the character is found using regex and finditer(). The mid occurrence
is the mid element of the indices list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mid occurrence of K in string

# Using finditer() + list comprehension + regex

import re

 

# initializing string

test_str = "geeksforgeeks is best for all geeks"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = 'e'

 

# getting all the indices of K

# using regex

indices = [ele.start() for ele in re.finditer(K, test_str)]

 

# getting mid index

res = indices[len(indices) // 2]

 

# printing result

print("Mid occurrence of K : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeksforgeeks is best for all geeks
    Mid occurrence of K : 10

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

