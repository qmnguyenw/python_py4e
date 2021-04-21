numpy.diff() in Python



 **numpy.diff(arr[, n[, axis]])** function is used when we calculate the
n-th order discrete difference along the given axis. The first order
difference is given by out[i] = arr[i+1] – arr[i] along the given axis. If we
have to calculate higher differences, we are using diff recursively.

>  **Synatx:** numpy.diff()
>
>  **Parameters:**  
>  **arr :** [array_like] Input array.  
>  **n :** [int, optional] The number of times values are differenced.  
>  **axis :** [int, optional] The axis along which the difference is taken,
> default is the last axis.
>
>  **Returns :** [ndarray]The n-th discrete difference. The output is the same
> as a except along axis where the dimension is smaller by n.

 **Code #1 :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# numpy.diff() method

 

 

# importing numpy

import numpy as geek 

 

# input array

arr = geek.array([1, 3, 4, 7, 9])

 

print("Input array : ", arr)

print("First order difference : ", geek.diff(arr))

print("Second order difference : ", geek.diff(arr, n = 2))

print("Third order difference : ", geek.diff(arr, n = 3))  
  
---  
  
 __

 __

 **Output:**

    
    
    Input array  :  [1 3 4 7 9]
    First order difference  :  [2 1 3 2]
    Second order difference :  [-1  2 -1]
    Third order difference  :  [ 3 -3]
    

  
**Code #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# numpy.diff() method

 

 

# importing numpy

import numpy as geek 

 

# input array

arr = geek.array([[1, 2, 3, 5], [4, 6, 7,
9]])

 

print("Input array : ", arr)

print("Difference when axis is 0 : ", geek.diff(arr, axis = 0))

print("Difference when axis is 1 : ", geek.diff(arr, axis = 1))  
  
---  
  
 __

 __

 **Output:**

    
    
    Input array  :  [[1 2 3 5]
     [4 6 7 9]]
    Difference with axis 0 :  [[3 4 4 4]]
    Difference with axis 1 :  [[1 1 2]
     [2 1 2]]
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

