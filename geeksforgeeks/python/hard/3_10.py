Find the roots of the polynomials using NumPy



In this article, let’s discuss how to find the roots of a polynomial of a
NumPy array. It can be found using various methods, let’s see them in detail.

 **Method 1:** Using np.roots()

This function returns the roots of a polynomial with coefficients given in p.
The coefficients of the polynomial are to be put in an array in the respective
order.

For example, if the polynomial is **x 2 +3x + 1**, then the array will be [1,
3, 1]

>  _ **Syntax :** numpy.roots(p)_
>
>  _ **Parameters :**_  
>  _ **p :** [array_like] Rank-1 array of polynomial coefficients._
>
>  _ **Return :** [ndarray] An array containing the roots of the polynomial._

Let’s see some examples:

  

  

 **Example 1:** Find the roots of polynomial x2 +2x + 1

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import numpy library

import numpy as np

 

 

# Enter the coefficients of the poly in the array

coeff = [1, 2, 1]

print(np.roots(coeff))  
  
---  
  
 __

 __

 **Output:**

    
    
    [-1. -1.]

 **Example 2:** Find the roots of the polynomial x3 +3 x2  \+ 2x +1

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import numpy library

import numpy as np

 

 

# Enter the coefficients of the poly 

# in the array

coeff = [1, 3, 2, 1]

print(np.roots(coeff))  
  
---  
  
 __

 __

 **Output:**

> [-2.32471796+0.j -0.33764102+0.56227951j -0.33764102-0.56227951j]

 **Method 2:** Using np.poly1D()

  

  

This function helps to define a polynomial function. It makes it easy to apply
“natural operations” on polynomials. The coefficients of the polynomial are to
be put in an array in the respective order.

For example, for the polynomial x2 +3x + 1, the array will be [1, 3, 1]

 **Approach:**

  * Apply function np.poly1D() on the array and store it in a variable.
  * Find the roots by multiplying the variable by roots or r(in-built keyword) and print the result to get the roots of the given polynomial

>  **Syntax:** numpy.poly1d(arr, root, var):

Let’s see some examples:

 **Example 1:** Find the roots of polynomial x2 +2x + 1

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import numpy library

import numpy as np

 

 

# enter the coefficients of poly 

# in the array

p = np.poly1d([1, 2, 1])

 

# multiplying by r(or roots) to 

# get the roots

root_of_poly = p.r

print(root_of_poly)  
  
---  
  
 __

 __

 **Output:**

    
    
    [-1. -1.]

 **Example 2:** Find the roots of the polynomial x3 +3 x2 \+ 2x +1

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import numpy library

import numpy as np

 

 

# enter the coefficients of poly

# in the array

p = np.poly1d([1, 3, 2, 1])

 

# multiplying by r(or roots) to get 

# the roots

root_of_poly = p.r

print(root_of_poly)  
  
---  
  
 __

 __

 **Output:**

> [-2.32471796+0.j -0.33764102+0.56227951j -0.33764102-0.56227951j]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

