Python – Group keys to values list



Sometimes, while working with Python dictionaries, we can have problem in
which we need to find all possible values of all keys in a dictionary. This
utility is quite common and can occur in many domains including day-day
programming and school programming. Lets discuss certain way in which this
task can be performed.

 **Method #1 : Using loop +defaultdict()**  
The combination of above functionalities can be used to perform this task. In
this, we capture all the elements in a list by initializing defaultdict with
list datatype and keep on appending all the values to associated key.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group keys to values list

# Using loop + defaultdict()

from collections import defaultdict

 

# initializing list

test_list = [{'gfg' : 1, 'is' : 4, 'best' : 7}, 

 {'gfg' : 9, 'is' : 8, 'best' : 3},

 {'gfg' : 4, 'is' : 4, 'best' : 7},

 {'gfg' : 7, 'is' : 2, 'best' : 8},

 {'gfg' : 1, 'is' : 4, 'best' : 7},

 {'gfg' : 10, 'is' : 9, 'best' : 2},

 {'gfg' : 0, 'is' : 5, 'best' : 6}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Group keys to values list

# Using loop + defaultdict()

res = defaultdict(set)

for sub in test_list:

 for key, val in sub.items():

 res[key].add(val)

 

# printing result 

print("The grouped key values : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

> The original list is : [{‘best’: 7, ‘gfg’: 1, ‘is’: 4}, {‘best’: 3, ‘gfg’:
> 9, ‘is’: 8}, {‘best’: 7, ‘gfg’: 4, ‘is’: 4}, {‘best’: 8, ‘gfg’: 7, ‘is’: 2},
> {‘best’: 7, ‘gfg’: 1, ‘is’: 4}, {‘best’: 2, ‘gfg’: 10, ‘is’: 9}, {‘best’: 6,
> ‘gfg’: 0, ‘is’: 5}]  
> The grouped key values : {‘best’: {8, 2, 3, 6, 7}, ‘gfg’: {0, 1, 4, 7, 9,
> 10}, ‘is’: {8, 9, 2, 4, 5}}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

