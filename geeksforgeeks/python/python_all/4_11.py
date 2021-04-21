Python – Test if any set element exists in List



Given a set and list, the task is to write a python program to check if any
set element exists in the list.

 **Examples:**

>  **Input :** test_dict1 = test_set = {6, 4, 2, 7, 9, 1}, test_list = [6, 8,
> 10]
>
>  **Output :** True
>
>  **Explanation :** 6 occurs in list from set.
>
>  
>
>
>  
>
>
>  **Input :** test_dict1 = test_set = {16, 4, 2, 7, 9, 1}, test_list = [6, 8,
> 10]
>
>  **Output :** False
>
>  **Explanation :** No set element exists in list.

 **Method #1 : Using** **any()**

In this, we iterate for all the elements of the set and check if any occurs in
the list. The _any()_ , returns true for any element matching condition.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if any set element exists in List

# Using any()

 

# initializing set

test_set = {6, 4, 2, 7, 9, 1}

 

# printing original set

print("The original set is : " + str(test_set))

 

# initializing list

test_list = [6, 8, 10]

 

# any() checking for any set element in check list

res = any(ele in test_set for ele in test_list)

 

# printing result

print("Any set element is in list ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original set is : {1, 2, 4, 6, 7, 9}
    Any set element is in list ? : True

 **Method #2 : Using** **& operator**

In this, we check for any element by using and operation between set and list,
if any element matches, the result is True.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if any set element exists in List

# Using & operator

 

# initializing set

test_set = {6, 4, 2, 7, 9, 1}

 

# printing original set

print("The original set is : " + str(test_set))

 

# initializing list

test_list = [6, 8, 10]

 

# & operator checks for any common element

res = bool(test_set & set(test_list))

 

# printing result

print("Any set element is in list ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original set is : {1, 2, 4, 6, 7, 9}
    Any set element is in list ? : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

