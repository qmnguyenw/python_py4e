Python | Ways to sum list of lists and return sum list



The list is an important container and used almost in every code of day-day
programming as well as web-development, more it is used, more is the
requirement to master it and hence knowledge of its operations is necessary.
Given a list of lists, the program to suppose to return the sum as the final
list.

Let’s see some of the methods to sum a list of list and return list.

 **Method # 1:** Using Naive method

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sum of list of list

# using naive method

 

# Declaring initial list of list

L = [[1, 2, 3],

 [4, 5, 6],

 [7, 8, 9]]

 

# Printing list of list

print("Initial List - ", str(L))

 

# Using naive method

res = list()

for j in range(0, len(L[0])):

 tmp = 0

 for i in range(0, len(L)):

 tmp = tmp + L[i][j]

 res.append(tmp)

 

# printing result

print("final list - ", str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial List -  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    final list -  [12, 15, 18]
    

  
**Method #2:** Using numpy array  
A numpy is a general-purpose array-processing package. It provides a high-
performance multidimensional array object, and tools for working with these
arrays.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sum of list of list

# using numpy array functions

import numpy as np

 

# Declaring initial list of list

List = np.array([[1, 2, 3],

 [4, 5, 6],

 [7, 8, 9]])

 

# Printing list of list

print("Initial List - ", str(List))

 

# Using numpy sum

res = np.sum(List, 0)

 

# printing result

print("final list - ", str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial List -  [[1 2 3]
                     [4 5 6]
                     [7 8 9]]
    final list -  [12 15 18]
    

  
**Method #3:** Using zip() and list comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sum of list of list using 

# zip and list comprehension

 

# Declaring initial list of list

List = [[1, 2, 3],

 [4, 5, 6],

 [7, 8, 9]]

 

# Printing list of list

print("Initial List - ", str(List))

 

# Using list comprehension

res = [sum(i) for i in zip(*List)]

 

# printing result

print("final list - ", str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial List -  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    final list -  [12, 15, 18]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

