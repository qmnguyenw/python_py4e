Sympy – stats.P() in Python



With the help of **sympy.stats.P()** method, we can find the probability of
an occasion or a hypothetical situation by using sympy.stats.P() method.

>  **Syntax :** sympy.stats.P(function)  
>  **Return :** Return the probability of a hypothesis.

 **Example #1 :**  
In this example we can see that by using sympy.stats.P() method, we are able
to find the probability of an hypothetical situation by using this method.

 __

 __  
 __

 __

 __  
 __  
 __

# Import sympy, P, Dice

from sympy.stats import P, Die

 

situation = Die('X', 2)

 

# Using stats.P() method

gfg = P(situation < 5)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> 1
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

# Import sympy, P, Dice

from sympy.stats import P, Die

 

situation = Die('X', 6)

 

# Using stats.P() method

gfg = P(situation > 3)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> 1/2

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

