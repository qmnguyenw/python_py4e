Generate five random numbers from the normal distribution using NumPy



In Numpy we are provided with the module called random module that allows us
to work with random numbers. The random module provides different methods for
data distribution. In this article, we have to create an array of specified
shape and fill it random numbers or values such that these values are part of
a normal distribution or Gaussian distribution. This distribution is also
called the Bell Curve this is because of its characteristics shape.

To generate five random numbers from the normal distribution we will use
numpy.random.normal() method of the random module.

> **Syntax:** numpy.random.normal(loc = 0.0, scale = 1.0, size = None)
>
> **Parameters:**
>
>  **loc:** Mean of distribution
>
>  
>
>
>  
>
>
>  **scale:** Standard derivation
>
> **size:** Resultant shape.  
> If size argument is empty then by default single value is returned.

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing module

import numpy as np

 

 

# numpy.random.normal() method

r = np.random.normal(size=5)

 

# printing numbers

print(r)  
  
---  
  
 __

 __

 **Output :**

    
    
    [ 0.27491897 -0.18001994 -0.01783066  1.07701319 -0.11356911]
    

**Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing module

import numpy as np

 

 

# numpy.random.normal() method

random_array = np.random.normal(0.0, 1.0, 5)

 

# printing 1D array with random numbers

print("1D Array with random values : \n", random_array)  
  
---  
  
 __

 __

 **Output :**

    
    
    1D Array with random values :
    [ 0.14559212  1.97263406  1.11170937 -0.88192442  0.8249291 ]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

