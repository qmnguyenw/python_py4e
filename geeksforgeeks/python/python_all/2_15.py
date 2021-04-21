Python – Index Ranks of Elements



Given a list of elements, our task is to get the index ranks of each element.

![Index Rank of Number = \(Sum of occurrence indices of number\) /
number](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f1a25fe2a79b7322a9d938d3388c53d4_l3.png)

> **Input :** test_list = [3, 4, 6, 5, 3, 4, 9, 1, 2, 1, 8, 3, 2, 3, 9]
>
>  **Output :** [(1, 16.0), (2, 10.0), (3, 9.333333333333334), (4, 1.5), (5,
> 0.6), (6, 0.3333333333333333), (8, 1.25), (9, 2.2222222222222223)]
>
>  **Explanation :** 1 occurs in list at index 7 and 9. 9 + 7 = 16 / 1 = 16.
>
>  
>
>
>  
>
>
> **Input :** test_list = [3, 4, 6, 5, 3, 4, 9, 1, 2, 1, 8, 3, 2, 3, 9]
>
>  **Output :** [(1, 16.0), (2, 10.0), (3, 9.333333333333334), (4, 1.5), (5,
> 0.6), (6, 0.3333333333333333), (8, 1.25), (9, 2.2222222222222223)]
>
>  **Explanation :** 5 occurs at index 3. 3 / 5 = 0.6.

 **Example : Using** **loop** **+** **filter()** **+** **list comprehension**
**+** **set()** **+** **sum()** **+** **loop**

In this, the indices of elements are extracted using filter() and list
comprehension. The set() is used to get unique numbers that are present in the
list. The sum() is used to compute the summation of all indices.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index Ranks of Elements

# Using loop + filter() + list comprehension. + set() + sum() + loop

 

# initializing list

test_list = [3, 4, 6, 5, 3, 4, 9,

 1, 2, 1, 8, 3, 2, 3, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

all_ele = set(test_list)

for ele in all_ele:

 

 # getting indices of each element 

 indices = list(filter(lambda sub: test_list[sub] ==
ele, range(len(test_list))))

 

 # index rank

 idx_rank = sum(indices) / ele

 res.append((ele, idx_rank))

 

# printing result

print("Index rank of each element : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [3, 4, 6, 5, 3, 4, 9, 1, 2, 1, 8, 3, 2, 3, 9]
>
> Index rank of each element : [(1, 16.0), (2, 10.0), (3, 9.333333333333334),
> (4, 1.5), (5, 0.6), (6, 0.3333333333333333), (8, 1.25), (9,
> 2.2222222222222223)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

