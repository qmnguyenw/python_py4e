Python program to mask a list using values from another list



Given two lists, the task is to write a python program that marks 1 for
elements present in the other list else mark 0.

>  **Input :** test_list = [5, 2, 1, 9, 8, 0, 4], search_list = [1, 10, 8, 3,
> 9]
>
>  **Output :** [0, 0, 1, 1, 1, 0, 0]
>
>  **Explanation :** 1, 9, 8 are present in test_list at position 2, 3, 4 and
> are masked by 1. Rest are masked by 0.
>
>  **Input :** test_list = [5, 2, 1, 19, 8, 0, 4], search_list = [1, 10, 8, 3,
> 9]
>
>  
>
>
>  
>
>
>  **Output :** [0, 0, 1, 0, 1, 0, 0]
>
>  **Explanation :** 1, 8 are present in test_list at position 2, 4 and are
> masked by 1. Rest are masked by 0.

 **Method #1: Using** **list comprehension**

In this, we iterate through search list and in operator used to check
composition using list comprehension and assign 1 for presence and 0 for
absence.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Boolean composition mask in list

# Using list comprehension

 

# initializing list

test_list = [5, 2, 1, 9, 8, 0, 4]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing search list

search_list = [1, 10, 8, 3, 9]

 

# list comprehension iteration and in operator

# checking composition

res = [1 if ele in search_list else 0 for ele in
test_list]

 

# printing result

print("The Boolean Masked list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [5, 2, 1, 9, 8, 0, 4]
    The Boolean Masked list : [0, 0, 1, 1, 1, 0, 0]

 **Method #2: Using** **set()** **+** **list comprehension**

In this, duplicate elements are removed from the search list to reduce search
space using set(). Rest all the operations are similar to the above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Boolean composition mask in list

# Using set() + list comprehension

 

# initializing list

test_list = [5, 2, 1, 9, 8, 0, 4]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing search list

search_list = [1, 10, 8, 3, 9]

 

# list comprehension iteration and in operator

# checking composition

# set() removes duplicates

res = [1 if ele in set(search_list) else 0 for ele
in test_list]

 

# printing result

print("The Boolean Masked list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [5, 2, 1, 9, 8, 0, 4]
    The Boolean Masked list : [0, 0, 1, 1, 1, 0, 0]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

