Python – Extract list with difference in extreme values greater than K



Given a list of lists. The task is to filter all rows whose difference in min
and max values is greater than K.

 **Examples:**

>  **Input** : test_list = [[13, 5, 1], [9, 1, 2], [3, 4, 2], [1, 10, 2]], K =
> 5  
> **Output** : [[9, 1, 2], [1, 10, 2], [13, 5, 1]]  
> **Explanation** : 8, 9, 12 are differences, greater than K.
>
>  **Input** : test_list = [[13, 5, 1], [9, 1, 2], [3, 4, 2], [1, 10, 2]], K =
> 15  
> **Output** : []  
> **Explanation** : No list with diff > K.

**Method #1 : Using** **list comprehension** **+** **min()** **+** **max()**

  

  

In this, we perform task of iteration using list comprehension and the task of
checking is done using the comparison operator. Values are computed using
max() and min().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter rows with Extreme values greater than K

# Using min() + max() + list comprehension

 

# initializing list

test_list = [[3, 5, 1], [9, 1, 2], [3, 4,
2], [1, 10, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 5

 

# max() and min() getting extreme difference

res = [sub for sub in test_list if max(sub) -
min(sub) > K]

 

# printing result 

print("Filtered rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[3, 5, 1], [9, 1, 2], [3, 4, 2], [1, 10, 2]]  
> Filtered rows : [[9, 1, 2], [1, 10, 2]]

 **Method #2 : Using filter() + lambda + min() + max()**

In this, we perform task of filtering using filter() and lambda, rest min()
and max(), are used to get extreme values difference.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter rows with Extreme values greater than K

# Using filter() + lambda + min() + max()

 

# initializing list

test_list = [[3, 5, 1], [9, 1, 2], [3, 4,
2], [1, 10, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 5

 

# max() and min() getting extreme difference

res = list(filter(lambda sub : max(sub) - min(sub) >
K, test_list))

 

# printing result 

print("Filtered rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[3, 5, 1], [9, 1, 2], [3, 4, 2], [1, 10, 2]]  
> Filtered rows : [[9, 1, 2], [1, 10, 2]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

