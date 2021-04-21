Python | Indices of sorted list of list elements



Sorting is a common construct and there have been many variations of it being
discussed. But sometimes, we need to perform the sorting on the list of list
and moreover just require to find the _order in which element occurs before
getting sorted_. Let’s find out how to get indices of sorted order in list of
lists.

 **Method #1 : Using List comprehension +enumerate() + sort()**

The combination of above 3 functions can be used to perform this particular
task. In this, we perform the sorting taking triplets consisting of element
and row and column coordinates and return them in 2nd step.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Indices of sorted list of list elements

# using List comprehension + enumerate() + sort()

 

# initializing list

test_list = [[4, 5, 1],

 [9, 3, 2],

 [8, 6]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using List comprehension + enumerate() + sort()

# Indices of sorted list of list elements

res = [(i, j) for i, x in enumerate(test_list)

 for j, k in enumerate(x)]

 

res.sort(key = lambda ij: test_list[ij[0]][ij[1]]) 

 

# print result

print("The indices of sorted order are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [[4, 5, 1], [9, 3, 2], [8, 6]]  
> The indices of sorted order are : [(0, 2), (1, 2), (1, 1), (0, 0), (0, 1),
> (2, 1), (2, 0), (1, 0)]
>
>  
>
>
>  
>

**Method #2 : Usingsorted() \+ lambda**

The task performed above can be performed as arguments to the sorted function
and lambda function performs the task of list comprehension function as above.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Indices of sorted list of list elements

# using sorted() + lambda

 

# initializing list

test_list = [[4, 5, 1],

 [9, 3, 2],

 [8, 6]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using sorted() + lambda

# Indices of sorted list of list elements

res = sorted([(i, j) for i, x in enumerate(test_list)

 for j, k in enumerate(x)],

 key = lambda ij: test_list[ij[0]][ij[1]])

 

# print result

print("The indices of sorted order are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [[4, 5, 1], [9, 3, 2], [8, 6]]  
> The indices of sorted order are : [(0, 2), (1, 2), (1, 1), (0, 0), (0, 1),
> (2, 1), (2, 0), (1, 0)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

