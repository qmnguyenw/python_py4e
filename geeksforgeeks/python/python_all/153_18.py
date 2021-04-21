Python | Solve given list containing numbers and arithmetic operators



Given a list containing numbers and arithmetic operators, the task is to solve
the list.

 **Example:**

    
    
     **Input:** lst =  [2, '+', 22, '+', 55, '+', 4]
    **Output:** 83
    
    **Input:** lst =  [12, '+', 8, '-', 5]
    **Output:** 15
    

Below are some ways to achieve the above tasks.

 **Method #1: Using Iteration**  
We can use iteration as the simplest approach to solve the list with importing
different operators.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to solve the list

# containing numbers and arithmetic operators

 

# Importing

from operator import add, sub

 

# Function to solve list

def find(Input):

 ans = 0

 options = {'+': add, '-': sub}

 option = add 

 for item in Input:

 if item in options:

 option = options[item]

 else:

 number = float(item)

 ans = option(ans, number)

 return ans

 

# Input Initialization

lst = [91, '+', 132, '-', 156, '+', 4]

 

# Calling function

Output = find(lst)

 

# Printing output

print("Initial list", lst)

print("Answer after solving list is:", Output)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Initial list [91, '+', 132, '-', 156, '+', 4]
    Answer after solving list is: 71.0
    

