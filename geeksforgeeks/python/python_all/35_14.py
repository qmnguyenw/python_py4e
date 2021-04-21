Python program to find Tuples with positive elements in List of tuples



Given a list of tuples. The task is to get all the tuples that have all
positive elements.

 **Examples:**

>  **Input** : test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)]  
> **Output** : [(4, 5, 9)]  
> **Explanation** : Extracted tuples with all positive elements.
>
>  **Input** : test_list = [(-4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)]  
> **Output** : []  
> **Explanation** : No tuple with all positive elements.

**Method #1 : Using list comprehension + all()**

  

  

In this, all() is used to check for all the tuples, list comprehension helps
in the iteration of tuples.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Positive Tuples in List

# Using list comprehension + all()

 

# initializing list

test_list = [(4, 5, 9), (-3, 2, 3), (-3,
5, 6), (4, 6)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# all() to check each element

res = [sub for sub in test_list if all(ele >= 0 for
ele in sub)]

 

# printing result

print("Positive elements Tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list is : [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]  
> Positive elements Tuples : [(4, 5, 9), (4, 6)]

 **Method #2 : Using filter() + lambda + all()**

In this, the task of filteration is performed using filter() and lambda
function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Positive Tuples in List

# Using filter() + lambda + all()

 

# initializing list

test_list = [(4, 5, 9), (-3, 2, 3), (-3,
5, 6), (4, 6)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# all() to check each element

res = list(filter(lambda sub: all(ele >= 0 for ele
in sub), test_list))

 

# printing result

print("Positive elements Tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list is : [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]  
> Positive elements Tuples : [(4, 5, 9), (4, 6)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

