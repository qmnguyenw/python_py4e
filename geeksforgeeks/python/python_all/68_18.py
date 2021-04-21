Minimum of two numbers in Python



Given two numbers, write a Python code to find the Minimum of these two
numbers.

 **Examples:**

    
    
    **Input:** a = 2, b = 4
    **Output:** 2
    
    **Input:** a = -1, b = -4
    **Output:** -4
    

**Method #1:** This is the naive approach where we will compare the numbers
using if-else statement and will print the output accordingly.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find the

# minimum of two numbers

 

 

def minimum(a, b):

 

 if a <= b:

 return a

 else:

 return b

 

# Driver code

a = 2

b = 4

print(minimum(a, b))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    2

 **Method #2:** Using min() function

This function is used to find the minimum of the values passed as its
arguments.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find the

# minimum of two numbers

 

 

a = 2

b = 4

 

minimum = min(a, b)

print(minimum)  
  
---  
  
 __

 __

 **Output:**

    
    
    2

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

