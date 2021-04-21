Python – Test K in Range



Given a List, Test if all elements in given range is equal to K.

>  **Input** : test_list = [2, 3, 4, 4, 4, 4, 6, 7, 8, 2], i, j = 2, 5, K = 4  
> **Output** : True  
> **Explanation** : All elements in range are 4.
>
>  **Input** : test_list = [2, 3, 4, 9, 4, 4, 6, 7, 8, 2], i, j = 2, 5, K = 4  
> **Output** : False  
> **Explanation** : All elements in range are not 4.

**Method #1 : Using** **any()**

In this, we check for negation of logic to be found, check if we get any
element other than K, we return the negation of truth value to get actual
result.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test K in Range

# Using any()

 

# initializing list

test_list = [2, 3, 4, 4, 4, 4, 6, 7,
8, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Range

i, j = 2, 5

 

# initializing K 

K = 4

 

# any() to check if any element other than K present 

# negation gives result 

res = not any(test_list[idx] != K for idx in range(i, j
+ 1))

 

# printing result 

print("Are all elements in range K ? : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [2, 3, 4, 4, 4, 4, 6, 7, 8, 2]
    Are all elements in range K ? : True
    

**Method #2 : Using all()**

In this, we check for all elements to be K in required range of list using
all().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test K in Range

# Using all() 

 

# initializing list

test_list = [2, 3, 4, 4, 4, 4, 6, 7,
8, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Range

i, j = 2, 5

 

# initializing K 

K = 4

 

# all() to check all elements to be K 

res = all(test_list[idx] == K for idx in range(i, j
+ 1))

 

# printing result 

print("Are all elements in range K ? : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [2, 3, 4, 4, 4, 4, 6, 7, 8, 2]
    Are all elements in range K ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

