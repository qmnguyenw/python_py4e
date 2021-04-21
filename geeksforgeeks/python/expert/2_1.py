Python – Face detection and sending notification



Nowadays python has become one of the most popular languages as well as
favourite programming language among developers. The simplified syntax and
pattern of this language make the presence of this language in the trending
list.

The biggest strength of Python is a huge collection of standard library which
can be used for the following:

  * Machine Learning
  * GUI Applications (like Kivy, Tkinter, PyQt etc. )
  * Web frameworks like Django (used by YouTube, Instagram, Dropbox)
  * Image processing (like OpenCV, Pillow)
  * Web scraping (like Scrapy, BeautifulSoup, Selenium)
  * Test frameworks
  * Multimedia
  * Scientific computing
  * Text processing and many more..

For Machine learning and AI python language is the first priority for the
developers because pre-built libraries of python language (like NumPy, Pandas,
Pybrain, and SciPy) help expedite AI development.

In this article , A simple method is implemented using python how to detect
human face and after detecting sends notifications to the user. If face is not
recognised it does not send notifications to the owner.

 **Technologies used:**

  

  

  *  **OpenCV:** OpenCV is a huge open-source library for computer vision, machine learning, and image processing. OpenCV supports a wide variety of programming languages like Python, C++, Java, etc. It can process images and videos to identify objects, faces, or even the handwriting of a human. When it is integrated with various libraries, such as Numpy which is a highly optimized library for numerical operations, then the number of weapons increases in your Arsenal i.e whatever operations one can do in Numpy can be combined with OpenCV.This OpenCV tutorial will help you learn the Image-processing from Basics to Advance, like operations on Images, Videos using a huge set of Opencv-programs and projects.

 **Sinch** : Sinch is used to send messages to the user whenever the camera
will detect any face. The user will have to make an account on sinch then
he/she can get the ‘service_plan_id’ and ‘token’ from them. After which the
user can input the latter in the code. The sender and recipients number also
needs to be changed accordingly.

 **Steps to SMS Token:**

  1. Create a new account on Sinch (Refer this link)

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210116135245/step1-660x359.png)

Click on Sign – Up

2\. **Click on messaging and conversations Panel :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210116135255/step2-660x316.png)

Click on massaging and conservations

3\. **Click on SMS option on the Home window:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210116135329/step3-660x315.png)

Click on sms

4. **You will get your code from there.**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210116202622/step450-660x336.png)

We are using Harcascade Classifier front face file download that file and
specify the path.

 **Clx-sdk-xms 1.0.0 :** It is a Python SDK for the CLX Communications REST
API (also called XMS) for sending and receiving single or batch SMS messages.
It also supports scheduled sends, organizing your frequent recipients into
groups, and customizing your message for each recipient using parametrization.
Sinch uses clx-sdk-xms to create API’S.

## Python3

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

 

from cv2 import cv2

 

import clx.xms

import requests

# By creating an account in sinch sms You can get your code.

# code for sms starts here 

#client is a object that carries your unique token.

client = clx.xms.Client(service_plan_id='your_service id',

 token='token_id')

 

create = clx.xms.api.MtBatchTextSmsCreate()

create.sender = 'sender no.'

create.recipients = {'recipients no.'}

create.body = 'This is a test message from your Sinch account'

# code for sms ends here

# Face Recognition starts from here.

# load the required trained XML classifiers

#https://github.com/opencv/opencv/blob/master

#/data/haarcascades/haarcascade_frontalface_default.xml

# Trained XML classifiers describes some features of some

# object we want to detect a cascade function is trained

# from a lot of positive(faces) and negative(non-faces)

# images.

 

detector = cv2.CascadeClassifier(

 "path")

 

# capture frames from a camera

 

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#We want to send sms only once not untill the face is there and for that we
are

#initializing the counter

counter = 0

# loop runs if capturing has been initialized.

 

while True:

 # reads frames from a camera

 

 ret, img = cap.read()

 

 if ret:

 # convert to gray scale of each frames

 

 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

 # Detects faces of different sizes in the input image

 

 faces = detector.detectMultiScale(gray, 1.1, 4)

 

 for face in faces:

 

 x, y, w, h = face

 # if there is any face and counter is zero then only it will send
notification to the sender

 if(face.any() and counter ==0):

 try:

 batch = client.create_batch(create)

 except (requests.exceptions.RequestException,
clx.xms.exceptions.ApiException) as ex:

 print('Failed to communicate with XMS: %s' % str(ex))

 #sms ends here

 # To draw a rectangle in a face

 cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0),
2)

 

 

 cv2.imshow("Face", img)

 counter = 1

 # Wait for 'q' key to stop

 

 key = cv2.waitKey(1)

 if key == ord("q"):

 break

# Close the window

cap.release()

# De-allocate any associated memory usage

 

cv2.destroyAllWindows()  
  
---  
  
 __

 __

 **Output:**

 **Detecting image:**

  
![](https://media.geeksforgeeks.org/wp-content/uploads/20210105212544/new.jpg)

 **Notification:**

  
![](https://media.geeksforgeeks.org/wp-content/uploads/20210116223945/new.jpg)

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

