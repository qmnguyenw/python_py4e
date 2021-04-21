Python – Group Elements in Matrix



Given a Matrix with two columns, group 2nd column elements on basis of 1st
column.

>  **Input** : test_list = [[5, 8], [2, 0], [5, 4], [2, 3], [2, 9]]  
>  **Output** : {5: [8, 4], 2: [0, 3, 9]}  
>  **Explanation** : 8 and 4 are mapped to 5 in Matrix, all others to 2.
>
>  **Input** : test_list = [[2, 8], [2, 0], [2, 4], [2, 3], [2, 9]]  
>  **Output** : {2: [8, 4, 0, 3, 9]}  
>  **Explanation** : All mapped to 2.

 **Method #1 : Using dictionary comprehension + loop**

This is one of the ways in which this task can be performed. In this, we
construct the dictionary with empty list values from row 1 and then run a loop
to assign values into it.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group Elements in Matrix

# Using dictionary comprehension + loop

 

# initializing list

test_list = [[5, 8], [2, 0], [5, 4], [2,
3], [7, 9]]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing empty dictionary with default empty list 

res = {idx[0]: [] for idx in test_list}

 

# using loop for grouping

for idx in test_list:

 res[idx[0]].append(idx[1])

 

# printing result 

print("The Grouped Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [[5, 8], [2, 0], [5, 4], [2, 3], [7, 9]]
    The Grouped Matrix : {5: [8, 4], 2: [0, 3], 7: [9]}
    

**Method #2 : Using loop + defaultdict()**

This is similar to above method. The difference being that initial empty mesh
is created using defaultdict().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group Elements in Matrix

# Using loop + defaultdict()

from collections import defaultdict

 

# initializing list

test_list = [[5, 8], [2, 0], [5, 4], [2,
3], [7, 9]]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing empty dictionary using defaultdict

res = defaultdict(list)

 

# using loop for grouping

for idx in test_list:

 res[idx[0]].append(idx[1])

 

# printing result 

print("The Grouped Matrix : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [[5, 8], [2, 0], [5, 4], [2, 3], [7, 9]]
    The Grouped Matrix : {5: [8, 4], 2: [0, 3], 7: [9]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

