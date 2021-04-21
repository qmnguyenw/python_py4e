Python Program to get indices of sign change in a list



Given List, the task is to write a python program that extracts all the
indices from which sign shift occurred.

>  **Input :** test_list = [7, 6, -3, -4, -7, 8, 3, -6, 7, 8]
>
>  **Output** : [1, 4, 6, 7]
>
>  **Explanation :** 6 -> -3, at 1st index, -7 -> 8 at 4th index and so on are
> shifts.
>
>  **Input :** test_list = [7, 6, -3, -4, -7, 8, 3, 6, 7, 8]
>
>  
>
>
>  
>
>
>  **Output :** [1, 4]
>
>  **Explanation :** 6 -> -3, at 1st index, -7 -> 8 at 4th index are shifts.

 **Method 1 :** _Using_ _loop_ _and_ _conditional statements_

In this, we check current and next element to be of opposite signs using
conditional statements. Loop is used to iterate through all the elements.

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

test_list = [7, 6, -3, -4, -7, 8, 3,
-6, 7, 8]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for idx in range(0, len(test_list) - 1):

 

 # checking for successive opposite index

 if test_list[idx] > 0 and test_list[idx + 1] < 0 or
test_list[idx] < 0 and test_list[idx + 1] > 0:

 res.append(idx)

 

# printing result

print("Sign shift indices : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [7, 6, -3, -4, -7, 8, 3, -6, 7, 8]
>
> Sign shift indices : [1, 4, 6, 7]
>
>  
>
>
>  
>

 **Method 2 :** _Using_ _list comprehension_

Similar to above method, but this provides a one liner alternative using list
comprehension.

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

test_list = [7, 6, -3, -4, -7, 8, 3,
-6, 7, 8]

 

# printing original list

print("The original list is : " + str(test_list))

 

# list comprehension to provide one liner alternative

res = [idx for idx in range(0, len(test_list) -
1) if test_list[idx] >

 0 and test_list[idx + 1] < 0 or test_list[idx] < 0
and test_list[idx + 1] > 0]

 

# printing result

print("Sign shift indices : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [7, 6, -3, -4, -7, 8, 3, -6, 7, 8]
>
> Sign shift indices : [1, 4, 6, 7]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

