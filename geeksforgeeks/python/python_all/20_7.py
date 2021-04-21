Python progran to extract rows with common difference elements



Given a Matrix, extract rows with AP sequence.

>  **Input** : test_list = [[4, 7, 10], [8, 10, 12], [10, 11, 13], [6, 8, 10]]  
> **Output** : [[4, 7, 10], [8, 10, 12], [6, 8, 10]]  
> **Explanation** : 3, 4, and 2 are common difference in AP.
>
>  **Input** : test_list = [[4, 7, 10], [8, 10, 13], [10, 11, 13], [6, 8, 10]]  
> **Output** : [[4, 7, 10], [6, 8, 10]]  
> **Explanation** : 3 and 2 are common difference in AP.

**Method #1: Using loop**

In this, we check for all the elements having a common difference using a
loop, if any element not found to be in sync, then the row is flagged off and
not added to the result.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract rows with common difference elements

# Using loop

 

# initializing list

test_list = [[4, 7, 10],

 [8, 10, 12],

 [10, 11, 13], 

 [6, 8, 10]]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for row in test_list:

 flag = True

 for idx in range(0, len(row) - 1):

 

 # check for common difference

 if row[idx + 1] - row[idx] != row[1] -
row[0]:

 flag = False

 break

 if flag :

 res.append(row)

 

# printing result 

print("Filtered Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 7, 10], [8, 10, 12], [10, 11, 13], [6, 8, 10]]  
> Filtered Matrix : [[4, 7, 10], [8, 10, 12], [6, 8, 10]]

 **Method #2: Using all() + list comprehension**

In this, we check for all values to have common difference using all(), list
comprehension is used to perform an iteration of rows.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# all() + list comprehension

# Using list comprehension + all()

 

# initializing list

test_list = [[4, 7, 10],

 [8, 10, 12],

 [10, 11, 13], 

 [6, 8, 10]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking for all values to have common difference 

res = [row for row in test_list

 if all(row[idx + 1] - row[idx] == row[1] -
row[0]

 for idx in range(0, len(row) - 1))]

 

# printing result 

print("Filtered Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 7, 10], [8, 10, 12], [10, 11, 13], [6, 8, 10]]  
> Filtered Matrix : [[4, 7, 10], [8, 10, 12], [6, 8, 10]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

