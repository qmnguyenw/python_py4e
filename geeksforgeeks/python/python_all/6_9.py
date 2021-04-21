Python program to find the redundancy rates for each row of a matrix



Given a Matrix, the task is to write a python program that can compute
redundancy rates of each row, i.e rate of total number of repeated characters.

 **Redundancy Rate** : Rate of repetition of elements.

 **Formula:**

 __

 __  
 __

 __

 __  
 __  
 __

1 - (total unique elements) / (total elements)  
  
---  
  
 __

 __

 **Examples:**

>  **Input :** test_list = [[4, 5, 2, 4, 3], [5, 5, 5, 5, 5], [8, 7, 8, 8, 7],
> [1, 2, 3, 4, 5]]
>
>  
>
>
>  
>
>
>  **Output :** [0.19999999999999996, 0.8, 0.6, 0.0]
>
>  **Explanation :** 1 – [2/5] = 0.6 for 3rd row.
>
>  **Input :** test_list = [[5, 5, 5, 5, 5], [8, 7, 8, 8, 7], [1, 2, 3, 4, 5]]
>
>  **Output :** [0.8, 0.6, 0.0]
>
>  **Explanation :** 1 – [2/5] = 0.6 for 2nd row.

 **Method 1 :** _Using_ _loop_ _and_ _set()_

In this, we perform task of computing rate using fraction of unique elements
computed using length of set, to all the elements in list, subtracted from 1.

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

test_list = [[4, 5, 2, 4, 3], [5, 5, 5,
5, 5],

 [8, 7, 8, 8, 7], [1, 2, 3, 4, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for sub in test_list:

 

 # getting Redundancy

 res.append(1 - len(set(sub)) / len(sub))

 

# printing result

print("Matrix Redundancy ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 5, 2, 4, 3], [5, 5, 5, 5, 5], [8, 7, 8, 8, 7],
> [1, 2, 3, 4, 5]]
>
> Matrix Redundancy ? : [0.19999999999999996, 0.8, 0.6, 0.0]

 **Method 2 :** _Using_ _list comprehension_

Uses similar functionality as above method, only difference is that its one
liner solution computed using list comprehension.

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

test_list = [[4, 5, 2, 4, 3], [5, 5, 5,
5, 5],

 [8, 7, 8, 8, 7], [1, 2, 3, 4, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# list comprehension for one liner

res = [1 - len(set(sub)) / len(sub) for sub in
test_list]

 

# printing result

print("Matrix Redundancy ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 5, 2, 4, 3], [5, 5, 5, 5, 5], [8, 7, 8, 8, 7],
> [1, 2, 3, 4, 5]]
>
> Matrix Redundancy ? : [0.19999999999999996, 0.8, 0.6, 0.0]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

