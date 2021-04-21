Python – Test if all rows contain any common element with other Matrix



Given two Matrices, check if all rows contain at least one element common with
the same index row of other Matrix.

>  **Input** : test_list1 = [[5, 6, 1], [2, 4], [9, 3, 5]], test_list2 = [[9,
> 1, 2], [9, 8, 2], [3, 7, 10]]  
> **Output** : True  
> **Explanation** : 1, 2 and 3 are common elements in rows.
>
>  **Input** : test_list1 = [[5, 6, 1], [2, 4], [9, 2, 6]], test_list2 = [[9,
> 1, 2], [9, 8, 2], [3, 7, 6]]  
> **Output** : True  
> **Explanation** : 1, 2 and 6 are common elements in rows.  
>

**Method #1 : Using loop + in operator**

In this, we iterate each row of matrix, and check for any element matching in
other list using in operator, if any element is found, we mark it true, if all
rows are true, True is returned.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if all rows contain any common element with other Matrix

# Using loop "+" in operator

 

# initializing lists

test_list1 = [[5, 6, 1], [2, 4], [9, 3,
5]]

test_list2 = [[9, 1, 2], [9, 8, 2], [3,
7, 10]]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

res = True

for idx in range(0, len(test_list1)):

 

 temp = False

 

 # checking for any common element in 2nd list

 for ele in test_list1[idx]:

 if ele in test_list2[idx]:

 temp = True

 break

 

 # if any element not found, Result is false 

 if not temp :

 res = False

 break

 

# printing result 

print("All row contain commmon elements with other Matrix : " +
str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list 1 is : [[5, 6, 1], [2, 4], [9, 3, 5]]
    The original list 2 is : [[9, 1, 2], [9, 8, 2], [3, 7, 10]]
    All row contain commmon elements with other Matrix : True
    

**Method #2 : Using any() + loop**

In this, one nested loop is avoided and the result is computed using any() for
getting any common element in the 2nd Matrix.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if all rows contain any common element with other Matrix

# Using loop any() "+" loop

 

# initializing lists

test_list1 = [[5, 6, 1], [2, 4], [9, 3,
5]]

test_list2 = [[9, 1, 2], [9, 8, 2], [3,
7, 10]]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

res = True

for idx in range(0, len(test_list1)):

 

 # checking for common element in list 2 in same index

 temp = any(ele in test_list2[idx] for ele in
test_list1[idx])

 

 # if any element not found, Result is false 

 if not temp :

 res = False

 break

 

# printing result 

print("All row contain commmon elements with other Matrix : " +
str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list 1 is : [[5, 6, 1], [2, 4], [9, 3, 5]]
    The original list 2 is : [[9, 1, 2], [9, 8, 2], [3, 7, 10]]
    All row contain commmon elements with other Matrix : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

