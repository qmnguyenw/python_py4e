Erosion and Dilation of images using OpenCV in python



 **Morphological operations** are a set of operations that process images
based on shapes. They apply a structuring element to an input image and
generate an output image.  
The most basic morphological operations are two: **Erosion and Dilation**  
 **Basics of Erosion:**

  * Erodes away the boundaries of foreground object
  * Used to diminish the features of an image.

 **Working of erosion:**

  1. A kernel(a matrix of odd size(3,5,7) is convolved with the image.
  2. A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
  3. Thus all the pixels near boundary will be discarded depending upon the size of kernel.
  4. So the thickness or size of the foreground object decreases or simply white region decreases in the image.

 **Basics of dilation:**

  * Increases the object area
  * Used to accentuate features

 **Working of dilation:**

  1. A kernel(a matrix of odd size(3,5,7) is convolved with the image
  2. A pixel element in the original image is ‘1’ if atleast one pixel under the kernel is ‘1’.
  3. It increases the white region in the image or size of foreground object increases

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate erosion and

# dilation of images.

import cv2

import numpy as np

 

# Reading the input image

img = cv2.imread('input.png', 0)

 

# Taking a matrix of size 5 as the kernel

kernel = np.ones((5,5), np.uint8)

 

# The first parameter is the original image,

# kernel is the matrix with which image is 

# convolved and third parameter is the number 

# of iterations, which will determine how much 

# you want to erode/dilate a given image. 

img_erosion = cv2.erode(img, kernel, iterations=1)

img_dilation = cv2.dilate(img, kernel, iterations=1)

 

cv2.imshow('Input', img)

cv2.imshow('Erosion', img_erosion)

cv2.imshow('Dilation', img_dilation)

 

cv2.waitKey(0)  
  
---  
  
 __

 __

 **The second image is the eroded form of the original image and the third
image is the dilated form.**  
![](https://media.geeksforgeeks.org/wp-content/uploads/Selection_014.png)  
 **Uses of Erosion and Dilation:**

  

  

  1. Erosion:
    * It is useful for removing small white noises.
    * Used to detach two connected objects etc.
  2. Dilation:
    * In cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won’t come back, but our object area increases.
    * It is also useful in joining broken parts of an object.

This article is contributed by **Pratima Upadhyay**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
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

