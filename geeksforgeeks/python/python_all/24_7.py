Python program to find start and end indices of all Words in a String



Given a String, return all the start indices and end indices of each word.

 **Examples:**

>  **Input** : test_str = ‘ Geekforgeeks is Best’  
> **Output** : [(1, 12), (16, 17), (19, 22)]  
> **Explanation** : “Best” Starts at 19th index, and ends at 22nd index.
>
>  **Input** : test_str = ‘ Geekforgeeks is Best’  
> **Output** : [(1, 12), (17, 18), (20, 23)]  
> **Explanation** : “Best” Starts at 20th index, and ends at 23rd index.

**Method : Using** **list comprehension** **+** **regex** **\+ finditer()**

  

  

In this, we extract all the words using finditer() and regex, to get initial
and end index, we use start() and end() and encapsulate using list
comprehension in form of tuple list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Word Ranges in String

# Using list comprehension + regex + finditer()

import re

 

# initializing string

test_str = ' Geekforgeeks is Best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# regex to get words, loop to get each start and end index

res = [(ele.start(), ele.end() - 1) for ele in
re.finditer(r'\S+', test_str)]

 

# printing result

print("Word Ranges are : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is :  Geekforgeeks   is Best    for  geeks
    Word Ranges are : [(1, 12), (16, 17), (19, 22), (27, 29), (32, 36)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

