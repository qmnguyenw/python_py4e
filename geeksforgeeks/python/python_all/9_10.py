Python Program to Sort Matrix Rows According to Primary and Secondary Indices



Given Matrix, the task here is to write a Python program to sort rows based on
primary and secondary indices. First using primary indices the rows will be
arranged based on the element each row has at the specified primary index. Now
if two rows have the same element at the given primary index, sorting will be
performed again using secondary index.

>  **Input :** test_list = [[2, 5, 7, 4], [8, 1, 3, 10], [9, 1, 9, 4], [10, 1,
> 1, 4]], pri, sec = 3, 2
>
>  **Output :** [[10, 1, 1, 4], [2, 5, 7, 4], [9, 1, 9, 4], [8, 1, 3, 10]]
>
>  **Explanation :** Sorted by 3rd index, and then by 2nd index in case of
> equal elements in 3rd index.
>
>  **Input :** test_list = [[2, 5, 7, 4], [8, 1, 3, 10], [9, 1, 9, 4], [10, 1,
> 1, 4]], pri, sec = 1, 2
>
>  
>
>
>  
>
>
>  **Output :** [[10, 1, 1, 4], [8, 1, 3, 10], [9, 1, 9, 4], [2, 5, 7, 4]]
>
>  **Explanation :** Sorted by 1st index, and then by 2nd index in case of
> equal elements in 1st index.

 **Method 1 :** _Using_ _sort()_ _and_ _lambda_

This performs in-place sorting using sort() and lambda function is used to
perform sorting using sort order defined in order in key from lambda function.

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

test_list = [[2, 5, 7, 4], [8, 1, 3, 10],
[9, 1, 9, 4], [10, 1, 1, 4]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing pri, sec

pri, sec = 3, 2

 

# inplace sorting using sort()

test_list.sort(key=lambda ele: (ele[pri], ele[sec]))

 

# printing result

print("Matrix after sorting : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[2, 5, 7, 4], [8, 1, 3, 10], [9, 1, 9, 4], [10, 1,
> 1, 4]]
>
> Matrix after sorting : [[10, 1, 1, 4], [2, 5, 7, 4], [9, 1, 9, 4], [8, 1, 3,
> 10]]
>
>  
>
>
>  
>

 **Method 2 :** _Using_ _sorted()_ _and_ _itemgetter()_

In this, we perform task of sorting using sorted() and itemgetter() is used to
perform task of getting the index as required.

**Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import operator

 

# initializing list

test_list = [[2, 5, 7, 4], [8, 1, 3, 10],
[9, 1, 9, 4], [10, 1, 1, 4]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing pri, sec

pri, sec = 3, 2

 

# inplace sorting using sort()

res = sorted(test_list, key=operator.itemgetter(pri, sec))

 

# printing result

print("Matrix after sorting : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[2, 5, 7, 4], [8, 1, 3, 10], [9, 1, 9, 4], [10, 1,
> 1, 4]]
>
> Matrix after sorting : [[10, 1, 1, 4], [2, 5, 7, 4], [9, 1, 9, 4], [8, 1, 3,
> 10]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

