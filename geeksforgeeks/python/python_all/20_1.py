Python – Test Consecutive Element Matrix



Given a Matrix, test if it is made of consecutive elements.

>  **Input** : test_list = [[4, 5, 6], [7], [8, 9, 10], [11, 12]]  
> **Output** : True  
> **Explanation** : Elements in Matrix range from 4 to 12.
>
>  **Input** : test_list = [[4, 5, 6], [7], [8, 18, 10], [11, 12]]  
> **Output** : False  
> **Explanation** : Elements not consecutive and not in a range.  
>

**Method #1: Using loop**

In this, we check for consecution within the row, and before each row, check
for 1st element to be next to last element from previous row.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test Consecutive Element Matrix

# Using loop

 

# initializing list

test_list = [[4, 5, 6], [7], [8, 9, 10],
[11, 12]]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = True

mem_list = []

for sub in test_list:

 flag = True

 for ele in sub:

 

 # checking for last element to be Consecutive

 if len(mem_list) != 0:

 if mem_list[-1] != ele - 1:

 flag = False

 break

 mem_list.append(ele)

 

 if not flag:

 res = False

 break

 

# printing result

print("Is Matrix Consecutive ? : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[4, 5, 6], [7], [8, 9, 10], [11, 12]]
    Is Matrix Consecutive ? : True
    

**Method #2 : Using chain.from_iterable() + all()**

In this, we flatten matrix to list, and then check for all elements in
consecution using all(), to be 1 greater than the preceeding element in
flattened Matrix.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test Consecutive Element Matrix

# Using chain.from_iterable() + all()

from itertools import chain

 

# initializing list

test_list = [[4, 5, 6], [7], [8, 9, 10],
[11, 12]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# flattening matrix

test_list = list(chain.from_iterable(test_list))

 

# checking for boolean true

res = all(test_list[idx - 1] == test_list[idx] -

 1 for idx in range(1, len(test_list)))

 

# printing result

print("Is Matrix Consecutive ? : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[4, 5, 6], [7], [8, 9, 10], [11, 12]]
    Is Matrix Consecutive ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

