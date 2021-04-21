numpy.mean() in Python



 **numpy.mean(arr, axis = None) : **Compute the arithmetic mean (average) of
the given data (array elements) along the specified axis.

>  **Parameters :**  
>  **arr :** [array_like]input array.  
>  **axis :** [int or tuples of int]axis along which we want to calculate the
> arithmetic mean. Otherwise, it will consider arr to be flattened(works on
> all  
> the axis). axis = 0 means along the column and axis = 1 means working along
> the row.  
>  **out :** [ndarray, optional]Different array in which we want to place the
> result. The array must have the same dimensions as expected output.  
>  **dtype :** [data-type, optional]Type we desire while computing mean.
>
>  **Results :** Arithmetic mean of the array (a scalar value if axis is none)
> or array with mean values along specified axis.

 **Code #1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.mean() method 

import numpy as np

 

# 1D array 

arr = [20, 2, 7, 1, 34]

 

print("arr : ", arr) 

print("mean of arr : ", np.mean(arr))

   
  
---  
  
__

__

**Output :**

  

  

    
    
    arr :  [20, 2, 7, 1, 34]
    mean of arr :  12.8
    

  
**Code #2:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.mean() method 

import numpy as np

 

 

# 2D array 

arr = [[14, 17, 12, 33, 44], 

 [15, 6, 27, 8, 19], 

 [23, 2, 54, 1, 4, ]] 

 

# mean of the flattened array 

print("\nmean of arr, axis = None : ", np.mean(arr)) 

 

# mean along the axis = 0 

print("\nmean of arr, axis = 0 : ", np.mean(arr, axis = 0)) 

 

# mean along the axis = 1 

print("\nmean of arr, axis = 1 : ", np.mean(arr, axis = 1))

 

out_arr = np.arange(3)

print("\nout_arr : ", out_arr) 

print("mean of arr, axis = 1 : ", 

 np.mean(arr, axis = 1, out = out_arr))  
  
---  
  
 __

 __

 **Output :**

    
    
    mean of arr, axis = None :  18.6
    
    mean of arr, axis = 0 :  [17.33333333  8.33333333 31.         14.         22.33333333]
    
    mean of arr, axis = 1 :  [24.  15.  16.8]
    
    out_arr :  [0 1 2]
    mean of arr, axis = 1 :  [24 15 16]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

