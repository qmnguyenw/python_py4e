sympy.integrals.rationaltools.ratint_logpart() in python



With the help of **ratint_logpart()** method, we can integrate the indefinite
rational function by implementing Lazard Rioboo Trager algorithm by using this
method and returns the integrated polynomial.

>  **Syntax :** ratint_logpart(f, g, x, t=None)
>
>  **Return :** Return the integrated function.

 **Example #1 :**

In this example we can see that by using **ratint_logpart()** method, we are
able to compute the indefinite rational integration using Lazard Rioboo Trager
algorithm.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import ratint_logpart

from sympy.integrals.rationaltools import ratint_logpart

from sympy.abc import x

from sympy import Poly

 

# Using ratint_logpart() method

gfg = ratint_logpart(Poly(1, x, domain='ZZ'), 

 Poly(x*2 + x + 1, x, domain='ZZ'), x)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> [(Poly(3*x + 1, x, domain=’ZZ’), Poly(-3*_t + 1, _t, domain=’ZZ’))]

 **Example #2 :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import ratint_logpart

from sympy.integrals.rationaltools import ratint_logpart

from sympy.abc import x, y

from sympy import Poly

 

# Using ratint_logpart() method

gfg = ratint_logpart(Poly(10, y, domain='ZZ'), 

 Poly(y**2 - 3*y - 2, y, domain='ZZ'), y)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> [(Poly(y – 17*_t/20 – 3/2, y, domain=’QQ[_t]’), Poly(-17*_t**2 + 100, _t,
> domain=’ZZ’))]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

