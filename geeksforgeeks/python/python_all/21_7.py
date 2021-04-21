Python – Test if Rows have Similar frequency



In this article we have a given Matrix, test if all rows have similar
elements.

>  **Input** : test_list = [[6, 4, 2, 7, 3], [7, 3, 6, 4, 2], [2, 4, 7, 3, 6]]  
> **Output** : True  
> **Explanation** : All lists have 2, 3, 4, 6, 7.  
>  **Input** : test_list = [[6, 4, 2, 7, 3], [7, 5, 6, 4, 2], [2, 4, 7, 3, 6]]  
> **Output** : False  
> **Explanation** : 2nd list has 5 instead of 3.

**Method #1 : Using Counter() + list comprehension**

In this, we compute the elements’ frequency dictionary using Counter(), and
compare with each row in Matrix, if they check out then True is returned.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if Rows have Similar frequency

# Using Counter() + list comprehension

from collections import Counter

 

# initializing list

test_list = [[6, 4, 2, 7, 3], [7, 3, 6,
4, 2], [2, 4, 7, 3, 6]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking if all rows are similar 

res = all(dict(Counter(row)) ==
dict(Counter(test_list[0])) for row in test_list)

 

# printing result 

print("Are all rows similar : " + str(res))  
  
---  
  
 __

 __

 **Output**

  

  

> The original list is : [[6, 4, 2, 7, 3], [7, 3, 6, 4, 2], [2, 4, 7, 3, 6]]  
> Are all rows similar : True

