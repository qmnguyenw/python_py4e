sympy.integrals.transforms.cosine_transform() in python



With the help of **cosine_transform()** method, we can compute the cosine
transformation and return the transformed function by using this method.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200708161452/Screenshot20200708161126-300x67.png)

cosine transformation

>  **Syntax :** cosine_transform(f, x, k, **hints)
>
>  **Return :** Return the transformed function.

 **Example #1 :**

In this example we can see that by using **cosine_transform()** method, we are
able to compute the cosine transformation and return the transformed function.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import cosine_transform

from sympy import cosine_transform, exp, sqrt, cos

from sympy.abc import x, k, a

 

# Using cosine_transform() method

gfg = cosine_transform(exp(-a * x), x, k)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> sqrt(2)*a/(sqrt(pi)*(a**2 + k**2))

 **Example #2 :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import cosine_transform

from sympy import cosine_transform, exp, sqrt, cos

from sympy.abc import x, k, a

 

# Using cosine_transform() method

gfg = cosine_transform(exp(-a * x), x, 5)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> sqrt(2)*a/(sqrt(pi)*(a**2 + 25))

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

