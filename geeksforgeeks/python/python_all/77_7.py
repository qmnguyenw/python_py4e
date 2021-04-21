Python – Key Value list pairings in Dictionary



Sometimes, while working with Python dictionaries, we can have problems in
which we need to pair all the keys with all values to form a dictionary with
all possible pairings. This can have application in many domains including
day-day programming. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using list comprehension**  
This task can be performed using this method. In this we manually extract each
key and then iterate with all the values of them to form new dictionary list.
This has drawbacks of only available for certain keys.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Key Value list pairings in Dictionary

# Using list comprehension

 

# initializing dictionary

test_dict = {'gfg' : [7, 8],

 'best' : [10, 11, 7]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Key Value list pairings in Dictionary

# Using list comprehension

res = [{'gfg': i, 'best': j} for i in
test_dict['gfg']

 for j in test_dict['best']]

 

# printing result 

print("All key value paired List : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: [7, 8], ‘best’: [10, 11, 7]}  
> All key value paired List : [{‘gfg’: 7, ‘best’: 10}, {‘gfg’: 7, ‘best’: 11},
> {‘gfg’: 7, ‘best’: 7}, {‘gfg’: 8, ‘best’: 10}, {‘gfg’: 8, ‘best’: 11},
> {‘gfg’: 8, ‘best’: 7}]

  

  

**Method #2 : Usingdict() + zip() + product()**  
The combination of above methods can also be used to perform this task. In
this, the formation of combinations is done using product(), and linking of
values is done using zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Key Value list pairings in Dictionary

# Using dict() + zip() + product()

from itertools import product

 

# initializing dictionary

test_dict = {'gfg' : [7, 8],

 'best' : [10, 11, 7]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Key Value list pairings in Dictionary

# Using dict() + zip() + product()

res = [dict(zip(test_dict, sub)) for sub in
product(*test_dict.values())]

 

# printing result 

print("All key value paired List : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: [7, 8], ‘best’: [10, 11, 7]}  
> All key value paired List : [{‘gfg’: 7, ‘best’: 10}, {‘gfg’: 7, ‘best’: 11},
> {‘gfg’: 7, ‘best’: 7}, {‘gfg’: 8, ‘best’: 10}, {‘gfg’: 8, ‘best’: 11},
> {‘gfg’: 8, ‘best’: 7}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

