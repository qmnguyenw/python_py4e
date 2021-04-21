How to Display an Image in Grayscale in Matplotlib?



In this article, we are going to depict images using _matplotlib_ module in
greyscale representation i.e. image representation using two colors only i.e.
black and white.

###  **Required modules**

  *  **PIL** is the Python Imaging Library which provides the python interpreter with image editing capabilities. The Image module provides a class with the same name which is used to represent a _PIL_ image. The module also provides a number of factory functions, including functions to load images from files, and to create new images. _PIL.Image.open()_ method in _PIL_ module opens and identifies the given image file.
  *  **Matplotlib** is a plotting library for creating static, animated, and interactive visualizations in Python. The _matplotlib_ module can be used in Python scripts, the Python and IPython shell, web application servers, and various graphical user interface toolkits like Tkinter, awxPython, etc.

 **Step-by-step Approach:**

  * Import required modules

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries.

import numpy as np

import matplotlib.pyplot as plt

from PIL import Image  
  
---  
  
 __

 __

  * Displaying Original picture.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# storing image path

fname = r'g4g.png'

 

# opening image using pil

image = Image.open(fname)

 

# plottingimage

plt.imshow(image)

plt.show()  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201214164308/Screenshot181-300x289.png)

  * Displaying Grayscale image, store the image path here let’s say it fname. Now open the image using PIL image method and convert it to L mode If you have an L mode image, that means it is a single-channel image – normally interpreted as greyscale. It only stores a greyscale, not color. Plotting the image as _cmap_ _= ‘gray’_ convert the colours. All the work is done you can now see your image.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# storing image path

fname = r'g4g.png'

 

# opening image using pil

image = Image.open(fname).convert("L")

 

# maping image to gray scale

plt.imshow(image, cmap='gray')

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201213142350/Screenshot170-300x289.png)

 **Below are some programs which depict how to display an image in grayscale
using Matplotlib module:**

 **Example 1:**

 **Image used:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20201213142733/gfg.png)

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries.

import numpy as np

import matplotlib.pyplot as plt

from PIL import Image

 

 

# storing image path

fname = r'gfg.png'

 

# opening image using pil

image = Image.open(fname).convert("L")

 

# maping image to gray scale

plt.imshow(image, cmap='gray')

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201213142838/Screenshot171-300x282.png)

 **Example 2:**

 **Image Used:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201213142938/geeks.png)

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries.

import numpy as np

import matplotlib.pyplot as plt

from PIL import Image

 

 

# storing image path

fname = r'geeks.png'

 

# opening image using pil

image = Image.open(fname).convert("L")

 

# maping image to gray scale

plt.imshow(image, cmap='gray')

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201213143049/Screenshot172-300x219.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

