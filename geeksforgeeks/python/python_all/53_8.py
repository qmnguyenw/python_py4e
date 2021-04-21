Python – Inversion in nested dictionary



Given a nested dictionary, perform inversion of keys, i.e innermost nested
becomes outermost and vice-versa.

>  **Input** : test_dict = {“a” : {“b” : {}},  
> “d” : {“e” : {}},  
> “f” : {“g” : {}}  
>  **Output** : {‘b’: {‘a’: {}}, ‘e’: {‘d’: {}}, ‘g’: {‘f’: {}}  
>  **Explanation** : Nested dictionaries inverted as outer dictionary keys and
> viz-a-vis.
>
>  **Input** : test_dict = {“a” : {“b” : { “c” : {}}}}  
>  **Output** : {‘c’: {‘b’: {‘a’: {}}}}  
>  **Explanation** : Just a single key, mapping inverted till depth.

 **Method : Using loop + recursion**

This is brute way in which this task can be performed. In this, we extract all
the paths from outer to inner for each key using recursion and then use this
to reverse the ordering in result.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Inversion in nested dictionary

# Using loop + recursion

 

# utility function to get all paths till end 

def extract_path(test_dict, path_way):

 if not test_dict:

 return [path_way]

 temp = []

 for key in test_dict:

 temp.extend(extract_path(test_dict[key], path_way + [key]))

 return temp

 

# function to compute inversion

def hlper_fnc(test_dict):

 all_paths = extract_path(test_dict, [])

 res = {}

 for path in all_paths:

 front = res

 for ele in path[::-1]:

 if ele not in front :

 front[ele] = {}

 front = front[ele]

 return res

 

# initializing dictionary

test_dict = {"a" : {"b" : {"c" : {}}},

 "d" : {"e" : {}},

 "f" : {"g" : {"h" : {}}}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# calling helper function for task 

res = hlper_fnc(test_dict)

 

# printing result 

print("The inverted dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'a': {'b': {'c': {}}}, 'd': {'e': {}}, 'f': {'g': {'h': {}}}}
    The inverted dictionary : {'c': {'b': {'a': {}}}, 'e': {'d': {}}, 'h': {'g': {'f': {}}}}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

