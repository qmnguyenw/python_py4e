Python – Filter rows with Elements as Multiple of K



Given a Matrix, extract rows with elements multiple of K.

>  **Input** : test_list = [[5, 10, 15], [4, 8, 12], [100, 15], [5, 10, 23]],
> K = 4  
> **Output** : [[4, 8, 12]]  
> **Explanation** : All are multiples of 4.
>
>  **Input** : test_list = [[5, 10, 15], [4, 8, 11], [100, 15], [5, 10, 23]],
> K = 4  
> **Output** : []  
> **Explanation** : No rows with all multiples of 4.

**Method #1 : Using list comprehension + all()**

In this, we check for all elements to be multiple using all(), and iteration
of rows occur using list comprehension.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Access element at Kth index in String

# Using list comprehension + all()

 

# initializing string list

test_list = [[5, 10, 15], [4, 8, 3], [100,
15], [5, 10, 23]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 5

 

res = [sub for sub in test_list if all(ele % K ==
0 for ele in sub)]

 

# printing result

print("Rows with K multiples : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list is : [[5, 10, 15], [4, 8, 3], [100, 15], [5, 10, 23]]  
> Rows with K multiples : [[5, 10, 15], [100, 15]]

 **Method #2 : Using filter() + lambda + all()**

In this, we perform task of filtering using filter() and lambda function and
task of checking for all elements in rows using all().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Access element at Kth index in String

# Using filter() + lambda + all()

 

# initializing string list

test_list = [[5, 10, 15], [4, 8, 3], [100,
15], [5, 10, 23]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 5

 

# using all() to check for all elements being multiples of K

res = list(filter(lambda sub : all(ele % K == 0
for ele in sub), test_list))

 

# printing result 

print("Rows with K multiples : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list is : [[5, 10, 15], [4, 8, 3], [100, 15], [5, 10, 23]]  
> Rows with K multiples : [[5, 10, 15], [100, 15]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

