Detection of a specific color(blue here) using OpenCV with Python



The following code in python uses OpenCV library which is employed for image
processing techniques. The program allows the detection of a specific color in
a live stream video content. A video is composed of infinite frames at
different time instants. We will detect the colour of every frame one by one.  
**The code will only compile in linux environment.**  

Make sure that **openCV** is installed in your system before you run the
program.  
**For installation:**

  * Run the command following on your terminal to install it from the Ubuntu or Debian respository. 

    
    
    sudo apt-get install libopencv-dev python-opencv

  * OR In order to download OpenCV from the official site run the following command: 

    
    
    bash install-opencv.sh

on your terminal. Type your sudo password and you will have installed OpenCV.
This operation may take a long time due to the packages to be installed and
the compilation process.

  * To install numpy just use the command:   

    
    
    sudo pip install numpy

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for Detection of a

# specific color(blue here) using OpenCV with Python

import cv2

import numpy as np

# Webcamera no 0 is used to capture the frames

cap = cv2.VideoCapture(0)

# This drives the program into an infinite loop.

while(1): 

 # Captures the live stream frame-by-frame

 _, frame = cap.read()

 # Converts images from BGR to HSV

 hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

 lower_blue = np.array([110,50,50])

 upper_blue = np.array([130,255,255])

 # Here we are defining range of bluecolor in HSV

 # This creates a mask of blue coloured

 # objects found in the frame.

 mask = cv2.inRange(hsv, lower_blue, upper_blue)

 # The bitwise and of the frame and mask is done so

 # that only the blue coloured objects are highlighted

 # and stored in res

 res = cv2.bitwise_and(frame,frame, mask= mask)

 cv2.imshow('frame',frame)

 cv2.imshow('mask',mask)

 cv2.imshow('res',res)

 # This displays the frame, mask

 # and res which we created in 3 separate windows.

 k = cv2.waitKey(5) & 0xFF

 if k == 27:

 break

# Destroys all of the HighGUI windows.

cv2.destroyAllWindows()

# release the captured frame

cap.release()  
  
---  
  
 __

 __

 **Explanation of Code:**

  * **Camera Settings:** In order to perform runtime operations, the device’s web-camera is used. To capture a video, we need to create a VideoCapture object. Its argument can be either the device index or the name of a video file. The device index is just the number to specify which camera. Normally one camera will be connected, so we simply pass 0. You can select the second camera by passing 1 and so on. After that, you can capture frame-by-frame. But in the end, don’t forget to release the capture. Moreover, if anyone wants to apply this colour detection technique on any image it can be done with little modifications in the code which I’ll discuss later.
  *  **Capturing frames:** The infinite loop is used so that the web camera captures the frames in every instance and is open during the entire course of the program.   
After capturing the live stream frame by frame we are converting each frame in
BGR color space(the default one) to HSV color space. There are more than 150
color-space conversion methods available in OpenCV. But we will look into only
two which are most widely used ones, BGR to Gray and BGR to HSV. For color
conversion, we use the function cv2.cvtColor(input_image, flag) where flag
determines the type of conversion. For BGR to HSV, we use the flag
cv2.COLOR_BGR2HSV. Now we know how to convert BGR images to HSV, we can use
this to extract a colored object. In HSV, it is more easier to represent a
color than RGB color-space.  
In specifying the range , we have specified the range of blue color. Whereas
you can enter the range of any colour you wish.

  *  **Masking technique:** The mask is basically creating some specific region of the image following certain rules. Here we are creating a mask that comprises of an object in blue color. After that, I have used a bitwise_and on the input image and the threshold image so that only the blue coloured objects are highlighted and stored in res.   
We then display the frame, res, and mask on 3 separate windows using imshow
function.

  *  **Display the frame:** As imshow() is a function of HighGui it is required to call waitKey regularly, in order to process its event loop.   
The function waitKey() waits for key event for a “delay” (here, 5
milliseconds). If you don’t call waitKey, HighGui cannot process windows
events like redraw, resizing, input event etc. So just call it, even with a
1ms delay .

  *  **Summarizing the process** : 
    1. Take each frame of the video.
    2. Convert each frame from BGR to HSV color-space.
    3. Threshold the HSV image for a range of blue color.

This article is contributed by **Pratima Upadhyay**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.  

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

  
  

  

My Personal Notes _arrow_drop_up_

Save

