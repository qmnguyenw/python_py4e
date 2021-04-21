Python – Remove Top level from Dictionary



Sometimes, while working with Python Dictionaries, we can have nesting of
dictionaries, with each key being single values dictionary. In this we need to
remove the top level of dictionary. This can have application in data
preprocessing. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Usingvalues() \+ dictionary comprehension**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of dictionary reconstruction using dictionary
comprehension and nested lists are extracted using values().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Top level from Dictionary

# Using dictionary comprehension + values()

 

# initializing dictionary

test_dict = {'gfg' : {'data1' : [4, 5, 6, 7]},

 'is' : {'data2' : [1, 3, 8]},

 'best' : {'data3' : [9, 10, 13]}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Remove Top level from Dictionary

# Using dictionary comprehension + values()

res = dict(ele for sub in test_dict.values() for ele in
sub.items())

 

# printing result 

print("The top level removed dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: {‘data2’: [1, 3, 8]}, ‘gfg’: {‘data1’:
> [4, 5, 6, 7]}, ‘best’: {‘data3’: [9, 10, 13]}}  
> The top level removed dictionary is : {‘data1’: [4, 5, 6, 7], ‘data2’: [1,
> 3, 8], ‘data3’: [9, 10, 13]}

  

  

**Method #2 : UsingChainMap() + dict()**  
The combination of above functionalities can also be used to solve this
problem. In this, we employ ChainMap() to perform mapping of nested values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Top level from Dictionary

# Using ChainMap() + dict()

from collections import ChainMap

 

# initializing dictionary

test_dict = {'gfg' : {'data1' : [4, 5, 6, 7]},

 'is' : {'data2' : [1, 3, 8]},

 'best' : {'data3' : [9, 10, 13]}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Remove Top level from Dictionary

# Using ChainMap() + dict()

res = dict(ChainMap(*test_dict.values()))

 

# printing result 

print("The top level removed dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: {‘data2’: [1, 3, 8]}, ‘gfg’: {‘data1’:
> [4, 5, 6, 7]}, ‘best’: {‘data3’: [9, 10, 13]}}  
> The top level removed dictionary is : {‘data1’: [4, 5, 6, 7], ‘data2’: [1,
> 3, 8], ‘data3’: [9, 10, 13]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

