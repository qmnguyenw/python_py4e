sympy.stats.Wald() in Python



With the help of **sympy.stats.Wald()** method, we can get the continuous
random variable which represents the inverse gaussian distribution as well as
Wald distribution by using this method.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200605163202/Screenshot-2020-06-05-16.29.34.png)

>  **Syntax :** sympy.stats.Wald(name, mean, lamda)  
> Where, mean and lamda are positive number.
>
>  **Return :** Return the continuous random variable.

 **Example #1 :**  
In this example we can see that by using sympy.stats.Wald() method, we are
able to get the continuous random variable representing inverse gaussian or
wald distribution by using this method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Import sympy and Wald

from sympy.stats import Wald, density

from sympy import Symbol, pprint

 

z = Symbol("z")

mean = Symbol("mean", positive = True)

lamda = Symbol("lamda", positive = True)

 

# Using sympy.stats.Wald() method

X = Wald("x", mean, lamda)

gfg = density(X)(z)

 

pprint(gfg)  
  
---  
  
 __

 __

 **Output :**

> 2  
> -lamda*(-mean + z)  
> ——————–  
> ____ 2  
> ___ _______ / 1 2*mean *z  
> \/ 2 *\/ lamda * / — *e  
> / 3  
> \/ z  
> ———————————————–  
> ____  
> 2*\/ pi

 **Example #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Import sympy and Wald

from sympy.stats import Wald, density

from sympy import Symbol, pprint

 

z = 0.86

mean = 6

lamda = 2.35

 

# Using sympy.stats.Wald() method

X = Wald("x", mean, lamda)

gfg = density(X)(z)

 

pprint(gfg)  
  
---  
  
 __

 __

 **Output :**

> 0.498668646362573  
> —————–  
> ____  
> \/ pi

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

