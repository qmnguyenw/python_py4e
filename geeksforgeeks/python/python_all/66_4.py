Sympy – stats.DiscreteUniform() in Python



With the help of **sympy.stats.DiscreteUniform()** method, we can get the
random variable who is representing the discrete uniform values for input by
using sympy.stats.DiscreteUniform() method.

>  **Syntax :** sympy.stats.DiscreteUniform(list/tuple)  
>  **Return :** Return the discrete uniform value.

 **Example #1 :**  
In this example we can see that by using sympy.stats.DiscreteUniform()
method, we are able to get the random variable representing the discrete
uniform value by using this method.

 __

 __  
 __

 __

 __  
 __  
 __

# Import sympy and DiscreteUniform

from sympy.stats import DiscreteUniform, density

from sympy import symbols

 

# Using stats.DiscreteUniform() method

X = DiscreteUniform('X', symbols('g f g'))

gfg = density(X).dict

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> {g: 1/3, f: 1/3}
>
>  
>
>
>  
>

 **Example #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Import sympy and DiscreteUniform

from sympy.stats import DiscreteUniform, density

from sympy import symbols

 

# Using stats.DiscreteUniform() method

Y = DiscreteUniform('Y', list(range(5))) 

gfg = density(Y).dict

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> {0: 1/5, 1: 1/5, 2: 1/5, 3: 1/5, 4: 1/5}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

