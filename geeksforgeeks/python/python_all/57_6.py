sympy.integrals.rationaltools.ratint_ratpart() in python



With the help of **ratint_ratpart()** method, we can implement the Horowitz
Ostrogradsky algorithm and it will return the fractions A and B by using this
method.

>  **Syntax :** ratint_ratpart(f, g, x)
>
>  **Return :** Return the fraction A and B.

 **Example #1 :**

In this example we can see that by using **ratint_ratpart()** method, we are
able to compute the rational integration using Horowitz Ostrogradsky algorithm
and return the fractions A and B.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import ratint_ratpart

from sympy.integrals.rationaltools import ratint_ratpart

from sympy.abc import x, y

from sympy import Poly

 

# Using ratint_ratpart() method

gfg = ratint_ratpart(Poly(5, x, domain='ZZ'), Poly(x**4
+ 1, x, domain='ZZ'), x)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> (0, 5/(x**4 + 1))

 **Example #2 :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import ratint_ratpart

from sympy.integrals.rationaltools import ratint_ratpart

from sympy.abc import x, y

from sympy import Poly

 

# Using ratint_ratpart() method

gfg = ratint_ratpart(Poly(13, x, domain='ZZ'),
Poly(4*x**2 + x - 2, x, domain='ZZ'), x)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> (0, 13/(4*x**2 + x – 2))

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

