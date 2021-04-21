Python – Extract Row with any Boolean True



Given a Boolean Matrix, extract row which contains at least one boolean True
value.

>  **Input** : test_list = [[False, False], [True, True, True], [False, True],
> [False]]  
> **Output** : [[True, True, True], [False, True]]  
> **Explanation** : All rows with atleast 1 True extracted.
>
>  **Input** : test_list = [[False, False], [False]]  
> **Output** : []  
> **Explanation** : No rows with even one True.  
>

**Method #1 : Using** **list comprehension** **+** **any()**

In this, we check for any element to be boolean true using any() and list
comprehension is used for task of iteration of rows in matrix.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Row with any Boolean True

# Using list comprehension + any()

 

# initializing list

test_list = [[False, False], [True, True, True],
[False, True], [False]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# using any() to check for any True value 

res = [sub for sub in test_list if any(ele for ele
in sub)]

 

# printing result 

print("Extracted Rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[False, False], [True, True, True], [False, True],
> [False]] Extracted Rows : [[True, True, True], [False, True]]

 **Method #2 : Using any() +** **filter()** **+** **lambda**

In this, we perform task of checking for any True value using any() and
filter() and lambda is used to filter out matching rows.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Row with any Boolean True

# Using any() + filter() + lambda

 

# initializing list

test_list = [[False, False], [True, True, True],
[False, True], [False]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# using any() to check for any True value 

# filter() to perform filtering

res = list(filter(lambda sub : any(ele for ele in
sub), test_list))

 

# printing result 

print("Extracted Rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[False, False], [True, True, True], [False, True],
> [False]] Extracted Rows : [[True, True, True], [False, True]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

