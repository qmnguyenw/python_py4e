Python – Decrement Dictionary value by K



Sometimes, while working with dictionaries, we can have a use-case in which we
require to decrement a particular key’s value by K in dictionary. It may seem
a quite straight forward problem, but catch comes when the existence of a key
is not known, hence becomes a 2 step process at times. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using get()**  
The get function can be used to initialize a non-existing key with 0 and then
the decrement is possible. By this way the problem of non-existing key can be
avoided.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Decrement Dictionary value by K

# Using get()

 

# Initialize dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'for' : 4,
'CS' : 5}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Initialize K 

K = 5

 

# Using get()

# Decrement Dictionary value by K

test_dict['best'] = test_dict.get('best', 0) - K

 

# printing result 

print("Dictionary after the decrement of key : " + str(test_dict))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘for’: 4, ‘CS’: 5, ‘is’: 2, ‘gfg’: 1}  
> Dictionary after the decrement of key : {‘best’: -5, ‘for’: 4, ‘CS’: 5,
> ‘is’: 2, ‘gfg’: 1}

  

  

**Method #2 : Usingdefaultdict()**  
This problem can also be solved by using a defaultdict method, which
initializes the potential keys and doesn’t throw an exception in case of non-
existence of keys.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Decrement Dictionary value by K

# Using defaultdict()

from collections import defaultdict

 

# Initialize dictionary

test_dict = defaultdict(int)

 

# printing original dictionary

print("The original dictionary : " + str(dict(test_dict)))

 

# Initialize K 

K = 5

 

# Using defaultdict()

# Decrement Dictionary value by K

test_dict['best'] -= K

 

# printing result 

print("Dictionary after the decrement of key : " +
str(dict(test_dict)))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {}  
> Dictionary after the decrement of key : {‘best’: -5}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

