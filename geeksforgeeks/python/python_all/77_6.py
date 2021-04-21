Python – Dictionary values String Length Summation



Sometimes, while working with Python dictionaries we can have problem in which
we need to perform the summation of all the string lengths which as present as
dictionary values. This can have application in many domains such as web
development and day-day programming. Lets discuss certain ways in which this
task can be performed.

 **Method #1 : Usingsum() + generator expression + len()**  
The combination of above functions can be used to perform this task. In this,
we compute length using len(), summation using sum() and iteration using
generator expression.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary values String Length Summation

# Using sum() + len() + generator expression

from collections import ChainMap

 

# initializing dictionary

test_dict = {'gfg' : '2345',

 'is' : 'abcde',

 'best' : 'qwerty'}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Dictionary values String Length Summation

# Using sum() + len() + generator expression

res = sum((len(val) for val in test_dict.values()))

 

# printing result 

print("The string values length summation : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: ‘abcde’, ‘best’: ‘qwerty’, ‘gfg’:
> ‘2345’}  
> The string values length summation : 15

  

  

**Method #2 : Usingmap() + len() + sum()**  
This performs the task similar to above function. The only difference is that
iteration is performed using map() than generator expression.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary values String Length Summation

# Using map() + len() + sum()

 

# initializing dictionary

test_dict = {'gfg' : '2345',

 'is' : 'abcde',

 'best' : 'qwerty'}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Dictionary values String Length Summation

# Using map() + len() + sum()

res = sum(map(len, test_dict.values()))

 

# printing result 

print("The string values length summation : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: ‘abcde’, ‘best’: ‘qwerty’, ‘gfg’:
> ‘2345’}  
> The string values length summation : 15

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

