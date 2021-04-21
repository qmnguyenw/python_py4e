Python – Flatten and remove keys from Dictionary



Given a dictionary, perform flattening and removal of certain dictionary keys.

>  **Input** : test_dict = {‘a’: 14, ‘b’: 16, ‘c’: {‘d’: {‘e’: 7}}}, rem_keys
> = [“c”, “a”, “d”]  
>  **Output** : {‘b’: 16, ‘e’: 7}  
>  **Explanation** : All “c”, “a” and “d” has been removed.
>
>  **Input** : test_dict = {‘a’: 14, ‘b’: 16, ‘c’: {‘d’: {‘e’: 7}}}, rem_keys
> = [“c”, “d”, “e”]  
>  **Output** : {‘a’: 14, ‘b’: 16}  
>  **Explanation** : All “c”, “e” and “d” has been removed.

 **Method : Using recursion + isinstance() + loop**

The combination of above functions can be used to solve this problem. In this,
we check for dictionary as instance for nested dictionary using isinstance()
and recur each time for inner dictionary. The loop is used to iterate for
keys.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Flatten and remove keys from Dictonary

# Using loop + recursion + isinstance()

 

# function to compute removal and flattening

def hlper_fnc(test_dict, rem_keys):

 if not isinstance(test_dict, dict):

 return test_dict 

 res = {}

 

 for key, val in test_dict.items():

 rem = hlper_fnc(val, rem_keys)

 

 # performing removal

 if key not in rem_keys:

 res[key] = rem

 else:

 if isinstance(rem, dict):

 res.update(rem)

 return res

 

# initializing dictionary

test_dict = {'a': 14, 'b': 16, 'c': {'d':
{'e': 7}}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing removal keys 

rem_keys = ["c", "d"]

 

# calling helper function for task 

res = hlper_fnc(test_dict, rem_keys)

 

# printing result 

print("The removed and flattened dictionary : " + str(res))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘a’: 14, ‘b’: 16, ‘c’: {‘d’: {‘e’: 7}}}  
> The removed and flattened dictionary : {‘a’: 14, ‘b’: 16, ‘e’: 7}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

