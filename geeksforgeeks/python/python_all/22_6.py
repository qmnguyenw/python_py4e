Python – Group Consecutive elements by Sign



Given a list group of consecutive elements on basis of signs.

>  **Input** : test_list = [5, -3, 2, 4, 6, -2, -1, -7, -9, 2, 3]  
> **Output** : [[5], [-3], [2, 4, 6], [-2, -1, -7, -9], [2, 3]]  
> **Explanation** : Elements inserted into new list on sign change.
>
>  **Input** : test_list = [-2,3,4,5,6,-3]  
>  **Output** : [[-2], [3, 4, 5, 6], [-3]]  
>  **Explanation** : Elements inserted into new list on sign change.  
>

**Method #1: Using the loop**

In this, whenever a sign(positive or negative) change occurs, a new list is
initiated otherwise the elements are appended to a similar list as
initialized.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group Consecutive elements by Sign

# Using loop

 

# initializing list

test_list = [5, -3, 2, 4, 6, -2, -1,
-7, 

 -9, 2, 3, 10, -3, -5, 3]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = [[]]

for (idx, ele) in enumerate(test_list):

 

 # checking for similar signs by XOR

 if ele ^ test_list[idx - 1] < 0:

 res.append([ele])

 else:

 res[-1].append(ele)

 

# printing result 

print("Elements after sign grouping : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [5, -3, 2, 4, 6, -2, -1, -7, -9, 2, 3, 10, -3, -5, 3]  
> Elements after sign grouping : [[5], [-3], [2, 4, 6], [-2, -1, -7, -9], [2,
> 3, 10], [-3, -5], [3]]

 **Method #2: Using groupby() + list comprehension**

In this, we perform the task of grouping using groupby(), and list
comprehension is used to perform the task of iterating through the list. The
condition for the sign is injected using the lambda function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group Consecutive elements by Sign

# Using groupby() + list comprehension

import itertools

 

# initializing list

test_list = [-2, 3, 4, 5, 6, -3]

 

# printing original list

print("The original list is : " + str(test_list))

 

# grouped using groupby()

res = [list(ele) for idx, ele in itertools.groupby(test_list,
lambda a: a > 0)]

 

# printing result

print("Elements after sign grouping : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [-2, 3, 4, 5, 6, -3]  
> Elements after sign grouping : [[-2], [3, 4, 5, 6], [-3]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

