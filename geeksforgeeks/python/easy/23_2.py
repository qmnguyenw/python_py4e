Addition and Blending of images using OpenCV in Python



When we talk about images, we know its all about the matrix either _binary
image(0, 1)_ , _gray scale image(0-255)_ or _RGB image(255 255 255)_. So
additions of the image is adding the numbers of two matrices. In OpenCV, we
have a command **_cv2.add()_** to add the images.

Below is code for Addition of two images using OpenCV :

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for adding

# images using OpenCV

 

# import OpenCV file

import cv2

 

# Read Image1

mountain = cv2.imread('F:\mountain.jpg', 1)

 

# Read image2

dog = cv2.imread('F:\dog.jpg', 1)

 

# Add the images

img = cv2.add(mountain, dog)

 

# Show the image

cv2.imshow('image', img)

 

# Wait for a key

cv2.waitKey(0)

 

# Distroy all the window open

cv2.distroyAllWindows()  
  
---  
  
 __

 __

But sometimes we do not want to perform simple addition in image, so in this
case we have blending. This is also image addition, but different weights are
given to images so that it gives a feeling of blending or transparency. Images
are added as per the equation below :

    
    
    g(x) = (1 - _a_ )f(x) + _a_ f1(x)

By varying _a_ from 0 -> 1, you can perform a cool transition between one
image to another. Here two images are taken to blend together. First image is
given a weight of 0.3 and second image is given 0.7, **_cv2.addWeighted()_**
applies following equation on the image :

    
    
    img = _a_ . img1 + _b_ . img 2 + _y_

Here _y_ is taken as zero.

  

  

Below is code for Blending of images using OpenCV :

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for blending of

# images using OpenCV

 

# import OpenCV file

import cv2

 

# Read Image1

mountain = cv2.imread('F:\mountain.jpg', 1)

 

# Read image2

dog = cv2.imread('F:\dog.jpg', 1)

 

# Blending the images with 0.3 and 0.7

img = cv2.addWeighted(mountain, 0.3, dog, 0.7, 0)

 

# Show the image

cv2.imshow('image', img)

 

# Wait for a key

cv2.waitKey(0)

 

# Distroy all the window open

cv2.distroyAllWindows()  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

