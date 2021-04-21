How to Display an OpenCV image in Python with Matplotlib?



The _OpenCV_ module is an open-source computer vision and machine learning
software library. It is a huge open-source library for computer vision,
machine learning, and image processing. _OpenCV_ supports a wide variety of
programming languages like Python, C++, Java, etc. It can process images and
videos to identify objects, faces, or even the handwriting of a human. When it
is integrated with various libraries, such as _numpy_ which is a highly
optimized library for numerical operations, then the number of weapons
increases in your Arsenal i.e whatever operations one can do in _Numpy_ can be
combined with _OpenCV_.

First, let’s look at how to display images using OpenCV:

Now there is one function called cv2.imread() which will take the path of an
image as an argument. Using this function you will read that particular image
and simply display it using the cv2.imshow() function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import required module

import cv2

 

# read the Image by giving path

image = cv2.imread('gfg.png')

 

# display that image

cv2.imshow('GFG', image)  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201106211219/output1-176x200.PNG)

DIspaly image using OpenCV

Now let’s jump into displaying the images with _Matplotlib_ module. It is an
amazing visualization library in Python for 2D plots of arrays. The
_Matplotlib_ module is a multi-platform data visualization library built on
_NumPy_ arrays and designed to work with the broader _SciPy_ stack.

We are doing minor changes to the above code to display our image with
_Matplotlib_ module.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import required module

import cv2

import matplotlib.pyplot as plt

 

# read image

image = cv2.imread('gfg.png')

 

# call imshow() using plt object

plt.imshow(image)

 

# display that image

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201106215359/output2-300x293.PNG)

image plot with Matplotlib

One can also display gray scale _OpenCV_ images with _Matplotlib_ module for
that you just need to convert colored image into a gray scale image.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import required modules

import cv2

import matplotlib.pyplot as plt

 

# read the image

image = cv2.imread('gfg.png')

 

# convert color image into grayscale image

img1 = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

 

# plot that grayscale image with Matplolib

# cmap stands for colormap

plt.imshow(img1, cmap='gray')

 

# display that image

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201107093307/output3-300x295.PNG)

Display grayscale image plot with Matplotlib

This is how we can display _OpenCV_ images in python with _Matplotlib_ module.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

