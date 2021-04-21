Filtering Images based on size attributes in Python



Prerequisite : PIL_working-images-python

Given an Image directory, our program will create a new image directory based
on given threshold size.

A simple Python3 function that inputs the path of python file, the threshold
width in pixels and the threshold height in pixels, searches all the images
present in that only directory and creates a new directory having filtered out
all the images according the given threshold size, or resizes it to the given
threshold width and height.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

>  **Steps to Follow :**
>
> 1\. Install necessary Libraries like PIL  
> 2\. Import libraries : PIL, shutil, os, os.path  
> 3\. Save the code as sizeFilter.py  
> 4\. Open Terminal (where the python file is present and run)-> python
> sizeFilter.py
>
>  
>
>
>  
>

  
Below is the Python3 implementation of above approach :

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Filtering Images

# based on Size Attributes 

from PIL import Image

from shutil import copyfile

import os, os.path

 

 

def filterImages(path, thresholdWidth, thresholdHeight):

 

 # Defining images array for

 # identifying only image files

 imgs = []

 

 # List of possible images extensions

 # add if you want more

 valid_images = [".jpg", ".gif", ".png", ".tga",

 ".jpeg", ".PNG", ".JPG", ".JPEG"]

 

 # Storing all images in images array (imgs)

 for f in os.listdir(path):

 ext = os.path.splitext(f)[1]

 

 if ext.lower() not in valid_images:

 continue

 imgs.append(f)

 

 # Checking whether the filteredImages

 # directory exists or not

 directory = os.path.dirname('filteredImages' + path)

 if not os.path.exists(directory):

 os.makedirs(directory)

 

 # Defining filteredIMages array for

 # storing all the images we need

 filteredImages = []

 

 for i in imgs:

 image = Image.open(os.path.join(path, i))

 

 # Storing width and height of a image

 width, height = image.size

 

 # if only width exceeds the thresholdWidth

 if (width > thresholdWidth and

 height <= thresholdHeight):

 

 image.resize((thresholdWidth, 

 (thresholdWidth * height)

 // width)).save(i)

 

 # if only height exceeds the thresholdHeight

 elif (width <= thresholdWidth and

 height > thresholdHeight):

 

 image.resize(((thresholdHeight * width)

 // height, thresholdHeight)).save(i)

 

 # if both the paramateres exceeds

 # the threshold attributes

 elif (width > thresholdWidth and

 height > thresholdHeight):

 

 image.resize((thresholdWidth, thresholdHeight)).save(i)

 

 copyfile(os.path.join(path, i),

 os.path.join(path + '/filteredImages', i))

 

 filteredImages.append(i)

 

 # returning the filteredImages array

 return filteredImages

 

# Driver Code

if __name__ == '__main__':

 

 filteredImages = []

 

 # Enter the path of the python sizeFilter

 # file, the thresholdWidth(in pixels) and

 # thresholdHeight(in pixels)

 filteredImages = filterImages("/home/SahilKhosla/Desktop/Current
Project", 1000, 1000)  
  
---  
  
 __

 __

  
Output :  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

