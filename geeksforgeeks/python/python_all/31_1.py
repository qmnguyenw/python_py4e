Python – Replace None with Empty Dictionary



Given a dictionary, replace None values in every nesting with an empty
dictionary.

>  **Input** : test_dict = {“Gfg” : {1 : None, 7 : None}, “is” : None, “Best”
> : [1, { 5 : None }, 9, 3]}  
> **Output** : {‘Gfg’: {1: {}, 7: {}}, ‘is’: {}, ‘Best’: [1, {5: {}}, 9, 3]}  
> **Explanation** : All None values are replaced by empty dictionaries.
>
>  **Input** : test_dict = {“Gfg” : {7 : None}, “is” : None, “Best” : [1, { 5
> : None }, 9, 3]}  
> **Output** : {‘Gfg’: {7: {}}, ‘is’: {}, ‘Best’: [1, {5: {}}, 9, 3]}  
> **Explanation** : All None values are replaced by empty dictionaries.

**Method : Using recursion +** **isinstance()**

In this, we check for dictionary instance using isinstance() and call for
recursion for nested dictionary replacements. This also checks for nested
instances in form of list elements and checks for the list using isinstance().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace None with Empty Dictionary

# Using recursion + isinstance()

 

# helper function to perform task

 

 

def replace_none(test_dict):

 

 # checking for dictionary and replacing if None

 if isinstance(test_dict, dict):

 

 for key in test_dict:

 if test_dict[key] is None:

 test_dict[key] = {}

 else:

 replace_none(test_dict[key])

 

 # checking for list, and testing for each value

 elif isinstance(test_dict, list):

 for val in test_dict:

 replace_none(val)

 

 

# initializing dictionary

test_dict = {"Gfg": {1: None, 7: 4}, "is":
None,

 "Best": [1, {5: None}, 9, 3]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# calling helper fnc

replace_none(test_dict)

 

# printing result

print("The converted dictionary : " + str(test_dict))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Gfg’: {1: None, 7: 4}, ‘is’: None, ‘Best’:
> [1, {5: None}, 9, 3]}  
> The converted dictionary : {‘Gfg’: {1: {}, 7: 4}, ‘is’: {}, ‘Best’: [1, {5:
> {}}, 9, 3]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

