numpy.matrix() in Python



This class returns a matrix from a string of data or array-like object. Matrix
obtained is a specialised 2D array.  
 **Syntax :**

    
    
    numpy.matrix(data, dtype = None) : 

**Parameters :**

    
    
    **data  :** data needs to be array-like or string 
    **dtype :** Data type of returned array. 
         
    

**Returns :**

    
    
    data interpreted as a matrix

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.matrix class

 

import numpy as geek

 

# string input

a = geek.matrix('1 2; 3 4')

print("Via string input : \n", a, "\n\n")

 

# array-like input

b = geek.matrix([[5, 6, 7], [4, 6]])

print("Via array-like input : \n", b)  
  
---  
  
 __

 __

 **Output :**

    
    
    Via string input : 
     [[1 2]
     [3 4]] 
    
    
    Via array-like input : 
     [[[5, 6, 7] [4, 6]]]
     

**References :**  
https://docs.scipy.org/doc/numpy/reference/generated/numpy.mat.html#numpy.mat

  

  

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

