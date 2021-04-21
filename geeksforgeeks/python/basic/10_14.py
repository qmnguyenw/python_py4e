Python | Dictionary key combinations



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to get all the possible pair combinations of dictionary pairs.
This kind of applications can occur in data science domain. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Using list comprehension +enumerate()**  
In this method, we just iterate the dictionary through list comprehension and
construct the pairs of keys and insert in new list. The enumerate function is
used to bind the key elements together by accessing the indices.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary key combinations

# Using list comprehension + enumerate()

 

# Initializing dict

test_dict = {'gfg' : 1, 'is' : 2, 'the' : 3,
'best' : 4}

 

# printing original dict

print("The original dict is : " + str(test_dict))

 

# Dictionary key combinations

# Using list comprehension + enumerate()

test_dict = list(test_dict)

res = [(x, y) for idx, x in enumerate(test_dict) for y
in test_dict[idx + 1: ]]

 

# printing result

print("The dictionary key pair list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dict is : {'is': 2, 'the': 3, 'best': 4, 'gfg': 1}
    The dictionary key pair list is : [('is', 'the'), ('is', 'best'), ('is', 'gfg'), ('the', 'best'), ('the', 'gfg'), ('best', 'gfg')]
    

**Method #2 : Usingitertools.combinations()**  
This task can be performed using the functionality of combinations(), which
internally takes just the keys to form the element pairs.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary key combinations

# Using itertools.combinations()

import itertools

 

# Initializing dict

test_dict = {'gfg' : 1, 'is' : 2, 'the' : 3,
'best' : 4}

 

# printing original dict

print("The original dict is : " + str(test_dict))

 

# Dictionary key combinations

# Using itertools.combinations()

res = list(itertools.combinations(test_dict, 2))

 

# printing result

print("The dictionary key pair list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dict is : {'is': 2, 'the': 3, 'best': 4, 'gfg': 1}
    The dictionary key pair list is : [('is', 'the'), ('is', 'best'), ('is', 'gfg'), ('the', 'best'), ('the', 'gfg'), ('best', 'gfg')]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

