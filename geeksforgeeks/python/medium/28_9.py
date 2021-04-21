Opencv Python program for Face Detection



  
The objective of the program given is to detect object of interest(face) in
real time and to keep tracking of the same object.This is a simple example of
how to detect face in Python. You can try to use training samples of any other
object of your choice to be detected by training the classifier on required
objects.

Here is the steps to download the requirements below.

 **Steps:**

  1. Download Python 2.7.x version, numpy and Opencv 2.7.x version.Check if your Windows either 32 bit or 64 bit is compatible and install accordingly.
  2. Make sure that numpy is running in your python then try to install opencv.
  3. Put the haarcascade_eye.xml & haarcascade_frontalface_default.xml files in the same folder(links given in below code).

 **Implementation  
**

 __

 __  
 __

 __

 __  
 __  
 __

# OpenCV program to detect face in real time

# import libraries of python OpenCV 

# where its functionality resides

import cv2 

 

# load the required trained XML classifiers

# https://github.com/Itseez/opencv/blob/master/

# data/haarcascades/haarcascade_frontalface_default.xml

# Trained XML classifiers describes some features of some

# object we want to detect a cascade function is trained

# from a lot of positive(faces) and negative(non-faces)

# images.

face_cascade =
cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

 

# https://github.com/Itseez/opencv/blob/master

# /data/haarcascades/haarcascade_eye.xml

# Trained XML file for detecting eyes

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 

 

# capture frames from a camera

cap = cv2.VideoCapture(0)

 

# loop runs if capturing has been initialized.

while 1: 

 

 # reads frames from a camera

 ret, img = cap.read() 

 

 # convert to gray scale of each frames

 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

 

 # Detects faces of different sizes in the input image

 faces = face_cascade.detectMultiScale(gray, 1.3, 5)

 

 for (x,y,w,h) in faces:

 # To draw a rectangle in a face 

 cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 

 roi_gray = gray[y:y+h, x:x+w]

 roi_color = img[y:y+h, x:x+w]

 

 # Detects eyes of different sizes in the input image

 eyes = eye_cascade.detectMultiScale(roi_gray) 

 

 #To draw a rectangle in eyes

 for (ex,ey,ew,eh) in eyes:


cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)

 

 # Display an image in a window

 cv2.imshow('img',img)

 

 # Wait for Esc key to stop

 k = cv2.waitKey(30) & 0xff

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

  

  

![output](https://media.geeksforgeeks.org/wp-content/uploads/output1.jpg)

 **  
Next Article:**Opencv C++ Program for face detection

References:

  * https://www.youtube.com/v=WfdYYNamHZ8
  * http://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html?highlight=cascadeclassifier#cascadeclassifier
  * http://www.multimedia-computing.de/mediawiki//images/5/52/MRL-TR-May02-revised-Dec02.pdf

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

