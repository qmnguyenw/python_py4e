Complex Numbers in Python | Set 2 (Important Functions and Constants)



Introduction to python complex numbers: Complex Numbers in Python | Set 1
(Introduction)  
Some more important functions and constants are discussed in this article.  
 **Operations on complex numbers** :

 **1\. exp()** :- This function returns the **exponent** of the complex number
mentioned in its argument.

 **2\. log(x,b)** :- This function returns the **logarithmic value of x with
the base b** , both mentioned in its arguments. If base is not specified,
natural log of x is returned.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# exp(), log()

 

# importing "cmath" for complex number operations

import cmath

import math

 

# Initializing real numbers

x = 1.0

y = 1.0

 

# converting x and y into complex number

z = complex(x, y);

 

# printing exponent of complex number

print ("The exponent of complex number is : ", end="")

print (cmath.exp(z))

 

# printing log form of complex number

print ("The log(base 10) of complex number is : ", end="")

print (cmath.log(z,10))  
  
---  
  
 __

 __

Output:

    
    
    The exponent of complex number is : (1.4686939399158851+2.2873552871788423j)
    The log(base 10) of complex number is : (0.15051499783199057+0.3410940884604603j)
    

  

  

**3\. log10()** :- This function returns the **log base 10** of a complex
number.

 **4\. sqrt()** :- This computes the **square root** of a complex number.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# log10(), sqrt()

# importing "cmath" for complex number operations

import cmath

import math

 

# Initializing real numbers

x = 1.0

y = 1.0

 

# converting x and y into complex number

z = complex(x, y);

 

# printing log10 of complex number

print ("The log10 of complex number is : ", end="")

print (cmath.log10(z))

 

# printing square root form of complex number

print ("The square root of complex number is : ", end="")

print (cmath.sqrt(z))  
  
---  
  
 __

 __

Output:

    
    
    The log10 of complex number is : (0.15051499783199057+0.3410940884604603j)
    The square root of complex number is : (1.09868411346781+0.45508986056222733j)
    

**5\. isfinite()** :- Returns **true if both real and imaginary part** of
complex number are **finite** , else returns false.

 **6\. isinf()** :- Returns **true if either real or imaginary part** of
complex number is/are **infinite** , else returns false.

 **7\. isnan()** :- Returns true if **either real or imaginary part** of
complex number is **NaN** , else returns false.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# isnan(), isinf(), isfinite()

 

# importing "cmath" for complex number operations

import cmath

import math

 

# Initializing real numbers

x = 1.0

y = 1.0

a = math.inf

b = math.nan

 

# converting x and y into complex number

z = complex(x,y);

 

# converting x and a into complex number

w = complex(x,a);

 

# converting x and b into complex number

v = complex(x,b);

 

# checking if both numbers are finite

if cmath.isfinite(z):

 print ("Complex number is finite")

else : print ("Complex number is infinite") 

 

# checking if either number is/are infinite

if cmath.isinf(w):

 print ("Complex number is infinite")

else : print ("Complex number is finite") 

 

# checking if either number is/are infinite

if cmath.isnan(v):

 print ("Complex number is NaN")

else : print ("Complex number is not NaN")   
  
---  
  
__

__

Output:

  

  

    
    
    Complex number is finite
    Complex number is infinite
    Complex number is NaN
    

**Constants**

There are two constants defined in cmath module, **“pi”** , which returns the
numerical value of pi. The second one is **“e”** which returns the numerical
value of exponent.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# pi and e 

 

# importing "cmath" for complex number operations

import cmath

import math

 

# printing the value of pi 

print ("The value of pi is : ", end="")

print (cmath.pi)

 

# printing the value of e

print ("The value of exponent is : ", end="")

print (cmath.e)  
  
---  
  
 __

 __

Output:

    
    
    The value of pi is : 3.141592653589793
    The value of exponent is : 2.718281828459045
    

Complex Numbers in Python | Set 3 (Trigonometric and Hyperbolic Functions)

  
This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

