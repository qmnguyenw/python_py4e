Python – Remove None Nested Records



Sometimes, while working with Python Records, can have problem in which we
need to perform the removal of data which have all key’s values as None in
nested records. This kind of problem can have application in data
preprocessing. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Usingall() \+ dictionary comprehension**  
The combination of above functionalities can be used to solve this problem. In
this, the removal of all the values with all None values are not included in
dictionary re construction are done using all().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove None Nested Records

# Using all() + dictionary comprehension

 

# initializing dictionary

test_dict = {'gfg' : {'a' : 1, 'b' : 2}, 

 'is' : {'d' : None, 'e' : None}, 

 'best' : {'g' : 1}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Remove None Nested Records

# Using all() + dictionary comprehension

res = {key: sub1 for key, sub1 in test_dict.items() if not

 all(sub2 is None for sub2 in sub1.values())}

 

# printing result 

print("The dictionary after removal : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: {‘b’: 2, ‘a’: 1}, ‘is’: {‘e’: None,
> ‘d’: None}, ‘best’: {‘g’: 1}}  
> The dictionary after removal : {‘gfg’: {‘b’: 2, ‘a’: 1}, ‘best’: {‘g’: 1}}

  

  

**Method #2 : Usingany() \+ dictionary comprehension**  
The combination of above functions can also be used to solve this problem. In
this, we keep all the records which have any key as not none using any().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove None Nested Records

# Using any() + dictionary comprehension

 

# initializing dictionary

test_dict = {'gfg' : {'a' : 1, 'b' : 2}, 

 'is' : {'d' : None, 'e' : None}, 

 'best' : {'g' : 1}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Remove None Nested Records

# Using any() + dictionary comprehension

res = {key: sub1 for key, sub1 in test_dict.items() if

 any(sub2 is not None for sub2 in sub1.values())}

 

# printing result 

print("The dictionary after removal : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: {‘b’: 2, ‘a’: 1}, ‘is’: {‘e’: None,
> ‘d’: None}, ‘best’: {‘g’: 1}}  
> The dictionary after removal : {‘gfg’: {‘b’: 2, ‘a’: 1}, ‘best’: {‘g’: 1}}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

