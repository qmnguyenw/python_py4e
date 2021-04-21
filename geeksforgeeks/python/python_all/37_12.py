Python – Filter Tuples with All Even Elements



Given List of tuples, filter only those with all even elements.

>  **Input** : test_list = [(6, 4, 2, 8), (5, 6, 7, 6), (8, 1, 2), (7, )]  
>  **Output** : [(6, 4, 2, 8)]  
>  **Explanation** : Only 1 tuple with all even elements.
>
>  **Input** : test_list = [(6, 4, 2, 9), (5, 6, 7, 6), (8, 1, 2), (7, )]  
>  **Output** : []  
>  **Explanation** : No tuple with all even elements.

 **Method #1 : Using loop**

In this, we iterate each tuple, and check for all even elements using %
operator and if even one element is odd, tuple is flagged and not added in
result list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Tuples with All Even Elements

# Using loop

 

# initializing list

test_list = [(6, 4, 2, 8), (5, 6, 7, 6),
(8, 0, 2), (7, )]

 

# printing original list

print("The original list is : " + str(test_list))

 

res_list = []

for sub in test_list:

 res = True

 

 # check if all are even

 for ele in sub:

 if ele % 2 != 0:

 res = False

 break

 if res:

 res_list.append(sub)

 

# printing results

print("Filtered Tuples : " + str(res_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(6, 4, 2, 8), (5, 6, 7, 6), (8, 0, 2), (7, )]
    Filtered Tuples : [(6, 4, 2, 8), (8, 0, 2)]
    

**Method #2 : Using all() + list comprehension**

In this, the task of checking for all elements to be even is done using all(),
and list comprehension is used for task of filtering post checking.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Tuples with All Even Elements

# Using all() + list comprehension

 

# initializing list

test_list = [(6, 4, 2, 8), (5, 6, 7, 6),
(8, 0, 2), (7, )]

 

# printing original list

print("The original list is : " + str(test_list))

 

# testing for tuple to be even using all()

res = [sub for sub in test_list if all(ele % 2 ==
0 for ele in sub)]

 

# printing results

print("Filtered Tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(6, 4, 2, 8), (5, 6, 7, 6), (8, 0, 2), (7, )]
    Filtered Tuples : [(6, 4, 2, 8), (8, 0, 2)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

