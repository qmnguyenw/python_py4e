Python Program to test whether the length of rows are in increasing order



Given a Matrix, the following program is used to test if length all rows of a
matrix are in increasing order or not. If yes, it returns True, otherwise
False.

>  **Input** : test_list = [[3], [1, 7], [10, 2, 4], [8, 6, 5, 1, 4]]  
> **Output** : True  
> **Explanation** : 1 < 2 < 3 < 5, increasing lengths of rows, hence True.  
>  **Input** : test_list = [[3], [1, 7], [10], [8, 6, 5, 1, 4]]  
> **Output** : False  
> **Explanation** : 1 <2 >1 < 5, Non-increasing lengths of rows, hence False.

 **Method 1 :** _Using_ _loop_ _and_ _len()_

In this, we are using loop to check whether the length of next row is greater
than the present row, if not, result is flagged off.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[3], [1, 7], [10, 2, 4], [8,
6, 5, 1, 4]]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = True

for idx in range(len(test_list) - 1) :

 

 # flag off in case next length is not greater

 # than current

 if len(test_list[idx + 1]) <= len(test_list[idx]):

 res = False

 break

 

# printing result 

print("Are rows of increasing lengths ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original list is : [[3], [1, 7], [10, 2, 4], [8, 6, 5, 1, 4]]
>
> Are rows of increasing lengths ? : True

 **Method 2 :** _Using_ _all()_ _and_ _list comprehension_

In this, we test for next length being greater than the current length using
len() and all() is used to check for all the rows.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[3], [1, 7], [10, 2, 4], [8,
6, 5, 1, 4]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking for truth for all rows in matrix

res = all(len(test_list[idx + 1]) > len(test_list[idx])
for idx in range(len(test_list) - 1))

 

# printing result 

print("Are rows of increasing lengths ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[3], [1, 7], [10, 2, 4], [8, 6, 5, 1, 4]]
>
> Are rows of increasing lengths ? : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

