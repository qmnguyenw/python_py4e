Python | Background subtraction using OpenCV



 **Background Subtraction** has several use cases in everyday life, It is
being used for object segmentation, security enhancement, pedestrian tracking,
counting the number of visitors, number of vehicles in traffic etc. It is able
to learn and identify the foreground mask.

As the name suggests, it is able to subtract or eliminate the background
portion in an image. Its output is a binary segmented image which essentially
gives information about the non-stationary objects in the image. There lies a
problem in this concept of finding non-stationary portion, as the shadow of
the moving object can be moving and sometimes being classified in the
foreground.

The popular Background subtraction algorithms are:

  *  **BackgroundSubtractorMOG** : It is a gaussian mixture based background segmentation algorithm.
  *  **BackgroundSubtractorMOG2**: It uses the same concept but the major advantage that it provides is in terms of stablity even when there is change in luminosity and better identification capablity of shadows in the frames.
  *  **Geometric multigrid**: It makes uses of statiistical method and per pixel bayesin segmentation algorithm.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code for Background subtraction using OpenCV

import numpy as np

import cv2

 

cap = cv2.VideoCapture('/home/sourabh/Downloads/people-walking.mp4')

fgbg = cv2.createBackgroundSubtractorMOG2()

 

while(1):

 ret, frame = cap.read()

 

 fgmask = fgbg.apply(frame)

 

 cv2.imshow('fgmask', fgmask)

 cv2.imshow('frame',frame )

 

 

 k = cv2.waitKey(30) & 0xff

 if k == 27:

 break

 

 

cap.release()

cv2.destroyAllWindows()  
  
---  
  
 __

 __

 **Original video frame:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190628230551/Screenshot-
from-2019-06-28-21-52-12-300x190.jpg)

 **Background subtracted video frame:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190628230638/Screenshot-
from-2019-06-28-21-52-121-300x193.jpg)  
Thus, we saw an application of background subtraction algorithm detecting
motions, life in video frames.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

