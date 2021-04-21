Python – Element wise Matrix Difference



Given two Matrixes, the task is to write a Python program to perform element-
wise difference.

 **Examples:**

>  **Input** : test_list1 = [[2, 4, 5], [5, 4, 2], [1, 2, 3]], test_list2 =
> [[6, 4, 6], [9, 6, 3], [7, 5, 4]]  
> **Output** : [[4, 0, 1], [4, 2, 1], [6, 3, 1]]  
> **Explanation** : 6 – 2 = 4, 4 – 4 = 0, 6 – 5 = 1. And so on.  
>
>
> **Input** : test_list1 = [[2, 4, 5], [1, 2, 3]], test_list2 = [[6, 4, 6],
> [7, 5, 4]]  
> **Output** : [[4, 0, 1], [6, 3, 1]]  
> **Explanation** : 6 – 2 = 4, 4 – 4 = 0, 6 – 5 = 1. And so on.  
>

**Method #1 : Using loop +** **zip()**

  

  

In this, we perform task of combining indices within rows and rows using zip
and nested loop is used to iterate through all the elements of all the rows.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Element-wise Matrix Difference

# Using loop + zip()

 

# initializing lists

test_list1 = [[2, 4, 5], [5, 4, 2], [1,
2, 3]]

test_list2 = [[6, 4, 6], [9, 6, 3], [7,
5, 4]]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

res = []

 

# iterating for rows

for sub1, sub2 in zip(test_list1, test_list2):

 temp = []

 

 # interate for elements

 for ele1, ele2 in zip(sub1, sub2):

 temp.append(ele2 - ele1)

 res.append(temp)

 

# printing result

print("The Matrix Difference : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 is : [[2, 4, 5], [5, 4, 2], [1, 2, 3]]
    The original list 2 is : [[6, 4, 6], [9, 6, 3], [7, 5, 4]]
    The Matrix Difference : [[4, 0, 1], [4, 2, 1], [6, 3, 1]]

 **Method #2 : Using** **list comprehension** **+** **zip()**

In this, we perform task of zipping using zip() and list comprehension is used
to solve this problem in one liner way.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Element-wise Matrix Difference

# Using loop + zip()

 

# initializing lists

test_list1 = [[2, 4, 5], [5, 4, 2], [1,
2, 3]]

test_list2 = [[6, 4, 6], [9, 6, 3], [7,
5, 4]]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# using list comprehension to perform task in one line

res = [[ele2 - ele1 for ele1, ele2 in zip(sub1, sub2)]

 for sub1, sub2 in zip(test_list1, test_list2)]

 

# printing result

print("The Matrix Difference : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 is : [[2, 4, 5], [5, 4, 2], [1, 2, 3]]
    The original list 2 is : [[6, 4, 6], [9, 6, 3], [7, 5, 4]]
    The Matrix Difference : [[4, 0, 1], [4, 2, 1], [6, 3, 1]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

