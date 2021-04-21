Python – Summation of kth column in a matrix



Sometimes, while working with Python Matrix, we may have a problem in which we
require to find the summation of a particular column. This can have a possible
application in day-day programming and competitive programming. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Usingsum() + zip()**  
This task can be solved using the combination of above functions. In this, we
pass in the zip() the list, to access all columns and sum() to get summation
of columns.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Matrix Kth column summation

# using sum() + zip()

 

# initialize list

test_list = [[5, 6, 7],

 [9, 10, 2], 

 [10, 3, 4]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize K

K = 2

 

# Matrix Kth column summation

# using sum() + zip()

res = [sum(idx) for idx in zip(*test_list)][K] 

 

# printing result

print("Sum of Kth column is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[5, 6, 7], [9, 10, 2], [10, 3, 4]]
    Sum of Kth column is : 13
    

**Method #2 : Using loop**  
This is brute force way to solve this problem. In this, we iterate through the
matrix and take summation of column by testing column number.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Matrix Kth column summation

# Using loop

 

# initialize list

test_list = [[5, 6, 7],

 [9, 10, 2], 

 [10, 3, 4]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize K

K = 2

 

# Matrix Kth column summation

# Using loop

res = 0

for sub in test_list:

 for idx in range(0, len(sub)):

 if idx == K:

 res = res + sub[idx]

 

# printing result

print("Sum of Kth column is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[5, 6, 7], [9, 10, 2], [10, 3, 4]]
    Sum of Kth column is : 13
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

