Python program to sort matrix based upon sum of rows



Given a Matrix, perform sort based upon the sum of rows.

>  **Input** : test_list = [[4, 5], [2, 5, 7], [2, 1], [4, 6, 1]]  
> **Output** : [[2, 1], [4, 5], [4, 6, 1], [2, 5, 7]]  
> **Explanation** : 3 < 9 < 11 < 14\. Sorted sum.
>
>  **Input** : test_list = [[4, 5], [2, 5, 7], [4, 6, 1]]  
> **Output** : [[4, 5], [4, 6, 1], [2, 5, 7]]  
> **Explanation** : 9 < 11 < 14\. Sorted sum.

**Method #1 : Using sort() + sum()**

In this, task of sorting is done using sort(), and computation of sum is done
by sum(), and passed as key fnc. to sort().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by row sum

# Using sort() + sum()

 

# helper_fnc

def sum_sort(row):

 

 # getting sum 

 return sum(row)

 

# initializing list

test_list = [[4, 5], [2, 5, 7], [2, 1],
[4, 6, 1]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# using sort() to perform sort

test_list.sort(key = sum_sort)

 

# printing result 

print("Sum sorted Matrix : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 5], [2, 5, 7], [2, 1], [4, 6, 1]]  
> Sum sorted Matrix : [[2, 1], [4, 5], [4, 6, 1], [2, 5, 7]]

 **Method #2 : Using** **sorted()** **\+ sum() +** **lambda**

In this, the task of sorting is done using sorted() and lambda is used in
place of the external function call for the key.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by row sum

# Using sorted() + sum() + lambda

 

# initializing list

test_list = [[4, 5], [2, 5, 7], [2, 1],
[4, 6, 1]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# using lambda fnction preventing fnc. call

res = sorted(test_list, key=lambda row: sum(row))

 

# printing result

print("Sum sorted Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 5], [2, 5, 7], [2, 1], [4, 6, 1]]  
> Sum sorted Matrix : [[2, 1], [4, 5], [4, 6, 1], [2, 5, 7]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

