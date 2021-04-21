Python – Swap K suffix with prefix



Given a List, perform a swap of K prefix and suffix.

 **Examples:**

>  **Input** : test_list = [5, 6, 3, 1, 0, 1, 3, 5, 7, 9], K = 2  
>  **Output** : [7, 9, 3, 1, 0, 1, 3, 5, 5, 6]  
>  **Explanation** : Rear 2 and Front 2 elements swapped.
>
>  **Input** : test_list = [5, 6, 3, 1, 0, 1, 3, 5, 7, 9], K = 1  
>  **Output** : [9, 6, 3, 1, 0, 1, 3, 5, 7, 5]  
>  **Explanation** : Rear 1 and Front 1 element swapped.

 **Method #1: Using slice and range swap**

  

  

In this, we perform the task of getting the required slice using list slicing
and perform range swap to swap elements. This is inplace method to solve this
problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Swap K suffix with prefix

# Using range swap + slice()

 

# initializing list

test_list = [5, 6, 3, 1, 0, 1, 3, 5,
7, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 3

 

# performing range swap

test_list[:K], test_list[len(

 test_list) - K:] = test_list[len(test_list) - K:],
test_list[:K]

 

# printing result

print("After prefix suffix swap : " + str(test_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [5, 6, 3, 1, 0, 1, 3, 5, 7, 9]
    After prefix suffix swap : [5, 7, 9, 1, 0, 1, 3, 5, 6, 3]
    

**Method #2 : Using slice notation**

In this we perform reconstruction of list elements using slicing each list
performing slice.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Swap K suffix with prefix

# Using slice notation

 

# initializing list

test_list = [5, 6, 3, 1, 0, 1, 3, 5,
7, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 3

 

# joining parts using slice

res = test_list[len(test_list) - K:] + \

 test_list[K: len(test_list) - K] + test_list[:K]

 

# printing result

print("After prefix suffix swap : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [5, 6, 3, 1, 0, 1, 3, 5, 7, 9]
    After prefix suffix swap : [5, 7, 9, 1, 0, 1, 3, 5, 6, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

