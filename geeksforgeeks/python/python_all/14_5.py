Python – Index Value repetition in List



Given a list of elements, The task is to write a Python program to repeat each
index value as per the value in that index.

>  **Input** : test_list = [3, 0, 4, 2]  
> **Output** : [0, 0, 0, 2, 2, 2, 2, 3, 3]  
> **Explanation** : 0 is repeated 3 times as its index value is 3.
>
>  **Input** : test_list = [3, 4, 2]  
> **Output** : [0, 0, 0, 1, 1, 1, 1, 2, 2]  
> **Explanation** : 1 is repeated 4 times as its value is 4.  
>

**Method #1 : Using** **list comprehension** **+** **enumerate()**

In this, we perform task of repetition using * operator, and enumerate() is
used to get indices along with values for repetition. List comprehension is
used to iteration all the elements.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index Value repetition in List

# Using list comprehension + enumerate()

 

# initializing Matrix

test_list = [3, 0, 4, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# enumerate() gets index and value of similar index element

res = [ele for sub in ([idx] * ele for idx, 

 ele in enumerate(test_list)) for ele in sub]

 

# printing result

print("Constructed List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [3, 0, 4, 2]
    Constructed List : [0, 0, 0, 2, 2, 2, 2, 3, 3]

 **Method #2 : Using** **chain.from_iterable()** **+** **list comprehension**

In this, we perform the last step of flattening of list using
chain.from_iterable(). List comprehension performs the task of iteration of
all the elements.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index Value repetition in List

# Using chain.from_iterable() + list comprehension

import itertools

 

# initializing Matrix

test_list = [3, 0, 4, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# enumerate() gets index and

# value of similar index element

# from_iterable() used to flatten

res = list(itertools.chain(*([idx] * ele for idx, 

 ele in enumerate(test_list))))

 

# printing result

print("Constructed List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [3, 0, 4, 2]
    Constructed List : [0, 0, 0, 2, 2, 2, 2, 3, 3]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

