Python Program to replace list elements within a range with a given number



Given a range, the task here is to write a python program that can update the
list elements falling under a given index range with a specified number.

>  **Input :** test_list = [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1], i, j = 4,
> 8, K = 9
>
>  **Output :** [4, 6, 8, 1, 9, 9, 9, 9, 12, 3, 9, 1]
>
>  **Explanation :** List is updated with 9 from 4th to 8th index.
>
>  **Input :** test_list = [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1], i, j = 4,
> 8, K = 8
>
>  
>
>
>  
>
>
>  **Output :** [4, 6, 8, 1, 8, 8, 8, 8, 12, 3, 9, 1]
>
>  **Explanation :** List is updated with 8 from 4th to 8th index.

 **Method 1 :** _Using_ _slicing_ _and_ _* operator_

In this, we perform task of getting elements of range using slicing and *
operator is used to perform update and provide required elements to fill
updates.

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

 

# initializing i, j

i, j = 4, 8

 

# initializing K

K = 9

 

# getting range using slicing and

# required elements using * operator

test_list[i:j] = [K] * (j - i)

 

# printing result

print("Range Updated list : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1]
>
> Range Updated list : [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1, 9]
>
>  
>
>
>  
>

 **Method 2 :** _Using_ _repeat()_ _and_ _list slicing_

The similar task can also be performed using repeat(), which uses unbuilt
constructs to get required elements.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from itertools import repeat

 

# initializing list

test_list = [4, 6, 8, 1, 2, 9, 0, 10,
12, 3, 9, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing i, j

i, j = 4, 8

 

# initializing K

K = 9

 

# getting range using slicing and

# required elements using repeat()

test_list[i:j] = repeat(K, (j - i))

 

# printing result

print("Range Updated list : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1]
>
> Range Updated list : [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1, 9]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

