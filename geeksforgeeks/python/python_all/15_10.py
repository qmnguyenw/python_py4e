Python program to find the group sum till each K in a list



Given a List, the task is to write a Python program to perform grouping of sum
till K occurs.

 **Examples:**

>  **Input** : test_list = [2, 3, 5, 6, 2, 6, 8, 9, 4, 6, 1], K = 6  
> **Output** : [10, 6, 2, 6, 21, 6, 1]  
> **Explanation** : 2 + 3 + 5 = 10, grouped and cummulated before 6.  
>
>
> **Input** : test_list = [2, 3, 5, 6, 2, 6, 8], K = 6  
> **Output** : [10, 6, 2, 6, 8]  
> **Explanation** : 2 + 3 + 5 = 10, grouped and cummulated before 6.  
>

**Method : Using loop**

  

  

In this, we maintain a sum counter, if K occurs the summation is appended to
result list, along with K, else the summation counter is updated with current
value.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group Sum till each K

# Using loop

from collections import defaultdict

 

# initializing list

test_list = [2, 3, 5, 6, 2, 6, 8, 9,
4, 6, 1]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# initializing K

K = 6

 

temp_sum = 0

res = []

for ele in test_list:

 if ele != K:

 temp_sum += ele

 

 # append and re initializing if K occurs

 else:

 res.append(temp_sum)

 res.append(ele)

 temp_sum = 0

 

res.append(temp_sum)

 

# printing result

print("Computed list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [2, 3, 5, 6, 2, 6, 8, 9, 4, 6, 1]
    Computed list : [10, 6, 2, 6, 21, 6, 1]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

