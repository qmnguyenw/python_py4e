Python program to construct Equidigit tuples



Given the Elements list, divide the tuple list into similar digit tuples
pairs.

>  **Input** : test_list = [5654, 223, 982143, 34, 1021]  
> **Output** : [(56, 54), (2, 23), (982, 143), (3, 4), (10, 21)]  
> **Explanation** : Element in tuples equidistributed.
>
>  **Input** : test_list = [5654, 223, 1021]  
> **Output** : [(56, 54), (2, 23), (10, 21)]  
> **Explanation** : Element in tuples equidistributed.  
>

**Method #1 : Using loop + slicing + str()**

In this, we perform the task of dividing by getting mid-idx and then slice
from mid, initially integral number is split to a string by using str().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Construct Equidigit tuples

# Using loop + slicing str()

 

# initializing list

test_list = [5654, 223, 982143, 34, 1021]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for sub in test_list:

 

 # getting mid element

 mid_idx = len(str(sub)) // 2

 

 # slicing Equidigits

 el1 = str(sub)[:mid_idx]

 el2 = str(sub)[mid_idx:]

 

 res.append((int(el1), int(el2)))

 

# printing result 

print("Equidigit tuples List : " + str(res))  
  
---  
  
 __

 __

**Output:**

> The original list is : [5654, 223, 982143, 34, 1021]  
> Equidigit tuples List : [(56, 54), (2, 23), (982, 143), (3, 4), (10, 21)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

