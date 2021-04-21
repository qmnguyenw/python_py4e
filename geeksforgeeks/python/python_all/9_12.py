Python Program to Remove First Diagonal Elements from a Square Matrix



Given a square matrix of N*N dimension, the task is to write a Python program
to remove the first diagonal.

 **Examples:**

>  **Input :** test_list = [[5, 3, 3, 2, 1], [5, 6, 7, 8, 2], [9, 3, 4, 6, 7],
> [0, 1, 2, 3, 5], [2, 5, 4, 3, 5]]
>
>  **Output :** [[3, 3, 2, 1], [5, 7, 8, 2], [9, 3, 6, 7], [0, 1, 2, 5], [2,
> 5, 4, 3]]
>
>  **Explanation :** Removed 5, 6, 4, 3, 5 from lists, 1st diagonals.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [[5, 3, 3, 2], [5, 6, 7, 8], [9, 3, 4, 6], [0, 1,
> 2, 3]]
>
>  **Output :** [[3, 3, 2], [5, 7, 8], [9, 3, 6], [0, 1, 2]]
>
>  **Explanation :** Removed 5, 6, 4, 3 from lists, 1st diagonals.

 **Method 1 :** _Using_ _loop_ _and_ _enumerate()_

In this we iterate through each row using loop, and compare index of element
with row number, if found equal, the element is omitted.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[5, 3, 3, 2, 1], [5, 6, 7,
8, 2], [

 9, 3, 4, 6, 7], [0, 1, 2, 3, 5],
[2, 5, 4, 3, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for idx, ele in enumerate(test_list):

 

 # removing element whose index is equal to row index

 res.append([el for idxx, el in enumerate(ele) if idxx !=
idx])

 

# printing result

print("Filtered Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[5, 3, 3, 2, 1], [5, 6, 7, 8, 2], [9, 3, 4, 6, 7],
> [0, 1, 2, 3, 5], [2, 5, 4, 3, 5]]
>
>  
>
>
>  
>
>
> Filtered Matrix : [[3, 3, 2, 1], [5, 7, 8, 2], [9, 3, 6, 7], [0, 1, 2, 5],
> [2, 5, 4, 3]]

 **Method 2 :** _Using_ _list comprehension_ _and_ _enumerate()_

In this, we perform task of iteration using list comprehension, providing one
liner solution to above method.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[5, 3, 3, 2, 1], [5, 6, 7,
8, 2], [

 9, 3, 4, 6, 7], [0, 1, 2, 3, 5],
[2, 5, 4, 3, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# list comprehension to perform task as one liner

res = [[el for idxx, el in enumerate(ele) if idxx !=
idx]

 for idx, ele in enumerate(test_list)]

 

# printing result

print("Filtered Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[5, 3, 3, 2, 1], [5, 6, 7, 8, 2], [9, 3, 4, 6, 7],
> [0, 1, 2, 3, 5], [2, 5, 4, 3, 5]]
>
> Filtered Matrix : [[3, 3, 2, 1], [5, 7, 8, 2], [9, 3, 6, 7], [0, 1, 2, 5],
> [2, 5, 4, 3]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

