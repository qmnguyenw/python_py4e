Python – Consecutive Tuple difference



Given List of tuples, find index-wise absolute difference of consecutive
tuples.

>  **Input** : test_list = [(5, 3), (1, 4), (9, 5), (3, 5)]  
>  **Output** : [(4, 1), (7, 1), (6, 0)]  
>  **Explanation** : 5 – 1 = 4, 4 – 3 = 1. hence (4, 1) and so on.
>
>  **Input** : test_list = [(9, 5), (3, 5)]  
>  **Output** : [(6, 0)]  
>  **Explanation** : 9 – 3 = 6, 5 – 5 = 0.

 **Method #1 : Using list comprehension**

This is one way in which this task can be performed. In this, we employ brute
force strategy on list using list comprehension strategy to perform this task
as a one-liner.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive Tuple difference

# Using list comprehension

 

# initializing lists

test_list = [(6, 3), (1, 4), (8, 5), (3,
5)]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension to perform absolute difference

# using abs() for difference

res = [(abs(test_list[idx + 1][0] -
test_list[idx][0]), abs(test_list[idx + 1][1] -
test_list[idx][1])) 

 for idx in range(len(test_list) - 1)]

 

# printing result 

print("The extracted list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [(6, 3), (1, 4), (8, 5), (3, 5)]
    The extracted list : [(5, 1), (7, 1), (5, 0)]
    

**Method #2 : Using tuple() + map() + sub**

The combination of above functions can be used to solve this problem. In this,
we perform the task of perform subtraction using sub and map() is used to
extend the logic to whole list elements. Doesn’t output absolute result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive Tuple difference

# Using tuple() + map() + sub

from operator import sub

 

# initializing lists

test_list = [(6, 3), (1, 4), (8, 5), (3,
5)]

 

# printing original list

print("The original list : " + str(test_list))

 

# using loop to iterate elements

# using sub and map() to perform the subtraction to whole elements

res = []

for idx in range(len(test_list) - 1):

 res.append(tuple(map(sub, test_list[idx + 1][0:],
test_list[idx][0:])))

 

# printing result 

print("The extracted list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [(6, 3), (1, 4), (8, 5), (3, 5)]
    The extracted list : [(-5, 1), (7, 1), (-5, 0)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

