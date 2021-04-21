Python – Remove positional rows



Given a Matrix, the task is to write a Python program to remove rows that have
certain positions.

 **Example:**

    
    
     **Input:** test_list = [[3, 5, 2], [1, 8, 9], 
                    [5, 3, 1], [0, 1, 6], 
                [9, 4, 1], [1, 2, 10], 
                [0, 1, 2]]; idx_lis = [1, 2, 5]
    **Output:** [[3, 5, 2], [0, 1, 6], [9, 4, 1], [0, 1, 2]]
    **Explanation:** 1st, 2nd and 5th rows are removed.
    
    **Input:** test_list = [[3, 5, 2], [1, 8, 9], 
                 [5, 3, 1], [0, 1, 6], 
                 [9, 4, 1], [1, 2, 10], 
                 [0, 1, 2]]; idx_lis = [1, 3, 5]
    **Output:** [[3, 5, 2], [5, 3, 1], [9, 4, 1], [0, 1, 2]]
    **Explanation:** 1st, 3rd and 5th rows are removed.

 **Method #1 : Using** **loop** **+** **pop()** **+** **back iteration**

In this, removal is handled using pop(), and back iteration is necessary to
make sure due to rearrangement at deletion, the wrong positional row is not
removed.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove positional rows

# Using loop + pop() + back iteration

 

# initializing list

test_list = [[3, 5, 2], [1, 8, 9], [5, 3,
1], 

 [0, 1, 6], [9, 4, 1], [1, 2, 10], 

 [0, 1, 2]]

 

# printing original list

print("The original list is: " + str(test_list))

 

# initializing indices

idx_lis = [1, 2, 5]

 

# back iteration

for idx in idx_lis[::-1]:

 

 # pop() used for removal

 test_list.pop(idx)

 

# printing result

print("Matrix after removal: " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original list is: [[3, 5, 2], [1, 8, 9], [5, 3, 1], [0, 1, 6], [9, 4,
> 1], [1, 2, 10], [0, 1, 2]]
>
> Matrix after removal: [[3, 5, 2], [0, 1, 6], [9, 4, 1], [0, 1, 2]]

 **Method #2 : Using** **enumerate()** **+** **list comprehension**

In this, rather than removing rows by index, we perform the task of only
adding rows that are not part of removing the index list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove positional rows

# Using enumerate() + list comprehension

 

# initializing list

test_list = [[3, 5, 2], [1, 8, 9], [5, 3,
1], 

 [0, 1, 6], [9, 4, 1], [1, 2, 10], 

 [0, 1, 2]]

 

# printing original list

print("The original list is: " + str(test_list))

 

# initializing indices

idx_lis = [1, 2, 5]

 

# using enumerate() to get index and value of each row

res = [sub[1] for sub in enumerate(test_list) if
sub[0] not in idx_lis]

 

# printing result

print("Matrix after removal: " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is: [[3, 5, 2], [1, 8, 9], [5, 3, 1], [0, 1, 6], [9, 4,
> 1], [1, 2, 10], [0, 1, 2]]
>
> Matrix after removal: [[3, 5, 2], [0, 1, 6], [9, 4, 1], [0, 1, 2]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

