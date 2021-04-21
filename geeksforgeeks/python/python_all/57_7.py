sympy.integrals.rationaltools.ratint() in python



With the help of **ratint()** method, we can compute the indefinite
integration of a rational function. If a function is a rational function,
their is a Lazard Rioboo Trager and the Horowitz Ostrogradsky algorithms that
are implemented in this method.

>  **Syntax :** ratint(f, x, **flags)
>
>  **Return :** Return the integrated function.

 **Example #1 :**

In this example we can see that by using **ratint()** method, we are able to
compute the indefinite integration of a rational function and return the
integrated function by using this method.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import ratint

from sympy.integrals.rationaltools import ratint

from sympy.abc import x

 

# Using ratint() method

gfg = ratint((x**5 - 2*x**3 + x -
2)/12, x)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> x**6/72 – x**4/24 + x**2/24 – x/6

 **Example #2 :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import ratint

from sympy.integrals.rationaltools import ratint

from sympy.abc import y

 

# Using ratint() method

gfg = ratint((3*y**3 + 4*x**2 + y -
2), y)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> 3*y**4/4 + y**2/2 + y*(4*x**2 – 2)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

