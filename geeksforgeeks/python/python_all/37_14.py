Python – Filter Tuple with Elements capped on K



Given a List of Tuples, extract tuples in which each element is max K.

>  **Input** : test_list = [(4, 5, 3), (3, 4, 7), (4, 3, 2), (4, 7, 8)], K = 7  
>  **Output** : [(4, 5, 3), (3, 4, 7), (4, 3, 2)]  
>  **Explanation** : All tuples have maximum value 7.
>
>  **Input** : test_list = [(4, 5, 3), (4, 3, 2), (4, 7, 8)], K = 7  
>  **Output** : [(4, 5, 3), (4, 3, 2)]  
>  **Explanation** : All tuples have maximum value 7.

 **Method #1 : Using loop**

In this, we iterate through all tuple elements, if element found greater than
K, then tuple is flagged and not added in result list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Tuple with Elements capped on K

# Using loop

 

# initializing list

test_list = [(4, 5, 3), (3, 4, 7), (4, 3,
2), (4, 7, 8)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 5

 

res_list = []

for sub in test_list:

 res = True

 for ele in sub:

 

 # check if any element is greater than K

 if ele > K :

 res = False

 break

 if res:

 res_list.append(sub)

 

# printing result 

print("The filtered tuples : " + str(res_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(4, 5, 3), (3, 4, 7), (4, 3, 2), (4, 7, 8)]
    The filtered tuples : [(4, 5, 3), (4, 3, 2)]
    

**Method #2 : Using all() + list comprehension**

In this, we check for all the elements to be at max K using all(), if yes,
then those tuples are added to result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Tuple with Elements capped on K

# Using all() + list comprehension

 

# initializing list

test_list = [(4, 5, 3), (3, 4, 7), (4, 3,
2), (4, 7, 8)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 5

 

# using all() to check for each tuple being in K limit

res = [sub for sub in test_list if all(ele <= K for
ele in sub)]

 

# printing result 

print("The filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(4, 5, 3), (3, 4, 7), (4, 3, 2), (4, 7, 8)]
    The filtered tuples : [(4, 5, 3), (4, 3, 2)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

