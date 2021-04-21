Python program to return rows that have have element at a specified index



Given two Matrices, the task is to write a Python program that can extract all
the rows from both matrix which have similar element at its Kth index, mapped
at similar row position.

 **Examples:**

>  **Input :** test_list1 = [[1, 8, 3], [9, 2, 0], [6, 4, 4], [6, 4, 4]],
> test_list2 = [[1, 9, 3], [8, 2, 3], [5, 4, 6], [5, 4, 6]], K = 1
>
>  **Output :** [[9, 2, 0], [8, 2, 3], [6, 4, 4], [5, 4, 6], [6, 4, 4], [5, 4,
> 6]]
>
>  **Explanation :** All elements with similar elements at 1st index
> extracted.
>
>  
>
>
>  
>
>
>  **Input :** test_list1 = [[1, 8, 3], [9, 2, 0], [6, 4, 4], [6, 5, 4]],
> test_list2 = [[1, 9, 3], [8, 2, 3], [5, 4, 6], [5, 4, 6]], K = 1
>
>  **Output :** [[9, 2, 0], [8, 2, 3], [6, 4, 4], [5, 4, 6]]
>
>  **Explanation :** All elements with similar elements at 1st index
> extracted.

 **Method 1 :** _Using_ _loop_ _and_ _enumerate()_

In this, the list is iterated from the start row till the end, and each row’s
Kth index is matched, if found, both rows are appended to the result.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing lists

test_list1 = [[1, 8, 3], [9, 2, 0], [6,
4, 4], [6, 4, 4]]

test_list2 = [[1, 9, 3], [8, 2, 3], [5,
4, 6], [5, 4, 6]]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# initializing K

K = 1

 

res = []

for idx in range(len(test_list1)):

 

 # comparing lists

 if test_list1[idx][K] == test_list2[idx][K]:

 res.append(test_list1[idx])

 res.append(test_list2[idx])

 

 

# printing result

print("K index matching rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list 1 is : [[1, 8, 3], [9, 2, 0], [6, 4, 4], [6, 4, 4]]
>
>  
>
>
>  
>
>
> The original list 2 is : [[1, 9, 3], [8, 2, 3], [5, 4, 6], [5, 4, 6]]
>
> K index matching rows : [[9, 2, 0], [8, 2, 3], [6, 4, 4], [5, 4, 6], [6, 4,
> 4], [5, 4, 6]]

 **Method 2:** _Using_ _list comprehension_ _and_ _zip()_

In this, we perform the task of getting pairing using zip(), and then compare
the Kth element, append and iterate using extend() and list comprehension.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing lists

test_list1 = [[1, 8, 3], [9, 2, 0], [6,
4, 4], [6, 4, 4]]

test_list2 = [[1, 9, 3], [8, 2, 3], [5,
4, 6], [5, 4, 6]]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# initializing K

K = 1

 

# zip() combines elements together

res = []

[res.extend([t1, t2])

 for t1, t2 in zip(test_list1, test_list2) if t1[K] ==
t2[K]]

 

# printing result

print("K index matching rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list 1 is : [[1, 8, 3], [9, 2, 0], [6, 4, 4], [6, 4, 4]]
>
> The original list 2 is : [[1, 9, 3], [8, 2, 3], [5, 4, 6], [5, 4, 6]]
>
> K index matching rows : [[9, 2, 0], [8, 2, 3], [6, 4, 4], [5, 4, 6], [6, 4,
> 4], [5, 4, 6]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

