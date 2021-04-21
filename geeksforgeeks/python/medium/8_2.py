Python Mahotas – Introduction



 **Mahotas** is a computer vision and image processing and manipulation
library for Python. A library is a collection of functions and methods that
allows you to perform many actions without having to write hundreds of lines
of code. Mahotas includes many algorithms that operates with arrays, mahotas
currently has over 100 functions for image processing and computer vision and
is constantly growing.

Mahotas provides a good solution in finding patterns in the image for example
“Where’s Wally Problem” can be solved easily using Mahotas.

 **How to install Mahotas :**

    
    
    pip install mahotas

 **Notable algorithms available in Mahotas :**

1\. Watershed  
2\. Convex points calculations.  
3\. Hit & miss, thinning.  
4\. Zernike & Haralick, LBP, and TAS features.  
5\. Speeded-Up Robust Features (SURF), a form of local features.  
6\. Thresholding.  
7\. Convolution.  
8\. Sobel edge detection.  
9\. Spline interpolation  
10\. SLIC super pixels.

  

  

 **Example 1:** Loading Image

 __

 __  
 __

 __

 __  
 __  
 __

# importing required libraries

import numpy as np

import mahotas

import pylab

 

# loading iamge

img = mahotas.imread('dog_image.png')

 

# showing the original image

imshow(img)

show()  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200617032157/final485.png)

 **Example 2:** Creating distance transform

 __

 __  
 __

 __

 __  
 __  
 __

# importing required libraries

import pylab as p

import numpy as np

import mahotas

 

# creating numpy array of type bool

f = np.ones((256, 256), bool)

 

# setting false values

f[200:, 240:] = False

f[128:144, 32:48] = False

 

# f is basically True with the exception of two islands:

# one in the lower-right

# corner, another, middle-left

 

# creating a distance using numpy array

dmap = mahotas.distance(f)

 

# showing iamge

p.imshow(dmap)

p.show()  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200617031249/final484.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

