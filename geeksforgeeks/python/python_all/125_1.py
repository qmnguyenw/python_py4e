Python | Get all tuple keys from dictionary



Sometimes, while working with Python dictionaries, we can have it’s keys in
form of tuples. A tuple can have many elements in it and sometimes, it can be
essential to get them. If they are a part of a dictionary keys and we desire
to get all the tuple key elements, we need to perform certain functionalities
to achieve this. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using list comprehension**  
In this method, we just iterate through the each dictionary item and get it’s
key’s elements into a list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get all tuple keys from dictionary

# Using list comprehension

 

# Initializing dict

test_dict = {(5, 6) : 'gfg', (1, 2, 8) :
'is', (9, 10) : 'best'}

 

# printing original dict

print("The original dict is : " + str(test_dict))

 

# Get all tuple keys from dictionary

# Using list comprehension

res = [ele for key in test_dict for ele in key]

 

# printing result

print("The dictionary tuple key elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dict is : {(5, 6): 'gfg', (9, 10): 'best', (1, 2, 8): 'is'}
    The dictionary tuple key elements are : [5, 6, 9, 10, 1, 2, 8]
    

**Method #2 : Usingchain.from_iterable()**  
This task can be performed in more compact form, using one word instead of
one-line by using from_iterable(), which internally accesses the tuple
elements and stores in list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get all tuple keys from dictionary

# Using chain.from_iterable()

from itertools import chain

 

# Initializing dict

test_dict = {(5, 6) : 'gfg', (1, 2, 8) :
'is', (9, 10) : 'best'}

 

# printing original dict

print("The original dict is : " + str(test_dict))

 

# Get all tuple keys from dictionary

# Using chain.from_iterable()

res = list(chain.from_iterable(test_dict))

 

# printing result

print("The dictionary tuple key elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dict is : {(5, 6): 'gfg', (9, 10): 'best', (1, 2, 8): 'is'}
    The dictionary tuple key elements are : [5, 6, 9, 10, 1, 2, 8]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

