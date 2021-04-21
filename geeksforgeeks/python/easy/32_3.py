Complex Numbers in Python | Set 1 (Introduction)



Not only real numbers, Python can also handle complex numbers and its
associated functions using the file “cmath”. Complex numbers have their uses
in many applications related to mathematics and python provides useful tools
to handle and manipulate them.

 **Converting real numbers to complex number**

An complex number is represented by “ **x + yi** “. Python converts the real
numbers x and y into complex using the function **complex(x,y)**. The real
part can be accessed using the function **real()** and imaginary part can be
represented by **imag()**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# complex(), real() and imag()

 

# importing "cmath" for complex number operations

import cmath

 

# Initializing real numbers

x = 5

y = 3

 

# converting x and y into complex number

z = complex(x,y);

 

# printing real and imaginary part of complex number

print ("The real part of complex number is : ",end="")

print (z.real)

 

print ("The imaginary part of complex number is : ",end="")

print (z.imag)  
  
---  
  
 __

 __

Output:

    
    
    The real part of complex number is : 5.0
    The imaginary part of complex number is : 3.0
    

  

  

**Phase of complex number**

Geometrically, the phase of a complex number is the **angle between the
positive real axis and the vector representing complex number**. This is also
known as **argument** of complex number. Phase is returned using **phase()** ,
which takes complex number as argument. The range of phase lies from **-pi to
+pi.** i.e from **-3.14 to +3.14**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# phase()

 

# importing "cmath" for complex number operations

import cmath

 

# Initializing real numbers

x = -1.0

y = 0.0

 

# converting x and y into complex number

z = complex(x,y);

 

# printing phase of a complex number using phase()

print ("The phase of complex number is : ",end="")

print (cmath.phase(z))  
  
---  
  
 __

 __

Output:

    
    
    The phase of complex number is : 3.141592653589793
    

**Converting from polar to rectangular form and vice versa**

Conversion to polar is done using **polar()** , which returns a **pair(r,ph)**
denoting the **modulus r** and phase **angle ph**. modulus can be displayed
using **abs()** and phase using **phase()**.  
A complex number converts into rectangular coordinates by using **rect(r,
ph)** , where **r is modulus** and **ph is phase angle**. It returns a value
numerically equal to **r * (math.cos(ph) + math.sin(ph)*1j)**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# polar() and rect()

 

# importing "cmath" for complex number operations

import cmath

import math

 

# Initializing real numbers

x = 1.0

y = 1.0

 

# converting x and y into complex number

z = complex(x,y);

 

# converting complex number into polar using polar()

w = cmath.polar(z)

 

# printing modulus and argument of polar complex number

print ("The modulus and argument of polar complex number is :
",end="")

print (w)

 

# converting complex number into rectangular using rect()

w = cmath.rect(1.4142135623730951, 0.7853981633974483)

 

# printing rectangular form of complex number

print ("The rectangular form of complex number is : ",end="")

print (w)  
  
---  
  
 __

 __

Output:

    
    
    The modulus and argument of polar complex number is : (1.4142135623730951, 0.7853981633974483)
    The rectangular form of complex number is : (1.0000000000000002+1j)
    

Complex Numbers in Python | Set 2 (Important Functions and Constants)  

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

