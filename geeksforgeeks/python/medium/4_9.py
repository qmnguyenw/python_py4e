Python program to convert Set into Tuple and Tuple into Set



Let’s see how to convert the set into tuple and tuple into the set. For
performing the task we are use some methods like tuple(), set(), type().

  *  **tuple()** : tuple method is used to convert into a tuple. This method accepts other type values as an argument and returns a tuple type value.
  *  **set()** : set method is to convert other type values to set this method is also accepted other type values as an argument and return a set type value.
  *  **type()** : type method helps the programmer to check the data type of value. This method accepts a value as an argument and it returns type of the value.

 **Example:**

    
    
     **Input:** {'a', 'b', 'c', 'd', 'e'}
    **Output:** ('a', 'c', 'b', 'e', 'd')
    **Explanation:** converting Set to tuple
    
    **Input:** ('x', 'y', 'z')
    **Output:** {'z', 'x', 'y'}
    **Explanation:** Converting tuple to set
    

**Example 1:** convert set into tuple.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# program to convert set to tuple

# create set

s = {'a', 'b', 'c', 'd', 'e'}

 

# print set

print(type(s), " ", s)

 

# call tuple() method 

# this method convert set to tuple

t = tuple(s)

 

# print tuple

print(type(t), " ", t)  
  
---  
  
 __

 __

 **Output:**

    
    
    <class 'set'>   {'a', 'c', 'b', 'e', 'd'}
    <class 'tuple'>   ('a', 'c', 'b', 'e', 'd')
    

**Example 2:** tuple into the set.

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

#program to convert tuple into set

 

# create tuple

t = ('x', 'y', 'z')

 

# print tuple

print(type(t), " ", t)

 

# call set() method

s = set(t)

 

# print set

print(type(s), " ", s)  
  
---  
  
 __

 __

 **Output:**

    
    
    <class 'tuple'>    ('x', 'y', 'z')
    <class 'set'>    {'z', 'x', 'y'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

