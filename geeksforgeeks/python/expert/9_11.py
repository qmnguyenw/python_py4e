numpy.delete() in Python



The **numpy.delete()** function returns a new array with the deletion of sub-
arrays along with the mentioned axis.

**Syntax:**

    
    
    numpy.delete(array, object, axis = None)

 **Parameters :**

    
    
     **array   :** [array_like]Input array. 
    **object  :** [int, array of ints]Sub-array to delete
    **axis    :** Axis along which we want to delete sub-arrays. By default, it object is applied to  
                    flattened array
    
    

**Return :**

    
    
    An array with sub-array being deleted as per the mentioned object along a given axis. 
    

**Code 1 : Deletion from 1D array**  

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.delete()

 

import numpy as geek

 

#Working on 1D

arr = geek.arange(5)

print("arr : \n", arr)

print("Shape : ", arr.shape)

 

# deletion from 1D array 

 

object = 2

a = geek.delete(arr, object)

print("\ndeleteing {} from array : \n {}".format(object,a))

print("Shape : ", a.shape)

 

object = [1, 2]

b = geek.delete(arr, object)

print("\ndeleteing {} from array : \n {}".format(object,a))

print("Shape : ", a.shape)  
  
---  
  
 __

 __

 **Output :**  

    
    
    arr : 
     [0 1 2 3 4]
    Shape :  (5,)
    
    deleteing arr 2 times : 
     [0 1 3 4]
    Shape :  (4,)
    
    deleteing arr 3 times : 
     [0 3 4]
    Shape :  (4,)
    

**Code 2 :**  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.delete()

 

import numpy as geek

 

#Working on 1D

arr = geek.arange(12).reshape(3, 4)

print("arr : \n", arr)

print("Shape : ", arr.shape)

 

# deletion from 2D array 

a = geek.delete(arr, 1, 0)

'''

 [[ 0 1 2 3]

 [ 4 5 6 7] -> deleted

 [ 8 9 10 11]]

'''

print("\ndeleteing arr 2 times : \n", a)

print("Shape : ", a.shape)

 

# deletion from 2D array 

a = geek.delete(arr, 1, 1)

'''

 [[ 0 1* 2 3]

 [ 4 5* 6 7] 

 [ 8 9* 10 11]]

 ^

 Deletion

'''

print("\ndeleteing arr 2 times : \n", a)

print("Shape : ", a.shape)  
  
---  
  
 __

 __

 **Output :**  

    
    
    arr : 
     [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    Shape :  (3, 4)
    
    deleteing arr 2 times : 
     [[ 0  1  2  3]
     [ 8  9 10 11]]
    Shape :  (2, 4)
    
    deleteing arr 2 times : 
     [[ 0  2  3]
     [ 4  6  7]
     [ 8 10 11]]
    Shape :  (3, 3)
    
    deleteing arr 3 times : 
     [ 0  3  4  5  6  7  8  9 10 11]
    Shape :  (3, 3)
    
    

**Code 3: Deletion performed using Boolean Mask**  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.delete()

 

import numpy as geek

 

arr = geek.arange(5)

print("Original array : ", arr)

mask = geek.ones(len(arr), dtype=bool)

 

# Equivalent to np.delete(arr, [0,2,4], axis=0)

mask[[0,2]] = False

print("\nMask set as : ", mask)

result = arr[mask,...]

print("\nDeletion Using a Boolean Mask : ", result)  
  
---  
  
 __

 __

 **Output :**  

    
    
    Original array :  [0 1 2 3 4]
    
    Mask set as :  [False  True False  True  True]
    
    Deletion Using a Boolean Mask :  [1 3 4]
    

**References :**  
https://docs.scipy.org/doc/numpy/reference/generated/numpy.delete.html  
 **Note :**  
These codes won’t run on online-ID. Please run them on your systems to explore
the working  
.  
This article is contributed by **Mohit Gupta_OMG 😀**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

