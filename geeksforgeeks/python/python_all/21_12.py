Python – Sort row by K multiples



Given a Matrix, perform row sorting by number of multiple of K present in row.

>  **Input** : test_list = [[3, 4, 8, 1], [12, 32, 4, 16], [1, 2, 3, 4], [9,
> 7, 5]], K = 4  
> **Output** : [[9, 7, 5], [1, 2, 3, 4], [3, 4, 8, 1], [12, 32, 4, 16]]  
> **Explanation** : 0 < 1 < 2 < 4, multiple of 4 occurrence order.
>
>  **Input** : test_list = [[3, 4, 8, 1], [12, 32, 4, 16], [1, 2, 3, 4], [9,
> 7, 5]], K = 2  
> **Output** : [[9, 7, 5], [1, 2, 3, 4], [3, 4, 8, 1], [12, 32, 4, 16]]  
> **Explanation** : 0 < 2 = 2 < 4, multiple of 2 occurrence order.

**Method #1 : Using sort() + % operator + len()**

In this, we test for multiple using % operator and then compute count by
getting length of filtered elements, provided to key to sort() which performs
inplace sorting of rows.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort row by K multiples

# Using sort() + % operator + len()

 

# checking for multiples count

 

 

def k_mul(row):

 return len([ele for ele in row if ele % K ==
0])

 

 

# initializing list

test_list = [[3, 4, 8, 1], [12, 32, 4,
16], [1, 2, 3, 4], [9, 7, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 4

 

# performing sort

test_list.sort(key=k_mul)

 

# printing result

print("Sorted result : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[3, 4, 8, 1], [12, 32, 4, 16], [1, 2, 3, 4], [9, 7,
> 5]]  
> Sorted result : [[9, 7, 5], [1, 2, 3, 4], [3, 4, 8, 1], [12, 32, 4, 16]]

 **Method #2 : Using** **sorted()** **+** **lambda** **+** **len()**

In this, sorting is done using sorted(), len() is used to get length of all
the muliples of K as in above method. The lambda function provides single
statement alternative to perform logical injection.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort row by K multiples

# Using sorted() + lambda + len()

 

# initializing list

test_list = [[3, 4, 8, 1], [12, 32, 4,
16], [1, 2, 3, 4], [9, 7, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 4

 

# performing sort using sorted()

# lambda avoiding external function call

res = sorted(test_list, key=lambda row: len(

 [ele for ele in row if ele % K == 0]))

 

# printing result

print("Sorted result : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[3, 4, 8, 1], [12, 32, 4, 16], [1, 2, 3, 4], [9, 7,
> 5]]  
> Sorted result : [[9, 7, 5], [1, 2, 3, 4], [3, 4, 8, 1], [12, 32, 4, 16]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

