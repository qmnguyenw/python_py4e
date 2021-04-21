Python – Convert Flat dictionaries to Nested dictionary



Sometimes, while working with records, we can have problem in which we need to
perform the task of conversion of multiple flat dictionaries to a single
nested dictionary. This can have application in many domains in which data is
used extensively. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Usingdict() \+ key access**  
This is one of the way in which this task can be performed. In this, we
construct empty dictionary using dict and assign a new level to dictionary
using manual brute key access.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Flat dictionaries to Nested dictionary

# Using key access + dict()

 

# initializing dictionaries

test_dict1 = {'gfg' : 1, 'best' : 2}

test_dict2 = {'for' : 3, 'geeks' : 5}

 

# printing original dictionaries

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# Convert Flat dictionaries to Nested dictionary

# Using key access + dict()

res = dict()

res["level1"] = test_dict1

res['level2'] = test_dict2

 

# printing result 

print("The nested dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary 1 is : {‘gfg’: 1, ‘best’: 2}  
> The original dictionary 2 is : {‘geeks’: 5, ‘for’: 3}  
> The nested dictionary is : {‘level2’: {‘geeks’: 5, ‘for’: 3}, ‘level1’:
> {‘gfg’: 1, ‘best’: 2}}

  

  

**Method #2 : Usingzip()**  
This is another way in which this task can be performed. In this we link inner
keys to outer keys using zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Flat dictionaries to Nested dictionary

# Using zip()

 

# initializing dictionaries

test_dict1 = {'gfg' : 1, 'best' : 2}

test_dict2 = {'for' : 3, 'geeks' : 5}

 

# printing original dictionaries

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# Convert Flat dictionaries to Nested dictionary

# Using zip()

key_dict = ['level1', 'level2']

dict_list = [test_dict1, test_dict2]

res = dict(zip(key_dict, dict_list))

 

# printing result 

print("The nested dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary 1 is : {‘gfg’: 1, ‘best’: 2}  
> The original dictionary 2 is : {‘geeks’: 5, ‘for’: 3}  
> The nested dictionary is : {‘level2’: {‘geeks’: 5, ‘for’: 3}, ‘level1’:
> {‘gfg’: 1, ‘best’: 2}}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

