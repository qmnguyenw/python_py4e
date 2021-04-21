Python – K middle elements



Given a List, extract K elements occurring in middle of list.

>  **Input** : test_list = [2, 3, 5, 7, 8, 5, 3, 5, 9], K = 3  
> **Output** : [7, 8, 5]  
> **Explanation** : Middle 3 elements are extracted.
>
>  **Input** : test_list = [2, 3, 5, 7, 8, 5, 3, 5, 9], K = 7  
> **Output** : [3, 5, 7, 8, 5, 3, 5]  
> **Explanation** : Middle 7 elements are extracted.

**Method #1: Using loop**

In this, we initially formulate the range, extracting half pre middle, and
half post middle elements, and then use a loop to extract desired elements.
Works evenly in odd length lists.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K middle elements

# Using loop

 

# initializing list

test_list = [2, 3, 5, 7, 8, 5, 3, 5,
9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 5

 

# computing strt, and end index 

strt_idx = (len(test_list) // 2) - (K // 2)

end_idx = (len(test_list) // 2) + (K // 2)

 

# using loop to get indices 

res = []

for idx in range(len(test_list)):

 

 # checking for elements in range

 if idx >= strt_idx and idx <= end_idx:

 res.append(test_list[idx])

 

# printing result 

print("Extracted elements list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [2, 3, 5, 7, 8, 5, 3, 5, 9]
    Extracted elements list : [5, 7, 8, 5, 3]
    

**Method #2: Using** **list slicing** ****

In this, after range computation step, the range extraction occurs using list
slicing.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K middle elements

# Using list slicing 

 

# initializing list

test_list = [2, 3, 5, 7, 8, 5, 3, 5,
9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 5

 

# computing strt, and end index 

strt_idx = (len(test_list) // 2) - (K // 2)

end_idx = (len(test_list) // 2) + (K // 2)

 

# slicing extracting middle elements

res = test_list[strt_idx: end_idx + 1]

 

# printing result 

print("Extracted elements list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [2, 3, 5, 7, 8, 5, 3, 5, 9]
    Extracted elements list : [5, 7, 8, 5, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

