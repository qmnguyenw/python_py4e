Python Program to convert a list into matrix with size of each row increasing
by a number



Given a list and a number N, the task here is to write a python program to
convert it to matrix where each row has N elements more than previous row
elements from list.

>  **Input :** test_list = [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1], N = 3
>
>  **Output :** [[4, 6, 8], [4, 6, 8, 1, 2, 9], [4, 6, 8, 1, 2, 9, 0, 10, 12],
> [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1]]
>
>  **Explanation** : Each row has 3 elements more than previous row.
>
>  **Input :** test_list = [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1], N = 4
>
>  
>
>
>  
>
>
>  **Output :** [[4, 6, 8, 1], [4, 6, 8, 1, 2, 9, 0, 10], [4, 6, 8, 1, 2, 9,
> 0, 10, 12, 3, 9, 1]]
>
>  **Explanation :** Each row has 4 elements more than previous row.

 **Method 1 :** _Using_ _loop_ _and_ _slicing_

In this, we perform task of getting chunks using slicing, and conversion of
list into Matrix is done using loop.

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

test_list = [4, 6, 8, 1, 2, 9, 0, 10,
12, 3, 9, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing N

N = 3

 

res = []

for idx in range(0, len(test_list) // N):

 

 # getting incremented chunks

 res.append(test_list[0: (idx + 1) * N])

 

# printing result

print("Constructed Chunk Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1]
>
> Constructed Chunk Matrix : [[4, 6, 8], [4, 6, 8, 1, 2, 9], [4, 6, 8, 1, 2,
> 9, 0, 10, 12], [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1]]
>
>  
>
>
>  
>

 **Method 2 :** _Using_ _list comprehension and list slicing_

In this, we perform task of setting values using list comprehension as a
shorthand. Rest all the operations are done similar to above method.

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

test_list = [4, 6, 8, 1, 2, 9, 0, 10,
12, 3, 9, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing N

N = 3

 

# getting incremented chunks

# using list comprehension as shorthand

res = [test_list[0: (idx + 1) * N] for idx in
range(0, len(test_list) // N)]

 

# printing result

print("Constructed Chunk Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1]
>
> Constructed Chunk Matrix : [[4, 6, 8], [4, 6, 8, 1, 2, 9], [4, 6, 8, 1, 2,
> 9, 0, 10, 12], [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

