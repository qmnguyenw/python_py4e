Real-Time Edge Detection using OpenCV in Python | Canny edge detection method



The objective of the program given is to perform edge detection of images in
real-time. In this article, the popular canny edge detection algorithm is used
to detect a wide range of edges in images. OpenCV has in-built function
cv2.Canny() which takes our input image as first argument and its aperture
size(min value and max value) as last two arguments. This is a simple example
of how to detect edges in Python.

 **Steps to download the requirements below:**

  1. Download Python 2.7.x version, numpy and OpenCV 2.7.x or 3.1.0 version.Check if your Windows either 32 bit or 64 bit is compatible and install accordingly.
  2. Make sure that numpy is running in your python then try to install opencv.

 **Implementation  
**

 __

 __  
 __

 __

 __  
 __  
 __

# OpenCV program to perform Edge detection in real time

# import libraries of python OpenCV 

# where its functionality resides

import cv2 

 

# np is an alias pointing to numpy library

import numpy as np

 

 

# capture frames from a camera

cap = cv2.VideoCapture(0)

 

 

# loop runs if capturing has been initialized

while(1):

 

 # reads frames from a camera

 ret, frame = cap.read()

 

 # converting BGR to HSV

 hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

 

 # define range of red color in HSV

 lower_red = np.array([30,150,50])

 upper_red = np.array([255,255,180])

 

 # create a red HSV colour boundary and 

 # threshold HSV image

 mask = cv2.inRange(hsv, lower_red, upper_red)

 

 # Bitwise-AND mask and original image

 res = cv2.bitwise_and(frame,frame, mask= mask)

 

 # Display an original image

 cv2.imshow('Original',frame)

 

 # finds edges in the input image image and

 # marks them in the output map edges

 edges = cv2.Canny(frame,100,200)

 

 # Display edges in a frame

 cv2.imshow('Edges',edges)

 

 # Wait for Esc key to stop

 k = cv2.waitKey(5) & 0xFF

 if k == 27:

 break

 

 

# Close the window

cap.release()

 

# De-allocate any associated memory usage

cv2.destroyAllWindows()   
  
---  
  
__

__

Output:

![output](https://media.geeksforgeeks.org/wp-content/uploads/op2.jpg)

  

  

 **References:**

  * http://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/canny_detector/canny_detector.html
  * http://docs.opencv.org/trunk/da/d22/tutorial_py_canny.html
  * https://en.wikipedia.org/wiki/Canny_edge_detector
  * http://www.ijcsmc.com/docs/papers/July2013/V2I7201329.pdf

This article is contributed by **Afzal Ansari**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

