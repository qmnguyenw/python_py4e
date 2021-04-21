Python – Filter rows with required elements



Given a Matrix, filter rows with required elements from other list.

>  **Input** : test_list = [[2, 4, 6], [7, 4, 3, 2], [2, 4, 8], [1, 1, 9]],
> check_list = [4, 6, 2, 8]  
> **Output** : [[2, 4, 6], [2, 4, 8]]  
> **Explanation** : All elements are from the check list.
>
>  **Input** : test_list = [[2, 4, 6], [7, 4, 3, 2], [2, 4, 8], [1, 1, 9]],
> check_list = [6, 2, 8]  
> **Output** : []  
> **Explanation** : No list with all elements from check list.

**Method #1 : Using** **list comprehension** **+** **all()**

In this, we perform iteration and filtering using list comprehension from list
and check for all elements present in each row using all().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter rows with required elements

# Using list comprehension + all()

 

# initializing list

test_list = [[2, 4, 6], [7, 4, 3, 2], [2,
4, 8], [1, 1, 9]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing check_list

check_list = [4, 6, 2, 8]

 

# using in operator to check for presence

res = [sub for sub in test_list if all(ele in
check_list for ele in sub)]

 

# printing result

print("Filtered rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[2, 4, 6], [7, 4, 3, 2], [2, 4, 8], [1, 1, 9]]  
> Filtered rows : [[2, 4, 6], [2, 4, 8]]

 **Method #2 : Using** **filter()** **+** **lambda** **\+ all()**

In this, the task of filtering is done using filter() and lambda, all() is
used for the task of extracting all elements from that are present in the
checklist.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter rows with required elements

# Using filter() + lambda + all()

 

# initializing list

test_list = [[2, 4, 6], [7, 4, 3, 2], [2,
4, 8], [1, 1, 9]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing check_list 

check_list = [4, 6, 2, 8]

 

# using in operator to check for presence

# filter(), getting all rows checking from check_list

res = list(filter(lambda sub : all(ele in check_list
for ele in sub), test_list))

 

# printing result 

print("Filtered rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[2, 4, 6], [7, 4, 3, 2], [2, 4, 8], [1, 1, 9]]  
> Filtered rows : [[2, 4, 6], [2, 4, 8]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

