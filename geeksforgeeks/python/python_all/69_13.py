Python – Remove unwanted Keys associations



Sometimes, while working with Python dictionaries, we can have problem in
which we need to remove some unwanted keys and its associated nestings. This
can have application across many domains including web development and
competitive programming. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_dict = {‘best’ : {‘for’ : {‘geeks’ : {‘CS’ : {‘Gfg’ :
> 12}}}}}  
>  **Output** : {‘best’: {‘for’: {}}}
>
>  **Input** : test_dict = {‘best’ : 14, ‘gfg’ : 13}  
>  **Output** : {‘best’ : 14, ‘gfg’ : 13}

 **Method #1 : Usingisinstance() \+ loop + recursion**  
The combination of above functionalities can be used to solve this problem. In
this, we check for the element value being a dictionary or key using
isinstance() and we recur for the construction of all the keys that are not
present as unwanted keys.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove unwanted Keys associations

# Using isinstance() + loop + recursion

 

def helper_fnc(test_dict, unw_keys):

 temp = {}

 for key, val in test_dict.items():

 if key in unw_keys:

 continue

 if isinstance(val, dict):

 temp[key] = helper_fnc(val, unw_keys)

 else:

 temp[key] = val

 return temp

 

# initializing dictionary

test_dict = {"Gfg" : {'is' : 45, 'good' : 15}, 

 'best' : {'for' : {'geeks' : {'CS' : 12}}}}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing unwanted keys

unw_keys = ['is', 'geeks']

 

# Remove unwanted Keys associations

# Using isinstance() + loop + recursion

res = helper_fnc(test_dict, unw_keys)

 

# printing result 

print("The filtered dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘Gfg’: {‘is’: 45, ‘good’: 15}, ‘best’: {‘for’:
> {‘geeks’: {‘CS’: 12}}}}  
> The filtered dictionary : {‘Gfg’: {‘good’: 15}, ‘best’: {‘for’: {}}}

