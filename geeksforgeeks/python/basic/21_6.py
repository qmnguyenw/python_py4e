Python math function | sqrt()



  
 **sqrt()** function is an inbuilt function in Python programming language
that returns the square root of any number.

    
    
     **Syntax:**
    **math.sqrt(x)**
    
    **Parameter:**
    x is any number such that x>=0 
    
    **Returns:**
    It returns the square root of the number 
    passed in the parameter. 

__

__  
__

__

__  
__  
__

# Python3 program to demonstrate the

# sqrt() method 

 

# import the math module 

import math 

 

# print the square root of 0 

print(math.sqrt(0)) 

 

# print the square root of 4

print(math.sqrt(4)) 

 

# print the square root of 3.5

print(math.sqrt(3.5))   
  
---  
  
__

__

Output:

    
    
    0.0
    2.0
    1.8708286933869707
    

**Error:** When x<0 it does not executes due to a runtime error.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate the error in

# sqrt() method 

 

# import the math module 

import math 

 

# print the error when x<0 

print(math.sqrt(-1))   
  
---  
  
__

__

**Output:**

    
    
    Traceback (most recent call last):
      File "/home/67438f8df14f0e41df1b55c6c21499ef.py", line 8, in 
        print(math.sqrt(-1)) 
    ValueError: math domain error
    

**Practical Application :** Given a number, check if its prime or not.  
 **Approach:** Run a loop from 2 to sqrt(n) and check if any number in range
(2-sqrt(n)) divides n.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for practical application of sqrt() function

 

# import math module

import math

 

# function to check if prime or not 

def check(n):

 if n == 1:

 return False

 

 # from 1 to sqrt(n) 

 for x in range(2, (int)(math.sqrt(n))+1):

 if n % x == 0:

 return False

 return True

 

# driver code

n = 23

if check(n):

 print("prime") 

else:

 print("not prime")  
  
---  
  
 __

 __

 **Output:**

    
    
    prime
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

