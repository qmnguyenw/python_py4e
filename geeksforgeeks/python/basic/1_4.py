How to find Definite Integral using Python ?



Definite integrals are the extension after indefinite integrals, definite
integrals have limits [a, b]. It gives the area of a curve bounded between
given limits.

![\\int_{a}^b F\(x\)dx](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-c91edcaf50de122be07888e1c07a9540_l3.png)

It denotes the area of curve F(x) bounded between a and b, where a is the
lower limit and b is the upper limit.

In this article, we will discuss how we can solve definite integrals in
python, and would also visualize the area between them using matplotlib. We
would also use the NumPy module for defining the range of the variable we are
integrating. Let’s Begin with installing the modules.

### Module needed:

  *  **matplotlib**: We would use this to visualize our area under the graph formed by a definite integral.
  *  **numpy** **:** Helper library to define ranges of definite integrals.
  *  **sympy:** Library to calculate the numerical solution of the integral easily.

### Approach

 **For calculating area under curve**

  

  

  * Import module
  * Declare function
  * Integrate.

 _ **Syntax :**_ __

> _sympy.integrate(expression, reference variable)_

 **For plotting** _ ****_

  * Import module
  * Define a function
  * Define a variable
  * Draw the curve
  * Fill the color under it using some condition.
  * Display plot

Given below is the implementation for the same.

 **The area between a curve and standard axis**

 **Example 1** :

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import matplotlib.pyplot as plt

import numpy as np

import sympy as sy

 

 

def f(x):

 return x**2

 

x = sy.Symbol("x")

print(sy.integrate(f(x), (x, 0, 2)))  
  
---  
  
 __

 __

 **Output:**

    
    
    8/3

 **Example 2:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import matplotlib.pyplot as plt

import numpy as np

 

 

def f(x):

 return x**2

 

x = np.linspace(0, 2, 1000)

plt.plot(x, f(x))

plt.axhline(color="black")

plt.fill_between(x, f(x), where=[(x > 0) and (x < 2) for
x in x])

plt.show()  
  
---  
  
 __

 __

