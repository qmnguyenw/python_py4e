Python – Extract range of Consecutive Similar elements ranges from string list



Given a list, extract range of consecutive similar elements.

>  **Input** : test_list = [2, 3, 3, 3, 8, 8]  
> **Output** : [(2, 0, 0), (3, 1, 3), (8, 4, 5)]  
> **Explanation** : 2 occurs from 0th to 0th index, 3 from 1st to 3rd index.
>
>  **Input** : test_list = [3, 3, 3]  
> **Output** : [(3, 0, 3)]  
> **Explanation** : 3 from 0th to 3rd index.

**Approach: Using loop**

This is a brute way to tackle this problem. In this, we loop for each element
and get a similar element range. These are traced and appended in list
accordingly with elements.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive Similar elements ranges

# Using loop

 

# initializing list

test_list = [2, 3, 3, 3, 8, 8, 6, 7,
7]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

idx = 0

while idx < (len(test_list)):

 strt_pos = idx

 val = test_list[idx]

 

 # getting last pos.

 while (idx < len(test_list) and test_list[idx] == val): 

 idx += 1

 end_pos = idx - 1

 

 # appending in format [ele, strt_pos, end_pos]

 res.append((val, strt_pos, end_pos))

 

# printing result 

print("Elements with range : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [2, 3, 3, 3, 8, 8, 6, 7, 7]  
> Elements with range : [(2, 0, 0), (3, 1, 3), (8, 4, 5), (6, 6, 6), (7, 7,
> 8)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

