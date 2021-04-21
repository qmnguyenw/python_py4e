numpy.add() in Python



 **numpy.add()** function is used when we want to compute the addition of
two array. It add arguments element-wise. If shape of two arrays are not same,
that is arr1.shape != arr2.shape, they must be broadcastable to a common
shape (which may be the shape of one or the other).

>  **Syntax :** numpy.add(arr1, arr2, /, out=None, *, where=True,
> casting=’same_kind’, order=’K’, dtype=None, subok=True[, signature, extobj],
> ufunc ‘add’)
>
>  **Parameters :**  
>  **arr1 :** [array_like or scalar] Input array.  
>  **arr2 :** [array_like or scalar] Input array.  
>  **out :** [ndarray, optional] A location into which the result is stored.  
>  -> If provided, it must have a shape that the inputs broadcast to.  
>  -> If not provided or None, a freshly-allocated array is returned.  
>  **where :** [array_like, optional] Values of True indicate to calculate the
> ufunc at that position, values of False indicate to leave the value in the
> output alone.  
>  ****kwargs :** Allows to pass keyword variable length of argument to a
> function. Used when we want to handle named argument in a function.
>
>  **Return :** [ndarray or scalar] The sum of arr1 and arr2, element-wise.
> Returns a scalar if both arr1 and arr2 are scalars.

 **Code #1 : Working**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# numpy.add() function

# when inputs are scalar

 

import numpy as geek

in_num1 = 10

in_num2 = 15

 

print ("1st Input number : ", in_num1)

print ("2nd Input number : ", in_num2)

 

out_num = geek.add(in_num1, in_num2) 

print ("output number after addition : ", out_num)   
  
---  
  
__

__

**Output :**

    
    
    1st Input  number :  10
    2nd Input  number :  15
    output number after addition  :  25
    

  
**Code #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# numpy.add() function

# when inputs are array

 

import numpy as geek

 

in_arr1 = geek.array([[2, -7, 5], [-6, 2,
0]])

in_arr2 = geek.array([[5, 8, -5], [3, 6, 9]])

 

print ("1st Input array : ", in_arr1) 

print ("2nd Input array : ", in_arr2) 

 

out_arr = geek.add(in_arr1, in_arr2) 

print ("output added array : ", out_arr)   
  
---  
  
__

__

**Output :**

    
    
    1st Input array :  [[ 2 -7  5]
     [-6  2  0]]
    2nd Input array :  [[ 5  8 -5]
     [ 3  6  9]]
    output added array :  [[ 7  1  0]
     [-3  8  9]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

