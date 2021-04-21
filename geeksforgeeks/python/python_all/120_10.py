Python | Test if key exists in tuple keys dictionary



Sometimes, while working with dictionary data, we need to check if a
particular key is present in dictionary. If keys are elementary, the solution
of problem in discussed and easier to solve. But sometimes, we can have tuple
as key of dictionary. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Usingany() \+ generator expression**

Combination of above functionalities can be used to perform this task. In
this, we check for each element inside each key for the target key. The any()
is used to check in any keys of dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if key exists in tuple keys dictionary

# using any() + generator expression

 

# initialize dictionary

test_dict = {(4, 5) : '1', (8, 9) : '2', (10,
11) : '3'}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Test key 

key = 10

 

# Test if key exists in tuple keys dictionary

# using any() + generator expression

res = any(key in sub for sub in test_dict)

 

# printing result

print("Does key exists in dictionary? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {(4, 5): '1', (8, 9): '2', (10, 11): '3'}
    Does key exists in dictionary? : True
    

  

  

**Method #2 : Usingfrom_iterable()**

This task can also be performed using this function. In this, we flatten the
keys and then check for existence.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if key exists in tuple keys dictionary

# using from_iterable()

from itertools import chain

 

# initialize dictionary

test_dict = {(4, 5) : '1', (8, 9) : '2', (10,
11) : '3'}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Test key 

key = 10

 

# Test if key exists in tuple keys dictionary

# using from_iterable()

res = key in chain.from_iterable(test_dict)

 

# printing result

print("Does key exists in dictionary? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {(4, 5): '1', (8, 9): '2', (10, 11): '3'}
    Does key exists in dictionary? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

