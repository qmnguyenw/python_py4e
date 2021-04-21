Image processing with Scikit-image in Python



 ** _scikit-image_** is an image processing Python package that works with
NumPy arrays which is a collection of algorithms for image processing. Let’s
discuss how to deal with images into set of information and it’s some
application in the real world.

 **Important features of scikit-image :**

> Simple and efficient tools for image processing and computer vision
> techniques.  
> Accessible to everybody and reusable in various contexts.  
> Built on the top of NumPy, SciPy, and matplotlib.  
> Open source, commercially usable – BSD license.

 **Note :** Before installing scikit-image, ensure that NumPy and SciPy are
pre-installed. Now, the easiest way to install scikit-image is using pip :

    
    
    pip install -U scikit-image
    

  
Most functions of skimage are found within submodules. Images are represented
as NumPy arrays, for example 2-D arrays for grayscale 2-D images.

  

  

 **Code #1 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to process

# images using skikit-image

 

# importing data from skimage

from skimage import data

 

camera = data.camera() 

 

# An image with 512 rows

# and 512 columns

type(camera) 

 

print(camera.shape)  
  
---  
  
 __

 __

Output :

    
    
    numpy.ndarray
    (512, 512)
    

  
**Code #2 :** skimage.data submodule provides a set of functions returning
example images.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to process

# images using skikit-image

 

# importing filters and

# data from skimage

from skimage import filters

from skimage import data

 

# Predefined function to fetch data

coins = data.coins() 

 

# way to find threshold

threshold_value = filters.threshold_otsu(coins) 

 

print(threshold_value)  
  
---  
  
 __

 __

Output :

    
    
    107
    

  
**Code #3 :** Load own images as NumPy arrays from image files.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to process

# images using skikit-image

import os

 

# importing io from skimage

import skimage

from skimage import io

 

# way to load car image from file

file = os.path.join(skimage.data_dir, 'cc.jpg')

 

 

cars = io.imread(file)

 

# way to show the input image

io.imshow(cars)

io.show()  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/skikit-image.png)

 **Applications :**

  * Analysis of Medical images.
  * Classification of images for detection.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

