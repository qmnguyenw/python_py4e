Python Pillow – Creating a Watermark



In this article, we will see how the creation of a watermark is done using the
Pillow library in Python. Pillow is a Python Image Library(PIL) that is used
for manipulating images and working on the different formats of images like
(‘jpeg’, ‘png’, ‘gif’, ‘tiff’ etc.). There are various image processing you
can do using pillow library like resizing, creating watermarks, rotation of
the image, merging various images, blurring the image, etc. PIL displays the
image in a photo viewer.

 **Installation:**

To install the library, run the below command in your command prompt.

    
    
    python -m pip install pip

or

    
    
    python -m pip install pillow

If pip and pillow are already installed in your device, the system would
mention “Requirement already satisfied:”

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210327143347/Screenshot180.png)

There are two types of watermark:

  1. Text watermark,
  2. Image watermark.

##  **Text Watermark**

It is an approach for text documentation copyright protection. In an image, we
can place some simple custom text on images in different fonts and formats.

 **Step 1:** Import all the libraries

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the library

from PIL import Image

import matplotlib.pyplot as plt

import numpy as np  
  
---  
  
 __

 __

**Step 2:** Open the image using a photo viewer.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

image= Image.open("puppy.jpg")

 

# this open the photo viewer

image.show() 

plt.imshow(image)  
  
---  
  
 __

 __

