numpy.argwhere() in Python



 **numpy.argwhere()** function is used to find the indices of array elements
that are non-zero, grouped by element.

>  **Syntax :** numpy.argwhere(arr)
>
>  **Parameters :**  
>  **arr :** [array_like] Input array.
>
>  **Return :** [ndarray] Indices of elements that are non-zero. Indices are
> grouped by element.

 **Code #1 :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# argwhere() function

 

import numpy as geek

 

# input array

in_arr = [[ 2, 0, 7], [ 0, 5, 9]]

print ("Input array : ", in_arr) 

 

out_arr = geek.argwhere(in_arr)

print ("Output indices of non zero array element: \n", out_arr)  
  
---  
  
 __

 __

 **Output:**

    
    
    Input array :  [[2, 0, 7], [0, 5, 9]]
    Output indices of non zero array element: 
     [[0 0]
     [0 2]
     [1 1]
     [1 2]]
    

  
**Code #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# argwhere() function

 

import numpy as geek

 

# input array

in_arr = geek.arange(8).reshape(4, 2)

print ("Input array : ", in_arr) 

 

out_arr = geek.argwhere(in_arr>4)

print ("Output indices greater than 4: \n", out_arr)  
  
---  
  
 __

 __

 **Output:**

    
    
    Input array :  [[0 1]
     [2 3]
     [4 5]
     [6 7]]
    Output indices greater than 4: 
     [[2 1]
     [3 0]
     [3 1]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

