Python – Remove Tuples with difference greater than K



Given Dual Tuples List, remove pairs with difference greater than K.

>  **Input** : test_list = [(4, 8), (1, 7), (9, 12), (3, 12), (2, 10)], K = 6  
> **Output** : [(4, 8), (9, 12), (1, 7)]  
> **Explanation** : 4 (8 – 4), 3 (12 – 9) and 6 are all not greater than 6,
> hence retained.
>
>  **Input** : test_list = [(4, 8), (1, 7), (9, 12), (3, 12), (2, 10)], K = 3  
> **Output** : [(9, 12)]  
> **Explanation** : 3 (12 – 9) is not greater than 3, hence retained.

**Method #1 : Using list comprehension**

In this, we perform filtering by testing the absolute difference using _abs()_
, if found smaller than K, its retained, hence greater than K difference
tuples are removed.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Tuples with difference greater than K

# Using list comprehension

 

# initializing list

test_list = [(4, 8), (1, 7), (9, 12), (3,
12), (2, 10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 5

 

# filtering using list comprehension, checking for smaller than K diff.

res = [sub for sub in test_list if abs(sub[0] -
sub[1]) <= K]

 

# printing result

print("Tuples List after removal : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(4, 8), (1, 7), (9, 12), (3, 12), (2, 10)]  
> Tuples List after removal : [(4, 8), (9, 12)]

 **Method #2 : Using filter() + lambda + abs()**

In this, task of filtering is performed using _filter()_ and _lambda_
function, _abs()_ is used to get the absolute difference.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Tuples with difference greater than K

# Using filter() + lambda + abs()

 

# initializing list

test_list = [(4, 8), (1, 7), (9, 12), (3,
12), (2, 10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 5

 

# Using filter() and lambda function for filtering

res = list(filter(lambda sub: abs(sub[0] -
sub[1]) <= K, test_list))

 

# printing result

print("Tuples List after removal : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(4, 8), (1, 7), (9, 12), (3, 12), (2, 10)]  
> Tuples List after removal : [(4, 8), (9, 12)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

