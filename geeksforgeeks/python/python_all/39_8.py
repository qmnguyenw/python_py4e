Python – K consecutive Maximum



Given a List, find maximum of next K elements from each index.

>  **Input** : test_list = [4, 3, 9, 2, 6, 12, 4, 3, 2, 4, 5], K = 4  
>  **Output** : [9, 9, 9, 12, 12, 12, 4, 5]  
>  **Explanation** : Max of next 4 elements, (max(4, 3, 9, 2) = 9)
>
>  **Input** : test_list = [4, 3, 9, 2, 6], K = 4  
>  **Output** : [9, 9]  
>  **Explanation** : Max of next 4 elements, (max(4, 3, 9, 2) = 9)

 **Method #1 : Using loop + max() + slicing**

In this, we iterate for elements in loop, slicing till next K, and use max()
to get maximum of them for current index.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K consecutive Maximum 

# Using max() + loop + slicing

 

# initializing list

test_list = [4, 3, 8, 2, 6, 7, 4, 3,
2, 4, 5]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 4

 

res = []

for idx in range(len(test_list) - K + 1):

 

 # slice next K and compute Maximum

 res.append(max(test_list[idx : idx + K]))

 

# printing result 

print("Next K Maximum List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 3, 8, 2, 6, 7, 4, 3, 2, 4, 5]
    Next K Maximum List : [8, 8, 8, 7, 7, 7, 4, 5]
    

**Method #2 : Using list comprehension**

This is yet another way to solve this, one-liner alternative to above method
using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K consecutive Maximum 

# Using list comprehension

 

# initializing list

test_list = [4, 3, 8, 2, 6, 7, 4, 3,
2, 4, 5]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 4

 

# one-liner to solve problem

res = [max(test_list[idx : idx + K]) for idx in
range(len(test_list) - K + 1)]

 

# printing result 

print("Next K Maximum List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 3, 8, 2, 6, 7, 4, 3, 2, 4, 5]
    Next K Maximum List : [8, 8, 8, 7, 7, 7, 4, 5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

