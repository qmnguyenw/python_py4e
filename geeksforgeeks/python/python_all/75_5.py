Python – Convert String to Nested Dictionaries



Sometimes, while working with dictionaries, we can have a problem in which we
need to convert a String to nested dictionary, each separator occurrence
meaning a new nesting. This is a particular problem but can occur in data
domains and day-day programming. Let’s discuss certain way in which this task
can be done.

 **Method : Using loop + recursion**  
This is way in which this task can be performed. In this, we recur for nesting
of dictionary as we encounter a separator occurrence.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String to Nested Dictionaries

# Using loop

 

def helper_fnc(test_str, sep):

 if sep not in test_str:

 return test_str

 key, val = test_str.split(sep, 1)

 return {key: helper_fnc(val, sep)}

 

# initializing string

test_str = 'gfg_is_best_for_geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing separator

sep = '_'

 

# Convert String to Nested Dictionaries

# Using loop

res = helper_fnc(test_str, sep)

 

# printing result 

print("The nested dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg_is_best_for_geeks
    The nested dictionary is : {'gfg': {'is': {'best': {'for': 'geeks'}}}}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

