Python – Nested Dictionary values summation



Sometimes, while working with Python dictionaries, we can have problem in
which we have nested records and we need cumulative summation of it’s keys
values. This can have possible application in domains such as web development
and competitive programming. Lets discuss certain ways in which this task can
be performed.

 **Method #1 : Using loop +items() + values()**  
The combination of above functionalities can be used to solve this problem. In
this, we iterate through all the values extracted using values() and perform
the task of summation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nested Dictionary values summation

# Using loop + items() + values()

 

# initializing dictionary

test_dict = {'gfg' : {'a' : 4, 'b' : 5, 'c' :
8},

 'is' : {'a' : 8, 'c' : 10},

 'best' : {'c' : 19, 'b' : 10}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Nested Dictionary values summation

# Using loop + items() + values()

res = dict()

for sub in test_dict.values():

 for key, ele in sub.items():

 res[key] = ele + res.get(key, 0)

 

# printing result 

print("The summation dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: {‘a’: 4, ‘b’: 5, ‘c’: 8}, ‘best’: {‘b’:
> 10, ‘c’: 19}, ‘is’: {‘a’: 8, ‘c’: 10}}  
> The summation dictionary is : {‘a’: 12, ‘b’: 15, ‘c’: 37}

  

  

**Method #2 : UsingCounter() + values()**  
The combination of above methods can be used to perform this task. In this, we
save the required frequency using Counter() and extraction of values can be
done using values().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nested Dictionary values summation

# Using Counter() + values()

from collections import Counter

 

# initializing dictionary

test_dict = {'gfg' : {'a' : 4, 'b' : 5, 'c' :
8},

 'is' : {'a' : 8, 'c' : 10},

 'best' : {'c' : 19, 'b' : 10}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Nested Dictionary values summation

# Using Counter() + values()

res = Counter()

for val in test_dict.values():

 res.update(val)

 

# printing result 

print("The summation dictionary is : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: {‘a’: 4, ‘b’: 5, ‘c’: 8}, ‘best’: {‘b’:
> 10, ‘c’: 19}, ‘is’: {‘a’: 8, ‘c’: 10}}  
> The summation dictionary is : {‘a’: 12, ‘b’: 15, ‘c’: 37}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

