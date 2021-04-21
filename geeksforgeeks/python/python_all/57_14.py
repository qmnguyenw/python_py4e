sympy.transforms.inverse_mellin_transform() in python



With the help of **inverse_mellin_transform** method, we can compute the
inverse mellin transform and return the function.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200704141641/Screenshot-2020-07-04-14.04.04.png)

>  **Syntax :** inverse_mellin_transform(F, s, x, strip)  
>  **Return :** Return the function F(x).

 **Example #1 :**  
In this example we can see that by using **inverse_mellin_transform()**
method, we are able to get the function F(x) by performing inverse mallin
transformation.

 __

 __  
 __

 __

 __  
 __  
 __

# import inverse_mellin_transform

from sympy.integrals.transforms import inverse_mellin_transform

from sympy import oo, gamma

from sympy.abc import x, s

 

# Using inverse_mellin_transform() method

gfg = inverse_mellin_transform(gamma(s), s, x, (0, oo))

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

  

  

> exp(-x)

 **Example #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# import inverse_mellin_transform

from sympy.integrals.transforms import inverse_mellin_transform

from sympy import oo, gamma

from sympy.abc import x, s

 

# Using inverse_mellin_transform() method

gfg = inverse_mellin_transform(gamma(s + 1), s, x, (0, oo))

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> x*exp(-x)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

