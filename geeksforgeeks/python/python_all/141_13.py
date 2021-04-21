Python program to create a list centered on zero



Given two integer variables, _limit_ and _diff_ , write a Python program to
create a list that is centered on zero, using _limit_ , which specifies limit
of the list and _diff_ that specifies the common difference between integers.

 **Examples:**

    
    
    **Input :** limit = 1, diff = 0.5
    **Output :** [-1, -0.5, 0.0, 0.5, 1]
    
    **Input :** limit = 25, diff = 5
    **Output :** [-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25]
    

**Approach #1 :** Naive Approach

This is a naive approach to the above problem. First, create an empty list
‘lst’, and then we use a while loop to append the next integer with a
difference equal to ‘diff’.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Convert a

# list to dictionary

 

def create(limit, diff):

 

 lst = [-limit]

 while lst[-1] < limit:

 lst.append(lst[-1] + diff)

 lst[-1] = limit

 return lst

 

# Driver code

limit = 1

diff = 0.5

print(create(limit, diff))  
  
---  
  
 __

 __

 **Output:**

    
    
    [-1, -0.5, 0.0, 0.5, 1]
    

  
**Approach #2 :** Using Python Numpy

Using Numpy module makes the solution a lot easier. In this method, we use
np.arange which return evenly spaced values within a given interval ‘diff’.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Convert a

# list to dictionary

import numpy as np

 

def create(limit, diff):

 lst = np.arange(diff, limit, diff)

 if (lst[-1] != limit):

 lst = np.r_[lst, limit]

 

 return np.r_[-lst[::-1], 0, lst].tolist()

 

# Driver code

limit = 1

diff = 0.5

print(create(limit, diff))  
  
---  
  
 __

 __

 **Output:**

    
    
    [-1.0, -0.5, 0.0, 0.5, 1.0]
    

  
**Approach #3 :** list comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Python program to create a list centered on zero

 

def create(limit, diff):

 length = int(((limit/diff)*2)+1) 

 list = [-limit+i*diff for i in range(length)]

 return list

 

 

# Driver code

limit = 1

diff = 0.5

print(create(limit, diff))  
  
---  
  
 __

 __

 **Output:**

    
    
    [-1.0, -0.5, 0.0, 0.5, 1.0]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

