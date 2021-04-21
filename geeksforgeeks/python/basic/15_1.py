numpy.hstack() in Python



 **numpy.hstack()** function is used to stack the sequence of input arrays
horizontally (i.e. column wise) to make a single array.

>  **Syntax :** numpy.hstack(tup)
>
>  **Parameters :**  
>  **tup :** [sequence of ndarrays] Tuple containing arrays to be stacked. The
> arrays must have the same shape along all but the second axis.
>
>  **Return :** [stacked ndarray] The stacked array of the input arrays.

 **Code #1 :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# hstack() function

 

import numpy as geek

 

# input array

in_arr1 = geek.array([ 1, 2, 3] )

print ("1st Input array : \n", in_arr1) 

 

in_arr2 = geek.array([ 4, 5, 6] )

print ("2nd Input array : \n", in_arr2) 

 

# Stacking the two arrays horizontally

out_arr = geek.hstack((in_arr1, in_arr2))

print ("Output horizontally stacked array:\n ", out_arr)  
  
---  
  
 __

 __

 **Output:**

    
    
    1st Input array : 
     [1 2 3]
    2nd Input array : 
     [4 5 6]
    Output horizontally stacked array:
      [1 2 3 4 5 6]
    

  
**Code #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# hstack() function

 

import numpy as geek

 

# input array

in_arr1 = geek.array([[ 1, 2, 3], [ -1, -2,
-3]] )

print ("1st Input array : \n", in_arr1) 

 

in_arr2 = geek.array([[ 4, 5, 6], [ -4, -5,
-6]] )

print ("2nd Input array : \n", in_arr2) 

 

# Stacking the two arrays horizontally

out_arr = geek.hstack((in_arr1, in_arr2))

print ("Output stacked array :\n ", out_arr)  
  
---  
  
 __

 __

 **Output:**

    
    
    1st Input array : 
     [[ 1  2  3]
     [-1 -2 -3]]
    2nd Input array : 
     [[ 4  5  6]
     [-4 -5 -6]]
    Output stacked array :
      [[ 1  2  3  4  5  6]
     [-1 -2 -3 -4 -5 -6]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

