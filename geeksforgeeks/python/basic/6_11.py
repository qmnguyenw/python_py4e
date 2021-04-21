Maximum of two numbers in Python



Given two numbers, write a Python code to find the Maximum of these two
numbers.

 **Examples:**

    
    
    **Input:** a = 2, b = 4
    **Output:** 4
    
    **Input:** a = -1, b = -4
    **Output:** -1
    

**Method #1:** This is the naive approach where we will compare tow numbers
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

# maximum of two numbers

 

 

def maximum(a, b):

 

 if a >= b:

 return a

 else:

 return b

 

# Driver code

a = 2

b = 4

print(maximum(a, b))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    4

 **Method #2:** Using max() function

This function is used to find the maximum of the values passed as its
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

# maximum of two numbers

 

 

a = 2

b = 4

 

maximum = max(a, b)

print(maximum)  
  
---  
  
 __

 __

 **Output:**

    
    
    4

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

