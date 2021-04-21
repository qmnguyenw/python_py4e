Benefit of NumPy arrays over Python arrays



The need for NumPy arises when we are working with multi-dimensional arrays.
The traditional array module does not support multi-dimensional arrays.

Let’s first try to create a single-dimensional array (i.e one row & multiple
columns) in Python without installing NumPy Package to get a more clear
picture.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from array import *

 

 

arr = array('i', [25, 16, 3])

print(arr)  
  
---  
  
 __

 __

 **Output:**

    
    
    array('i', [25, 16, 3])
    

Now, Let’s try to create a multi-dimensional array by using the array module.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from array import *

 

 

arr = array('i', [25, 16, 3], [5, 19, 28])

print(arr)  
  
---  
  
 __

 __

 **Output:**

    
    
    TypeError: array() takes at most 2 arguments (3 given)
    

We see that the array module does not support multi-dimensional array, this is
where we require NumPy. NumPy supports large, multi-dimensional arrays and has
a large collection of high-level math functions that can operate on those
arrays.

Let’s use NumPy to create a multi-dimensional array.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from numpy import *

 

 

arr = array ([[25, 31, 3], [5, 19, 28]])

print(arr)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[25 31  3]
     [ 5 19 28]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

