Python – Index Directory of Elements



Given a list of elements, the task is to write a python program to compute all
the indices of all the elements.

 **Examples:**

    
    
     **Input:** test_list = [7, 6, 3, 7, 8, 3, 6, 7, 8]
    **Output:** {8: [4, 8], 3: [2, 5], 6: [1, 6], 7: [0, 3, 7]}
    **Explanation:** 8 occurs at 4th and 8th index, 3 occurs at 2nd and 5th index and so on.
    
    **Input:** test_list = [7, 6, 3, 7, 8, 3, 6]
    **Output:** {8: [4], 3: [2, 5], 6: [1, 6], 7: [0, 3]}
    **Explanation:** 8 occurs at 4th index, 3 occurs at 2nd and 5th index and so on.

 **Method #1:** Using dictionary comprehension + enumerate() \+ set()

In this, we get all the indices using _enumerate()_ to append to index list
for matching values. Dictionary comprehension is used for iteration of all
elements in the list. The _set()_ is used to get all the elements without
repetition.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index Directory of Elements

# Using dictionary comprehension + enumerate()

 

# initializing list

test_list = [7, 6, 3, 7, 8, 3, 6, 7,
8]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting each element index values

res = {key: [idx for idx, val in enumerate(test_list) if
val == key]

 for key in set(test_list)}

 

# printing result

print("Index Directory : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original list is : [7, 6, 3, 7, 8, 3, 6, 7, 8]
    Index Directory : {8: [4, 8], 3: [2, 5], 6: [1, 6], 7: [0, 3, 7]}

 **Method #2 :** Using dictionary comprehension + groupby() \+ enumerate() \+
sorted() \+ itemgetter()

In this, we sort and group like elements, using _groupby()_ and _sorted()_.
The _itemgetter()_ , is used to get values for sort by values from index and
values extracted using _enumerate()_. Dictionary comprehension is used to get
paired index of the grouped result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index Directory of Elements

 

# Using dictionary comprehension + groupby() + 

# enumerate() + sorted() + itemgetter()

from itertools import groupby

from operator import itemgetter

 

# initializing list

test_list = [7, 6, 3, 7, 8, 3, 6, 7,
8]

 

# printing original list

print("The original list is : " + str(test_list))

 

# after grouping after sorting

# and rearranging and assigning values with index

res = {key: [idx for idx, _ in groups] for key, groups in
groupby(

 sorted(enumerate(test_list), key=itemgetter(1)),
key=itemgetter(1))}

 

# printing result

print("Index Directory : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [7, 6, 3, 7, 8, 3, 6, 7, 8]
    Index Directory : {3: [2, 5], 6: [1, 6], 7: [0, 3, 7], 8: [4, 8]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

