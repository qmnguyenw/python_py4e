Python – Sort Matrix by Number of elements greater than its previous element



Given a Matrix, sort by occurrences where next element is greater than
current. Compute the count of i < i + 1 in each list, sort each row by count
of each of this condition in each row.

>  **Input** : test_list = [[4, 6, 2, 9, 10], [5, 3, 2, 5], [2, 4, 5, 6, 7,
> 7], [6, 3, 2]]  
> **Output** : [[6, 3, 2], [5, 3, 2, 5], [4, 6, 2, 9, 10], [2, 4, 5, 6, 7, 7]]  
> **Explanation** : for [4, 6, 2, 9, 10], the count is 3 as 6>=4, 9>=2 and
> 10>=9, similarly for [5, 3, 2, 5], [2, 4, 5, 6, 7, 7], [6, 3, 2] counts are
> 1,4 and 0 respectively. As, 0<1<3<4 so the order of rows is [6, 3, 2], [5,
> 3, 2, 5], [4, 6, 2, 9, 10], [2, 4, 5, 6, 7, 7]  
>
>
> **Input** : test_list = [[5, 3, 2, 5], [2, 4, 5, 6, 7, 7], [6, 3, 2]]  
> **Output** : [[6, 3, 2], [5, 3, 2, 5], [2, 4, 5, 6, 7, 7]]  
> **Explanation** : 0 < 1 < 4, is the greater next greater elements count. No
> next element is greater in 1st list.  
>

**Method #1 : Using sort() + len()**

In this, we perform task of sorting using _sort()_ and call external function
as the key to solve problem of counting elements with next element greater.
The size is computed using _len()_.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by Next Greater Frequency

# Using sort() + len()

 

 

# getting frequency of next greater

def get_greater_freq(row):

 

 # getting length

 return len([row[idx] for idx in range(0, len(row)
- 1) if row[idx] < row[idx + 1]])

 

 

# initializing list

test_list = [[4, 6, 2, 9, 10], [5, 3, 2,
5], [2, 4, 5, 6, 7, 7], [6, 3, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# inplace sorting

test_list.sort(key=get_greater_freq)

 

# printing result

print("Sorted rows : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 6, 2, 9, 10], [5, 3, 2, 5], [2, 4, 5, 6, 7, 7],
> [6, 3, 2]]  
> Sorted rows : [[6, 3, 2], [5, 3, 2, 5], [4, 6, 2, 9, 10], [2, 4, 5, 6, 7,
> 7]]

 **Method #2 : Using sorted() + len() + lambda**

In this, we perform task of sorting using _sorted(), lambda_ and _len()_ are
used for creating one-liner functionality to perform sorting o the basis of
number of elements grater than their previous element.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by Next Greater Frequency

# Using sorted() + len() + lambda

 

# initializing list

test_list = [[4, 6, 2, 9, 10], [5, 3, 2,
5], [2, 4, 5, 6, 7, 7], [6, 3, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# performing one-liner sorting

# avoiding external fnc. call

res = sorted(test_list, key=lambda row: len(

 [row[idx] for idx in range(0, len(row) - 1) if
row[idx] < row[idx + 1]]))

 

# printing result

print("Sorted rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 6, 2, 9, 10], [5, 3, 2, 5], [2, 4, 5, 6, 7, 7],
> [6, 3, 2]]  
> Sorted rows : [[6, 3, 2], [5, 3, 2, 5], [4, 6, 2, 9, 10], [2, 4, 5, 6, 7,
> 7]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

