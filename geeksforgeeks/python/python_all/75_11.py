Python – Removing Nested None Dictionaries



Sometimes, while working with Records, we can have a problem in which we need
to perform the removal of nested records from the dictionary which are empty.
This can have application in data preprocessing. Lets discuss certain ways in
which this task can be performed.

 **Method #1 : Usingdict() + filter()**  
This is one of the way in which this task can be performed. In this, we
perform the task of filtering the None values using filter().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Removing Nested None Dictionaries

# Using filter() + dict()

 

# initializing dictionary

test_dict = {'gfg' : {'a': 5}, 'best' : {}, 'for' :
{}, 'geeks' : {'b' : 6}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Removing Nested None Dictionaries

# Using filter() + dict()

res = dict(filter(lambda sub: sub[1], test_dict.items()))

 

# printing result 

print("The dictionary after filtering is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘geeks’: {‘b’: 6}, ‘for’: {}, ‘gfg’: {‘a’: 5},
> ‘best’: {}}  
> The dictionary after filtering is : {‘geeks’: {‘b’: 6}, ‘gfg’: {‘a’: 5}}

  

  

**Method #2 : Using dictionary comprehension**  
This is one of the way in which this task can be performed. In this we just
recreate the dictionary by checking the value presence of key.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Removing Nested None Dictionaries

# Using dictionary comprehension

 

# initializing dictionary

test_dict = {'gfg' : {'a': 5}, 'best' : {}, 'for' :
{}, 'geeks' : {'b' : 6}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Removing Nested None Dictionaries

# Using dictionary comprehension

res = {key : val for key, val in test_dict.items() if val}

 

# printing result 

print("The dictionary after filtering is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘geeks’: {‘b’: 6}, ‘for’: {}, ‘gfg’: {‘a’: 5},
> ‘best’: {}}  
> The dictionary after filtering is : {‘geeks’: {‘b’: 6}, ‘gfg’: {‘a’: 5}}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

