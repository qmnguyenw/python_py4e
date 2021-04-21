Python program to convert a list into a list of lists using a step value



Given a List, the task here is to write a python program that can split the
list into list of lists using by a step value here denoted via K.

>  **Input :** test_list = [5, 6, 3, 2, 7, 1, 9, 10, 8], K = 3
>
>  **Output :** [[5, 2, 9], [6, 7, 10], [3, 1, 8]]
>
>  **Explanation :** 5, 2 and 9 are 0th, 3rd and 6th element respectively, and
> hence ( difference 3 ) grouped together.
>
>  **Input :** test_list = [5, 6, 3, 2, 7, 1], K = 3
>
>  
>
>
>  
>
>
>  **Output :** [[5, 2], [6, 7], [3, 1]]
>
>  **Explanation :** 5 and 2 are 0th and 3rd element respectively, and hence (
> difference 3 ) grouped together.

 **Method 1 :** _Using_ _loop_ _and_ _slicing_

In this, loop is employed to skip numbers as required, and each subsequent
skipped sliced list is extracted using slicing and is appended to result.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [5, 6, 3, 2, 7, 1, 9, 10,
8]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing skips

K = 3

 

res = []

for idx in range(0, K):

 

 # 3rd arg. of slicing skips by K

 res.append(test_list[idx::K])

 

# printing result

print("Stepped splitted List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [5, 6, 3, 2, 7, 1, 9, 10, 8]
>
> Stepped splitted List : [[5, 2, 9], [6, 7, 10], [3, 1, 8]]
>
>  
>
>
>  
>

 **Method 2 :** _Using_ _list comprehension_ _and_ _slicing_

Similar to above method, only difference being usage of list comprehension for
task of iteration instead of loop for shorthand alternative.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [5, 6, 3, 2, 7, 1, 9, 10,
8]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing skips

K = 3

 

# list comprehension used as one liner

res = [test_list[idx::K] for idx in range(0, K)]

 

# printing result

print("Stepped splitted List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [5, 6, 3, 2, 7, 1, 9, 10, 8]
>
> Stepped splitted List : [[5, 2, 9], [6, 7, 10], [3, 1, 8]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

