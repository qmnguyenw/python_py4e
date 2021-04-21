Python – Alternate elements Similarity



Given list of elements, check if all the alternate elements are equal to K.

>  **Input** : test_list = [5, 3, 5, 2, 5, 8, 9], K = 5  
>  **Output** : False  
>  **Explanation** : 9 != 5, hence False.
>
>  **Input** : test_list = [4, 3, 4, 2, 4], K = 4  
>  **Output** : True  
>  **Explanation** : All alternates equal to 4.

 **Method #1 : Using loop**

This is brute way to solution to this problem. In this, iterate for each
element in list and check for each element if they are equal to K.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate elements Similarity

# Using loop

 

# initializing lists

test_list = [5, 3, 5, 2, 5, 8, 5]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 5

 

# using flag to Flag false if any one element is not K 

# using loop to check for each element

res = True

for idx, ele in enumerate(test_list):

 if not idx % 2 and ele != K: 

 res = False

 break

 

# printing result 

print("Are all alternate elements equal to K : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [5, 3, 5, 2, 5, 8, 5]
    Are all alternate elements equal to K : True
    

**Method #2 : Using all() + generator expression**

This is yet another way in which this task can be performed. In this, we check
for all elements using all() and generator expression is used for condition
check and iteration.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate elements Similarity

# Using all() + generator expression

 

# initializing lists

test_list = [5, 3, 5, 2, 5, 8, 5]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 5

 

# all() to encapsulate whole logic into one expression

res = all(test_list[idx] == K for idx in range(0,
len(test_list), 2))

 

# printing result 

print("Are all alternate elements equal to K : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [5, 3, 5, 2, 5, 8, 5]
    Are all alternate elements equal to K : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

