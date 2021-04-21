Python – Find starting index of all Nested Lists



In this article given a matrix, the task is to write a Python program to
compute the starting index of all the nested lists.

 **Example:**

>  **Input :** test_list = [[5], [9, 3, 1, 4], [3, 2], [4, 7, 8, 3, 1, 2], [3,
> 4, 5]]
>
>  **Output :** [0, 1, 5, 7, 13]
>
>  **Explanation :** 1 + 4 = lengths of 2 initial lists = 5, 3, of 3rd list
> start from 5th index [ 0 based indexing ],
>
>  
>
>
>  
>
>
> hence 5. as 3rd element in result list.
>
>  **Input :** test_list = [[5], [9, 3, 1, 4], [3, 2], [3, 4, 5]]
>
>  **Output :** [0, 1, 5, 7]
>
>  **Explanation :** 1 + 4 = lengths of 2 initial lists = 5, 3, of 3rd list
> start from 5th index [ 0 based indexing ],
>
> hence 5. as 3rd element in result list.

 **Method #1 : Using loop +** **len()**

In this, length of each sublist is computed using len() and summed,
cumulatively, and added as intermediate result. The initial index is
derivative of lengths of sublists.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initial element index in Matrix

# Using loop

 

# initializing list

test_list = [[5], [9, 3, 1, 4], [3, 2],
[4, 7, 8, 3, 1, 2], [3, 4, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

lens = 0

for sub in test_list:

 

 # lengths of sublist computed

 res.append(lens)

 lens += len(sub)

 

# printing result

print("Initial element indices : " + str(res))  
  
---  
  
 __

 __

