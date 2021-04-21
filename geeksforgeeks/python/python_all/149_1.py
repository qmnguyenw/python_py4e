Python | Sort given list by frequency and remove duplicates



Problems associated with sorting and removal of duplicates is quite common in
development domain and general coding as well. The sorting by frequency has
been discussed, but sometimes, we even wish to remove the duplicates without
using more LOC’s and in a shorter way. Let’s discuss certain ways in which
this can be done.

 **Method #1 : Using count() + set() + sorted()**

The sorted function can be used to sort the elements as desired, the frequency
can be computed using the count function and removal of duplicates can be
handled using the set function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# sorting and removal of duplicates

# Using sorted() + set() + count()

 

# initializing list

test_list = [5, 6, 2, 5, 3, 3, 6, 5,
5, 6, 5]

 

# printing original list

print("The original list : " + str(test_list))

 

# using sorted() + set() + count()

# sorting and removal of duplicates

res = sorted(set(test_list), key = lambda ele:
test_list.count(ele))

 

# print result

print("The list after sorting and removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [5, 6, 2, 5, 3, 3, 6, 5, 5, 6, 5]
    The list after sorting and removal : [2, 3, 6, 5]
    

  

  

**Method #2 : UsingCounter.most_common() \+ list comprehension**

If one has a particular use case of sorting by the decreasing order of
frequency, one can also use most-common function of Counter library to get
frequency part.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# sorting and removal of duplicates

# Using Counter.most_common() + list comprehension

from collections import Counter

 

# initializing list

test_list = [5, 6, 2, 5, 3, 3, 6, 5,
5, 6, 5]

 

# printing original list

print("The original list : " + str(test_list))

 

# using Counter.most_common() + list comprehension

# sorting and removal of duplicates

res = [key for key, value in Counter(test_list).most_common()]

 

# print result

print("The list after sorting and removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [5, 6, 2, 5, 3, 3, 6, 5, 5, 6, 5]
    The list after sorting and removal : [5, 6, 3, 2]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

