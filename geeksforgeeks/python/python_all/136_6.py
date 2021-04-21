Filter Color with OpenCV



Colour segmentation or color filtering is widely used in OpenCV for
identifying specific objects/regions having a specific color. The most widely
used color space is RGB color space, it is called an **additive color space**
as the three color shades add up to give color to the image. To identify a
region of a specific color, put the threshold and create a mask to separate
the different colors. HSV color space is much more useful for this purpose as
the colors in HSV space are much more localized thus can be easily separated.
Color Filtering has many applications and uses cases such as in Cryptography,
infrared analysis, food preservation of perishable foods, etc. In such cases,
the concepts of Image processing can be used to find out or extract out
regions of a particular color.  
For color segmentation, all we need is the threshold values or the knowledge
of the lower bound and upper bound range of colors in one of the color spaces.
It works best in the Hue-Saturation-Value color space.  
After specifying the range of color to be segmented, it is needed to create a
mask accordingly and by using it, a particular region of interest can be
separated out.  

**Below is the code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import cv2

import numpy as np

cap = cv2.VideoCapture(0)

while(1):

 _, frame = cap.read()

 # It converts the BGR color space of image to HSV color space

 hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

 

 # Threshold of blue in HSV space

 lower_blue = np.array([60, 35, 140])

 upper_blue = np.array([180, 255, 255])

 # preparing the mask to overlay

 mask = cv2.inRange(hsv, lower_blue, upper_blue)

 

 # The black region in the mask has the value of 0,

 # so when multiplied with original image removes all non-blue regions

 result = cv2.bitwise_and(frame, frame, mask = mask)

 cv2.imshow('frame', frame)

 cv2.imshow('mask', mask)

 cv2.imshow('result', result)

 

 cv2.waitKey(0)

cv2.destroyAllWindows()

cap.release()  
  
---  
  
 __

 __

 **Original Image-**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190623003704/Screenshot-3091-300x238.png)

  

  

**Masked Image-**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190623003738/Screenshot-3111-300x237.png)

**Blue Color segmented regions-**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190623003814/Screenshot-3121-300x235.png)

Attention reader! Don’t stop learning now. Get hold of all the important CS
Theory concepts for SDE interviews with the **CS Theory Course** at a student-
friendly price and become industry ready.

My Personal Notes _arrow_drop_up_

Save

