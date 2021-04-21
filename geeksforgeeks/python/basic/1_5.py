Python – Check whether the extracted element from each row of matrix can be in
ascending order



Given a Matrix, the task here is to first select an element from each row in
such a manner that when taken in exact order they can potentially form a
sorted list or a list in ascending order. If it is possible return True else
False.

>  **Input** : test_list = [[3, 4, 6, 2], [3, 4, 9, 1], [8, 5, 4, 7], [9, 1,
> 2, 3]]
>
>  **Output :** True
>
>  **Explanation :** [2, 3, 4, 9] is possible increasing list.
>
>  **Input :** test_list = [[3, 4, 6, 2], [3, 4, 9, 1], [8, 5, 4, 7], [1, 1,
> 2, 3]]
>
>  
>
>
>  
>
>
>  **Output :** False
>
>  **Explanation :** Increasing list not possible.

 **Method :** _Using_ _loop_ _and_ _min()_

In this, we keep updating the minimum possible element from each row, if
minimum element greater than previous element, minimum is not found, the
result is flagged false indicating ascending list not possible.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[3, 4, 6, 2], [3, 4, 9, 1],
[8, 5, 4, 7], [9, 1, 2, 3]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing with min of 1st row

cur = min(test_list[0])

 

res = True

for sub in test_list[1:]:

 res = False

 

 # checking row for greater than previous minimum

 for idx in sub:

 if idx >= cur:

 res = True

 

 # storing new minimum

 cur = idx

 break

 

 if not res:

 break

 

# printing result

print("Is ascending list possible ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[3, 4, 6, 2], [3, 4, 9, 1], [8, 5, 4, 7], [9, 1, 2,
> 3]]
>
> Is ascending list possible ? : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

