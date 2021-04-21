numpy.where() in Python



The **numpy.where()** function returns the indices of elements in an input
array where the given condition is satisfied.

>  **Syntax :** numpy.where(condition[, x, y])  
>  **Parameters:**  
>  **condition :** When True, yield x, otherwise yield y.  
>  **x, y :** Values from which to choose. x, y and condition need to be
> broadcastable to some shape.
>
>  **Returns:**  
>  **out :** [ndarray or tuple of ndarrays] If both x and y are specified, the
> output array contains elements of x where condition is True, and elements
> from y elsewhere.
>
> If only condition is given, return the tuple condition.nonzero(), the
> indices where condition is True.

 **Code #1:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# where() function 

 

import numpy as np

 

np.where([[True, False], [True, True]],

 [[1, 2], [3, 4]], [[5, 6], [7, 8]])  
  
---  
  
 __

 __

 **Output :**

    
    
    array([[1, 6],
           [3, 4]])

**Code #2:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# where() function 

 

import numpy as np

 

# a is an array of integers.

a = np.array([[1, 2, 3], [4, 5, 6]])

 

print(a)

 

print ('Indices of elements <4')

 

b = np.where(a<4)

print(b)

 

print("Elements which are <4")

print(a[b])  
  
---  
  
 __

 __

 **Output :**

    
    
    [[1 2 3]
     [4 5 6]]
    
    Indices of elements <4
    (array([0, 0, 0], dtype=int64), array([0, 1, 2], dtype=int64))
    
    Elements which are <4
    array([1, 2, 3])
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

