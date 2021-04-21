Reading an image in OpenCV using Python



 **Prerequisite:** Basics of OpenCV

In this article, we’ll try to open an image by using OpenCV (Open Source
Computer Vision). To use the OpenCV library in python, we need to install
these libraries as a prerequisite:

  1. Numpy Library (Necessary, because OpenCV uses it in the background).
  2. OpenCV python  

**To install these libraries, we need to run these pip commands in cmd:**

    
    
    pip install opencv-python
    pip install numpy
    pip install matplotlib

To read the images cv2.imread() method is used. This method loads an image
from the specified file. If the image cannot be read (because of missing file,
improper permissions, unsupported or invalid format) then this method returns
an empty matrix.

>  _ **Syntax:** cv2.imread(path, flag)_
>
>  _ **Parameters:**_  
>  _ **path:** A string representing the path of the image to be read._  
>  _ **flag:** It specifies the way in which image should be read. It’s
> default value is **cv2.IMREAD_COLOR**_
>
>  _ **Return Value:** This method returns an image that is loaded from the
> specified file._

 **Note:** The image should be in the working directory or a full path of
image should be given.

  

  

All three types of flags are described below:

>  _ **cv2.IMREAD_COLOR:** It specifies to load a color image. Any
> transparency of image will be neglected. It is the default flag.
> Alternatively, we can pass integer value **1** for this flag._  
>  _ **cv2.IMREAD_GRAYSCALE:** It specifies to load an image in grayscale
> mode. Alternatively, we can pass integer value **0** for this flag._  
>  _ **cv2.IMREAD_UNCHANGED:** It specifies to load an image as such including
> alpha channel. Alternatively, we can pass integer value **-1** for this
> flag._

Below codes are implementations to read images and display images on the
screen using OpenCV and matplotlib libraries functions.  
  
**Example #1 (Using OpenCV) :**

**Image Used:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190802021607/geeks14.png)

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to read image

import cv2

# To read image from disk, we use

# cv2.imread function, in below method,

img = cv2.imread("geeksforgeeks.png", cv2.IMREAD_COLOR)

# Creating GUI window to display an image on screen

# first Parameter is windows title (should be in string format)

# Second Parameter is image array

cv2.imshow("Cute Kitens", img)

# To hold the window on screen, we use cv2.waitKey method

# Once it detected the close input, it will release the control

# To the next line

# First Parameter is for holding screen for specified milliseconds

# It should be positive integer. If 0 pass an parameter, then it will

# hold the screen until user close it.

cv2.waitKey(0)

# It is for removing/deleting created GUI window from screen

# and memory

cv2.destroyAllWindows()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190802022327/Annotation-2019-08-02-022111.png)

 **Example #2:** Opening in grascale mode

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain cv2.imread() method

# importing cv2

import cv2

# path

path = r'geeksforgeeks.png'

# Using cv2.imread() method

# Using 0 to read image in grayscale mode

img = cv2.imread(path, 0)

# Displaying the image

cv2.imshow('image', img)  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190802022316/Annotation-2019-08-02-022133.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

