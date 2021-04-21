Python | Group tuples in list with same first value



Given a list of tuples, the task is to print another list containing tuple of
same first element. Below are some ways to achieve above tasks.

 **Example:**

    
    
     **Input :** [('x', 'y'), ('x', 'z'), ('w', 't')]
    
    **Output:** [('w', 't'), ('x', 'y', 'z')]
    

**Method #1: Usingextend**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find common

# first element in list of tuple

 

# Function to solve the task

def find(Input):

 out = {}

 for elem in Input:

 try:

 out[elem[0]].extend(elem[1:])

 except KeyError:

 out[elem[0]] = list(elem)

 return [tuple(values) for values in out.values()]

 

# List initialization

Input = [('x', 'y'), ('x', 'z'), ('w', 't')]

 

# Calling function

Output = (find(Input))

 

# Printing

print("Initial list of tuple is :", Input)

print("List showing common first element", Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial list of tuple is : [('x', 'y'), ('x', 'z'), ('w', 't')]
    List showing common first element [('w', 't'), ('x', 'y', 'z')]
    

  

  

**Method #2: Usingdefaultdict**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find common first

# element in list of tuple

 

# Importing

from collections import defaultdict

 

# Function to solve the task

def find(pairs):

 mapp = defaultdict(list)

 for x, y in pairs:

 mapp[x].append(y)

 return [(x, *y) for x, y in mapp.items()]

 

# Input list initialization

Input = [('p', 'q'), ('p', 'r'),

 ('p', 's'), ('m', 't')]

 

# calling function

Output = find(Input)

 

# Printing

print("Initial list of tuple is :", Input)

print("List showing common first element", Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial list of tuple is : [('p', 'q'), ('p', 'r'), ('p', 's'), ('m', 't')]
    List showing common first element [('m', 't'), ('p', 'q', 'r', 's')]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

