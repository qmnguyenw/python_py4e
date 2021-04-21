Python – Rotate dictionary by K



Given a dictionary perform its reordering by right rotating dictionary keys by
K.

 **Examples:**

>  **Input** : test_dict = {1:6, 8:1, 9:3, 10:8, 12:6, 4:9}, K = 2  
> **Output** : {12: 6, 4: 9, 1: 6, 8: 1, 9: 3, 10: 8}  
> **Explanation** : After right rotation ( cyclic ) by 2 elements, items are
> re-arranged.  
>
>
> **Input** : test_dict = {1:6, 8:1, 9:3, 10:8, 12:6, 4:9}, K = 1  
> **Output** : {4: 9, 1: 6, 8: 1, 9: 3, 10: 8, 12: 6}  
> **Explanation** : After right rotation ( cyclic ) by 1 element, items are
> re-arranged.

**Method #1 : Using** **list comprehension** **+** **items()** **+**
**dictionary comprehension**

  

  

In this, we perform task of conversion of dictionary to tuples list, and then
perform list rotate, post that, result is again converted to dictionary to get
resultant keys rotation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rotate dictionary by K

# Using list comprehension + items() + dictionary comprehension

 

# initializing dictionary

test_dict = {1: 6, 8: 1, 9: 3, 10: 8,
12: 6, 4: 9}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K

K = 2

 

# converting to tuples list

test_dict = list(test_dict.items())

 

# performing rotate

res = [test_dict[(i - K) % len(test_dict)]

 for i, x in enumerate(test_dict)]

 

# reconverting to dictionary

res = {sub[0]: sub[1] for sub in res}

 

# printing result

print("The required result : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {1: 6, 8: 1, 9: 3, 10: 8, 12: 6, 4: 9}  
> The required result : {12: 6, 4: 9, 1: 6, 8: 1, 9: 3, 10: 8}

 **Method #2 : Using** **deque.rotate()** **\+ dictionary comprehension +
items()**

In this, we perform task of rotating using deque.rotate utility, rest all
functionalities are performed in similar ways as per in above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rotate dictionary by K

# Using deque.rotate() + dictionary comprehension + items()

from collections import deque

 

# initializing dictionary

test_dict = {1: 6, 8: 1, 9: 3, 10: 8,
12: 6, 4: 9}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K

K = 2

 

# converting to tuples list

test_dict = list(test_dict.items())

 

# performing rotate

# using deque

test_dict = deque(test_dict)

test_dict.rotate(K)

test_dict = list(test_dict)

 

# reconverting to dictionary

res = {sub[0]: sub[1] for sub in test_dict}

 

# printing result

print("The required result : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {1: 6, 8: 1, 9: 3, 10: 8, 12: 6, 4: 9}  
> The required result : {12: 6, 4: 9, 1: 6, 8: 1, 9: 3, 10: 8}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

