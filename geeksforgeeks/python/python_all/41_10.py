Python – Check if List is K increasing



Given a List, check if next element is always x + K than current(x).

>  **Input** : test_list = [3, 7, 11, 15, 19, 23], K = 4  
>  **Output** : True  
>  **Explanation** : Subsequent element difference is 4.
>
>  **Input** : test_list = [3, 7, 11, 12, 19, 23], K = 4  
>  **Output** : False  
>  **Explanation** : 12 – 11 = 1, which is not 4, hence False

 **Method #1 : Using loop**

In this, we iterate for each element of list, and check if element is not K
increasing, if found, the result is flagged false and returned.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if List is K increasing

# Using loop

 

# initializing list

test_list = [4, 7, 10, 13, 16, 19]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

res = True

for idx in range(len(test_list) - 1):

 

 # flagging if not found

 if test_list[idx + 1] != test_list[idx] + K:

 res = False

 

# printing results

print("Is list K increasing ? : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 7, 10, 13, 16, 19]
    Is list K increasing ? : True
    

**Method #2 : Using all() + generator expression**

In this, we check for all the elements being K increasing using all(), and
generator expression is used for iteration.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if List is K increasing

# Using all() + generator expression

 

# initializing list

test_list = [4, 7, 10, 13, 16, 19]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# using all() to check for all elements

res = all(test_list[idx + 1] == test_list[idx] + K
for idx in range(len(test_list) - 1))

 

# printing results

print("Is list K increasing ? : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 7, 10, 13, 16, 19]
    Is list K increasing ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

