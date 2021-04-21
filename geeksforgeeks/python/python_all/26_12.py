Python – Extract element from list succeeded by K



Given a list, extract the elements which are having K as the next element.

>  **Input** : test_list = [2, 3, 5, 7, 8, 5, 3, 5], K = 3  
> **Output** : [2, 5]  
> **Explanation** : Elements before 3 are 2, 5.
>
>  **Input** : test_list = [2, 3, 5, 7, 8, 5, 3, 8], K = 8  
> **Output** : [7, 3]  
> **Explanation** : Elements before 8 are 7, 3.

**Method #1: Using loop**

In this, we iterate the list and look for each K, and extract the element
preceding it.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract elements succeeded by K

# Using loop

 

# initializing list

test_list = [2, 3, 5, 7, 8, 5, 3, 5]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 5

 

# Using loop to extract elements succeeded by K

res = []

for idx in range(len(test_list) - 1):

 

 # checking for succession

 if test_list[idx + 1] == K:

 res.append(test_list[idx])

 

# printing result

print("Extracted elements list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [2, 3, 5, 7, 8, 5, 3, 5]
    Extracted elements list : [3, 8, 3]
    

**Method #2: Using** **list comprehension**

Another way to solve this question, in this, we use list comprehension as
shorthand to solve the problem of getting elements.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract elements succeeded by K

# Using list comprehension

 

# initializing list

test_list = [2, 3, 5, 7, 8, 5, 3, 5]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 5

 

# List comprehension used as shorthand

res = [test_list[idx]

 for idx in range(len(test_list) - 1) if
test_list[idx + 1] == K]

 

# printing result

print("Extracted elements list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [2, 3, 5, 7, 8, 5, 3, 5]
    Extracted elements list : [3, 8, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

