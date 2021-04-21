Python | Unique pairs in list



Sometimes, while working with python list, we can have a binary matrix (
Nested list having 2 elements ). And we can have a problem in which we need to
find the uniqueness of a pair. A pair is unique irrespective of order, it
doesn’t appear again in list. Let’s discuss certain way in which this task can
be performed.

 **Method : Usingfrozenset() + Counter() \+ list comprehension**  
The combination of above functions can perform this task. The frozenset() is
used for ignoring the ordering, Counter() is used to perform the task of
checking the uniqueness and iteration is done using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique pairs in list

# using frozenset() + Counter() + list comprehension

from collections import Counter

 

# initialize list

test_list = [[5, 6], [9, 8], [8, 9], [1,
4], [6, 5], [10, 1]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Unique pairs in list

# using frozenset() + Counter() + list comprehension

temp = Counter(frozenset(ele) for ele in test_list)

res = [temp[frozenset(ele)] == 1 for ele in test_list]

 

# printing result

print("The Unique status of elements is " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[5, 6], [9, 8], [8, 9], [1, 4], [6, 5], [10, 1]]
    The Unique status of elements is [False, False, False, True, False, True]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

