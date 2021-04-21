Python – Nearest occurrence between two elements in a List



Given a list and two elements, _x_ and _y_ find the nearest occurrence index
of element _x_ from element _y_.

>  **Input** : test_list = [2, 4, 5, 7, 8, 6, 3, 8, 7, 2, 0, 9, 4, 9, 4], x =
> 4, y = 6  
> **Output** : 1  
> **Explanation** : 4 is found at 1, 12 and 14th index, 6 is at 5th index,
> nearest is 1st index.
>
>  **Input** : test_list = [2, 4, 5, 7, 8, 6, 3, 8, 7, 2, 0, 9, 4, 9, 4], x =
> 7, y = 6  
> **Output** : 3  
> **Explanation** : 7 is found at 3rd and 8th index, 6 is at 5th index,
> nearest is 3rd index.

**Method : Using list comprehension + loop + index()**

In this, we find all indices of _y_ using list comprehension, and then get
index of _x_ using _index()_ , post that loop is used to get index difference,
the nearest index is returned as result.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nearest occurrence of x from y in List

# Using list comprehension + loop + index()

 

 

# function to find index of nearest

# occurance between two elements

def nearestOccuranceIndex(test_list, x, y):

 

 # checking if both elements are present in list

 if x not in test_list or y not in test_list:

 return -1

 # getting indices of x

 x_idx = [idx for idx in range(len(test_list)) if
test_list[idx] == x]

 

 # getting y index

 y_idx = test_list.index(y)

 

 # getting min_dist index

 min_dist = 1000000

 res = None

 for ele in x_idx:

 

 # checking for min ele, and updating index

 if abs(ele - y_idx) < min_dist:

 res = ele

 min_dist = abs(ele - y_idx)

 return res

 

 

# initializing list

input_list = [2, 4, 5, 7, 8, 6, 3, 8,
4, 2, 0, 9, 4, 9, 4]

 

# printing original list

print("The original list is : " + str(input_list))

 

# initializing x

x = 4

 

# initializing y

y = 6

 

# printing result

print("Minimum distance index: ", nearestOccuranceIndex(input_list, x,
y))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [2, 4, 5, 7, 8, 6, 3, 8, 4, 2, 0, 9, 4, 9, 4]  
> Minimum distance index: 8

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

