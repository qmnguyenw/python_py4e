numpy.random.randn() in Python



The **numpy.random.randn()** function creates an array of specified shape and
fills it with random values as per **standard normal** distribution.

If positive arguments are provided, randn generates an array of shape (d0, d1,
…, dn), filled with random floats sampled from a **univariate “normal”
(Gaussian) distribution of mean 0 and variance 1** (if any of the d_i are
floats, they are first converted to integers by truncation). A single float
randomly sampled from the distribution is returned if no argument is provided.

 **Syntax :**

    
    
    numpy.random.randn(d0, d1, ..., dn)

 **Parameters :**

    
    
    **d0, d1, ..., dn :** [int, optional]Dimension of the returned array we require, 
         If no argument is given a single Python float is returned.
    

**Return :**

  

  

    
    
    Array of defined shape, filled with random floating-point samples from 
    the standard normal distribution.
    

**Code 1 : randomly constructing 1D array**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.random.randn() method

 

import numpy as geek

 

# 1D Array

array = geek.random.randn(5)

print("1D Array filled with random values : \n", array);  
  
---  
  
 __

 __

 **Output :**

    
    
    1D Array filled with randnom values : 
     [-0.51733692  0.48813676 -0.88147002  1.12901958  0.68026197]
    
    

**Code 2 : randomly constructing 2D array**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.random.randn() method

 

import numpy as geek

 

# 2D Array 

array = geek.random.randn(3, 4)

print("2D Array filled with random values : \n", array);  
  
---  
  
 __

 __

 **Output :**

    
    
    2D Array filled with random values : 
     [[ 1.33262386 -0.88922967 -0.07056098  0.27340112]
     [ 1.00664965 -0.68443807  0.43801295 -0.35874714]
     [-0.19289416 -0.42746963 -1.80435223  0.02751727]]
    

**Code 3 : randomly constructing 3D array**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.random.randn() method

 

import numpy as geek

 

# 3D Array 

array = geek.random.randn(2, 2 ,2)

print("3D Array filled with random values : \n", array);  
  
---  
  
 __

 __

 **Output :**

    
    
    3D Array filled with random values : 
     [[[-0.00416587 -0.66211158]
      [-0.97254293 -0.68981333]]
    
     [[-0.18304476 -0.8371425 ]
      [ 2.18985366 -0.9740637 ]]]
    

**  
Code 4 : Manipulations with randomly created array**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.random.randn() method

 

import numpy as geek

 

# 3D Array 

array = geek.random.randn(2, 2 ,2)

print("3D Array filled with random values : \n", array);

 

# Multiplying values with 3

print("\nArray * 3 : \n", array *3)

 

# Or we cab directly do so by 

array = geek.random.randn(2, 2 ,2) * 3 + 2

print("\nArray * 3 + 2 : \n", array);  
  
---  
  
 __

 __

 **Output :**

    
    
    3D Array filled with random values : 
     [[[ 1.9609643  -1.89882763]
      [ 0.52252173  0.08159455]]
    
     [[-0.6060213  -0.86759247]
      [ 0.53870235 -0.77388125]]]
    
    Array * 3 : 
     [[[ 5.88289289 -5.69648288]
      [ 1.56756519  0.24478366]]
    
     [[-1.81806391 -2.6027774 ]
      [ 1.61610704 -2.32164376]]]
    
    Array * 3 + 2 : 
     [[[-2.73766306  6.80761741]
      [-1.57909191 -1.64195796]]
    
     [[ 0.51019498  1.30017345]
      [ 3.8107863  -4.07438963]]]

 **References :**  
https://docs.scipy.org/doc/numpy-
dev/reference/generated/numpy.random.randn.html

 **Note :**  
These codes won’t run on online-ID. Please run them on your systems to explore
the working.  
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

