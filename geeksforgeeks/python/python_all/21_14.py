Python – Maximum in Row Range



Given a range and a Matrix, extract the maximum element out of that range of
rows.

>  **Input** : test_list = [[4, 3, 6], [9, 1, 3], [4, 5, 2], [9, 10, 3], [5,
> 9, 12], [3, 14, 2]], i, j = 2, 5  
> **Output** : 12  
> **Explanation** : Checks for rows 2, 3 and 4, maximum element is 12.
>
>  **Input** : test_list = [[4, 3, 6], [9, 1, 3], [4, 5, 2], [9, 10, 3], [5,
> 9, 12], [3, 14, 2]], i, j = 1, 4  
> **Output** : 10  
> **Explanation** : Checks for rows 1, 2 and 3, maximum element is 10.

**Method #1 : Using** **max()** **+** **slicing** ****

In this, we perform the task of slicing the rows in which maximum has to be
found, then the maximum is found for each row using max(), another max() is
applied to get maximum upon extracted elements.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum in Rows Range

# Using max() + slicing

 

# initializing list

test_list = [[4, 3, 6], [9, 1, 3], [4, 5,
2],

 [9, 10, 3], [5, 9, 12], [3, 14, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range

i, j = 2, 4

 

res = 0

for idx in range(i, j):

 

 # getting max in range

 res = max(max(test_list[idx]), res)

 

# printing result

print("The maximum element in row range ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 3, 6], [9, 1, 3], [4, 5, 2], [9, 10, 3], [5, 9,
> 12], [3, 14, 2]]  
> The maximum element in row range ? : 10

 **Method #2 : Using max() +** **slicing + list comprehension**

In this, we perform the similar task as above using list comprehension to
offer one liner to this operation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum in Rows Range

# Using max() + slicing + list comprehension

 

# initializing list

test_list = [[4, 3, 6], [9, 1, 3], [4, 5,
2],

 [9, 10, 3], [5, 9, 12], [3, 14, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range

i, j = 2, 4

 

# getting max of maximum of sub lists

res = max([max(test_list[idx]) for idx in range(i, j)])

 

# printing result

print("The maximum element in row range ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 3, 6], [9, 1, 3], [4, 5, 2], [9, 10, 3], [5, 9,
> 12], [3, 14, 2]]  
> The maximum element in row range ? : 10

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

