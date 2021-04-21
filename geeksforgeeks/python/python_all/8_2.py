Python – Convert List to custom overlapping nested list



Given a list, the task is to write a Python program to convert it into a
custom overlapping nested list based on element size and overlap step.

 **Examples:**

>  **Input:** test_list = [3, 5, 6, 7, 3, 9, 1, 10], step, size = 2, 4
>
>  **Output:** [[3, 5, 6, 7], [6, 7, 3, 9], [3, 9, 1, 10], [1, 10]]
>
>  **Explanation:** Rows sliced for size 4, and overcoming started after 2
> elements of current row.
>
>  
>
>
>  
>
>
>  **Input:** test_list = [3, 5, 6, 7, 3, 9, 1, 10], step, size = 2, 3
>
>  **Output:** [[3, 5, 6], [6, 7, 3], [3, 9, 1], [1, 10]]
>
>  **Explanation:** Rows sliced for size 3, and overcoming started after 2
> elements of current row.

 **Method #1: Using** **list slicing** **+** **loop**

In this, row size is managed by slicing operation and overlap step is managed
by step mentioned in range() while using a loop for iteration.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert List to custom overlapping Matrix

# Using list slicing + loop

 

# initializing list

test_list = [3, 5, 6, 7, 3, 9, 1, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing step, size

step, size = 2, 4

 

res = []

for idx in range(0, len(test_list), step):

 

 # slicing list

 res.append(test_list[idx: idx + size])

 

# printing result

print("The created Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [3, 5, 6, 7, 3, 9, 1, 10]
>
> The created Matrix : [[3, 5, 6, 7], [6, 7, 3, 9], [3, 9, 1, 10], [1, 10]]
>
>  
>
>
>  
>

 **Method #2: Using** **list comprehension**

In this, similar functionality as the above method is used with a variation of
having shorthand using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert List to custom overlapping Matrix

# Using list comprehension

 

# initializing list

test_list = [3, 5, 6, 7, 3, 9, 1, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing step, size

step, size = 2, 4

 

# list comprehension used as shorthand to solve problem

res = [test_list[idx: idx + size] for idx in range(0, 

 len(test_list), 

 step)]

 

# printing result

print("The created Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [3, 5, 6, 7, 3, 9, 1, 10]
>
> The created Matrix : [[3, 5, 6, 7], [6, 7, 3, 9], [3, 9, 1, 10], [1, 10]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

