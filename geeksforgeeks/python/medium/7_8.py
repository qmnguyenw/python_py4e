Python – Eye blink detection project



In this tutorial you will learn about detecting a blink of human eye with the
feature mappers knows as **haar cascades**. Here in the project, we will use
the python language along with the OpenCV library for the algorithm execution
and image processing respectively. The haar cascades we are going to use in
the project are pretrained and stored along with the OpenCV library as
haarcascade_frontalface_default.xml and haarcascade_eye_tree_eyeglasses.xml
files. The project develops a basic understanding of the systems such as
driver drowsiness detection, eye blink locks, eye detection, face detection
and also the haar cascades usage with the OpenCV library.

 **About Haar Cascades:**  
Haar feature-based cascade classifiers is an effective object detection method
proposed by Paul Viola and Michael Jones in their paper, “Rapid Object
Detection using a Boosted Cascade of Simple Features” in 2001. It is a machine
learning-based approach where a cascade function is trained from a lot of
positive and negative images. Here positive images are the samples which
contain the target object and negative are the ones which don’t. It takes a
lot of positive and negative samples to train the classifier.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200610234041/Screenshot-from-2020-06-10-22-37-11.png)

Haar features , source – OpenCV docs

Now, we extract the features from the given input image with the haar features
shown in the above image. They are just like convolutional kernels. Each
feature is a single value obtained by subtracting the sum of pixels under the
white rectangle from the sum of pixels under the black rectangle.

  

![](https://media.geeksforgeeks.org/wp-content/uploads/20200610234715/jj.png)

Application of haarcascades, source – OpenCV Docs

 **The Excessive calculation:**  
With all the possible sizes of the classifiers the features are calculated,
but the amount of computation it takes to calculate the features, a _24×24_
window results over 160000 features. Also for each feature calculation, the
sum of the pixels is also needed. To make it computationally less expensive
the creators of haar cascades introduced the integral image, which means
however large your image, it reduces the calculations for a given pixel to an
operation involving just four pixels.

 **The false features**  
Now among the features that are calculated, most of the features are false and
irrelevant. Now the window which is applied to a region of the image may see a
different region which seems with the same features to the window but is not
in reality. So, there is a need to remove the false features which were done
by the **AdaBoost** which helped select the best features out of 160000+
features. Adaboost short form of Adaptive Boosting is a Machine learning
algorithm which was used for this sole task.

  

  

 **Algorithm :**

    
    
    
      1. The frame is captured and converted to grayscale.
    
      2. Bilateral Filtering is applied to remove impurities.
    
      3. Face is detected with the haarcascade.
    
      4. The ROI (Region Of Image) of Face is fed to eye detection part of algorithm.
    
      5. Eyes are detected and resulting list is passed to if-else contruct.
    
      6. If the length of list is more than two, means that the eyes are there.
    
      7. Else the program is marked to be eye blinked and restarted.
    
    
    

**Code:**  
The _haarcascade_frontalface_default.xml_ and
_haarcascade_eye_tree_eyeglasses.xml_ are the xml files stored in the same
directory as the python script.

 __

 __  
 __

 __

 __  
 __  
 __

#All the imports go here

import numpy as np

import cv2

 

#Initializing the face and eye cascade classifiers from xml files

face_cascade =
cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade =
cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

 

#Variable store execution state

first_read = True

 

#Starting the video capture

cap = cv2.VideoCapture(0)

ret,img = cap.read()

 

while(ret):

 ret,img = cap.read()

 #Coverting the recorded image to grayscale

 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

 #Applying filter to remove impurities

 gray = cv2.bilateralFilter(gray,5,1,1)

 

 #Detecting the face for region of image to be fed to eye classifier

 faces = face_cascade.detectMultiScale(gray, 1.3,
5,minSize=(200,200))

 if(len(faces)>0):

 for (x,y,w,h) in faces:

 img =
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

 

 #roi_face is face which is input to eye classifier

 roi_face = gray[y:y+h,x:x+w]

 roi_face_clr = img[y:y+h,x:x+w]

 eyes =
eye_cascade.detectMultiScale(roi_face,1.3,5,minSize=(50,50))

 

 #Examining the length of eyes object for eyes

 if(len(eyes)>=2):

 #Check if program is running for detection 

 if(first_read):

 cv2.putText(img, 

 "Eye detected press s to begin", 

 (70,70), 

 cv2.FONT_HERSHEY_PLAIN, 3,

 (0,255,0),2)

 else:

 cv2.putText(img, 

 "Eyes open!", (70,70), 

 cv2.FONT_HERSHEY_PLAIN, 2,

 (255,255,255),2)

 else:

 if(first_read):

 #To ensure if the eyes are present before starting

 cv2.putText(img, 

 "No eyes detected", (70,70),

 cv2.FONT_HERSHEY_PLAIN, 3,

 (0,0,255),2)

 else:

 #This will print on console and restart the algorithm

 print("Blink detected--------------")

 cv2.waitKey(3000)

 first_read=True

 

 else:

 cv2.putText(img,

 "No face detected",(100,100),

 cv2.FONT_HERSHEY_PLAIN, 3, 

 (0,255,0),2)

 

 #Controlling the algorithm with keys

 cv2.imshow('img',img)

 a = cv2.waitKey(1)

 if(a==ord('q')):

 break

 elif(a==ord('s') and first_read):

 #This will start the detection

 first_read = False

 

cap.release()

cv2.destroyAllWindows()  
  
---  
  
 __

 __

 **Sample Output:**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200611002440/result_eye.jpg)

Sample run of above code

The Source code and the cascade classifiers can be found here.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

