Complex Numbers in Python | Set 3 (Trigonometric and Hyperbolic Functions)



Some of the Important Complex number functions are discussed in the articles
below

Complex Numbers in Python | Set 1 (Introduction)  
Complex Numbers in Python | Set 2 (Important Functions and constants)

Trigonometric and Hyperbolic Functions are discussed in this article.

 **Trigonometric Functions**

 **1\. sin()** : This function returns the **sine** of the complex number
passed in argument.

  

  

 **2\. cos()** : This function returns the **cosine** of the complex number
passed in argument.

 **3\. tan()** : This function returns the **tangent** of the complex number
passed in argument.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# sin(), cos(), tan()

 

# importing "cmath" for complex number operations

import cmath

 

# Initializing real numbers

x = 1.0

 

y = 1.0

 

# converting x and y into complex number z

z = complex(x,y);

 

# printing sine of the complex number

print ("The sine value of complex number is : ",end="")

print (cmath.sin(z))

 

# printing cosine of the complex number

print ("The cosine value of complex number is : ",end="")

print (cmath.cos(z))

 

# printing tangent of the complex number

print ("The tangent value of complex number is : ",end="")

print (cmath.tan(z))  
  
---  
  
 __

 __

Output:

    
    
    The sine value of complex number is : (1.2984575814159773+0.6349639147847361j)
    The cosine value of complex number is : (0.8337300251311491-0.9888977057628651j)
    The tangent value of complex number is : (0.2717525853195118+1.0839233273386946j)
    

**4\. asin()** : This function returns the **arc sine** of the complex number
passed in argument.

 **5\. acos()** : This function returns the **arc cosine** of the complex
number passed in argument.

 **6\. atan()** : This function returns the **arc tangent** of the complex
number passed in argument.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# asin(), acos(), atan()

 

# importing "cmath" for complex number operations

import cmath

 

# Initializing real numbers

x = 1.0

 

y = 1.0

 

# converting x and y into complex number z

z = complex(x,y);

 

# printing arc sine of the complex number

print ("The arc sine value of complex number is : ",end="")

print (cmath.asin(z))

 

# printing arc cosine of the complex number

print ("The arc cosine value of complex number is : ",end="")

print (cmath.acos(z))

 

# printing arc tangent of the complex number

print ("The arc tangent value of complex number is : ",end="")

print (cmath.atan(z))  
  
---  
  
 __

 __

Output:

    
    
    The arc sine value of complex number is : (0.6662394324925153+1.0612750619050357j)
    The arc cosine value of complex number is : (0.9045568943023814-1.0612750619050357j)
    The arc tangent value of complex number is : (1.0172219678978514+0.40235947810852507j)
    

**Hyperbolic Functions**

  

  

 **1\. sinh()** : This function returns the **hyperbolic sine** of the complex
number passed in argument.

 **2\. cosh()** : This function returns the **hyperbolic cosine** of the
complex number passed in argument.

 **3\. tanh()** : This function returns the **hyperbolic tangent** of the
complex number passed in argument.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# sinh(), cosh(), tanh()

 

# importing "cmath" for complex number operations

import cmath

 

# Initializing real numbers

x = 1.0

 

y = 1.0

 

# converting x and y into complex number z

z = complex(x,y);

 

# printing hyperbolic sine of the complex number

print ("The hyperbolic sine value of complex number is : ",end="")

print (cmath.sinh(z))

 

# printing hyperbolic cosine of the complex number

print ("The hyperbolic cosine value of complex number is :
",end="")

print (cmath.cosh(z))

 

# printing hyperbolic tangent of the complex number

print ("The hyperbolic tangent value of complex number is :
",end="")

print (cmath.tanh(z))  
  
---  
  
 __

 __

Output:

    
    
    The hyperbolic sine value of complex number is : (0.6349639147847361+1.2984575814159773j)
    The hyperbolic cosine value of complex number is : (0.8337300251311491+0.9888977057628651j)
    The hyperbolic tangent value of complex number is : (1.0839233273386946+0.2717525853195117j)
    

**4\. asinh()** : This function returns the **inverse hyperbolic sine** of the
complex number passed in argument.

 **5\. acosh()** : This function returns the **inverse hyperbolic cosine** of
the complex number passed in argument.

 **6\. atanh()** : This function returns the **inverse hyperbolic tangent** of
the complex number passed in argument.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# asinh(), acosh(), atanh()

 

# importing "cmath" for complex number operations

import cmath

 

# Initializing real numbers

x = 1.0

 

y = 1.0

 

# converting x and y into complex number z

z = complex(x,y);

 

# printing inverse hyperbolic sine of the complex number

print ("The inverse hyperbolic sine value of complex number is :
",end="")

print (cmath.asinh(z))

 

# printing inverse hyperbolic cosine of the complex number

print ("The inverse hyperbolic cosine value of complex number is :
",end="")

print (cmath.acosh(z))

 

# printing inverse hyperbolic tangent of the complex number

print ("The inverse hyperbolic tangent value of complex number is :
",end="")

print (cmath.atanh(z))  
  
---  
  
 __

 __

Output:

    
    
    The inverse hyperbolic sine value of complex number is : (1.0612750619050357+0.6662394324925153j)
    The inverse hyperbolic cosine value of complex number is : (1.0612750619050357+0.9045568943023813j)
    The inverse hyperbolic tangent value of complex number is : (0.40235947810852507+1.0172219678978514j)
    

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

