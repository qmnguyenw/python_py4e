Python | Grayscaling of Images using OpenCV



 **Grayscaling** is the process of converting an image from other color spaces
e.g RGB, CMYK, HSV, etc. to shades of gray. It varies between complete black
and complete white.

###

Importance of grayscaling –

  *  **Dimension reduction:** For e.g. In RGB images there are three color channels and has three dimensions while grayscaled images are single dimensional.
  *  **Reduces model complexity:** Consider training neural article on RGB images of 10x10x3 pixel.The input layer will have 300 input nodes. On the other hand, the same neural network will need only 100 input node for grayscaled images.
  *  **For other algorithms to work:** There are many algorithms that are customized to work only on grayscaled images e.g. Canny edge detection function pre-implemented in OpenCV library works on Grayscaled images only.

Below is the code to Grayscale an image-

 __

 __  
 __

 __

 __  
 __  
 __

# importing opencv

import cv2

 

# Load our input image

image = cv2.imread('C:\\Documents\\full_path\\tomatoes.jpg')

cv2.imshow('Original', image)

cv2.waitKey()

 

# We use cvtColor, to convert to grayscale

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

 

cv2.imshow('Grayscale', gray_image)

cv2.waitKey(0) 

 

# window shown waits for any key pressing event

cv2.destroyAllWindows()  
  
---  
  
 __

 __

 **Input image:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190413234936/Screenshot-2741-300x213.png)  
 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190413235036/Screenshot-2751-300x213.png)

  
**Faster code –**

 __

 __  
 __

 __

 __  
 __  
 __

# Faster method

import cv2

 

# The second argument zero specifies that

# image is to be read in grayscale mode.

img = cv2.imread('C:\\Documents\\full_path\\tomatoes.jpg', 0) 

 

cv2.imshow('Grayscale', img)

cv2.waitKey()

 

cv2.destroyAllWindows()  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

