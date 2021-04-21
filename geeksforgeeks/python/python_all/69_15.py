Python – Test for empty Nested Records



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to test if a particular dictionary has nested records, and all
of them is empty, i.e with no key or no value in case of list. This kind of
problem is quite common in data domains such as Data Science.  
Let’s discuss certain way in which this task can be performed.

>  **Input** : test_dict = {‘Gfg’: [], ‘geeks’: {}}  
>  **Output** : True
>
>  **Input** : test_dict = {‘Gfg’: 4}  
>  **Output** : False

 **Method #1 : Using recursion +all() + isinstance()**  
The combination of above functionalities can be used to solve this problem. In
this, we check for all nesting using all(), recursion and isinstance() is used
to test for dictionary or list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for empty Nested Records

# Using recursion + all() + isinstance

 

# Helper function

def hlper_fnc(test_dict):

 if isinstance(test_dict, dict):

 return all(hlper_fnc(sub) for _, sub in test_dict.items())

 if isinstance(test_dict, list):

 return all(hlper_fnc(sub) for sub in test_dict)

 return False

 

# initializing dictionary

test_dict = {'Gfg': [], 'is': { 'best': [], 'for': {} },
'geeks': {}}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Test for empty Nested Records

# Using recursion + all() + isinstance

res = hlper_fnc(test_dict)

 

# printing result 

print("Is dictionary without data ? : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘is’: {‘best’: [], ‘for’: {}}, ‘geeks’: {},
> ‘Gfg’: []}  
> Is dictionary without data ? : True

