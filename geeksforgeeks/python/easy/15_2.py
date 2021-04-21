Python | OpenCV program to read and save an Image



OpenCV (Open Source Computer Vision) is a library of programming functions
mainly aimed at real-time computer vision. This is cross-platform library, it
provides functions that are used in multiple languages.

Coming to image processing, OpenCV enables us to perform multiple operations
on image, but in order to do that we need to read an image file as input, then
we can perform the desired operation and we can save it.

Let’s see a simple operation to read the image file using OpenCV library and
then save it.

 **Functions used :**

>  **- > imread(Location_of_image, integer): **The second parameter is an
> integer for changing the color of image. -1 To read image Unchanged and 0 To
> read image in gray scale.
>
>  
>
>
>  
>
>
>  **- > imwrite(Name_after_save, variable_containing_read_image)**
>
>  **- >waitKey(0):** After execution will keep the window open till a key is
> pressed
>
>  **- > destroyAllWindow():** It will close all the windows that were opened
> during the program run.

Below is the Python implementation:

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program To Read And Save image

import numpy as np

import cv2

 

# This will give error if you don't have a cv2 module

img = cv2.imread("G:\demo.jpg", -1)

 

# img is object of cv2 and stores the image read demo.jpg

cv2.imwrite("outputimage.jpg", img)

 

# The image is saved in folder where program is stored

cv2.waitKey(0)

 

cv2.destroyAllWindow()  
  
---  
  
 __

 __

 **Input :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/download-50.png)

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/upload2-2.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

