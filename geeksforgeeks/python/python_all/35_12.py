Python program to covert tuple into list by adding the given string after
every element



Given a Tuple. The task is to convert it to List by adding the given string
after every element.

 **Examples:**

    
    
     **Input** : test_tup = (5, 6, 7), K = "Gfg" 
    **Output** : [5, 'Gfg', 6, 'Gfg', 7, 'Gfg'] 
    **Explanation** : Added "Gfg" as succeeding element.
    
    **Input** : test_tup = (5, 6), K = "Gfg" 
    **Output** : [5, 'Gfg', 6, 'Gfg'] 
    **Explanation** : Added "Gfg" as succeeding element.

 **Method #1: Using list comprehension**

In this, we construct a tuple of each element of tuple with a succeeding
element and then run a nested loop to flatten each constructed tuple using
list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert tuple to List with succeeding element

# Using list comprehension

 

# initializing tuple

test_tup = (5, 6, 7, 4, 9)

 

# printing original tuple

print("The original tuple is : ", test_tup)

 

# initializing K

K = "Gfg"

 

# list comprehension for nested loop for flatten

res = [ele for sub in test_tup for ele in (sub, K)]

 

# printing result

print("Converted Tuple with K : ", res)  
  
---  
  
 __

 __

 **Output:**

  

  

> The original tuple is : (5, 6, 7, 4, 9)  
> Converted Tuple with K : [5, ‘Gfg’, 6, ‘Gfg’, 7, ‘Gfg’, 4, ‘Gfg’, 9, ‘Gfg’]

 **Method #2 : Using chain.from_iterable() + list() + generator expression**

This is similar to above method, difference is that nested loop is avoided by
flattenning using chain.from_iterable().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert tuple to List with succeeding element

# Using chain.from_iterable() + list() + generator expression

from itertools import chain

 

# initializing tuple

test_tup = (5, 6, 7, 4, 9)

 

# printing original tuple

print("The original tuple is : ", test_tup)

 

# initializing K

K = "Gfg"

 

# list comprehension for nested loop for flatten

res = list(chain.from_iterable((ele, K) for ele in test_tup))

 

# printing result

print("Converted Tuple with K : ", res)  
  
---  
  
 __

 __

 **Output:**

> The original tuple is : (5, 6, 7, 4, 9)  
> Converted Tuple with K : [5, ‘Gfg’, 6, ‘Gfg’, 7, ‘Gfg’, 4, ‘Gfg’, 9, ‘Gfg’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

