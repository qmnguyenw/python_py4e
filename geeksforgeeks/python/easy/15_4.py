numpy.multiply() in Python



 **numpy.multiply()** function is used when we want to compute the
multiplication of two array. It returns the product of arr1 and arr2, element-
wise.

>  **Syntax :** numpy.multiply(arr1, arr2, /, out=None, *, where=True,
> casting=’same_kind’, order=’K’, dtype=None, subok=True[, signature, extobj],
> ufunc ‘multiply’)
>
>  **Parameters :**  
>  **arr1:** [array_like or scalar]1st Input array.  
>  **arr2:** [array_like or scalar]2nd Input array.  
>  **dtype:** The type of the returned array. By default, the _dtype_ of arr
> is used.  
>  **out:** [ndarray, optional] A location into which the result is stored.  
>  -> If provided, it must have a shape that the inputs broadcast to.  
>  -> If not provided or None, a freshly-allocated array is returned.  
>  **where:** [array_like, optional] Values of True indicate to calculate the
> ufunc at that position, values of False indicate to leave the value in the
> output alone.  
>  ****kwargs:** Allows to pass keyword variable length of argument to a
> function. Used when we want to handle named argument in a function.
>
>  **Return:** [ndarray or scalar] The product of arr1 and arr2, element-wise.

 **Example #1 :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# numpy.multiply() function

 

import numpy as geek

in_num1 = 4

in_num2 = 6

 

print ("1st Input number : ", in_num1)

print ("2nd Input number : ", in_num2)

 

out_num = geek.multiply(in_num1, in_num2) 

print ("output number : ", out_num)   
  
---  
  
__

__

**Output :**

    
    
    1st Input number :  4
    2nd Input number :  6
    output number :  24
    

**Example #2 :**  
The following code is also known as the Hadamard product which is nothing but
the element-wise-product of the two matrices. It is the most commonly used
product for those who are interested in Machine Learning or statistics.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# numpy.multiply() function

 

import numpy as geek

 

in_arr1 = geek.array([[2, -7, 5], [-6, 2,
0]])

in_arr2 = geek.array([[0, -7, 8], [5, -2,
9]])

 

print ("1st Input array : ", in_arr1)

print ("2nd Input array : ", in_arr2)

 

 

out_arr = geek.multiply(in_arr1, in_arr2) 

print ("Resultant output array: ", out_arr)   
  
---  
  
__

__

**Output :**

    
    
    1st Input array :  [[ 2 -7  5]
     [-6  2  0]]
    2nd Input array :  [[ 0 -7  8]
     [ 5 -2  9]]
    Resultant output array:  [[  0  49  40]
     [-30  -4   0]]
    

Another way to find the same is

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as geek

in_arr1=geek.matrix([[2, -7, 5], [-6, 2,
0]])

in_arr2 = geek.matrix([[0, -7, 8], [5, -2,
9]])

 

print ("1st Input array : ", in_arr1)

print ("2nd Input array : ", in_arr2)

 

out_arr=geek.array(in_arr1)*geek.array(in_arr2)

print ("Resultant output array: ", out_arr)  
  
---  
  
 __

 __

 **Output :**

    
    
    1st Input array :  [[ 2 -7  5]
     [-6  2  0]]
    2nd Input array :  [[ 0 -7  8]
     [ 5 -2  9]]
    Resultant output array:  [[  0  49  40]
     [-30  -4   0]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

