Python – Sorted Nested Keys in Dictionary



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to extract all the keys of nested dictionaries and render them
in sorted order. This kind of application can occur in domains in which we
work with data. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using yield + isinstance() + loop**  
The combination of above functions can be used to perform this task. In this,
we perform the task of detection of keys using isinstance(). The yield keyword
is used to add intermediate results.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sorted Nested Keys in Dictionary

# Using yield + isinstance() + loop

 

def hlper_fnc(test_dict):

 for key, val in test_dict.items():

 yield key

 if isinstance(val, dict):

 yield from val

 

# initializing dictionary

test_dict = {'gfg': 43, 'is': {'best' : 14, 'for'
: 35, 'geeks' : 42}, 'and' : {'CS' : 29}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Sorted Nested Keys in Dictionary

# Using yield + isinstance() + loop

res = sorted(hlper_fnc(test_dict))

 

# printing result 

print("The sorted nested keys : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘and’: {‘CS’: 29}, ‘gfg’: 43, ‘is’: {‘for’:
> 35, ‘best’: 14, ‘geeks’: 42}}  
> The sorted nested keys : [‘CS’, ‘and’, ‘best’, ‘for’, ‘geeks’, ‘gfg’, ‘is’]

  

  

**Method #2 : Usingsorted() + list comprehension + isinstance()**  
The combination of above functions offer a shorthand solution to this problem.
In this, the sorting is done using sorted(). The isinstance() is used to
detect keys.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sorted Nested Keys in Dictionary

# Using sorted() + list comprehension + isinstance()

 

# initializing dictionary

test_dict = {'gfg': 43, 'is': {'best' : 14, 'for'
: 35, 'geeks' : 42}, 'and' : {'CS' : 29}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Sorted Nested Keys in Dictionary

# Using sorted() + list comprehension + isinstance()

res = sorted([key for val in test_dict.values() if
isinstance(val, dict)

 for key in val] + list(test_dict))

 

# printing result 

print("The sorted nested keys : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘and’: {‘CS’: 29}, ‘gfg’: 43, ‘is’: {‘for’:
> 35, ‘best’: 14, ‘geeks’: 42}}  
> The sorted nested keys : [‘CS’, ‘and’, ‘best’, ‘for’, ‘geeks’, ‘gfg’, ‘is’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

