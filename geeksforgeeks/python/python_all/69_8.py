Python – Swapping Hierarchy in Nested Dictionaries



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to perform heirarchy swapping of nested dictionaries. This
problem can have application in domains which require dictionary
restructuring. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_dict = {‘Gfg’: { ‘a’ : [1, 3, 7, 8], ‘b’ : [4, 9], ‘c’ :
> [0, 7]}}  
>  **Output** : {‘c’: {‘Gfg’: [0, 7]}, ‘b’: {‘Gfg’: [4, 9]}, ‘a’: {‘Gfg’: [1,
> 3, 7, 8]}}
>
>  **Input** : test_dict = {‘Gfg’: {‘best’ : [1, 3, 4]}}  
>  **Output** : {‘best’: {‘Gfg’: [1, 3, 4]}}

 **Method #1 : Using loop +items()**  
The combination of above functions can be used to solve this problem. In this,
we iterate the dictionary and restructure using brute force. The items() is
used to extract all the key-value pairs of dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Swapping Hierarchy in Nested Dictionaries

# Using loop + items()

 

# initializing dictionary

test_dict = {'Gfg': { 'a' : [1, 3], 'b' : [3,
6], 'c' : [6, 7, 8]},

 'Best': { 'a' : [7, 9], 'b' : [5, 3, 2],
'd' : [0, 1, 0]}}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Swapping Hierarchy in Nested Dictionaries

# Using loop + items()

res = dict()

for key, val in test_dict.items():

 for key_in, val_in in val.items():

 if key_in not in res:

 temp = dict()

 else:

 temp = res[key_in]

 temp[key] = val_in

 res[key_in] = temp

 

# printing result 

print("The rearranged dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘Gfg’: {‘a’: [1, 3], ‘c’: [6, 7, 8], ‘b’: [3,
> 6]}, ‘Best’: {‘d’: [0, 1, 0], ‘a’: [7, 9], ‘b’: [5, 3, 2]}}  
> The rearranged dictionary : {‘d’: {‘Best’: [0, 1, 0]}, ‘a’: {‘Gfg’: [1, 3],
> ‘Best’: [7, 9]}, ‘c’: {‘Gfg’: [6, 7, 8]}, ‘b’: {‘Gfg’: [3, 6], ‘Best’: [5,
> 3, 2]}}

