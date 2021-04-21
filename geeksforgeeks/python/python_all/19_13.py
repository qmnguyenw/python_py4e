Python – Rows with all List elements



Given a Matrix, get all the rows with all the list elements.

>  **Input** : test_list = [[7, 6, 3, 2], [5, 6], [2, 1, 8], [6, 1, 2]],
> sub_list = [1, 2]  
> **Output** : [[2, 1, 8], [6, 1, 2]]  
> **Explanation** : Extracted lists have 1 and 2.
>
>  **Input** : test_list = [[7, 6, 3, 2], [5, 6], [2, 1, 8], [6, 1, 2]],
> sub_list = [2, 6]  
> **Output** : [[7, 6, 3, 2], [6, 1, 2]]  
> **Explanation** : Extracted lists have 2 and 6.

 **Method #1: Using loop**

In this, we iterate for each row from Matrix, and check for presence of each
list element, if present row is returned as result. If any element is not
present, row is flagged off.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rows with all List elements

# Using loop

 

# initializing list

test_list = [[7, 6, 3, 2], [5, 6], [2, 1,
8], [6, 1, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing list

sub_list = [1, 2]

 

res = []

for row in test_list:

 

 flag = True

 

 # checking for all elements in list

 for ele in sub_list:

 if ele not in row:

 flag = False

 

 if flag:

 res.append(row)

 

# printing result

print("Rows with list elements : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[7, 6, 3, 2], [5, 6], [2, 1, 8], [6, 1, 2]]  
> Rows with list elements : [[2, 1, 8], [6, 1, 2]]

 **Method #2 : Using** **all()** **+** **list comprehension**

In this, all elements for presence as tested using all(), list comprehension
is used as a one-liner to perform the task of iterating through rows.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rows with all List elements

# Using all() + list comprehension

 

# initializing list

test_list = [[7, 6, 3, 2], [5, 6], [2, 1,
8], [6, 1, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing list 

sub_list = [1, 2]

 

# testing elements presence using all()

res = [row for row in test_list if all(ele in row
for ele in sub_list)]

 

# printing result 

print("Rows with list elements : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[7, 6, 3, 2], [5, 6], [2, 1, 8], [6, 1, 2]]  
> Rows with list elements : [[2, 1, 8], [6, 1, 2]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

