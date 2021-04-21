Python | Find Symmetric Pairs in dictionary



Sometimes, while working with Python dictionary, one can have a problem in
which one desires to get key-value pairs that are symmetrical, i.e that has
key-value pair of same value irrespective of the fact value is a key or value.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using generator + loop**

This task can be solved in brute force method using loops and generators by
yielding at runtime the values of matching key-value pairs.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Find Symmetric Pairs in dictionary

# using generator + loop

 

# generator function to perform task

def find_sym_pairs(test_dict):

 for key in test_dict.keys():

 val = test_dict.get(key)

 

 if test_dict.get(val) == key:

 yield key, val

 return

 

# Initializing dict

test_dict = {'a' : 1, 'b' : 2, 'c' : 3, 1 :
'a', 2 : 'b'}

 

# printing original dict 

print("The original dict is : " + str(test_dict))

 

# Find Symmetric Pairs in dictionary

# using generator + loop

res = []

for key, val in find_sym_pairs(test_dict):

 temp = (key, val)

 res.append(temp)

 

# printing result

print("The pairs of Symmetric values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dict is : {'a': 1, 1: 'a', 'c': 3, 'b': 2, 2: 'b'}
    The pairs of Symmetric values : [('a', 1), (1, 'a'), ('b', 2), (2, 'b')]
    

  

  

**Method #2 : Using list comprehension**

This task can also be performed as a one-liner using list comprehension as a
shortened way of performing loop-based solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Find Symmetric Pairs in dictionary

# Using list comprehension

 

# Initializing dict

test_dict = {'a' : 1, 'b' : 2, 'c' : 3, 1 :
'a', 2 : 'b'}

 

# printing original dict 

print("The original dict is : " + str(test_dict))

 

# Find Symmetric Pairs in dictionary

# Using list comprehension

temp = [(key, value) for key, value in test_dict.items()]

res = [(x, y) for (x, y) in temp if (y, x) in temp]

 

# printing result

print("The pairs of Symmetric values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dict is : {'a': 1, 1: 'a', 'c': 3, 'b': 2, 2: 'b'}
    The pairs of Symmetric values : [('a', 1), (1, 'a'), ('b', 2), (2, 'b')]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

