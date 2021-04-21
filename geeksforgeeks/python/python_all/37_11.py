Python – Extract tuples with elements in Range



Given list of tuples, extract tuples having elements in range.

>  **Input** : test_list = [(4, 5, 7), (5, 6), (3, 8, 10 ), (4, 10)], strt,
> end = 5, 6  
>  **Output** : [(5, 6)]  
>  **Explanation** : Only 1 tuple lies in range of 5-6.
>
>  **Input** : test_list = [(4, 5, 7), (5, 6), (3, 8, 10 ), (4, 10)], strt,
> end = 1, 10  
>  **Output** : [(4, 5, 7), (5, 6), (3, 8, 10 ), (4, 10)]  
>  **Explanation** : All lie in specified range.

 **Method #1 : Using list comprehension + all()**

In this, we check for all elements in range using comparison operator and
all() returns true for tuples that contain tuples in range specified.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract tuples with elements in Range

# Using all() + list comprehension

 

# initializing list

test_list = [(4, 5, 7), (5, 6), (3, 8, 10
), (4, 10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range 

strt, end = 4, 7

 

# list comprehension to encapsulate in 1 liner 

# all() checks for all elements in range 

res = [sub for sub in test_list if all(ele >= strt
and ele <= end for ele in sub)]

 

# printing results

print("Filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(4, 5, 7), (5, 6), (3, 8, 10), (4, 10)]
    Filtered tuples : [(4, 5, 7), (5, 6)]
    

**Method #2 : Using filter() + lambda + all()**

In this, we employ filter() to extract out tuples, according to function
provided by lambda, and all() as utility to test for all elements in range
tuple.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract tuples with elements in Range

# Using filter() + lambda + all() 

 

# initializing list

test_list = [(4, 5, 7), (5, 6), (3, 8, 10
), (4, 10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range 

strt, end = 4, 7

 

# list() to get back result as list 

# all() checks for all elements in range 

res = list(filter(lambda sub : all(ele >= strt and
ele <= end for ele in sub), test_list))

 

# printing results

print("Filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(4, 5, 7), (5, 6), (3, 8, 10), (4, 10)]
    Filtered tuples : [(4, 5, 7), (5, 6)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

