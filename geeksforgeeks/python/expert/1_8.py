Cropping an Image in a circular way using Python



In this article, we will learn to crop an image circularly using a pillow
library. Cropping an image circularly means selecting a circular region inside
an image and removing everything outside the circle.

**Approach:**

  * If you have an L mode image, the image becomes grayscale. So we create a new image with mode “L”.
  * An image is created with a white circle in the middle with dimensions same as the input image.
  * Convert a new image to an array.
  * Convert original image from an array.
  * Stack these two arrays together to crop out only the circular middle part.

 **Let’s take this initial image :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210201163555/gfg-300x300.jpeg)

 **Step 1:** Import the module and read the image.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

from PIL import Image, ImageDraw

 

 

img = Image.open("/content/gfg.jpeg")

display(img)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210201163555/gfg-300x300.jpeg)

 **Step 2:** Create an image.

We will use pieslice() function to get the circular part of the image in
white, then we will superimpose the original image and the luminous image.

 **ImageDraw.Draw.pieslice()** Same as arc, but also draws straight lines
between the endpoints and the center of the bounding box.

>  _ **Syntax:** PIL.ImageDraw.Draw.pieslice(xy, start, end, fill=None,
> outline=None)_
>
>  _ **Parameters:**_  
>  _ **xy** – Four points to define the bounding box. Sequence of [(x0, y0),
> (x1, y1)] or [x0, y0, x1, y1]._  
>  _ **start** – Starting angle, in degrees. Angles are measured from 3
> o’clock, increasing clockwise._  
>  _ **end** – Ending angle, in degrees._  
>  _ **fill** – Color to use for the fill._  
>  _ **outline** – Color to use for the outline._
>
>  _ **Returns:** An Image object in pieslice shape._

 **Code:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

h,w= img.size

 

# creating luminous image

lum_img = Image.new('L',[h,w] ,0) 

draw = ImageDraw.Draw(lum_img)

draw.pieslice([(0,0),(h,w)],0,360,fill=255)

img_arr = np.array(img)

lum_img_arr = np.array(lum_img)

display(Image.fromarray(lum_img_arr))  
  
---  
  
 __

 __

