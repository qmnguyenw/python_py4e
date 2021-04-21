Python – Get particular Nested level Items from Dictionary



Given a dictionary, extract items from particular level.

 **Examples:**

>  **Input** : {“Gfg” : { “n1”: 3, “nd2”: { “n2” : 6 }}, “is” : { “ne1”: 5,
> “ndi2”: { “ne2” : 8, “ne22” : 10 } }}, K = 2  
> **Output** : {‘n2’: 6, ‘ne2’: 8, ‘ne22’: 10}  
> **Explanation** : 2nd nesting items are extracted.
>
>  **Input** : {“Gfg” : { “n1”: 3, “nd2”: { “n2” : 6 }}, “is” : { “ne1”: 5,
> “ndi2”: { “ne2” : 8, “ne22” : 10 } }}, K = 1  
> **Output** : {“n1”: 3, “ne1”: 5}  
> **Explanation** : Elements of 1st nesting extracted.

**Method : Usingisinstance() \+ recursion**

  

  

This is one of the ways in which this task can be performed. In this, we
perform required recursion for inner nestings, and isinstance is used to
differentiate between dict instance and other data types to test for nesting.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get particular Nested level Items from Dictionary

# Using isinstance() + recursion

 

# helper function

 

 

def get_items(test_dict, lvl):

 

 # querying for lowest level

 if lvl == 0:

 yield from ((key, val) for key, val in test_dict.items()

 if not isinstance(val, dict))

 else:

 

 # recur for inner dictionaries

 yield from ((key1, val1) for val in test_dict.values()

 if isinstance(val, dict) for key1, val1 in get_items(val,
lvl - 1))

 

 

# initializing dictionary

test_dict = {"Gfg": { "n1": 3, "nd2": { "n2": 6
}}, 

 "is": { "ne1": 5, "ndi2": { "ne2": 8, "ne22":
10 } }}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K

K = 2

 

# calling function

res = get_items(test_dict, K)

 

# printing result

print("Required items : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output**

> The original dictionary is : {‘Gfg’: {‘n1’: 3, ‘nd2’: {‘n2’: 6}}, ‘is’:
> {‘ne1’: 5, ‘ndi2’: {‘ne2’: 8, ‘ne22’: 10}}}  
> Required items : {‘n2’: 6, ‘ne2’: 8, ‘ne22’: 10}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

