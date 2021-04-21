Python program to Sort Matrix by Maximum Row element



Given a Matrix, sort rows by maximum element.

>  **Input** : test_list = [[5, 7, 8], [9, 10, 3],  
> [10, 18, 3], [0, 3, 5]]  
> **Output** : [[10, 18, 3], [9, 10, 3], [5, 7, 8], [0, 3, 5]]  
> **Explanation** : 18, 10, 8 and 5 are maximum elements in rows, hence
> sorted.  
>  **Input** : test_list = [[9, 10, 3],  
> [10, 18, 3], [0, 3, 5]]  
> **Output** : [[10, 18, 3], [9, 10, 3], [0, 3, 5]]  
> **Explanation** : 18, 10, and 5 are maximum elements in rows, hence sorted.  
>

**Method #1 : Using sort() + max()**

In this, we perform task of sorting using sort() with key being maximum
element from each row. The reverse keyword is used to sort by keeping maximum
element rows at start and decreasing from there.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by Maximum Row element

# Using sort() + max()

 

def max_sort(row):

 return max(row)

 

# initializing list

test_list = [[5, 7, 8], [9, 10, 3],

 [10, 18, 3], [0, 3, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sort() for sorting, max to get maximum values

test_list.sort(key = max_sort, reverse = True)

 

# printing result 

print("The maximum sorted Matrix : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original list is : [[5, 7, 8], [9, 10, 3], [10, 18, 3], [0, 3, 5]]  
> The maximum sorted Matrix : [[10, 18, 3], [9, 10, 3], [5, 7, 8], [0, 3, 5]]

 **Method #2 : Using sorted() + lambda + max()**

In this, we perform task of sorting using sorted() for non-inplace sort, and
lambda function is used instead of external function to include maximum
element from row logic.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by Maximum Row element

# Using sorted() + lambda + max()

 

# initializing list

test_list = [[5, 7, 8], [9, 10, 3],

 [10, 18, 3], [0, 3, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sorted() for sorting, max to get maximum values

# reverse for reversed order

res = sorted(test_list, key = lambda row : max(row),
reverse=True)

 

# printing result 

print("The maximum sorted Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[5, 7, 8], [9, 10, 3], [10, 18, 3], [0, 3, 5]]  
> The maximum sorted Matrix : [[10, 18, 3], [9, 10, 3], [5, 7, 8], [0, 3, 5]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

