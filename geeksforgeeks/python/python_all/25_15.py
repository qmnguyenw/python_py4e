Python – Filter Rows with Range Elements



Given a Matrix, filter all the rows which contain all elements in the given
number range.

>  **Input** : test_list = [[3, 2, 4, 5, 10], [3, 2, 5, 19], [2, 5, 10], [2,
> 3, 4, 5, 6, 7]], i, j = 2, 5  
> **Output** : [[3, 2, 4, 5, 10], [2, 3, 4, 5, 6, 7]]  
> **Explanation** : 2, 3, 4, 5 all are present in above rows.
>
>  **Input** : test_list = [[3, 2, 4, 10], [3, 2, 5, 19], [2, 5, 10], [2, 3,
> 4, 5, 6, 7]], i, j = 2, 5  
> **Output** : [[2, 3, 4, 5, 6, 7]]  
> **Explanation** : 2, 3, 4, 5 all are present in above rows.  
>

**Method #1 : Using** **all()** **+** **list comprehension**

In this, we check for all the elements in range for presence using all() and
list comprehension is used for the task of iteration of elements.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Rows with Range Elements

# Using all() + list comprehension

 

# initializing list

test_list = [[3, 2, 4, 5, 10], [3, 2, 5,
19], 

 [2, 5, 10], [2, 3, 4, 5, 6, 7]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range

i, j = 2, 5

 

# checking for presence of all elements using in operator

res = [sub for sub in test_list if all(ele in sub
for ele in range(i, j + 1))]

 

# printing result

print("Extracted rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[3, 2, 4, 5, 10], [3, 2, 5, 19], [2, 5, 10], [2, 3,
> 4, 5, 6, 7]]  
> Extracted rows : [[3, 2, 4, 5, 10], [2, 3, 4, 5, 6, 7]]

 **Method #2 : Using** **filter()** **+** **lambda** **\+ all()**

In this, task of filtering is done using filter() and lambda function, all()
is again used to ensure all elements presence in range.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Rows with Range Elements

# Using filter() + lambda + all()

 

# initializing list

test_list = [[3, 2, 4, 5, 10], [3, 2, 5,
19],

 [2, 5, 10], [2, 3, 4, 5, 6, 7]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range

i, j = 2, 5

 

# filter() and lambda used to filter elements

res = list(filter(lambda sub: all(

 ele in sub for ele in range(i, j + 1)), test_list))

 

# printing result

print("Extracted rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[3, 2, 4, 5, 10], [3, 2, 5, 19], [2, 5, 10], [2, 3,
> 4, 5, 6, 7]]  
> Extracted rows : [[3, 2, 4, 5, 10], [2, 3, 4, 5, 6, 7]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

