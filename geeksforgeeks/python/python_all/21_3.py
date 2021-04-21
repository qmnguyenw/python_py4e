Python – Test if all elements are unique in columns in a Matrix



Given a Matrix, test if all columns contain unique elements.

>  **Input** : test_list = [[3, 4, 5], [1, 2, 4], [4, 1, 10]]  
> **Output** : True  
> **Explanation** : 3, 1, 4; 4, 2, 1; 5, 4, 10; All elements are unique in
> columns.
>
>  **Input** : test_list = [[3, 4, 5], [3, 2, 4], [4, 1, 10]]  
> **Output** : False  
> **Explanation** : 3, 3, 4; 3 repeated twice.  
>

**Method #1 : Using loop + set() + len()**

In this, we iterate for each column and test for unique elements using set
size using len(), if any column is found having a size not equal to the actual
list, then the result is flagged off.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if all elements Unique in Matrix Columns

# Using loop + set() + len()

 

# initializing list

test_list = [[3, 4, 5], [1, 2, 4], [4, 1,
10]]

 

# printing original lists

print("The original list is : " + str(test_list))

 

res = True

for idx in range(len(test_list[0])):

 

 # getting column 

 col = [ele[idx] for ele in test_list]

 

 # checking for all Unique elements

 if len(list(set(col))) != len(col):

 res = False

 break

 

# printing result 

print("Are all columns Unique : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [[3, 4, 5], [1, 2, 4], [4, 1, 10]]
    Are all columns Unique : True
    

**Method #2 : Using all() + list comprehension**

This can be solved in one-liner using all() which checks for all the columns,
made using list comprehension, if all columns return True, all() returns true.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if all elements Unique in Matrix Columns

# Using loop + set() + len()

 

# initializing list

test_list = [[3, 4, 5], [1, 2, 4], [4, 1,
10]]

 

# printing original lists

print("The original list is : " + str(test_list))

 

res = True

for idx in range(len(test_list[0])):

 

 # getting column 

 col = [ele[idx] for ele in test_list]

 

 # checking for all Unique elements

 if len(list(set(col))) != len(col):

 res = False

 break

 

# printing result 

print("Are all columns Unique : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [[3, 4, 5], [1, 2, 4], [4, 1, 10]]
    Are all columns Unique : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

