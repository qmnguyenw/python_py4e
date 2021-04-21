Python program to get the indices of each element of one list in another list



Given 2 lists, get all the indices of all occurrence of each element in list2
from list1.

>  **Input** : test_list = [4, 5, 3, 7, 8, 3, 2, 4, 3, 5, 8, 3], get_list =
> [7, 5, 4]  
> **Output** : [[3], [1, 9], [0, 7]]  
> **Explanation** : 5 is present at 1st and 9th index.
>
>  **Input** : test_list = [4, 5, 3, 7, 8, 3, 2, 4, 3, 5, 8, 3], get_list =
> [7, 5, 8]  
> **Output** : [[3], [1, 9], [4, 10]]  
> **Explanation** : 8 is present at 4th and 10th index.

**Method #1 : Using loop + setdefault()**

In this, we perform the task of getting all the elements list grouped with
their indices, and in 2nd run, get only the elements that are present in the
other list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Multiple Indices from list elements

# Using setdefault() + loop

 

# initializing list

test_list = [4, 5, 3, 7, 8, 3, 2, 4,
3, 5, 8, 3]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing get_list 

get_list = [7, 5, 3]

 

# getting all elements indices

ele_indices = dict() 

for idx, val in enumerate(test_list):

 ele_indices.setdefault(val, []).append(idx)

 

# filtering only required elements

res = [ele_indices.get(idx, [None]) for idx in get_list] 

 

# printing result 

print("Filtered Indices of elements in list 1 : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 5, 3, 7, 8, 3, 2, 4, 3, 5, 8, 3]
    Filtered Indices of elements in list 1  : [[3], [1, 9], [2, 5, 8, 11]]
    
    

**Method #2 : Using list comprehension + enumerate()**

In this we use a nested loop, to get all the indices, and then filter in case
of presence in another list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Multiple Indices from list elements

# Using list comprehension + enumerate()

 

# initializing list

test_list = [4, 5, 3, 7, 8, 3, 2, 4,
3, 5, 8, 3]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing get_list 

get_list = [7, 5, 3]

 

# enumerate() used to get idx, val simultaneously

res = [([idx for idx, val in enumerate(test_list) if val
== sub] if sub in test_list else [None])

 for sub in get_list]

 

# printing result 

print("Indices of elements in list 1 : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 5, 3, 7, 8, 3, 2, 4, 3, 5, 8, 3]
    Indices of elements in list 1  : [[3], [1, 9], [2, 5, 8, 11]]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

