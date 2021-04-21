Python – Nested Dictionary Subset



Given a Nested Dictionary, test if another dictionary is subset.

 **Examples:**

>  **Input** : test_dict = {“gfg”: 12, ‘best’ : {1 : 3, 4 : 3, ‘geeks’ : {8 :
> 7}}}, sub_dict = {8 : 7}  
> **Output** : True  
> **Explanation** : Required Nested dictionary present in Dictionary.  
>
>
> **Input** : test_dict = {“gfg”: 12, ‘best’ : {1 : 3, 4 : 3, ‘geeks’ : {8 :
> 7}}}, sub_dict = {9 : 7}  
> **Output** : False  
> **Explanation** : Nested dictionary not present in Dictionary.

**Method : Using** **all()** **+** **any()** **+** **isinstance()** **+**
**recursion**

  

  

In this, We check for subset at each nesting using function, and check for all
the keys matching using all(), any() is used for the utility to test for any
nested possible subset matching the tested subset on the test dictionary. Each
nesting is tested using recursion.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nested Dictionary Subset Python

# Using all() + any() + isinstance() + recursion

 

 

def check_eq(mast_dict, subdict):

 if not isinstance(mast_dict, (dict, list)):

 return mast_dict == subdict

 if isinstance(mast_dict, list):

 

 # check for nesting dictionaries in list

 return all(check_eq(x, y) for x, y in zip(mast_dict,
subdict))

 

 # check for all keys

 return all(mast_dict.get(idx) == subdict[idx] or
check_eq(mast_dict.get(idx), subdict[idx]) for idx in subdict)

 

 

def is_subset(mast_dict, subdict):

 if isinstance(mast_dict, list):

 

 # any matching dictionary in list

 return any(is_subset(idx, subdict) for idx in mast_dict)

 

 # any matching nested dictionary

 return check_eq(mast_dict, subdict) or (isinstance(mast_dict,
dict) and any(is_subset(y, subdict) for y in
mast_dict.values()))

 

 

# initializing dictionary

test_dict = {"gfg": 12, 'best': {1: 3, 4: 3,
'geeks': {8: 7}}, 'cs': 7}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing subset dict

sub_dict = {8: 7}

 

# calling func

res = is_subset(test_dict, sub_dict)

 

# printing result

print("Is dictionary subset : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘gfg’: 12, ‘best’: {1: 3, 4: 3, ‘geeks’: {8:
> 7}}, ‘cs’: 7}  
> Is dictionary subset : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

