How to compute natural, base 10, and base 2 logarithm for all elements in a
given array using NumPy?



numpy.log( ) function in Python returns natural logarithmic of the input where
the natural logarithm of a number is its logarithm to the base of the
mathematical constant e, where e is an irrational and transcendental number
approximately equal to 2.718281828459.

> **Syntax:** numpy.log(arr,out)
>
>  **Parameters:**  
>  **arr :** Input Value. Can be scalar and numpy ndim array as well.  
>  **out :** A location into which the result is stored. If provided, it must
> have a shape that the  
> inputs broadcast to. If not provided or None, a freshly-allocated array is
> returned.  
> shape must be same as input array.

If a scalar is provided to the function as input then the function is applied
on the scalar and a scalar is returned.

**Example:** if 3 was given as input then log(3) will be returned as output.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import numpy

 

n = 3

print("natural logarithm of {} is".format(n), numpy.log(n))

 

n = 5

print("natural logarithm of {} is".format(n), numpy.log(n))  
  
---  
  
 __

 __

 **Output:**

    
    
    natural logarithm of 3 is 1.0986122886681098
    natural logarithm of 5 is 1.6094379124341003
    

If input is an n-dim array then function is applied element-wise. ex-
np.log([1,2,3]) is equivalent to [np.log(1),np.log(2),np.log(3)]

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import numpy

 

 

arr = np.array([6, 2, 3, 4, 5])

print(numpy.log(arr))  
  
---  
  
 __

 __

 **Output:**

    
    
    [1.79175947 0.69314718 1.09861229 1.38629436 1.60943791]
    

Functions similar to numpy.log() :

  *  **numpy.log2()** **:** To calculate base 2 logarithms. Parameters of this functions are same as numpy.log(). It is also called the binary logarithm. Base 2 logarithm of y is the power to which the number 2 must be raised to obtain the value y.
  *  **numpy.log10()**: To calculate base 10 logarithms. Parameters are the same as numpy.log(). Base 10 logarithm of y is the power to which the number 10 must be raised to obtain the value y.

 **Example:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing numpy

import numpy

 

# natural logarithm

print("natural logarithm -")

arr = numpy.array([6, 2, 3, 4, 5])

print(numpy.log(arr))

 

# Base 2 logarithm

print("Base 2 logarithm -")

arr = numpy.array([6, 2, 3, 4, 5])

print(numpy.log2(arr))

 

# Base 10 logarithm

print("Base 10 logarithm -")

arr = numpy.array([6, 2, 3, 4, 5])

print(numpy.log10(arr))  
  
---  
  
 __

 __

 **Output:**

    
    
    natural logarithm -
    [1.79175947 0.69314718 1.09861229 1.38629436 1.60943791]
    Base 2 logarithm -
    [2.5849625  1.         1.5849625  2.         2.32192809]
    Base 10 logarithm -
    [0.77815125 0.30103    0.47712125 0.60205999 0.69897   ]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

