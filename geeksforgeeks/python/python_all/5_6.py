Python Program to Remove duplicate tuples irrespective of order



Given a list of binary tuples, the task is to write a Python program to remove
all tuples that are duplicates irrespective of order, i.e delete if contains
similar elements, irrespective of order.

>  **Input :** test_list = [(4, 6), (1, 2), (9, 2), (2, 1), (5, 7), (6, 4),
> (9, 2)]
>
>  **Output :** [(1, 2), (5, 7), (4, 6), (2, 9)]
>
>  **Explanation :** (2, 1), (6, 4) are removed as (1, 2), (4, 6) are already
> included.
>
>  **Input :** test_list = [(4, 7), (1, 2), (9, 2), (2, 1), (5, 7), (7, 4),
> (9, 2)]
>
>  
>
>
>  
>
>
>  **Output :** [(1, 2), (5, 7), (4, 7), (2, 9)]
>
>  **Explanation :** (2, 1), (7, 4) are removed as (1, 2), (4, 7) are already
> included.

 **Method 1 :** _Using_ _map()_ _,_ _sorted()_ _,_ _set()_ _and_ _list()_

In this, we sort each element of tuple using sorted() and map(). Then result
is converted to set to remove duplicates. At last, set is converted to list.

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

test_list = [(4, 6), (1, 2), (9, 2), (2,
1), (5, 7), (6, 4), (9, 2)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# using map() to get all sorted

# set removes duplicates

res = list({*map(tuple, map(sorted, test_list))})

 

# printing result

print("Tuples after removal : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(4, 6), (1, 2), (9, 2), (2, 1), (5, 7), (6, 4), (9,
> 2)]
>
> Tuples after removal : [(2, 9), (1, 2), (4, 6), (5, 7)]
>
>  
>
>
>  
>

 **Method 2 :** _Using_ _list comprehension,_ ___sorted()_ _and_ _set()_

This is a naive approach for the required solution. In this, each element of
list is sorted using list comprehension and sorted(), then result is converted
back to remove duplicates using set().

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

test_list = [(4, 6), (1, 2), (9, 2), (2,
1), (5, 7), (6, 4), (9, 2)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sorting tuples

temp = [tuple(sorted(sub)) for sub in test_list]

 

# removing duplicates

res = list(set(temp))

 

# printing result

print("Tuples after removal : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(4, 6), (1, 2), (9, 2), (2, 1), (5, 7), (6, 4), (9,
> 2)]
>
> Tuples after removal : [(2, 9), (1, 2), (4, 6), (5, 7)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

