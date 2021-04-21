How to convert a list and tuple into NumPy arrays?



In this article, let’s discuss how to convert a list and tuple into arrays
using NumPy. NumPy provides various methods to do the same. Let’s discuss them

 **Method 1:** Using numpy.asarray()

It converts the input to an array. The input may be lists of tuples, tuples,
tuples of tuples, tuples of lists and ndarray.

 **Syntax:**

    
    
    numpy.asarray(  a, type = None, order = None ) 

**Example:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

 

# list

list1 = [3, 4, 5, 6]

print(type(list1))

print(list1)

print()

 

# conversion

array1 = np.asarray(list1)

print(type(array1))

print(array1)

print()

 

# tuple

tuple1 = ([8, 4, 6], [1, 2, 3])

print(type(tuple1))

print(tuple1)

print()

 

# conversion

array2 = np.asarray(tuple1)

print(type(array2))

print(array2)  
  
---  
  
 __

 __

 **Output:**

    
    
    <class 'list'>
    [3, 4, 5, 6]
    
    <class 'numpy.ndarray'>
    [3 4 5 6]
    
    <class 'tuple'>
    ([8, 4, 6], [1, 2, 3])
    
    <class 'numpy.ndarray'>
    [[8 4 6]
     [1 2 3]]
    

**Method 2:** Using numpy.array()

It creates an array.

>  **Syntax:** numpy.array( object, dtype = None, *, copy = True, order = ‘K’,
> subok = False, ndmin = 0 )
>
>  **Parameters:**
>
>   1.  **object:** array-like
>   2.  **dtype:** data-type, optional ( The desired data-type for the array.
> If not given, then the type will be determined as the minimum type required
> to hold the objects in the sequence. )
>   3.  **copy:** bool, optional ( If true (default), then the object is
> copied. Otherwise, a copy will only be made if __array__ returns a copy, if
> obj is a nested sequence, or if a copy is needed to satisfy any of the other
> requirements (dtype, order, etc.). )
>   4.  **order:** {‘K’, ‘A’, ‘C’, ‘F’}, optional ( same as above )
>   5.  **subok:** bool, optional ( If True, then sub-classes will be passed-
> through, otherwise the returned array will be forced to be a base-class
> array (default). )
>   6.  **ndmin:** int, optional ( Specifies the minimum number of dimensions
> that the resulting array should have. Ones will be pre-pended to the shape
> as needed to meet this requirement. )
>

>
>  **Returns:** ndarray ( An array object satisfying the specified
> requirements. )

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

 

# list

list1 = [1, 2, 3]

print(type(list1))

print(list1)

print()

 

# conversion

array1 = np.array(list1)

print(type(array1))

print(array1)

print()

 

# tuple

tuple1 = ((1, 2, 3))

print(type(tuple1))

print(tuple1)

print()

 

# conversion

array2 = np.array(tuple1)

print(type(array2))

print(array2)

print()

 

# list, array and tuple

array3 = np.array([tuple1, list1, array2])

print(type(array3))

print(array3)  
  
---  
  
 __

 __

 **Output:**

    
    
    <class 'list'>
    [1, 2, 3]
    
    <class 'numpy.ndarray'>
    [1 2 3]
    
    <class 'tuple'>
    (1, 2, 3)
    
    <class 'numpy.ndarray'>
    [1 2 3]
    
    <class 'numpy.ndarray'>
    [[1 2 3]
     [1 2 3]
     [1 2 3]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

