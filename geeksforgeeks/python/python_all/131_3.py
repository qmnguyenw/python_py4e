Python | Farthest point on horizontal lines in 2D plane



Sometimes, while in competitive programming, we might be facing a problem
which is of geometry domain and works with x-y coordinate system. The list of
tuple can be used to store the same. And along with this, there might be a
problem in which we need point with max value of x axis with similar y axis
i.e farthest point on horizontal lines. Let’s discuss certain ways to discuss
this problem.

 **Method : Using list comprehension +max()**  
This is a generic brute force method applied to get the max x axis point for
common y axis, made as 1 liner using list comprehension. The max() is used
to find the max of x axis element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Farthest point on horizontal lines in 2D plane

# Using list comprehension + max()

from collections import defaultdict

 

# initializing list

test_list = [(1, 6), (4, 6), (2, 6), (6,
8), (1, 8), (2, 9)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Using list comprehension + max()

# Farthest point on horizontal lines in 2D plane

temp = defaultdict(list)

for key, val in test_list:

 temp[val].append(key)

res = [(key, val) for key, val in test_list if
max(temp[val]) == key]

 

# Printing result

print("The list after filtering just maximum points on lines : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(1, 6), (4, 6), (2, 6), (6, 8), (1, 8), (2, 9)]
    The list after filtering just maximum points on lines : [(4, 6), (6, 8), (2, 9)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

