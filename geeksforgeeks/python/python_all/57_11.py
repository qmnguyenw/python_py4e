sympy.integrals.inverse_laplace_transform() in python



With the help of **inverse_laplace_transform()** method, we can compute the
inverse of laplace transformation of F(s).

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200706185035/Screenshot-2020-07-06-18.47.01.png)

>  **Syntax :** inverse_laplace_transform(F, s, t)  
>  **Return :** Return the unevaluated tranformation function.

 **Example #1 :**  
In this example, we can see that by using inverse_laplace_transform()
method, we are able to compute the inverse laplace transformation and return
the unevaluated function.

 __

 __  
 __

 __

 __  
 __  
 __

# import inverse_laplace_transform

from sympy.integrals.transforms import inverse_laplace_transform

from sympy import exp, Symbol

from sympy.abc import s, t

 

a = Symbol('a', positive = True)

# Using inverse_laplace_transform() method

gfg = inverse_laplace_transform(exp(-a * s)/s, s, t)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

  

  

> Heaviside(-a + t)

 **Example #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# import inverse_laplace_transform

from sympy.integrals.transforms import inverse_laplace_transform

from sympy import exp, Symbol

from sympy.abc import s, t

 

a = Symbol('a', positive = True)

# Using inverse_laplace_transform() method

gfg = inverse_laplace_transform(exp(-a * s)/s, s, 5)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> Heaviside(5 – a)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

