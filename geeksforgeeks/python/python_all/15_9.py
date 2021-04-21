Python – Non K distant elements



Given a list, the task is to write a Python program to extract all the
elements such that no element is at K distant from one other.

 **Examples:**

>  **Input** : test_list = [8, 10, 16, 20, 3, 1, 7], K = 2  
> **Output** : [16, 20, 7]  
> **Explanation** : 16 + 2 = 18, 16 – 2 = 14, both are not in list, hence
> filtered.
>
>  **Input** : test_list = [8, 10, 16, 20], K = 2  
> **Output** : [16, 20, 7]  
> **Explanation** : 16 + 2 = 18, 16 – 2 = 14, both are not in list, hence
> filtered.

**Method #1: Using loop**

  

  

In this we iterate for all the elements and using in operator check for each
element if has element at K distance from it, if found, its not included in
list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Non K distant elements

# Using loop

 

# initializing list

test_list = [8, 10, 16, 20, 3, 1, 7]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

res = []

for ele in test_list:

 

 # check for K distant

 if ele + K not in test_list and ele - K not in
test_list:

 res.append(ele)

 

# printing result

print("The filtered List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [8, 10, 16, 20, 3, 1, 7]
    The filtered List : [16, 20, 7]

 **Method #2: Using** **list comprehension**

In this, we perform task of filtering and iteration using 1 liner using list
comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Non K distant elements

# Using list comprehension

 

# initializing list

test_list = [8, 10, 16, 20, 3, 1, 7]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

# using list comprehension to get all elements of non K distance

res = [ele for ele in test_list if ele +

 K not in test_list and ele - K not in test_list]

 

# printing result

print("The filtered List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [8, 10, 16, 20, 3, 1, 7]
    The filtered List : [16, 20, 7]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

