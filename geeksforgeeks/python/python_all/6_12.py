Python Program to find the Next Nearest element in a Matrix



Given a matrix, a set of coordinates and an element, the task is to write a
python program that can get the coordinates of the elements next occurrence.

>  **Input :** test_list = [[4, 3, 1, 2, 3], [7, 5, 3, 6, 3], [8, 5, 3, 5, 3],
> [1, 2, 3, 4, 6]], i, j = 1, 3, K = 3
>
>  **Output :** (1, 4)
>
>  **Explanation :** After (1, 3), 3 is found at (1, 4)
>
>  **Input :** test_list = [[4, 3, 1, 2, 3], [7, 5, 3, 6, 3], [8, 5, 3, 5, 3],
> [1, 2, 3, 4, 6]], i, j = 2, 3, K = 3
>
>  
>
>
>  
>
>
>  **Output :** (2, 4)
>
>  **Explanation :** After (2, 3), 3 is found at (2, 4)

 **Method :** _Using_ _loop_ _and_ _enumerate()_

In this we start iteration from the required coordinates and check just for
the next nearest K inside the rectangle formed from row + 1, col + 1 to N, N
coordinate. Returns -1, -1 if not occurrence is found.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# get Nearest coord.

def near_coord(test_list, x, y, val):

 for idx, row in enumerate(test_list[x:]):

 for j, ele in enumerate(row):

 

 # checking for value at lower formed rectangle

 if ele == val and j > y:

 return idx + x, j

 

 # if no index found

 return -1, -1

 

 

# initializing list

test_list = [[4, 3, 1, 2, 3], [7, 5, 3,
6, 3],

 [8, 5, 3, 5, 3], [1, 2, 3, 4, 6]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing check coord

i, j = 1, 3

 

# initializing K

K = 3

 

# getting nearest coordinates

res_abs, res_ord = near_coord(test_list, i, j, K)

 

# printing result

print("Found K index : " + str((res_abs, res_ord)))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 3, 1, 2, 3], [7, 5, 3, 6, 3], [8, 5, 3, 5, 3],
> [1, 2, 3, 4, 6]]
>
> Found K index : (1, 4)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

