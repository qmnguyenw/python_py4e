Python – Change the signs of elements of tuples in a list



Given a dual Tuple list, the task is to write a python program to convert
second element to negative magnitude of each tuple and first element to
positive magnitude of each tuple.

>  **Input :** test_list = [(3, -1), (-4, -3), (1, 3), (-2, 5), (-4, 2), (-9,
> -3)]
>
>  **Output :** [(3, -1), (4, -3), (1, -3), (2, -5), (4, -2), (9, -3)]
>
>  **Explanation :** All the first elements are positive, and 2nd index
> elements are negative, as desired.
>
>  **Input** : test_list = [(3, -1), (-4, -3), (1, 3), (-2, 5)]
>
>  
>
>
>  
>
>
>  **Output :** [(3, -1), (4, -3), (1, -3), (2, -5)]
>
>  **Explanation :** All the first elements are positive, and 2nd index
> elements are negative, as desired.

 **Method 1 :** _Using_ _loop_ _and_ _abs()_

In this, we iterate using loop and initially convert both to positive
magnitude using abs(). The 2nd element is signed “-” and is converted to
negative element as desired.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing lists

test_list = [(3, -1), (-4, -3), (1, 3),
(-2, 5), (-4, 2), (-9, -3)]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for sub in test_list:

 

 # 2nd element converted to negative magnitude

 res.append((abs(sub[0]), -abs(sub[1])))

 

# printing result

print("Updated Tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(3, -1), (-4, -3), (1, 3), (-2, 5), (-4, 2), (-9,
> -3)]
>
> Updated Tuple list : [(3, -1), (4, -3), (1, -3), (2, -5), (4, -2), (9, -3)]
>
>  
>
>
>  
>

 **Method 2 :** _Using_ _list comprehension_ __

Similar to above method, only difference being list comprehension is used as
one liner to perform this task.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing lists

test_list = [(3, -1), (-4, -3), (1, 3),
(-2, 5), (-4, 2), (-9, -3)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# list comprehension used as one liner

res = [(abs(sub[0]), -abs(sub[1])) for sub in
test_list]

 

# printing result

print("Updated Tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(3, -1), (-4, -3), (1, 3), (-2, 5), (-4, 2), (-9,
> -3)]
>
> Updated Tuple list : [(3, -1), (4, -3), (1, -3), (2, -5), (4, -2), (9, -3)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

