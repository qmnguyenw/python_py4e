Python – Replacing by Greatest Neighbour in list



Given a list, the task is to write a Python program to replace with the
greatest neighbor among previous and next elements.

>  **Input** : test_list = [5, 4, 2, 5, 8, 2, 1, 9],  
> **Output** : [5, 5, 5, 8, 8, 8, 9, 9]  
> **Explanation** : 4 is having 5 and 2 as neighbours, replaced by 5 as
> greater than 2.
>
>  **Input** : test_list = [5, 4, 2, 5],  
> **Output** : [5, 5, 5, 5]  
> **Explanation** : 4 is having 5 and 2 as neighbours, replaced by 5 as
> greater than 2.  
>

**Method 1 :** Using loop + chain conditional statements

In this, we use loop to iterate through all the elements in list and check for
neighbours for greater element using conditionals and then is replaced.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replacing by Greatest Neighbour

# Using loop + chain conditional statements

 

# initializing list

test_list = [5, 4, 2, 5, 8, 2, 1, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

for idx in range(1, len(test_list) - 1):

 

 # replacing by greater Neighbour

 test_list[idx] = test_list[idx - 1] \

 if test_list[idx - 1] > test_list[idx + 1] \

 else test_list[idx + 1]

 

# printing result

print("The elements after replacing : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [5, 4, 2, 5, 8, 2, 1, 9]
    The elements after replacing : [5, 5, 5, 8, 8, 8, 9, 9]

 **Method 2 :** Using max() \+ loop.

In this, we get the maximum element among neighbouring elements using max().
The loop is used to iterate through the elements.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replacing by Greatest Neighbour

# Using max() + loop

 

# initializing list

test_list = [5, 4, 2, 5, 8, 2, 1, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

for idx in range(1, len(test_list) - 1):

 

 # using max() to get maximum of Neighbours

 test_list[idx] = max(test_list[idx - 1], test_list[idx +
1])

 

# printing result 

print("The elements after replacing : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [5, 4, 2, 5, 8, 2, 1, 9]
    The elements after replacing : [5, 5, 5, 8, 8, 8, 9, 9]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

