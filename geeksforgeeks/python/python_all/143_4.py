Python | Multiply each element in a sublist by its index



Given a list of lists, the task is to multiply each element in a sublist by
its index and return a summed list.

Given below are a few methods to solve the problem.

 **Method #1: Using Naive Method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to multiply numbers with position

# and add them to return num

 

import numpy as np

 

# initialising list

ini_list = [[3, 4, 7], [ 6, 7, 8], [ 10,
7, 5], [ 11, 12, 13]]

 

# printing initial_list

print ("initial_list ", ini_list)

 

res = []

# Using Naive Method

for sub_list in ini_list:

 sublistsum = 0

 

 for i, value in enumerate(sub_list):

 sublistsum = sublistsum + i * value

 

 res.append(sublistsum)

 

# printing result

print ("result", res)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial_list  [[3, 4, 7], [6, 7, 8], [10, 7, 5], [11, 12, 13]]
    result [18, 23, 17, 38]
    

  
**Method #2: Using List comprehension**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to multiply numbers with position

# and add them to return num

 

 

# initialising list

ini_list = [[3, 4, 7], [ 6, 7, 8], [ 10,
7, 5], [ 11, 12, 13]]

 

# printing initial_list

print ("initial_list ", ini_list)

 

# Using list comprehension

res = [sum(i * j for i, j in enumerate(sublist)) 

 for sublist in ini_list]

 

# printing result

print ("result", res)

   
  
---  
  
__

__

**Output:**

    
    
    initial_list  [[3, 4, 7], [6, 7, 8], [10, 7, 5], [11, 12, 13]]
    result [18, 23, 17, 38]
    

  
**Method #3: Using numpy**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to multiply numbers with position

# and add them to return num

 

import numpy as np

 

# initialising list

ini_list = [[3, 4, 7], [ 6, 7, 8], [ 10,
7, 5], [ 11, 12, 13]]

 

# printing initial_list

print ("initial_list ", ini_list)

 

# Using numpy

res = [np.arange(len(sublist)).dot(sublist) for sublist in
ini_list]

 

# printing result

print ("result", res)

 

   
  
---  
  
__

__

**Output:**

    
    
    initial_list  [[3, 4, 7], [6, 7, 8], [10, 7, 5], [11, 12, 13]]
    result [18, 23, 17, 38]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

