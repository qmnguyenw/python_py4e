Python program to find number of local variables in a function



Given a Python program, task is to find the number of local variables present
in a function.

 **Examples:**

    
    
    **Input :** a = 1
            b = 2.1
            str = 'GeeksForGeeks'
        
    **Output :** 3
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We can use the co_nlocals() function which returns the number of local
variables used by the function to get the desired result.

 **Code #1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Implementation of above approach

 

# A function containing 3 variables 

def fun():

 a = 1

 str = 'GeeksForGeeks'

 

 

# Driver program

print(fun.__code__.co_nlocals)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    2
    

