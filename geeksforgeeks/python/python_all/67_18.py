Python – Flatten Nested Tuples



Sometimes, while working with Python Tuples, we can have a problem in which we
need to perform flattening of tuples, which can be nested and undesired. This
can have application across many domains such as Data Science and web
development. Let’s discuss certain way in which this task can be performed.

    
    
    **Input** : test_tuple = ((4, 7), ((4, 5), ((6, 7), (7, 6))))
    **Output** : ((4, 7), (4, 5), (6, 7), (7, 6))
    
    **Input** : test_tuple = ((4, 7), (5, 7), (1, 3))
    **Output** : ((4, 7), (5, 7), (1, 3))
    

**Method : Usingrecursion + isinstance()**  
The combination of above functionalities can help us achieve solution to this
problem. In this we use recusion to perform the task of digging into each
tuple for inner tuples, and for decision of flattening, isinstance() is used
depending upon tuple container or primitive data.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Flatten Nested Tuples

# Using recursion + isinstance()

 

# helper function

def flatten(test_tuple):

 

 if isinstance(test_tuple, tuple) and len(test_tuple) ==
2 and not isinstance(test_tuple[0], tuple):

 res = [test_tuple]

 return tuple(res)

 

 res = []

 for sub in test_tuple:

 res += flatten(sub)

 return tuple(res)

 

# initializing tuple

test_tuple = ((4, 5), ((4, 7), (8, 9), (10,
11)), (((9, 10), (3, 4))))

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# Flatten Nested Tuples

# Using recursion + isinstance()

res = flatten(test_tuple)

 

# printing result 

print("The flattened tuple : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original tuple : ((4, 5), ((4, 7), (8, 9), (10, 11)), ((9, 10), (3, 4)))
    The flattened tuple : ((4, 5), (4, 7), (8, 9), (10, 11), (9, 10), (3, 4))
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

