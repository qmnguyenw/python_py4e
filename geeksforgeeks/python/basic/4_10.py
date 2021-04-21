Transition from OpenCV 2 to OpenCV 3.x



OpenCV is one of the most popular and most used Computer vision libraries. It
contains tools to carry out image and video processing.

When OpenCV 3..4.1 is an improved version of OpenCV 2.4 as it introduced new
algorithms and features. Although some of the existing modules were rewritten
and moved to sub-modules. In this articles, I will focus on the changes made
in the existing modules of OpenCV 2.4 and how they can be implemented in
OpenCV 3.4.1.

### Feature Detection

Some of the feature detection algorithms (FREAK, BRIEF, SIFT and SURF) have
been moved to o _pencv_contrib repository_ and _xfeatures2d_ module. SIFT and
SURF algorithms are patented by their creators and are non-free. Although they
can be used for educational and research purposes.

 **SIFT :** Create SIFT feature detector object.

 __

 __  
 __

 __

 __  
 __  
 __

# OpenCV 2.4

sift = cv2.SIFT()

 

# OpenCV 3.4.1

sift = cv2.xfeatures2d.SIFT_create()  
  
---  
  
 __

 __

 ** **SURF :**** Create SURF feature detector object

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# OpenCV 2.4

surf = cv2.SURF()

 

# OpenCV 3.4.1

surf = cv2.xfeatures2d.SURF_create()  
  
---  
  
 __

 __

 ** **FAST :**** Create FAST detector object

 __

 __  
 __

 __

 __  
 __  
 __

# OpenCV 2.4

fast = cv2.FastFeatureDetector()

 

# OpenCV 3.4.1

fast = cv2.FastFeatureDetector_create()  
  
---  
  
 __

 __

 ** **ORB** :** Create ORB detector object

 __

 __  
 __

 __

 __  
 __  
 __

# OpenCV 2.4

orb = cv2.ORB()

 

# OpenCV 3.4.1

orb = cv2.ORB_create()  
  
---  
  
 __

 __

 **Simple Blob Detector**

 __

 __  
 __

 __

 __  
 __  
 __

# OpenCV 2.4

detector = cv2.SimpleBlobDetector()

 

# OpenCV 3.4.1

detector = cv2.SimpleBlobDetector_create()  
  
---  
  
 __

 __

### CIRCLE DETECTION

OpenCV uses Hough Gradient Method to detect circles that uses gradient
information of the edges.

 __

 __  
 __

 __

 __  
 __  
 __

# OpenCV 3.4.1

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 4, 10)  
  
---  
  
 __

 __

The name of the method has been changed fromCV_HOUGH_GRADIENT in 2.4 version
to HOUGH_GRADIENT in 3.4 version.

### CONTOURS

Initially the findContours() function returned only two parameters in OpenCV
2.4 . In OpenCV 3.2 onwards, the function was modified to return three
parameters i.e. the modified image, contours and hierarchy.

 __

 __  
 __

 __

 __  
 __  
 __

# OpenCV 2.4

contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_NONE)

 

# OpenCV 3.4.1

im, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, 

 cv2.CHAIN_APPROX_NONE)  
  
---  
  
 __

 __

These were a few important changes that could be useful while migrating the
code from OpenCV 2 .4 to OpenCV 3.x .

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

