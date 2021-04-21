Python – Accessing K element in set without deletion



In this article given a set(), the task is to write a Python program to access
an element K, without performing deletion using pop().

 **Example:**

    
    
     **Input :** test_set = {6, 4, 2, 7, 9}, K = 7
    **Output :** 3
    **Explanation :** 7 occurs in 3rd index in set.
    
    **Input :** test_set = {6, 4, 2, 7, 9}, K = 9
    **Output :** 4
    **Explanation :** 9 occurs in 4th index in set.

 **Method #1 : Using loop**

The most generic method is to perform iteration using loop, and if K is found,
print the element, and if required index.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Accessing K element in set without deletion

# Using loop

 

# initializing set

test_set = {6, 4, 2, 7, 9}

 

# printing original set

print("The original set is : " + str(test_set))

 

# initializing K

K = 7

 

res = -1

for ele in test_set:

 

 # checking for K element

 res += 1

 if ele == K:

 break

 

# printing result

print("Position of K in set : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original set is : {2, 4, 6, 7, 9}
    Position of K in set : 3

 **Method #2 : Using** **next()** **+** **iter()**

In this, container is converted to iterator and next() is used to increment
the position pointer, when element is found, we break from loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Accessing K element in set without deletion

# Using next() + iter()

 

# initializing set

test_set = {6, 4, 2, 7, 9}

 

# printing original set

print("The original set is : " + str(test_set))

 

# initializing K

K = 7

 

set_iter = iter(test_set)

for idx in range(len(test_set)):

 

 # incrementing position

 ele = next(set_iter)

 if ele == K:

 break

 

# printing result

print("Position of K in set : " + str(idx))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original set is : {2, 4, 6, 7, 9}
    Position of K in set : 3

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

