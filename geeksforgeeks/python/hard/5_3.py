Methods on NumPy.add()



The **ufunc** expect a set of scalars as input and produce a set of scalars as
output. Universal  
functions can be related to mathematical aspects such as, add, subtract,
divide, multiply, and likewise.

## Methods on numpy.add

Actually, universal functions are not functions instead, these are objects
representing functions. Here we are taking the function – add, they have two
input parameters and return one output parameter (signature mismatch of ufunc
will results in a ValueError. Hence this will work only for binary universal
functions).

 **The four methods on add are:**

  * reduce
  * accumulate
  * outer
  * reduceat

In this tutorial we are going through each of the above function in detail.

### numpy.ufunc.reduce()

The given input array is reduced by applying the universal function
recursively along a specified axis on consecutive elements.  
 **Note:** add.reduce() is equivalent to sum()

  

  

>  **Syntax:** ufunc.reduce(a, axis=0, dtype=None, out=None, keepdims=False,
> initial=, where=True)
>
>  **Parameters** **:**  
>  **a(array_like):** The array upon which processing occurs  
>  **axis(None or int or tuple of ints, optional):** Axis or axes along which
> a reduction is performed. The default is (axis = 0). Axis may be negative,
> whenever it counts backwards.None, a reduction is performed over all the
> axes.Tuple of ints, a reduction is performed on multiple axes.  
>  **dtype(data-type code, optional):** The type used to represent the
> intermediate results.  
>  **out(ndarray, None, or tuple of ndarray and None, optional):** Location
> into which the result is stored. If not provided or None, a freshly-
> allocated array is returned.  
>  **keepdims(bool, optional):** If this is set to True, the axes which are
> reduced are left in the result as dimensions with size one.  
>  **initial(scalar, optional):** The value with which to start the reduction.  
>  **where(array_like of bool, optional):** A boolean array which is
> broadcasted to match the dimensions of a, and selects elements to include in
> the reduction.
>
>  **Returns:**  
>  r : ndarray

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Reducing an array using np.add.reduce()

 

import numpy as np

 

 

# Array formation

a = np.arange(10)

 

# Reduction occurs column-wise with 

# 'int' datatype

b = np.add.reduce(a, dtype = int, axis = 0)

print("The array {0} gets reduced to {1}".format(a, b))  
  
---  
  
 __

 __

 **OUTPUT**

    
    
    The array [0 1 2 3 4 5 6 7 8 9] gets reduced to 45

### numpy.ufunc.accumulate()

It stores the intermediate results in an array and returns that. The result,
in the case of the add function, is equivalent to calling the cumsum function.

>  **Syntax:** ufunc.accumulate(array, axis=0, dtype=None, out=None)
>
>  **Parameters:**  
>  **array(array_like):** The array to act on.  
>  **axis(int, optional):** The axis along which to apply the accumulation;
> default is zero.  
>  **dtype(data-type code, optional):** The data-type used to represent the
> intermediate results. Defaults to the data-type of the output array if such
> is provided, or the data-type of the input array if no output array is
> provided.  
>  **out(ndarray, optional):** A location into which the result is stored. If
> not provided a freshly-allocated array is returned.
>
>  
>
>
>  
>
>
>  **Returns:**  
>  r : ndarray

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

 

# Array formation

a = np.arange(10)

 

# Cumulative sum of array, column wise,

# float datatype

c = np.add.accumulate(a, axis = 0, dtype = float)

 

print("The array {0} gets added cumulatively to {1}".format(a, c))  
  
---  
  
 __

 __

 **OUTPUT**

> The array [0 1 2 3 4 5 6 7 8 9] gets added cumulatively to [ 0. 1. 3. 6. 10.
> 15. 21. 28. 36. 45.]

### numpy.ufunc.outer()

The ‘outer’ method returns an array that has a rank, which is the sum of the
ranks of its two input arrays. The method is applied to all possible pairs of
the input array elements.

>  **Syntax:** ufunc.outer(A, B, **kwargs)
>
>  **Parameters:**  
>  **A(array_like):** First array  
>  **B(array_like):** Second array  
>  **kwargs(any):** Arguments to pass on to the ufunc.
>
>  **Returns:**  
>  r : ndarray

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# To find the outer of two input arrays

import numpy as np

 

 

# Initialization of a 2x2 matrix 

# as first input

a = np.arange(4).reshape(2,2)

 

# Initialization of an array as

# second input

b = np.arange(3)

 

# Outer of a & b

z = np.add.outer(b, a)

 

print("The outer of {0} & {1} is {2}".format(b,a,z))  
  
---  
  
 __

 __

 **OUTPUT**

    
    
    The outer of [0 1 2] & [[0 1]
     [2 3]] is [[[0 1]
      [2 3]]
    
     [[1 2]
      [3 4]]
    
     [[2 3]
      [4 5]]]

### numpy.ufunc.reduceat()

The ‘reduceat()‘ method requires as arguments, an input array, and a list of
indices. The reduceat() method goes through step-by-step procedures to
perform its operation. We will look up its action by four steps.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Reduceat method example

 

import numpy as np

 

 

a = np.arange(9)

z = np.add.reduceat(a, [1, 4, 2, 8])

 

print("Reduceat of matrix {} is {}".format(a,z))  
  
---  
  
 __

 __

 **OUTPUT**

> Reduceat of matrix [0 1 2 3 4 5 6 7 8] is [ 6 4 27 8]

 **STEP-1**  
It concerns with indices 1 and 4. This step results in a reduced operation of
the array elements between indices 1 and 4.

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

 

a = np.arange(9)

print("Result of STEP-I is", np.add.reduce(a[0:4]))  
  
---  
  
 __

 __

 **OUTPUT**

    
    
    Result of STEP-I is 6

 **STEP-2**  
The second step concerns indices 4 and 2. Since 2 is less than 4, the array
element at index 4 is returned:

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

 

a = np.arange(9)

print("Result of STEP-II is", a[4])  
  
---  
  
 __

 __

 **OUTPUT**

    
    
    Result of STEP-II is 4

 **STEP-3**  
The third step concerns indices 2 and 8. This step results in a reduce
operation of the array elements between indices 2 and 8:

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

 

a = np.arange(9)

print("Result of STEP-III is", np.add.reduce(a[2:8]))  
  
---  
  
 __

 __

 **OUTPUT**

    
    
    Result of STEP-III is 27

 **STEP-4**  
The fourth step concerns index 8. This step results in a reduce operation of
the array elements from index 8 to the end of the array:

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

 

a = np.arange(9)

print("Result of step IV is", np.add.reduce(a[8:]))  
  
---  
  
 __

 __

 **OUTPUT**

    
    
    Result of step IV is 8

By going through all this step we get the output of ‘numpy.add.reduceat’.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

