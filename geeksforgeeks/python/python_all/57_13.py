sympy.integrals.transforms.mellin_transform() in python



With the help of **transforms.mellin_transform()** method, we can compute
the mellin transform F(s) of f(x).

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200704133710/Screenshot-2020-07-04-13.30.44.png)

>  **Syntax :** transforms.mellin_transform(f, x, s)  
>  **Return :** Return the fundamental strip and auxiliary convergence
> conditions.

 **Example #1 :**  
In this example we can see that by using transforms.mellin_transform()
method, we are able to compute the mellin transformation and return the
fundamental strip and auxiliary convergence conditions.

 __

 __  
 __

 __

 __  
 __  
 __

# import mellin_transform

from sympy.integrals.transforms import mellin_transform

from sympy import exp

from sympy.abc import x, s

 

# Using mellin_transform() method

gfg = mellin_transform(exp(-x), x, s)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

  

  

> (gamma(s), (0, oo), True)

 **Example #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# import mellin_transform

from sympy.integrals.transforms import mellin_transform

from sympy import exp

from sympy.abc import x, s

 

# Using mellin_transform() method

gfg = mellin_transform(exp(-x), x, 3)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> (2, (0, oo), True)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

