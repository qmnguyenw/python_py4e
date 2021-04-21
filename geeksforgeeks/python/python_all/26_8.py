Python – Extract tuples having K digit elements



Given a list of tuples, extract all tuples having K digit elements.

>  **Input** : test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )], K
> = 2  
> **Output** : [(34, 55), (12, 45), (78,)]  
> **Explanation** : All tuples have numbers with 2 digits.
>
>  **Input** : test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (782, )],
> K = 3  
> **Output** : [(782,)]  
> **Explanation** : All tuples have numbers with 3 digits.

**Method #1 : Using** **all()** **+** **list comprehension**

In this, we check for each element being of K digit by converting to string
and checking its length. The all() is used to check if all elements are of
similar size.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract K digit Elements Tuples

# Using all() + list comprehension

 

# initializing list

test_list = [(54, 2), (34, 55), (222, 23),
(12, 45), (78, )]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

# using len() and str() to check length and 

# perform string conversion

res = [sub for sub in test_list if
all(len(str(ele)) == K for ele in sub)]

 

# printing result

print("The Extracted tuples : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(54, 2), (34, 55), (222, 23), (12, 45), (78,)]  
> The Extracted tuples : [(34, 55), (12, 45), (78,)]

 **Method #2 : Using all() + filter() + lambda**

This is similar to above method, difference being filter() and lambda is used
to solve problem of filtering.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract K digit Elements Tuples

# Using all() + filter() + lambda

 

# initializing list

test_list = [(54, 2), (34, 55), (222, 23),
(12, 45), (78, )]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

# filter() and lambda used for task of filtering

res = list(filter(lambda sub: all(len(str(ele))
== K for ele in sub), test_list))

 

# printing result

print("The Extracted tuples : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(54, 2), (34, 55), (222, 23), (12, 45), (78,)]  
> The Extracted tuples : [(34, 55), (12, 45), (78,)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

