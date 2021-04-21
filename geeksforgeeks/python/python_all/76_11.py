Python – Odd or Even elements combinations Summations in Matrix



Sometimes, while working with Python, we can have problems in which we need to
extract all possible summations of elements, one from each row in matrix,
either all odd or even elements. This is quite peculiar problem, but can have
applications in certain domains. Lets discuss certain way in which this task
can be performed.

 **Method : Using generator expression + lambda + sum() + map() + all()**  
The combination of above methods can be used to perform this task. In this, we
perform the task of extraction of pairs, all odd or even using all() +
generator expression. The task of construction of summations is done using
sum() and lambda function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Odd or Even elements combinations Summations in Matrix

# Using generator expression + lambda + sum() + map() + all()

from itertools import product

 

# initializing list

test_list = [[1, 5, 6], [7, 2, 4], [8, 9,
3]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Odd or Even elements combinations Summations in Matrix

# Using generator expression + lambda + sum() + map() + all()

temp1 = product(*test_list)

temp2 = (sub for sub in temp1 if all(ele % 2 ==
0 for ele in sub)

 or all(ele % 2 == 1 for ele in sub))

res = {sum(map(lambda idx : idx, ele)) : ele for ele
in temp2}

 

# printing result 

print("The all possible sums are : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [[1, 5, 6], [7, 2, 4], [8, 9, 3]]  
> The all possible sums are : {16: (6, 2, 8), 17: (1, 7, 9), 18: (6, 4, 8),
> 21: (5, 7, 9), 11: (1, 7, 3), 15: (5, 7, 3)}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

