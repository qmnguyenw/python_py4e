Python – Extend consecutive tuples



Given list of tuples, join consecutive tuples.

>  **Input** : test_list = [(3, 5, 6, 7), (3, 2, 4, 3), (9, 4), (2, 3, 2)]  
>  **Output** : [(3, 5, 6, 7, 3, 2, 4, 3), (3, 2, 4, 3, 9, 4), (9, 4, 2, 3,
> 2)]  
>  **Explanation** : Elements joined with their consecutive tuples.
>
>  **Input** : test_list = [(3, 5, 6, 7), (3, 2, 4, 3)]  
>  **Output** : [(3, 5, 6, 7, 3, 2, 4, 3)]  
>  **Explanation** : Elements joined with their consecutive tuples.

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this, we perform
task of joining consecution by access inside loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extend consecutive tuples

# Using loop

 

# initializing list

test_list = [(3, 5, 6, 7), (3, 2, 4, 3),
(9, 4), (2, 3, 2), (3, ), (3, 6)]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for idx in range(len(test_list) - 1):

 

 # joining tuples

 res.append(test_list[idx] + test_list[idx + 1])

 

# printing results

print("Joined tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(3, 5, 6, 7), (3, 2, 4, 3), (9, 4), (2, 3, 2), (3, ), (3, 6)]
    Joined tuples : [(3, 5, 6, 7, 3, 2, 4, 3), (3, 2, 4, 3, 9, 4), (9, 4, 2, 3, 2), (2, 3, 2, 3), (3, 3, 6)]
    

**Method #2 : Using zip() + list comprehension**

In this, we construct consecutive list using zip() and slicing and then form
pairs accordingly.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extend consecutive tuples

# Using zip() + list comprehension

 

# initializing list

test_list = [(3, 5, 6, 7), (3, 2, 4, 3),
(9, 4), (2, 3, 2), (3, ), (3, 6)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# zip to combine consecutive elements 

res = [a + b for a, b in zip(test_list,
test_list[1:])]

 

# printing results

print("Joined tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(3, 5, 6, 7), (3, 2, 4, 3), (9, 4), (2, 3, 2), (3, ), (3, 6)]
    Joined tuples : [(3, 5, 6, 7, 3, 2, 4, 3), (3, 2, 4, 3, 9, 4), (9, 4, 2, 3, 2), (2, 3, 2, 3), (3, 3, 6)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

