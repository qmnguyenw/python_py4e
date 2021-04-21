Python – K list Nested Dictionary Mesh



Given 2 lists, create nested mesh with constant List.

>  **Input** : test_list1 = [4, 6], test_list2 = [2, 7], K = []  
>  **Output** : {4: {2: [], 7: []}, 6: {2: [], 7: []}}  
>  **Explanation** : Nested dictionary initialized with [].
>
>  **Input** : test_list1 = [4], test_list2 = [2], K = [1]  
>  **Output** : {4: {2: [1]}}  
>  **Explanation** : Nested dictionary initialized with [1].

 **Method : Using dictionary comprehension**

In this, we use nested dictionary comprehension, inner one for list 2 elements
to each element of list 1 as key and outer to assign keys from list 1.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K list Nested Dictionary Mesh

# Using * operator

 

# initializing lists

test_list1 = [4, 6, 8, 7]

test_list2 = [2, 7, 9, 4]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# initializing K 

K = [None]

 

# initializing K list mesh

res = {idx: {sub2: K for sub2 in test_list2} for idx in
test_list1}

 

# printing result 

print("Created Mesh : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [4, 6, 8, 7]
    The original list 2 : [2, 7, 9, 4]
    Created Mesh : {4: {2: [None], 7: [None], 9: [None], 4: [None]}, 6: {2: [None], 7: [None], 9: [None], 4: [None]}, 8: {2: [None], 7: [None], 9: [None], 4: [None]}, 7: {2: [None], 7: [None], 9: [None], 4: [None]}}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

