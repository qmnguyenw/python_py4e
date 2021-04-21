Python – Change Keys Case in Dictionary



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to perform manipulation of cases of keys. This can have possible
application in many domains including school programming and data domains.
Lets discuss a way to solve this task.

>  **Input** : test_dict = {‘Gfg’ : {‘a’ : 5, ‘b’ : {‘best’ : 6}}}  
>  **Output** : {‘GFG’: {‘A’: 5, ‘B’: {‘BEST’: 6}}}
>
>  **Input** : test_dict = {‘Gfg’ : 6}  
>  **Output** : {‘GFG’: 6}

 **Method : Usingisinstance() + toupper() \+ recursion + loop**  
The combination of above functions can also be used to solve this problem. In
this, we use toupper() to perform upper case of keys, recursion is used to
perform keys manipulation in nested keys as well. The isinstance() is used to
check if nesting is dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Change Keys Case in Dictionary

# Using isinstance() + toupper() + recursion + loop

 

# helper function

def keys_upper(test_dict):

 res = dict()

 for key in test_dict.keys():

 if isinstance(test_dict[key], dict):

 res[key.upper()] = keys_upper(test_dict[key])

 else:

 res[key.upper()] = test_dict[key]

 return res

 

# initializing dictionary

test_dict = {'Gfg' : {'a' : 5, 'b' : 6}, 'is' :
{'for' :2}, 'best': 3}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Change Keys Case in Dictionary

# Using isinstance() + toupper() + recursion + loop

res = keys_upper(test_dict)

 

# printing result 

print("The modified dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original dictionary : {'is': {'for': 2}, 'Gfg': {'b': 6, 'a': 5}, 'best': 3}
    The modified dictionary : {'GFG': {'A': 5, 'B': 6}, 'IS': {'FOR': 2}, 'BEST': 3}
    

