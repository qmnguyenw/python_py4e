Python – Inter Matrix Grouping



Given 2 Matrix, with 2 elements in each row, group them on basis on first
element.

>  **Input** : test_list1 = [[2, 0], [8, 4], [9, 3]], test_list2 = [[8, 1],
> [9, 7], [2, 10]]  
>  **Output** : {2: [0, 10], 8: [4, 1], 9: [3, 7]}  
>  **Explanation** : All values after mapping cross Matrix, 2 mapped to 0 and
> 10.
>
>  **Input** : test_list1 = [[8, 4], [9, 3]], test_list2 = [[8, 1], [9, 7]]  
>  **Output** : {8: [4, 1], 9: [3, 7]}  
>  **Explanation** : All values after mapping cross Matrix.

 **Method #1 : Using defaultdict() + loop**

This is one of the ways in which this task can be performed. In this, we
iterate add both the lists and then form groups from similar elements and
convert to dictionary with value list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Inter Matrix Grouping

# Using defaultdict() + loop

from collections import defaultdict

 

# initializing lists

test_list1 = [[5, 8], [2, 0], [8, 4], [9,
3]]

test_list2 = [[8, 1], [9, 7], [2, 10], [5,
6]]

 

# printing original list

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# initializing mapping list 

res = defaultdict(list)

 

# concatenation matrix using 2 lists

for key, val in test_list1 + test_list2:

 res[key].append(val)

 

# printing result 

print("The Grouped Matrix : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [[5, 8], [2, 0], [8, 4], [9, 3]]
    The original list 2 : [[8, 1], [9, 7], [2, 10], [5, 6]]
    The Grouped Matrix : {5: [8, 6], 2: [0, 10], 8: [4, 1], 9: [3, 7]}
    

**Method #2 : Using dictionary comprehension + dict()**

This is yet another way in which this task can be performed. In this, we
iterate for all the elements of both matrix by converting each to dictionary
and group its values. Its important to have traces of each element’s mapping
in both the Matrix.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Inter Matrix Grouping

# Using dictionary comprehension + dict()

 

# initializing lists

test_list1 = [[5, 8], [2, 0], [8, 4], [9,
3]]

test_list2 = [[8, 1], [9, 7], [2, 10], [5,
6]]

 

# printing original list

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# mapping dictionaries together, converting each row to dictionary

res = {key: [dict(test_list1)[key], dict(test_list2)[key]] for
key in dict(test_list1)}

 

# printing result 

print("The Grouped Matrix : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [[5, 8], [2, 0], [8, 4], [9, 3]]
    The original list 2 : [[8, 1], [9, 7], [2, 10], [5, 6]]
    The Grouped Matrix : {5: [8, 6], 2: [0, 10], 8: [4, 1], 9: [3, 7]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

