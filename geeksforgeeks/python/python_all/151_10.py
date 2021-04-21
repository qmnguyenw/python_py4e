Python | How to copy a nested list



In the previous article, we have seen how to clone or Copy a list, now let’s
see how to copy a nested list in Python.

 **Method #1: Using Iteration**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to copy a nested list

 

# List initialization

Input_list = [[0, 1, 2], [3, 4, 5], ]

Output = [] 

 

# Using iteration to assign values

for x in range(len(Input_list)):

 temp = []

 for elem in Input_list[x]:

 temp.append(elem)

 Output.append(temp)

 

# Printing Output

print("Initial list is:")

print(Input_list)

print("New assigned list is")

print(Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial list is:
    [[0, 1, 2], [3, 4, 5]]
    New assigned list is
    [[0, 1, 2], [3, 4, 5]]
    

  
**Method #2: Using deepcopy**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to copy a nested list

import copy

 

# List initialization

Input = [[1, 0, 1], [1, 0, 1]]

 

# using deepcopy

Output = copy.deepcopy(Input)

 

# Printing

print("Initial list is:")

print(Input)

print("New assigned list is")

print(Output)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Initial list is:
    [[1, 0, 1], [1, 0, 1]]
    New assigned list is
    [[1, 0, 1], [1, 0, 1]]
    

