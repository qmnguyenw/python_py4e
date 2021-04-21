numpy.asanyarray() in Python



 **numpy.asanyarray()** function is used when we want to convert input to an
array but it pass _ndarray_ subclasses through. Input can be scalars, lists,
lists of tuples, tuples, tuples of tuples, tuples of lists and ndarrays.

>  **Syntax :** numpy.asanyarray(arr, dtype=None, order=None)
>
>  **Parameters :**  
>  **arr :** [array_like] Input data, in any form that can be converted to an
> array. This includes scalars, lists, lists of tuples, tuples, tuples of
> tuples, tuples of lists, and ndarrays.  
>  **dtype :** [data-type, optional] By default, the data-type is inferred
> from the input data.  
>  **order :** Whether to use row-major (C-style) or column-major (Fortran-
> style) memory representation. Defaults to ‘C’.
>
>  **Return :** [ndarray or an ndarray subclass] Array interpretation of arr.
> If arr is _ndarray_ or a subclass of ndarray, it is returned as-is and no
> copy is performed.

 **Code #1 : List to array**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# numpy.asanyarray() function

 

import numpy as geek

my_list = [1, 3, 5, 7, 9]

 

print ("Input list : ", my_list)

 

 

out_arr = geek.asanyarray(my_list)

print ("output array from input list : ", out_arr)   
  
---  
  
__

__

**Output :**

    
    
    Input  list :  [1, 3, 5, 7, 9]
    output array from input list :  [1 3 5 7 9]
    

  
**Code #2 : Tuple to array**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# numpy.asanyarray() function

 

import numpy as geek

 

my_tuple = ([1, 3, 9], [8, 2, 6])

 

print ("Input tuple : ", my_tuple)

 

out_arr = geek.asanyarray(my_tuple) 

print ("output array from input tuple : ", out_arr)   
  
---  
  
__

__

**Output :**

    
    
    Input  tuple :  ([1, 3, 9], [8, 2, 6])
    output array from input tuple :  [[1 3 9]
     [8 2 6]]
    

  
**Code #3 : Scalar to array**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# numpy.asanyarray() function

 

import numpy as geek

 

my_scalar = 12

 

print ("Input scalar : ", my_scalar)

 

out_arr = geek.asanyarray(my_scalar) 

print ("output array from input scalar : ", out_arr) 

print(type(out_arr))  
  
---  
  
 __

 __

 **Output :**

    
    
    Input  scalar :  12
    output array from input scalar :  12
    class 'numpy.ndarray'
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

