sympy.integrals.singularityfunctions.singularityintegrate() in python



With the help of **singularityintegrate()** method, we can get the definite
integral of the singularity functions and return the integrated function by
using this method.

>  **Syntax :** singularityintegrate(f, x)
>
>  **Return :** Return the definite integral of function.

 **Example #1 :**

In this example we can see that by using **singularityintegrate()** method, we
are able to get the definite integral of a singularity function by using this
method and return the integrated function.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import singularityintegrate

from sympy.integrals.singularityfunctions import singularityintegrate

from sympy import SingularityFunction, symbols, Function

 

x, a, n, y = symbols('x a n y')

f = Function('f')

 

# Using singularityintegrate() method

gfg = singularityintegrate(SingularityFunction(x**2 + 1, a,
2), x)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> SingularityFunction(x**2 + 1, a, 3)/3

 **Example #2 :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import singularityintegrate

from sympy.integrals.singularityfunctions import singularityintegrate

from sympy import SingularityFunction, symbols, Function

 

x, a, n, y = symbols('x a n y')

f = Function('f')

 

# Using singularityintegrate() method

gfg = singularityintegrate(SingularityFunction(x**3, 4,
-2), x)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> SingularityFunction(x**3, 4, -1)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

