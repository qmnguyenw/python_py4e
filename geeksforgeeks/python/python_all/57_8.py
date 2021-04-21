sympy.integrals.transforms.inverse_hankel_transform() in python



With the help of **inverse_hankel_transform()** method, we can compute the
inverse of hankel transformation and returns the unevaluated function by using
this method.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200708220757/Screenshot20200708220628-300x79.png)

inverse hankel transformation

>  **Syntax :** inverse_hankel_transform(F, k, r, nu, **hints)
>
>  **Return :** Return the unevaluated function.

 **Example #1 :**

In this example we can see that by using **inverse_hankel_transform()**
method, we are able to compute the inverse hankel transformation and return
the unevaluated function.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import inverse_hankel_transform

from sympy import hankel_transform, inverse_hankel_transform, gamma

from sympy import gamma, exp, sinh, cosh

from sympy.abc import r, k, m, nu, a

 

ht = hankel_transform(5/(r*m), r, k, nu)

 

# Using inverse_hankel_transform() method

gfg = inverse_hankel_transform(ht, k, r, nu)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> 5/(m*r)

 **Example #2 :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import inverse_hankel_transform

from sympy import hankel_transform, inverse_hankel_transform, gamma

from sympy import gamma, exp, sinh, cosh

from sympy.abc import r, k, m, nu, a

 

ht = hankel_transform(exp(-2*r), r, k, 0)

 

# Using inverse_hankel_transform() method

gfg = inverse_hankel_transform(ht, k, r, 0)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> exp(-2*r)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

