Computer Vision module application for finding a target in a live camera



 _NOTE: Using an online compiler is not going to work here. Please install
Python 2.7x and cv2, argparse modules to actually try out this example._

For most of us, who are big fans of all those action movies, and games like
Modern Warfare, Black Ops, and so on, it has always been a dream to have the
opportunity of saying “Target acquired…Waiting for approval”.Team Alpha you
are permitted to fire,Mission is a go. Let’s blow it guys!!! Hurrah!” Of
course, well, you can’t always get what you want-But, at least now, I can get
you close enough to your dream. All you need for this lesson is Python 2.7,
cv2 module and it would be great if you have a nice video recorder with the
help of which you can get the live video stream. Anyways, it won’t matter even
if you don’t have one.

 **Step – 1 : Check your weapons**

Download Python 2.7 and ensure that you have the cv2 module (please note that
cv module is old and has been replaced by cv2 ) and argparse module. For this
:

    
    
    import cv2 as cv
    import argparse
    

If this does not give an error, then you are good to go…

  

  

 **Step – 2 : Mission details**

Now that you have your weapons with you, it’s time for you to ensure that you
have all the mission details required. First, we need to specify our target.
So, our target is:

![Sri](https://media.geeksforgeeks.org/wp-content/uploads/pentagon.png)

Now that you have your target with you, it’s time to set up a test field. Get
several printouts of the target and paste it at several places in your house.
Now, if you really want to get the feel, make a quadcopter, fix a small camera
in it, and record the whole house properly and ensure that you cover the
places where you have pasted the targets. In case if you don’t want to go
through all this trouble, just grab a camera and record your house yourself. I
would recommend you to keep the video short.

 **Step – 3 : Buckle up! We have a mission to complete!**

Okay. This is Alpha 1 reporting on duty! Send us the mission coordinates!

You have the target, now you need to acquire it! So, for this we are going to
use Computer Vision module (cv2).Code Snippet:

Direct Code Link: https://ide.geeksforgeeks.org/xfUet4

  

  

    
    
    import argparse
    import cv2
    
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", help="path to the video file")
    args = vars(ap.parse_args())
    
    # load the video
    camVideo = cv2.VideoCapture(args["video"])
    
    # keep looping
    while True:
    
        # grab the current frame and initialize the status text
        (grabbed, frame) = camVideo.read()
        status = "No Target in sight"
    
        # check to see if we have reached the end of the
        # video
        if not grabbed:
            break
    
        # convert the frame to grayscale, blur it, and detect edges
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #grayscale
        blurred = cv2.GaussianBlur(gray, (7, 7), 0) #blur
        edged = cv2.Canny(blurred, 50, 150) #canny edge detection
    
        # find contours in the edge map
        (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    
    # loop over the contours
    for cnt in cnts:
        approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),
        True)
    
    if len(approx)==5:
        cv2.drawContours(frame, [approx], -1, (0, 0, 255), 4)
        status = "Target(s) in sight!"
    
        # draw the status text on the frame
        cv2.putText(frame, status, (20, 30), cv2.FONT_HERSHEY_SIMPLEX,
        0.5,(0, 0, 255), 2)
    
        # show the frame and record if a key is pressed
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
    
        # if the 's' key is pressed, stop the loop
        if key == ord("s"):
            break
    
        # cleanup the input recorded video and close any open windows
    
    camVideo.release()
    cv2.destroyAllWindows()
    

**Code explained:**

We loop over each frame of the recorded video and for detection of our target
we convert it to gray-scale, blur it, and finally use canny edge detection
method to find the outlined image.

Remember that, camVideo.read() will return a tuple with first element
specifying whether the frame was read successfully or not, second element is
the actual frame we will be working on!

Now, once you have the frame, we will use contour approximation and then check
the number of elements in the output obtained from previous step. If the
number of elements is 5, then we have the regular pentagon that we were
looking for, and hence we update the status.

Now this all was quite easy and basic. If you really want to build one such
program then you should have a look at various filters to remove noise effects
from the frame to get a more accurate result. Best thing you can do is keep
experimenting!

Try this exercise at your house, record the video and share your results with
us…

Signing off ! Peace! Stay safe 🙂

 **About the author:**

 **Vishwesh Shrimali** is an Undergraduate Mechanical Engineering student at
BITS Pilani. He fulfils![vish](http://d1gjlxt8vb0knt.cloudfront.net//wp-
content/uploads/vish-100x100.png) about all the requirements not taught in his
branch- white hat hacker, network security operator, and an ex – Competitive
Programmer. As a firm believer in power of Python, his majority work has been
in the same language. Whenever he get some time apart from programming,
attending classes, watching CSI Cyber, he go for a long walk and play guitar
in silence. His motto of life is – “Enjoy your life, ‘cause it’s worth
enjoying!”

 **If you also wish to showcase your blog here, please seeGBlog for guest blog
writing on GeeksforGeeks.**

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

