Python | Combining tuples in list of tuples



Sometimes, we might have to perform certain problems related to tuples in
which we need to segregate the tuple elements to combine with the each element
of complex tuple element( such as list ). This can have application in
situations we need to combine values to form a whole. Let’s discuss certain
ways in which this can be performed.

 **Method #1 : Using list comprehension**  
We can solve this particular problem using the list comprehension technique in
which we can iterate for each tuple list and join it with other tuple
attribute to join.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Combining tuples in list of tuples

# Using list comprehension

 

# initializing list

test_list = [([1, 2, 3], 'gfg'), ([5, 4, 3],
'cs')]

 

# printing original list

print("The original list : " + str(test_list))

 

# Using list comprehension

# Combining tuples in list of tuples

res = [ (tup1, tup2) for i, tup2 in test_list for tup1 in
i ]

 

# print result

print("The list tuple combination : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [([1, 2, 3], ‘gfg’), ([5, 4, 3], ‘cs’)]  
> The list tuple combination : [(1, ‘gfg’), (2, ‘gfg’), (3, ‘gfg’), (5, ‘cs’),
> (4, ‘cs’), (3, ‘cs’)]

  

  

**Method #2 : Usingproduct() \+ list comprehension**  
Apart from using the tuple for generation of tuples, the product function can
be used to get Cartesian product of list elements with tuple element, using
the iterator internally.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Combining tuples in list of tuples

# Using product() + list comprehension

from itertools import product

 

# initializing list

test_list = [([1, 2, 3], 'gfg'), ([5, 4, 3],
'cs')]

 

# printing original list

print("The original list : " + str(test_list))

 

# Using product() + list comprehension

# Combining tuples in list of tuples

res = [ele for i, j in test_list for ele in product(i,
[j])]

 

# print result

print("The list tuple combination : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [([1, 2, 3], ‘gfg’), ([5, 4, 3], ‘cs’)]  
> The list tuple combination : [(1, ‘gfg’), (2, ‘gfg’), (3, ‘gfg’), (5, ‘cs’),
> (4, ‘cs’), (3, ‘cs’)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

