Python – List Elements Grouping in Matrix



Given a Matrix, for groups according to list elements, i.e each group should
contain all elements from List.

>  **Input** : test_list = [[2, 6], [7, 8], [1, 4]], check_list = [1, 2, 4, 6]  
>  **Output** : [[7, 8], [[1, 2], [4, 6]]]  
>  **Explanation** : 1, 2, 4, 6 elements rows are grouped.
>
>  **Input** : test_list = [[2, 7], [7, 8], [1, 4]], check_list = [1, 2, 4, 6]  
>  **Output** : [[2, 7], [7, 8], [1, 4]]  
>  **Explanation** : No grouping possible.

 **Method : Using loop + list comprehension + Try-Except**

In this, for each row in matrix, get elements missing from list, after getting
elements, match with each row if we can find missing elements, if found, the
new group is made.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# List Elements Grouping in Matrix

# Using loop 

 

# initializing list

test_list = [[4, 6], [1, 2], [2, 6], [7,
8], [1, 4]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing check_list

check_list = [1, 2, 4, 6]

 

 

res = []

while test_list:

 

 # getting row

 sub1 = test_list.pop()

 

 # getting elements not in row

 sub2 = [ele for ele in check_list if ele not in
sub1]

 try:

 

 # testing if we have list of removed elements

 test_list.remove(sub2)

 

 # grouping if present

 res.append([sub1, sub2])

 except ValueError:

 

 # ungrouped. 

 res.append(sub1)

 

# printing result 

print("The Grouped rows : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[4, 6], [1, 2], [2, 6], [7, 8], [1, 4]]
    The Grouped rows : [[[1, 4], [2, 6]], [7, 8], [[1, 2], [4, 6]]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

