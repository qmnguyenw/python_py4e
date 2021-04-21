Python – Check Similar elements in Matrix rows



Given a Matrix and list, the task is to write a Python program to check if all
the matrix elements of the row are similar to the ith index of List.

>  **Input** : test_list = [[1, 1, 1], [4, 4], [3, 3, 3], [5, 5, 5, 5]]  
> **Output** : True  
> **Explanation** : All rows have same elements.
>
>  **Input** : test_list = [[1, 1, 4], [4, 4], [3, 3, 3], [5, 5, 5, 5]]  
> **Output** : False  
> **Explanation** : All rows don’t have same elements.  
>

**Method #1 : Using** **loop**

In this, we iterate through each row and check for its similar number in the
list, if all the elements in a row are the same as an ith element in the List,
true is returned, else false.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Similar all elements as List in Matrix rows

# Using loop

 

# initializing Matrix

test_list = [[1, 1, 1], [4, 4],

 [3, 3, 3], [5, 5, 5, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing tar_list 

tar_list = [1, 4, 3, 5]

 

res = True

flag = 0

for idx in range(len(test_list)):

 for ele in test_list[idx]:

 

 # checking for row index 

 # equal to list index elements 

 if ele != tar_list[idx]:

 res = False

 flag = 1

 break

 

 if flag:

 break

 

# printing result

print("Are row index element similar\

 to list index element ? : " + str(res))  
  
---  
  
 __

 __

**Output:**

> The original list is : [[1, 1, 1], [4, 4], [3, 3, 3], [5, 5, 5, 5]]  
> Are row index element similar to list index element ? : True

 **Method #2 : Using all() +** **generator expression**

In this, we check for all elements to be equal using all(), and check for all
elements follow this pattern using all() again. The iteration of elements and
rows is done using generator expression.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Similar all elements as List in Matrix rows

# Using all() + generator expression

 

# initializing Matrix

test_list = [[1, 1, 1], [4, 4],

 [3, 3, 3], [5, 5, 5, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing tar_list 

tar_list = [1, 4, 3, 5]

 

# nested all() used to check each element and rows

res = all(all(ele == tar_list[idx] for ele in
test_list[idx])

 for idx in range(len(test_list)) )

 

# printing result

print("Are row index element\

 similar to list index element ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[1, 1, 1], [4, 4], [3, 3, 3], [5, 5, 5, 5]]  
> Are row index element similar to list index element ? : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

