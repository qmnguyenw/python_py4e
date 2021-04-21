Python | Remove False row from matrix



Sometimes, while handling data, especially in Machine Learning domain, we need
to go through a lot of incomplete or empty data. We sometimes need to
eliminate the rows which do not contain a value in any of the columns. Let’s
discuss certain ways to remove the rows that have all _False values_ as list
columns.

 **Method #1 : Using list comprehension +count() + len()**

We can perform this particular task using the list comprehension recipe,
partnered with the combination of _len_ and count function to check for
similarity element counter equating to the length of list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removing False rows in matrix 

# using list comprehension + count() + len()

 

# initializing matrix

test_list = [[1, True, 2], [False, False, 3],

 [False, False, False], [1, 0, 1]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + count() + len()

# removing False rows in matrix

res = [sub for sub in test_list 

 if sub.count(False) != len(sub)]

 

# print result

print("The list after removal of False rows : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [[1, True, 2], [False, False, 3], [False, False, False],
> [1, 0, 1]]  
> The list after removal of False rows : [[1, True, 2], [False, False, 3], [1,
> 0, 1]]
>
>  
>
>
>  
>

**Method #2 : Using list comprehension +set()**

This particular task can also be performed by converting the entire row into a
set and then checking for the single value False set for equality and removing
if a match is found.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removing False rows in matrix 

# using list comprehension + set()

 

# initializing matrix

test_list = [[1, True, 2], [False, False, 3],

 [False, False, False], [1, 0, 1]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + set()

# removing False rows in matrix

res = [sub for sub in test_list if set(sub) !=
{False}]

 

# print result

print("The list after removal of False rows : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [[1, True, 2], [False, False, 3], [False, False, False],
> [1, 0, 1]]  
> The list after removal of False rows : [[1, True, 2], [False, False, 3], [1,
> 0, 1]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

