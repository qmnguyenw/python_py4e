sciPy stats.mean() function | Python



 **scipy.stats.mean(array, axis=0)** function calculates the arithmetic mean
of the array elements along the specified axis of the array (list in python).

It’s formula –  
![](https://media.geeksforgeeks.org/wp-content/uploads/mean-arithmetic.jpg)

>  **Parameters :**  
>  **array:** Input array or object having the elements to calculate the
> arithmetic mean.  
>  **axis:** Axis along which the mean is to be computed. By default axis = 0
>
>  **Returns :** Arithmetic mean of the array elements based on the set
> parameters.

 **Code #1:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Arithmetic Mean

 

import scipy

 

arr1 = scipy.mean([1, 3, 27]) 

 

print("Arithmetic Mean is :", arr1)   
  
---  
  
__

__

**Output:**

    
    
    Arithmetic Mean is : 10.3333333333
    

**Code #2:** With multi-dimensional data

 __

 __  
 __

 __

 __  
 __  
 __

# Arithmetic Mean

 

from scipy import mean

 

arr1 = [[1, 3, 27], 

 [3, 4, 6], 

 [7, 6, 3], 

 [3, 6, 8]] 

 

print("Arithmetic Mean is :", mean(arr1)) 

 

# using axis = 0

print("\nArithmetic Mean is with default axis = 0 : \n", 

 mean(arr1, axis = 0))

 

# using axis = 1

print("\nArithmetic Mean is with default axis = 1 : \n", 

 mean(arr1, axis = 1))   
  
---  
  
__

__

**Output:**

    
    
    Arithmetic Mean is : 6.41666666667
    
    Arithmetic Mean is with default axis = 0 : 
     [  3.5    4.75  11.  ]
    
    Arithmetic Mean is with default axis = 1 : 
     [ 10.33333333   4.33333333   5.33333333   5.66666667]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

