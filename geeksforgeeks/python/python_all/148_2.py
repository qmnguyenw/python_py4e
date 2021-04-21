Python | Find mismatch item on same index in two list



Given two list of integers, the task is to find the index at which the element
of two list doesn’t match.

    
    
     **Input:**
    Input1 = [1, 2, 3, 4]
    Input2 = [1, 5, 3, 6]
    
    **Output:** [1, 3]
    **Explanation:**
    At index=1 we have 2 and 5 and at index=3
    we have 4 and 6 which mismatches.
    

  
Below are some ways to achieve this task.

 **Method #1: Using Iteration**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find the index at which the

# element of two list doesn't match.

 

# List initialisation

Input1 = [1, 2, 3, 4]

Input2 = [1, 5, 3, 6]

 

# Index initialisation

y = 0

 

# Output list intialisation

Output = [] 

 

# Using iteration to find

for x in Input1:

 if x != Input2[y]:

 Output.append(y)

 y = y + 1

 

# Printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 3]
    

**Method #2: Using list Comprehension and zip**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find the index at which the

# element of two list doesn't match.

 

# List initialisation

Input1 = [1, 2, 3, 4]

Input2 = [1, 5, 3, 6]

 

# Using list comprehension and zip 

Output = [Input2.index(y) for x, y in

 zip(Input1, Input2) if y != x]

 

# Printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 3]
    

**Method #3: Using Enumerate**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find the index at which the

# element of two list doesn't match.

 

# List initialisation

Input1 = [1, 2, 3, 4]

Input2 = [1, 5, 3, 6]

 

# Using list comprehension and enumerate

Output = [index for index, elem in enumerate(Input2)

 if elem != Input1[index]]

 

# Printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

