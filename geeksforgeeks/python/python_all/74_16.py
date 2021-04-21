Python – Key with all Characters in String



Sometimes, while working with Python Strings, we can have problem in which we
need to extract all the keys that have all the characters in the character
value list. This kind of problem has application has many domains such as day-
day programming. Let’s discuss a way in which this problem can be solved.

 **Method : Usingall() \+ dictionary comprehension**  
The combination of above functionalities can be used to solve this problem. In
this, we use all() to perform check in whole of dictionary and extraction of
items using items().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Key with all Characters in String

# Using all() + dictionary comprehension

 

# initializing dictionary

test_dict = { 'gfg' : ['a', 'b', 'c', 'd', 'g'],

 'is' : ['b', 'f', 'e'],

 'best' : ['c', 'd', 'g'],

 'for' : ['n', 'z'],

 'CS' : ['g', 'd'] }

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing keys 

test_str = 'gd'

 

# Key with all Characters in String

# Using all() + dictionary comprehension

res = list({key for key, val in test_dict.items() 

 if all(chr in val for chr in test_str)})

 

# printing result 

print("The keys list : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: [‘b’, ‘f’, ‘e’], ‘best’: [‘c’, ‘d’,
> ‘g’], ‘for’: [‘n’, ‘z’], ‘CS’: [‘g’, ‘d’], ‘gfg’: [‘a’, ‘b’, ‘c’, ‘d’, ‘g’]}  
> The keys list : [‘best’, ‘CS’, ‘gfg’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

