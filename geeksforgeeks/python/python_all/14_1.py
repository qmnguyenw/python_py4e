Python – Extract Paired Rows



Given a Matrix, the task is to write a Python program to extract all the rows
which have paired elements. i.e elements have a frequency of mod 2.

>  **Input** : test_list = [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4], [1, 2], [1,
> 1, 2, 2]]  
> **Output** : [[5, 5, 4, 7, 7, 4], [1, 1, 2, 2]]  
> **Explanation** : All rows have pair elements, i.e have even occurrence.  
>
>
> **Input** : test_list = [[10, 2, 3, 2, 3], [5, 5, 4, 7, 4], [1, 2], [1, 1,
> 2, 2]]  
> **Output** : [[1, 1, 2, 2]]  
> **Explanation** : All rows have pair elements, i.e have even occurrence.

**Method #1 : Using** **all()** **+** **list comprehension** **+** **count()**

In this, we check for the count of each element using _count()_ , and _all()_
is used to test for all elements’ frequency is divisible by 2.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Paired Rows

# Using all() + list comprehension + count()

 

# initializing list

test_list = [[10, 2, 3, 2, 3], [5, 5, 4,
7, 7, 4],

 [1, 2], [1, 1, 2, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# count() checks for frequency to be mod 2

res = [row for row in test_list if all(

 row.count(ele) % 2 == 0 for ele in row)]

 

# printing result

print("Extracted rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4], [1, 2], [1, 1,
> 2, 2]]  
> Extracted rows : [[5, 5, 4, 7, 7, 4], [1, 1, 2, 2]]

 **Method #2 : Using** **filter()** **+** **lambda** **+** **count()** **+**
**all()** ****

In this, we perform the task of filtering using _filter()_ and _lambda_
function instead of list comprehension. The _count()_ and _all()_ are used to
check for the frequency of all the elements in rows.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Paired Rows

# Using filter() + lambda + count() + all()

 

# initializing list

test_list = [[10, 2, 3, 2, 3], [5, 5, 4,
7, 7, 4],

 [1, 2], [1, 1, 2, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# count() checks for frequency to be mod 2

# filter() and lambda used to perform filtering

res = list(filter(lambda row: all(

 row.count(ele) % 2 == 0 for ele in row), test_list))

 

# printing result

print("Extracted rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4], [1, 2], [1, 1,
> 2, 2]]  
> Extracted rows : [[5, 5, 4, 7, 7, 4], [1, 1, 2, 2]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

