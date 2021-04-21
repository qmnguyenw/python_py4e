numpy.ceil() in Python



The **numpy.ceil()** is a mathematical function that returns the ceil of the
elements of array. The ceil of the scalar x is the smallest integer i, such
that i >= x

>  **Syntax :** numpy.ceil(x[, out]) = ufunc ‘ceil’)  
>  **Parameters :**  
>  **a :** _[array_like]_ Input array
>
>  **Return :** The ceil of each element with float data-type.

  
**Code #1 : Working**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# ceil() function

import numpy as np

 

in_array = [.5, 1.5, 2.5, 3.5, 4.5, 10.1]

print ("Input array : \n", in_array)

 

ceiloff_values = np.ceil(in_array)

print ("\nRounded values : \n", ceiloff_values)

 

 

in_array = [.53, 1.54, .71]

print ("\nInput array : \n", in_array)

 

ceiloff_values = np.ceil(in_array)

print ("\nRounded values : \n", ceiloff_values)

 

in_array = [.5538, 1.33354, .71445]

print ("\nInput array : \n", in_array)

 

ceiloff_values = np.ceil(in_array)

print ("\nRounded values : \n", ceiloff_values)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    Input array : 
     [0.5, 1.5, 2.5, 3.5, 4.5, 10.1]
    
    Rounded values : 
     [  1.   2.   3.   4.   5.  11.]
    
    Input array : 
     [0.53, 1.54, 0.71]
    
    Rounded values : 
     [ 1.  2.  1.]
    
    Input array : 
     [0.5538, 1.33354, 0.71445]
    
    Rounded values : 
     [ 1.  2.  1.]
    

**Code #2 : Working**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# ceil() function

import numpy as np

 

in_array = [1.67, 4.5, 7, 9, 12]

print ("Input array : \n", in_array)

 

ceiloff_values = np.ceil(in_array)

print ("\nRounded values : \n", ceiloff_values)

 

 

in_array = [133.000, 344.54, 437.56, 44.9, 1.2]

print ("\nInput array : \n", in_array)

 

ceiloff_values = np.ceil(in_array)

print ("\nRounded values upto 2: \n", ceiloff_values)  
  
---  
  
 __

 __

 **Output :**

    
    
    Input array : 
     [1.67, 4.5, 7, 9, 12]
    
    Rounded values : 
     [  2.   5.   7.   9.  12.]
    
    Input array : 
     [133.0, 344.54, 437.56, 44.9, 1.2]
    
    Rounded values upto 2: 
     [ 133.  345.  438.   45.    2.]

  
**References :** https://docs.scipy.org/doc/numpy-
dev/reference/generated/numpy.ceil.html#numpy.ceil  
.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

