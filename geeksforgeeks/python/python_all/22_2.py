Python – Filter Sorted Rows



Given a Matrix, extract rows that are sorted, either by ascending or
descending.

>  **Input** : test_list = [[3, 6, 8, 10], [1, 8, 2, 4, 3], [8, 5, 3, 2], [1,
> 4, 5, 3]]  
> **Output** : [[3, 6, 8, 10], [8, 5, 3, 2]]  
> **Explanation** : Both lists are ordered, 1st ascending, second descending.
>
>  **Input** : test_list = [[3, 6, 8, 10], [1, 8, 2, 4, 3], [8, 5, 7, 2], [1,
> 4, 5, 3]]  
> **Output** : [[3, 6, 8, 10]]  
> **Explanation** : List ordered in ascending order.  
>

**Method #1 : Using** **list comprehension** **+** **sorted()** **\+ reverse**

In this, we check for each row, perform sort by sorted(), and reverse sorted
by passing reverse as key.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Sorted Rows

# Using list comprehension + sorted() + reverse

 

# initializing list

test_list = [[3, 6, 8, 10], [1, 8, 2, 4,
3], [8, 5, 3, 2], [1, 4, 5, 3]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# filtering using sorted() and reverse as key

res = [sub for sub in test_list if sub == list(

 sorted(sub)) or sub == list(sorted(sub,
reverse=True))]

 

# printing result

print("Extracted rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[3, 6, 8, 10], [1, 8, 2, 4, 3], [8, 5, 3, 2], [1, 4,
> 5, 3]]  
> Extracted rows : [[3, 6, 8, 10], [8, 5, 3, 2]]

 **Method #2 : Using** **filter()** **+** **lambda** **\+ sorted() + reverse**

In this, we perform task of filtering using lambda and sorted() and reverse
can be used to check for equality with ordered list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Sorted Rows

# Using filter() + lambda + sorted() + reverse

 

# initializing list

test_list = [[3, 6, 8, 10], [1, 8, 2, 4,
3], [8, 5, 3, 2], [1, 4, 5, 3]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# filtering using sorted() and reverse as key

res = list(filter(lambda sub: sub ==
list(sorted(sub)) or sub ==

 list(sorted(sub, reverse=True)), test_list))

 

# printing result

print("Extracted rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[3, 6, 8, 10], [1, 8, 2, 4, 3], [8, 5, 3, 2], [1, 4,
> 5, 3]]  
> Extracted rows : [[3, 6, 8, 10], [8, 5, 3, 2]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

