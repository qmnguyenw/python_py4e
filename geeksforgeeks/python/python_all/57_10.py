sympy.integrals.transforms.laplace_transform() in python



With the help of **laplace_transform()** method, we can compute the laplace
tranformation F(s) of f(t).

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200706183145/Screenshot-2020-07-06-18.26.26.png)

>  **Syntax :** laplace_transform(f, t, s)  
>  **Return :** Return the laplace transformation and convergence condition.

 **Example #1 :**  
In this example, we can see that by using laplace_transform() method, we are
able to compute the laplace transformation and return the transformation and
convergence condition.

 __

 __  
 __

 __

 __  
 __  
 __

# import laplace_transform

from sympy.integrals import laplace_transform

from sympy.abc import t, s, a

 

# Using laplace_transform() method

gfg = laplace_transform(t**a, t, s)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

  

  

> (s**(-a)*gamma(a + 1)/s, 0, a > -1)

 **Example #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# import laplace_transform

from sympy.integrals import laplace_transform

from sympy.abc import t, s, a

 

# Using laplace_transform() method

gfg = laplace_transform(t**a, t, 5)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> (5**(-a)*gamma(a + 1)/5, 0, a > -1)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

