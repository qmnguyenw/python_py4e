Python math function | modf()



 **modf()** function is an inbuilt function in Python that returns the
fractional and integer parts of the number in a two-item tuple. Both parts
have the same sign as the number. The integer part is returned as a float.

 **Syntax :**

    
    
    modf(number) 

**Parameter :**

    
    
    There is only one mandatory parameter which is the number. 

**Returns :**  
This method returns the fractional and integer parts of number in a two-item
tuple. Both parts have the same sign as the number. The integer part is
returned as a float.

 **Exception :**

  

  

    
    
     TypeError:  If anything other then a float number is passed, it returns a type error. 

Below is the Python3 implementation of **_modf()_** method :

 **Code #1**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate the function modf()

 

# This will import math module

import math 

 

# modf() function used with a positive number

print("math.modf(100.12) : ", math.modf(100.12))

 

# modf() function used with a negative number

print("math.modf(-100.72) : ", math.modf(-100.72)) 

 

print("math.modf(2) : ", math.modf(2))   
  
---  
  
__

__

**Output :**

    
    
    math.modf(100.12) :  (0.12000000000000455, 100.0)
    math.modf(-100.72) :  (-0.7199999999999989, -100.0)
    math.modf(2) :  (0.0, 2.0)
    

**Code #2 : TypeError**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate the

# error in function modf()

 

# This will import math module

import math 

 

# modf() function used with a positive number

print("math.modf(100.12) : ", math.modf("100.12"))  
  
---  
  
 __

 __

 **Output :**

    
    
    Traceback (most recent call last):
      File "/home/fa6d7643de17bafe9a0e0693458e4bdb.py", line 9, in 
        print("math.modf(100.12) : ", math.modf("100.12"))
    TypeError: a float is required
    

  
**Code #3** :

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate the

# error in function modf()

 

# This will import math module

from math import modf

 

lst = [3.12, -5.14, 13.25, -5.21]

tpl = (33.12, -15.25, 3.15, -31.2)

 

 

# modf() function on elements of list

print("modf() on First list element : ", modf(lst[0]))

print("modf() on third list element : ", modf(lst[2]))

 

# modf() function on elements of tuple

print("modf() on Second tuple element : ", modf(tpl[1]))

print("modf() on Fourth tuple element : ", modf(tpl[3]))  
  
---  
  
 __

 __

Output :

    
    
    modf() on First list element :  (0.1200000000000001, 3.0)
    modf() on third list element :  (0.25, 13.0)
    modf() on Second tuple element :  (-0.25, -15.0)
    modf() on Fourth tuple element :  (-0.1999999999999993, -31.0)
    

**Practical Application :**  
Given two float numbers, multiply the fractional part and return the answer.

 **Code #4 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate the

# application of function modf()

 

# This will import math module

import math 

 

# modf() function to multiply fractional part 

a = math.modf(11.2) 

b = math.modf(12.3)

 

# Multiply the fractional part as is stored 

# in 0th index of both the tuple

print(a[0]*b[0])  
  
---  
  
 __

 __

Output :

    
    
    0.05999999999999993
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

