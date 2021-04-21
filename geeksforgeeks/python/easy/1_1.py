How to Concatenate image using Pillow in Python ?



 **Prerequisites:** Python Pillow

Concatenate image means joining of two images. We can merge any image whether
it has different pixels, different image formats namely, ‘jpeg’, ‘png’, ‘gif’,
‘tiff’, etc. In python, we can join two images using the Python image library
also known as the pillow library. In this article, we will see how the
concatenation of images is done.

Concatenation of images can be done in two ways :

  * Horizontal
  * Vertical

###  **Concatenating images horizontally**

 **Approach:**

  * Import module
  * Open the images
  * Resize the image using Resize() function. Both the resize images should be of the same width and height so that their aspect ratio is intact and can be pasted into the new background image.
  * To create a new image it has a new() function which has 3 parameters (“mode”,(size),color)
  * Paste the image to new image using paste()

 **Program:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# library

from PIL import Image

import matplotlib.pyplot as plt

 

# opening up of images

img = Image.open("logo.png")

img1 = Image.open("logo2.png")

img.size

img1.size

img_size = img.resize((250, 90))

img1_size = img1.resize((250, 90))

 

# creating a new image and pasting 

# the images

img2 = Image.new("RGB", (500, 90), "white")

 

# pasting the first image (image_name,

# (position))

img2.paste(img_size, (0, 0))

 

# pasting the second image (image_name,

# (position))

img2.paste(img1_size, (250, 0))

 

plt.imshow(img2)  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210407000151/logomerge-300x77.png)

###  **Concatenating images vertically**

The whole code is the same as horizontal but the only change is that in
horizontal we double the width and the height is same but in vertical we make
the size of width same, but we double the height.

**Approach:**

  * Import the libraries for image processing.
  * Use Image.open() to open the library.
  * Use img.size to know the size of the image.
  * Use img.resize((width,height)) to resize the image.
  * Both the images should be of same size.
  * Create a new image using new() and pass the 3 parameters”mode”,size,”color”).
  * Size in new image should be (width, 2*height).
  * After the creation of new image, paste the first image by using paste() and pass the parameter(img_resize,(position)) #position(0,0)
  * After pasting the first image, paste the second image using paste and pass the parameter(img1_reszie, (position)). In position, width would be the same but the height would be the last position of the first image’s height. . #position=(0,180)
  * Use plt.imshow(img2) to show the concatenate of images.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# library

from PIL import Image

import matplotlib.pyplot as plt

 

 

# opening up of images

img = Image.open("logo.png")

img1 = Image.open("logo2.png")

img.size

img1.size

img_size = img.resize((250, 90))

img1_size = img1.resize((250, 90))

 

# creating a new image and pasting the 

# images

img2 = Image.new("RGB", (250, 180), "white")

 

# pasting the first image (image_name,

# (position))

img2.paste(img_size, (0, 0))

 

# pasting the second image (image_name,

# (position))

img2.paste(img1_size, (0, 90)

 

plt.imshow(img2)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210407000825/logomergevert-300x221.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

