Python – Append Multitype Values in Dictionary



Sometimes, while working with Python dictionaries, we can have problem in
which we need to update the dictionary values, according to the data type.
This type of problem can have application in many domains which include data.
Lets discuss a way in which this problem can be solved.

>  **Input** : test_dict = {‘gfg’ : “”, ‘is’ : {}, ‘best’ : []}  
>  **Output** : {‘gfg’: ‘geeks’, ‘is’: {‘c’: 7}, ‘best’: [4, 5]}
>
>  **Input** : test_dict = {‘gfg’ : “123”, ‘is’ : {}, ‘best’ : [“geeks”]}  
>  **Output** : {‘gfg’: ‘123geeks’, ‘is’: {‘c’: 7}, ‘best’: [‘geeks’, 4, 5]}

 **Method : Usingisinstance() + update() + extend()**  
The combination of above functions can be used to perform this task. In this,
we check for the data type of value using isinstance() and perform dictionary
update using update(), list update using extend().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Append Multitype Values in Dictionary

# Using isinstance() + update() + extend()

 

# helper_fnc

def update_dictionary(key, val, test_dict):

 

 if key not in test_dict:

 current_dict[key] = value 

 

 elif type(val) not in [str, list, dict]:

 raise ValueError("Invalid Data Type")

 

 elif isinstance(val, list):

 test_dict[key].extend(val)

 

 elif isinstance(val, dict):

 test_dict[key].update(val)

 

 else:

 test_dict[key] = test_dict[key] + val

 

 return test_dict

 

# initializing dictionary

test_dict = {'gfg' : "geekfor", 'is' : {'a' : 5,
'b' : 6}, 'best' : [1, 2, 3]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing dict, string and append

up_dict = {'c' : 7}

up_str = 'geeks'

up_list = [4, 5]

 

# Append Multitype Values in Dictionary

# Using isinstance() + update() + extend()

res = update_dictionary('gfg', up_str, test_dict)

res = update_dictionary('is', up_dict, res)

res = update_dictionary('best', up_list, res)

 

# printing result 

print("The update dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary is : {‘is’: {‘b’: 6, ‘a’: 5}, ‘best’: [1, 2, 3],
> ‘gfg’: ‘geekfor’}  
> The update dictionary : {‘is’: {‘b’: 6, ‘a’: 5, ‘c’: 7}, ‘best’: [1, 2, 3,
> 4, 5], ‘gfg’: ‘geekforgeeks’}

