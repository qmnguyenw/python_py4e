Python – Trim tuples by K



Given the Tuple list, trim each tuple by K.

 **Examples:**

>  **Input** : test_list = [(5, 3, 2, 1, 4), (3, 4, 9, 2, 1), (9, 1, 2, 3, 5),
> (4, 8, 2, 1, 7)], K = 2  
> **Output** : [(2,), (9,), (2,), (2,)]  
> **Explanation** : 2 elements each from front and rear are removed.  
>
>
> **Input** : test_list = [(5, 3, 2, 1, 4), (3, 4, 9, 2, 1), (9, 1, 2, 3, 5),
> (4, 8, 2, 1, 7)], K = 1  
> **Output** : [(3, 2, 1), (4, 9, 2), (1, 2, 3), (8, 2, 1)]  
> **Explanation** : 1 element each from front and rear are removed.

**Method #1: Using loop + slicing**

  

  

In this, we omit front and rear K elements by using slicing, converting tuple
to list, then reconversion to the tuple.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Trim tuples by K

# Using loop + slicing

 

# initializing list

test_list = [(5, 3, 2, 1, 4), (3, 4, 9,
2, 1),

 (9, 1, 2, 3, 5), (4, 8, 2, 1, 7)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

res = []

for ele in test_list:

 N = len(ele)

 

 # triming elements

 res.append(tuple(list(ele)[K: N - K]))

 

# printing result

print("Converted Tuples : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(5, 3, 2, 1, 4), (3, 4, 9, 2, 1), (9, 1, 2, 3, 5),
> (4, 8, 2, 1, 7)]  
> Converted Tuples : [(2,), (9,), (2,), (2,)]

 **Method #2: Using** **list comprehension + slicing** ****

In this, we perform tasks in a similar way as the above method, difference
being list comprehension is employed to perform the task in one-liner.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Trim tuples by K

# Using list comprehension + slicing

 

# initializing list

test_list = [(5, 3, 2, 1, 4), (3, 4, 9,
2, 1),

 (9, 1, 2, 3, 5), (4, 8, 2, 1, 7)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

# one-liner approach to solve problem

res = [tuple(list(ele)[K: len(ele) - K]) for ele
in test_list]

 

# printing result

print("Converted Tuples : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(5, 3, 2, 1, 4), (3, 4, 9, 2, 1), (9, 1, 2, 3, 5),
> (4, 8, 2, 1, 7)]  
> Converted Tuples : [(2,), (9,), (2,), (2,)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

