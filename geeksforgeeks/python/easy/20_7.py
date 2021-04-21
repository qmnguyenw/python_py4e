Functions in Python



A function in Python is an aggregation of related statements designed to
perform a computational, logical, or evaluative task. The idea is to put some
commonly or repeatedly done task together and make a function so that instead
of writing the same code again and again for different inputs, we can call the
function to reuse code contained in it over and over again.

Functions can be both built-in or user-defined. It helps the program to be
concise, non-repetitive, and organized.

 **Syntax:**

    
    
    def function_name(parameters):
        """docstring"""
        statement(s)

 **Example:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A simple Python function to check

# whether x is even or odd

def evenOdd(x):

 if (x % 2 == 0):

 print "even"

 else:

 print "odd"

# Driver code to call the function

evenOdd(2)

evenOdd(3)  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    even
    odd

