Python Program to convert complex numbers to Polar coordinates



Before starting with the program, let’s see the basics of Polar Coordinates
and then use Python’s cmath and abs module to convert it. Polar coordinates
are just a different way of representing Cartesian coordinates or Complex
Numbers. A complex number z is defined as :

![z=x+yj](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-022bc26f1732a96e4308738b42b0d4be_l3.png)

It is completely determined by its real part x and imaginary part y. Here, j
is the imaginary unit.

The polar coordinates (r , φ) is completely determined by modulus r and phase
angle φ.

 **Where,**

  

  

  *  **r:** Distance from z to origin, i.e., 

![r = \\sqrt{x^{2}+y^{2}}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a807f84bcd66c79c1a9453c02b4357b2_l3.png)

  * **φ:** Counterclockwise angle measured from the positive x-axis to the line segment that joins z to the origin.

The conversion of complex numbers to polar co-ordinates are explained below
with examples.

## Using cmath module

Python’s cmath module provides access to the mathematical functions for
complex numbers. It contains several functions that are used for converting
coordinates from one domain to another.

Out of them, some are explained as-

 **1\. cmath.polar(x):**

Return the representation of x in polar coordinates. cmath.polar() function is
used to convert a complex number to polar coordinates.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to implement

# the polar()function 

 

# importing "cmath" 

# for mathematical operations 

import cmath 

 

# using cmath.polar() method 

num = cmath.polar(1) 

print(num)  
  
---  
  
 __

 __

 **Output**

    
    
    (1.0, 0.0)
    

**2\. cmath.phase (z):** This method returns the phase of complex number
z(also known as the argument of z).

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import cmath

 

 

x = -1.0

y = 0.0

z = complex(x,y); 

 

# printing phase of a complex number using phase() 

print ("The phase of complex number is : ",end="") 

print (cmath.phase(z))   
  
---  
  
__

__

**Output**

    
    
    The phase of complex number is : 3.141592653589793
    

## Using abs()

 **abs():** This method returns the modulus (absolute value) of complex number
z.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

num1= 3 + 4j

print('Absolute value of 3 + 4j is:', abs(num1))  
  
---  
  
 __

 __

 **Output**

    
    
    Absolute value of 3 + 4j is: 5.0
    

You are given a complex number z and your task is to convert it to polar
coordinates.

 **Let us consider a complex number as 1+5j, and we need to convert it to
Polar coordinates.**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import cmath

 

 

c = complex(1+5j)

print(abs(c))  
  
---  
  
 __

 __

 **Output**

    
    
    5.0990195135927845
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

