Python | Get total keys in dictionary



Sometimes, while working with Python dictionaries, one can come in a problem
in which one needs to get the exact number of keys that are present in whole
of dictionaries including ones that are nested. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Using recursion +items() + sum() + len()**  
This task can be performed using the combination of above functions. In this,
we check if a nested is a dictionary of not and then extract it’s keys using
items() and then sum of find length of it using respective functions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get total keys in dictionary

# Using recursion + items() + sum() + len()

 

# Utility function to perform task 

def total_keys(test_dict):

 return (0 if not isinstance(test_dict, dict) 

 else len(test_dict) + sum(total_keys(val) for val in
test_dict.values()))

 

# Initialize dictionary

test_dict = { 'gfg' : { 'is' : 1, 'best' : { 'for' :
{'geeks' :4}}}}

 

# Printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using recursion + items() + sum() + len()

# Get total keys in dictionary

res = total_keys(test_dict)

 

# printing result 

print("Number of keys in dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary is : {‘gfg’: {‘best’: {‘for’: {‘geeks’: 4}}, ‘is’:
> 1}}  
> Number of keys in dictionary is : 5

  

  

**Method #2 : Usingyield() \+ recursion**  
This task can also be performed using the combination of above functions. This
is just another way to perform this task. The intermediate result is returned,
and hence this is a more efficient method of the 2.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get total keys in dictionary

from collections import Mapping

 

# Utility function to perform task

def total_keys(test_dict):

 for key, value in test_dict.items():

 if isinstance(value, Mapping):

 yield from total_keys(value)

 yield len(test_dict)

 

# Initialize dictionary

test_dict = { 'gfg' : { 'is' : 1, 'best' : { 'for' :
{'geeks' :4}}}}

 

# Printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using yield() + recursion

# Get total keys in dictionary

res = sum(total_keys(test_dict))

 

# printing result 

print("Number of keys in dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary is : {‘gfg’: {‘best’: {‘for’: {‘geeks’: 4}}, ‘is’:
> 1}}  
> Number of keys in dictionary is : 5

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

