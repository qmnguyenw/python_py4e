Python program to omit K length Rows



Given a Matrix, remove rows with length K.

>  **Input** : test_list = [[4, 7], [8, 10, 12, 8], [10, 11], [6, 8, 10]], K =
> 2  
> **Output** : [[8, 10, 12, 8], [6, 8, 10]]  
> **Explanation** : [4, 7] and [10, 11] omitted as length 2 rows.
>
>  **Input** : test_list = [[4, 7], [8, 10, 12, 8], [10, 11], [6, 8, 10]], K =
> 3  
> **Output** : [[4, 7], [8, 10, 12, 8], [10, 11]]  
> **Explanation** : [6, 8, 10] omitted as length 3 rows.  
>

**Method #1 : Using loop + len()**

In this, we check for the length of each row using len(), if found to be equal
to K, that row is omitted from Matrix.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Omit K length Rows

# Using loop + len()

 

# initializing list

test_list = [[4, 7],

 [8, 10, 12, 8],

 [10, 11], 

 [6, 8, 10]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

res = []

for row in test_list:

 

 # checking rows not K length

 if len(row) != K :

 res.append(row)

 

# printing result 

print("Filtered Matrix : " + str(res))  
  
---  
  
 __

 __

**Output:**

> The original list is : [[4, 7], [8, 10, 12, 8], [10, 11], [6, 8, 10]]  
> Filtered Matrix : [[8, 10, 12, 8], [6, 8, 10]]

 **Method #2 : Using filter() + lambda + len()**

In this, we use filter() to extract rows with lengths other than K. The lambda
function is used to render length computation logic.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Omit K length Rows

# Using filter() + lambda + len()

 

# initializing list

test_list = [[4, 7],

 [8, 10, 12, 8],

 [10, 11], 

 [6, 8, 10]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 4

 

# getting elements with length other than K 

res = list(filter(lambda row : len(row) != K,
test_list))

 

# printing result 

print("Filtered Matrix : " + str(res))  
  
---  
  
 __

 __

**Output:**

> The original list is : [[4, 7], [8, 10, 12, 8], [10, 11], [6, 8, 10]]  
> Filtered Matrix : [[4, 7], [10, 11], [6, 8, 10]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

