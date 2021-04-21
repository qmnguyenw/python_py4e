Python – Dual element Rows Combinations



Sometimes, while working with data, we can have a problem in which we need to
find combinations in list. This can be a simple. But sometimes, we need to
perform a variation of it and have a dual element row instead of a single
element. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension +enumerate()**  
The combination of above functions can be used to perform this task. In this,
we iterate through the list and perform the combinations using comprehension
and enumerate().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Dual element Rows Combinations

# using list comprehension + enumerate()

from collections import defaultdict

 

# Initializing list

test_list = [[3, 4], [5, 6], [7, 8]]

 

# printing original list 

print("The original list is : " + str(test_list))

 

# Dual element Rows Combinations

# using list comprehension + enumerate()

res = [test_list[idx - len(test_list)] + test_list[idx + 1
- len(test_list)] 

 for idx, ele in enumerate(test_list)]

 

# printing result 

print ("Combination of dual rows list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[3, 4], [5, 6], [7, 8]]
    Combination of dual rows list is : [[3, 4, 5, 6], [5, 6, 7, 8], [7, 8, 3, 4]]
    

**Method #2 : Using map() + lambda + combinations()**  
The combinations of above functions can be used to perform this task. In this,
the task of iteration and pairing is done by map() and combinations()
respectively.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Dual element Rows Combinations

# using map() + lambda + combinations()

from itertools import combinations

 

# Initializing list

test_list = [[3, 4], [5, 6], [7, 8]]

 

# printing original list 

print("The original list is : " + str(test_list))

 

# Dual element Rows Combinations

# using map() + lambda + combinations()

res = list(map(lambda ele: ele[0] + ele[1],
combinations(test_list, 2)))

 

# printing result 

print ("Combination of dual rows list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[3, 4], [5, 6], [7, 8]]
    Combination of dual rows list is : [[3, 4, 5, 6], [5, 6, 7, 8], [7, 8, 3, 4]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

