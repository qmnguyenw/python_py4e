Python | Increment value in dictionary



Sometimes, while working with dictionaries, we can have a use-case in which we
require to increment a particular key’s value in dictionary. It may seem a
quite straight forward problem, but catch comes when the existence of a key is
not known, hence becomes a 2 step process at times. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Usingget()**  
The get function can be used to initialize a non-existing key with 0 and then
the increment is possible. By this way the problem of non-existing key can be
avoided.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Increment value in dictionary

# Using get()

 

# Initialize dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'for' : 4,
'CS' : 5}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using get()

# Increment value in dictionary

test_dict['best'] = test_dict.get('best', 0) + 3

 

# printing result 

print("Dictionary after the increment of key : " + str(test_dict))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘is’: 2, ‘CS’: 5, ‘for’: 4, ‘gfg’: 1}  
> Dictionary after the increment of key : {‘is’: 2, ‘CS’: 5, ‘for’: 4, ‘best’:
> 3, ‘gfg’: 1}

  

  

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

# Increment value in dictionary

# Using defaultdict()

from collections import defaultdict

 

# Initialize dictionary

test_dict = defaultdict(int)

 

# printing original dictionary

print("The original dictionary : " + str(dict(test_dict)))

 

# Using defaultdict()

# Increment value in dictionary

test_dict['best'] += 3

 

# printing result 

print("Dictionary after the increment of key : " +
str(dict(test_dict)))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {}  
> Dictionary after the increment of key : {‘best’: 3}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

