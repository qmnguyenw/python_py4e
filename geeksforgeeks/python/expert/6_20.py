Python | Scipy integrate.dblquad() method



With the help of **scipy.integrate.dblquad()** method, we can get the double
integration of a given function from limit a to b by using
scipy.integrate.dblquad() method.

>  **Syntax :** scipy.integrate.dblquad(func, a, b)
>
>  **Return :** Return the double integrated value of a polynomial.

 **Example #1 :**  
In this example we can see that by using scipy.integrate.dblquad() method,
we are able to get the double integration of a polynomial from limit a to b by
using this method.

 __

 __  
 __

 __

 __  
 __  
 __

# import scipy.integrate.dblquad

from scipy import integrate

 

gfg = lambda y, x: x * y**2

 

# using scipy.integrate.dblquad() method

geek = integrate.dblquad(gfg, 0, 3, lambda x: 0,
lambda x: 1)

 

print(geek)  
  
---  
  
 __

 __

 **Output :**

  

  

> 1.4999999999999998

 **Example #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# import scipy.integrate.dblquad

from scipy import integrate

gfg = lambda y, x: x * y**2 + 2 * x*y + 4

 

# using scipy.integrate.dblquad() method

geek = integrate.dblquad(gfg, 1, 4, lambda x: 0,
lambda x: 1)

 

print(geek)  
  
---  
  
 __

 __

 **Output :**

> 21.999999999999996

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

