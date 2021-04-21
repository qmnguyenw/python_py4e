Python | Pair and combine nested list to tuple list



Sometimes we need to convert between the data types, primarily due to the
reason of feeding them to some function or output. This article solves a very
particular problem of pairing like indices in list of lists and then
construction of list of tuples of those pairs. Let’s discuss how to achieve
the solution of this problem.

 **Method #1 : Usingzip() \+ list comprehension**  
We can use zip function to link to each element’s like indices and list
comprehension can be used to perform the logic behind the conversion to tuple
and extending the logic to all the sublists.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Pairing and combining nested list to tuple list

# using zip() + list comprehension

 

# initializing lists 

test_list1 = [[1, 4, 5], [8, 7], [2]]

test_list2 = [['g', 'f', 'g'], ['f', 'r'],
['u']]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# using zip() + list comprehension

# Pairing and combining nested list to tuple list

res = [(u, v) for x, y in zip(test_list1, test_list2)

 for u, v in zip(x, y)]

 

# print result

print("The paired list of tuple is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 : [[1, 4, 5], [8, 7], [2]]  
> The original list 2 : [[‘g’, ‘f’, ‘g’], [‘f’, ‘r’], [‘u’]]  
> The paired list of tuple is : [(1, ‘g’), (4, ‘f’), (5, ‘g’), (8, ‘f’), (7,
> ‘r’), (2, ‘u’)]

  

  

**Method #2 : Usingzip() + itertools.chain.from_iterable()**  
This problem can also be solved using the zip function along with the
from_iterable function. The task performed by zip function remains the same
but conversion to tuple and do it for all elements can be handled by
from_iterable function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Pairing and combining nested list to tuple list

# using zip() + itertools.chain.from_iterable()

from itertools import chain

 

# initializing lists 

test_list1 = [[1, 4, 5], [8, 7], [2]]

test_list2 = [['g', 'f', 'g'], ['f', 'r'],
['u']]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# using zip() + itertools.chain.from_iterable()

# Pairing and combining nested list to tuple list

res = list(zip(chain.from_iterable(test_list1),

 chain.from_iterable(test_list2)))

 

# print result

print("The paired list of tuple is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 : [[1, 4, 5], [8, 7], [2]]  
> The original list 2 : [[‘g’, ‘f’, ‘g’], [‘f’, ‘r’], [‘u’]]  
> The paired list of tuple is : [(1, ‘g’), (4, ‘f’), (5, ‘g’), (8, ‘f’), (7,
> ‘r’), (2, ‘u’)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

