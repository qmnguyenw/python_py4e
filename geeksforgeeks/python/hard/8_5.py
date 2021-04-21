Saving Operated Video from a webcam using OpenCV



 **OpenCV** is a vast library that helps in providing various functions for
image and video operations. With OpenCV, we can perform operations on the
input video. OpenCV also allows us to save that operated video for further
usage. For saving images, we use cv2.imwrite() which saves the image to a
specified file location. But, for saving a recorded video, we create a Video
Writer object.

Firstly, we specify the fourcc variable. FourCC is a 4-byte code used to
specify the video codec. List of codes can be obtained at Video Codecs by
FourCC. The codecs for Windows is **DIVX** and for OSX is avc1, h263. FourCC
code is passed as **cv2.VideoWriter_fourcc(*’MJPG’)** for MJPG and
**cv2.VideoWriter_fourcc(*’XVID’)** for DIVX.

Then, the cv2.VideoWriter() function is used.

    
    
    **cv2.VideoWriter( filename, fourcc, fps, frameSize )**
    

The parameters are :

  1.  **filename:** Specifies the name of the output video file.
  2.  **fourcc:** (for recording) Defining the codec
  3.  **fps:** Defined frame rate of the output video stream
  4.  **frameSize:** Size of the video frames

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# saving an operated video

 

# organize imports

import numpy as np

import cv2

 

# This will return video from the first webcam on your computer.

cap = cv2.VideoCapture(0) 

 

# Define the codec and create VideoWriter object

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,
480))

 

# loop runs if capturing has been initialized. 

while(True):

 # reads frames from a camera 

 # ret checks return at each frame

 ret, frame = cap.read() 

 

 # Converts to HSV color space, OCV reads colors as BGR

 # frame is converted to hsv

 hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

 

 # output the frame

 out.write(hsv) 

 

 # The original input frame is shown in the window 

 cv2.imshow('Original', frame)

 

 # The window showing the operated video stream 

 cv2.imshow('frame', hsv)

 

 

 # Wait for 'a' key to stop the program 

 if cv2.waitKey(1) & 0xFF == ord('a'):

 break

 

# Close the window / Release webcam

cap.release()

 

# After we release our webcam, we also release the output

out.release() 

 

# De-allocate any associated memory usage 

cv2.destroyAllWindows()  
  
---  
  
 __

 __

 **Output:**  
The output screen shows up two windows. The window named ‘Original’ shows
input frames, whereas the ‘frame’ window shows the operated video sequence.  
![](https://media.geeksforgeeks.org/wp-content/uploads/HSV-2-1024x403.png)  
Also, a video is recorded and saved with the name ‘output’ in the same file
location with predefined frame rate and frame size.  
It is generally of the format .avi. The video saved is like this:Output Video

  

  

The input video can be operated in other color spaces too, like in
**grayscale**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# saving an operated video

 

# organize imports

import numpy as np

import cv2

 

# This will return video from the first webcam on your computer.

cap = cv2.VideoCapture(0) 

 

# Define the codec and create VideoWriter object

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,
480))

 

# loop runs if capturing has been initialized. 

while(True):

 # reads frames from a camera 

 # ret checks return at each frame

 ret, frame = cap.read() 

 

 # Converts to grayscale space, OCV reads colors as BGR

 # frame is converted to gray

 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

 

 # output the frame

 out.write(gray) 

 

 # The original input frame is shown in the window 

 cv2.imshow('Original', frame)

 

 # The window showing the operated video stream 

 cv2.imshow('frame', gray)

 

 

 # Wait for 'a' key to stop the program 

 if cv2.waitKey(1) & 0xFF == ord('a'):

 break

 

# Close the window / Release webcam

cap.release()

 

# After we release our webcam, we also release the out-out.release() 

 

# De-allocate any associated memory usage 

cv2.destroyAllWindows()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/Grayscale-2-1024x399.png)

A video file of this operated video is saved in the same file location as we
saw above.

This method can help us to create our own dataset for training data in
projects / models, to record from our webcam and do necessary operations and
also create the video in different color spaces.

Kindly refer this link for visualizing content in different color spaces:  
https://www.geeksforgeeks.org/python-visualizing-image-in-different-color-
spaces/

 **References:**

  1. https://docs.opencv.org/3.4/dd/d9e/classcv_1_1VideoWriter.html
  2. https://docs.opencv.org/3.1.0/dd/d43/tutorial_py_video_display.html
  3. https://en.wikipedia.org/wiki/FourCC
  4. https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

