Python | Append Odd element twice



Given a list of number, the task is to create a new list from the initial list
with the condition to append every odd element twice.

Below are some ways to achieve the above task.

 **Method #1: Using list comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to create a new list from initial list

# with condition to append every odd element twice.

 

# List initialization

Input = [1, 2, 3, 8, 9, 11]

 

# Using list comprehension 

Output = [elem for x in Input for elem in (x, )*(x
% 2 + 1)]

 

# printing 

print("Initial list is:'", Input)

print("New list is:", Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial list is:' [1, 2, 3, 8, 9, 11]
    New list is: [1, 1, 2, 3, 3, 8, 9, 9, 11, 11]
    

  
**Method #2: Using itertools**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to create a new list from initial list

# with condition to append every odd element twice.

 

# Importing

from itertools import chain

 

# List initialization

Input = [1, 2, 3, 8, 9, 11]

 

# Using list comprehension and chain

Output = list(chain.from_iterable([i] 

 if i % 2 == 0 else [i]*2 for i in Input))

 

# printing 

print("Initial list is:'", Input)

print("New list is:", Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial list is:' [1, 2, 3, 8, 9, 11]
    New list is: [1, 1, 2, 3, 3, 8, 9, 9, 11, 11]
    

  
**Method #3: Using Numpy array**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to create a new list from initial list

# with condition to append every odd element twice.

 

# Importing

import numpy as np

 

# List initialization

Input = [1, 2, 3, 8, 9, 11]

Output = []

 

# Using Numpy repeat

for x in Input:

 (Output.extend(np.repeat(x, 2, axis = 0))

 if x % 2 == 1 else Output.append(x))

 

# printing 

print("Initial list is:'", Input)

print("New list is:", Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial list is:' [1, 2, 3, 8, 9, 11]
    New list is: [1, 1, 2, 3, 3, 8, 9, 9, 11, 11]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

