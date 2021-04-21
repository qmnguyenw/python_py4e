Python | Thresholding techniques using OpenCV | Set-2 (Adaptive Thresholding)



 **Prerequisite:** Simple Thresholding using OpenCV

In the previous post, Simple Thresholding was explained with different types
of thresholding techniques. Another Thresholding technique is **Adaptive
Thresholding**. In Simple Thresholding, a global value of threshold was used
which remained constant throughout. So, a constant threshold value won’t help
in the case of variable lighting conditions in different areas. Adaptive
thresholding is the method where the threshold value is calculated for smaller
regions. This leads to different threshold values for different regions with
respect to the change in lighting. We use **cv2.adaptiveThreshold** for
this.

>  **Syntax** : cv2.adaptiveThreshold(source, maxVal, adaptiveMethod,
> thresholdType, blocksize, constant)
>
>  **Parameters:**  
>  -> **source** : Input Image array(Single-channel, 8-bit or floating-point)  
> -> **maxVal** : Maximum value that can be assigned to a pixel.  
> -> **adaptiveMethod** : Adaptive method decides how threshold value is
> calculated.
>
> **cv2.ADAPTIVE_THRESH_MEAN_C** : Threshold Value = (Mean of the
> neighbourhood area values – constant value). In other words, it is the mean
> of the blockSize×blockSize neighborhood of a point minus constant.
>
>  
>
>
>  
>
>
>  **cv2.ADAPTIVE_THRESH_GAUSSIAN_C** : Threshold Value = (Gaussian-weighted
> sum of the neighbourhood values – constant value). In other words, it is a
> weighted sum of the blockSize×blockSize neighborhood of a point minus
> constant.
>
> -> **thresholdType** : The type of thresholding to be applied.  
> -> **blockSize** : Size of a pixel neighborhood that is used to calculate a
> threshold value.  
> -> **constant** : A constant value that is subtracted from the mean or
> weighted sum of the neighbourhood pixels.

Below is the Python implementation :

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# adaptive thresholding type on an image

 

# organizing imports 

import cv2 

import numpy as np 

 

# path to input image is specified and 

# image is loaded with imread command 

image1 = cv2.imread('input1.jpg') 

 

# cv2.cvtColor is applied over the

# image input with applied parameters

# to convert the image in grayscale 

img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

 

# applying different thresholding 

# techniques on the input image

thresh1 = cv2.adaptiveThreshold(img, 255,
cv2.ADAPTIVE_THRESH_MEAN_C,

 cv2.THRESH_BINARY, 199, 5)

 

thresh2 = cv2.adaptiveThreshold(img, 255,
cv2.ADAPTIVE_THRESH_GAUSSIAN_C,

 cv2.THRESH_BINARY, 199, 5)

 

# the window showing output images

# with the corresponding thresholding 

# techniques applied to the input image

cv2.imshow('Adaptive Mean', thresh1)

cv2.imshow('Adaptive Gaussian', thresh2)

 

 

# De-allocate any associated memory usage 

if cv2.waitKey(0) & 0xff == 27: 

 cv2.destroyAllWindows()   
  
---  
  
__

__

**Input Image** :  
![](https://media.geeksforgeeks.org/wp-content/uploads/20190506013251/bp1.jpg)

 **Output** :![](https://media.geeksforgeeks.org/wp-
content/uploads/20190506013415/Screenshot-443.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

