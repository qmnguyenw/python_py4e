Resize Multiple Images using OpenCV-Python



In this article, we are going to write a python script using the OpenCV
library to Resize Multiple Images and save them as an image file. Resizing the
image refers to the growth of the images. Measurement works best in the use of
multiple images and in machine learning applications. It helps to reduce the
number of pixels from an image and that has several benefits e.g. It can
reduce neural network training time as the number of pixels in the image
greatly increases the number of input nodes which also improves the model
difficulty.

 **Approach:**

  * Firstly, load the required libraries into a Python file (argparse, OpenCV, etc.).
  * We are using **argparse()** function to get the path of the directory of images on which we need to perform the resizing.
  * Use for loop to iterate every **image** in the directory.
  * Load image in a variable using **cv2.imread()** function.
  * Define a resizing scale and set the calculated height and width.
  * Resize the image using **cv2.resize()** function.
  * Place the output file inside the output folder using **cv2.imwrite()** function.

All the images inside the Images folder will be resized and will be saved in
an output folder.

 **Below is the implementation:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Required Libraries

import cv2

import numpy as np

from os import listdir

from os.path import isfile, join

from pathlib import Path

import argparse

import numpy

 

# Argument parsing variable declared

ap = argparse.ArgumentParser()

 

ap.add_argument("-i", "--image",

 required=True,

 help="Path to folder")

 

args = vars(ap.parse_args())

 

# Find all the images in the provided images folder

mypath = args["image"]

onlyfiles = [f for f in listdir(mypath) if
isfile(join(mypath, f))]

images = numpy.empty(len(onlyfiles), dtype=object)

 

# Iterate through every image

# and resize all the images.

for n in range(0, len(onlyfiles)):

 

 path = join(mypath, onlyfiles[n])

 images[n] = cv2.imread(join(mypath, onlyfiles[n]),

 cv2.IMREAD_UNCHANGED)

 

 # Load the image in img variable

 img = cv2.imread(path, 1)

 

 # Define a resizing Scale

 # To declare how much to resize

 resize_scaling = 50

 resize_width = int(img.shape[1] * resize_scaling/100)

 resize_hieght = int(img.shape[0] *
resize_scaling/100)

 resized_dimentions = (resize_width, resize_hieght)

 

 # Create resized image using the calculated dimentions

 resized_image = cv2.resize(img, resized_dimentions,

 interpolation=cv2.INTER_AREA)

 

 # Save the image in Output Folder

 cv2.imwrite(

 'output/' + str(resize_width) + str(resize_hieght) +
str(n) + '_resized.jpg', resized_image)

 

print("Images resized Successfully")  
  
---  
  
 __

 __

