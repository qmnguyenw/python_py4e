Invisible Cloak using OpenCV | Python Project



Have you ever seen Harry Potter’s Invisible Cloak; Was it wonderful? Have you
ever wanted to wear that cloak? If Yes!! then in this post, we will build the
same cloak which Harry Potter uses to become invisible. Yes, we are not
building it in a real way but it is all about graphics trickery.

In this post, we will learn how to create our own ‘Invisibility Cloak’ using
simple computer vision techniques in **OpenCV**. Here we have written this
code in Python because it provides exhaustive and sufficient library to build
this program.

Here, we will create this magical experience using an image processing
technique called _**Color detection and segmentation**_. In order to run this
code, you need an mp4 video named “video.mp4“. You must have a cloth of same
color and no other color should be visible into that cloth. We are taking the
red cloth. If you are taking some other cloth, the code will remain the same
but with minute changes.

 **Why Red? Green is my favorite?**  
Sure, we could have used green, isn’t Red the magician’s color? Jokes aside,
colors like green or blue will also work fine with a little bit of changes in
code.  
This technique is opposite to the **Green Screening**. In green screening, we
remove background but here we will remove the foreground frame. So let’s start
our code.

 **Algorithm:**

  

  

> 1\. Capture and store the background frame [ This will be done for some
> seconds ]  
> 2\. Detect the red colored cloth using color detection and segmentation
> algorithm.  
> 3\. Segment out the red colored cloth by generating a mask. [ used in code ]  
> 4\. Generate the final augmented output to create a magical effect. [
> video.mp4 ]

 **Below is the Code:**

 __

 __  
 __

 __

 __  
 __  
 __

import cv2

import numpy as np

import time

 

# replace the red pixels ( or undesired area ) with

# background pixels to generate the invisibility feature.

 

## 1. Hue: This channel encodes color information. Hue can be

# thought of an angle where 0 degree corresponds to the red color, 

# 120 degrees corresponds to the green color, and 240 degrees 

# corresponds to the blue color.

 

## 2. Saturation: This channel encodes the intensity/purity of color.

# For example, pink is less saturated than red.

 

## 3. Value: This channel encodes the brightness of color.

# Shading and gloss components of an image appear in this 

# channel reading the videocapture video 

 

# in order to check the cv2 version

print(cv2.__version__) 

 

# taking video.mp4 as input.

# Make your path according to your needs 

capture_video = cv2.VideoCapture("video.mp4")

 

# give the camera to warm up

time.sleep(1) 

count = 0

background = 0

 

# capturing the background in range of 60

# you should have video that have some seconds

# dedicated to background frame so that it 

# could easily save the background image

for i in range(60):

 return_val, background = capture_video.read()

 if return_val == False :

 continue

 

background = np.flip(background, axis = 1) # flipping of the
frame 

 

# we are reading from video 

while (capture_video.isOpened()):

 return_val, img = capture_video.read()

 if not return_val :

 break

 count = count + 1

 img = np.flip(img, axis = 1)

 

 # convert the image - BGR to HSV

 # as we focused on detection of red color 

 

 # converting BGR to HSV for better 

 # detection or you can convert it to gray

 hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 

 

 #-------------------------------------BLOCK----------------------------#

 # ranges should be carefully chosen

 # setting the lower and upper range for mask1

 lower_red = np.array([100, 40, 40]) 

 upper_red = np.array([100, 255, 255])

 mask1 = cv2.inRange(hsv, lower_red, upper_red)

 # setting the lower and upper range for mask2 

 lower_red = np.array([155, 40, 40])

 upper_red = np.array([180, 255, 255])

 mask2 = cv2.inRange(hsv, lower_red, upper_red)

 #----------------------------------------------------------------------#

 

 # the above block of code could be replaced with

 # some other code depending upon the color of your cloth 

 mask1 = mask1 + mask2

 

 # Refining the mask corresponding to the detected red color

 mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,
3),

 np.uint8), iterations = 2)

 mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8),
iterations = 1)

 mask2 = cv2.bitwise_not(mask1)

 

 # Generating the final output

 res1 = cv2.bitwise_and(background, background, mask = mask1)

 res2 = cv2.bitwise_and(img, img, mask = mask2)

 final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

 

 cv2.imshow("INVISIBLE MAN", final_output)

 k = cv2.waitKey(10)

 if k == 27:

 break  
  
---  
  
 __

 __

 **Output:**  

You can check source code on the project github repository, for input video
and more details – here  
  
**Reference:** http://datasciencenthusiast.com/?p=71

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

