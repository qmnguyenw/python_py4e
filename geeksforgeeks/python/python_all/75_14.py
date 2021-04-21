Python – Nested record values summation



Sometimes, while working with records, we can have problem in which we need to
perform summation of nested keys of a key and record the sum as key’s value.
This can have possible applications in domains such as Data Science and web
development. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force way in which we can perform this task. In this, we iterate
through the nested dictionary summing up the values and assigning to
respective key.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nested record values summation

# Using loop

 

# initializing dictionary

test_dict = {'gfg' : {'a' : 4, 'b' : 5, 'c' :
6},

 'is' : {'a': 2, 'b' : 9, 'c' : 10},

 'best' : {'a' : 10, 'b' : 2, 'c' : 12}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Nested record values summation

# Using loop

res = dict()

for sub in test_dict:

 sum = 0

 for keys in test_dict[sub]:

 sum = sum + test_dict[sub][keys]

 res[sub] = sum

 

# printing result 

print("The dictionary after keys summation is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {'best': {'a': 10, 'c': 12, 'b': 2}, 'is': {'a': 2, 'c': 10, 'b': 9}, 'gfg': {'a': 4, 'c': 6, 'b': 5}}
    The dictionary after keys summation is : {'best': 24, 'is': 21, 'gfg': 15}
    

**Method #2 : Usingsum()**  
This is yet another way in which this task can be performed. In this, we
perform the task of computation using sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nested record values summation

# Using sum()

from collections import Counter

 

# initializing dictionary

test_dict = {'gfg' : {'a' : 4, 'b' : 5, 'c' :
6},

 'is' : {'a': 2, 'b' : 9, 'c' : 10},

 'best' : {'a' : 10, 'b' : 2, 'c' : 12}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Nested record values summation

# Using sum()

res = dict()

for sub in test_dict:

 res[sub] = sum([test_dict[sub][ele] for ele in
test_dict[sub]])

 

# printing result 

print("The dictionary after keys summation is : " +
str(dict(res)))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {'best': {'a': 10, 'c': 12, 'b': 2}, 'is': {'a': 2, 'c': 10, 'b': 9}, 'gfg': {'a': 4, 'c': 6, 'b': 5}}
    The dictionary after keys summation is : {'best': 24, 'is': 21, 'gfg': 15}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

