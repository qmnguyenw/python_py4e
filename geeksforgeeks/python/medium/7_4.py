Displaying the coordinates of the points clicked on the image using Python-
OpenCV



OpenCV helps us to control and manage different types of mouse events and
gives us the flexibility to operate them. There are many types of mouse
events. These events can be displayed by running the following code segment :

    
    
    import cv2
    [print(i) for i in dir(cv2) if 'EVENT' in i]
    

**Output :**

    
    
    EVENT_FLAG_ALTKEY
    EVENT_FLAG_CTRLKEY
    EVENT_FLAG_LBUTTON
    EVENT_FLAG_MBUTTON
    EVENT_FLAG_RBUTTON
    EVENT_FLAG_SHIFTKEY
    EVENT_LBUTTONDBLCLK
    EVENT_LBUTTONDOWN
    EVENT_LBUTTONUP
    EVENT_MBUTTONDBLCLK
    EVENT_MBUTTONDOWN
    EVENT_MBUTTONUP
    EVENT_MOUSEHWHEEL
    EVENT_MOUSEMOVE
    EVENT_MOUSEWHEEL
    EVENT_RBUTTONDBLCLK
    EVENT_RBUTTONDOWN
    EVENT_RBUTTONUP
    

Now let us see how to display the coordinates of the points clicked on the
image. We will be displaying both the points clicked by right-click as well as
left-click.

 **Algorithm :**

  1. Import the cv2 module.
  2. Import the image using the cv2.imread() function.
  3. Display the image the image using the cv2.imshow() funciton.
  4. Call the cv2.setMouseCallback() fucniton and pass the image window and the user-defined function as parameters.
  5. In the user-defined function, check for left mouse clicks using the cv2.EVENT_LBUTTONDOWN attribute.
  6. Display the coordinates on the Shell.
  7. Display the coordinates on the created window.
  8. Do the same for right mouse clicks using the cv2.EVENT_RBUTTONDOWN attribute. Change the color while displaying the coordinates on the image to distinguish from left clicks.
  9. Outside the user-defined function, use the cv2.waitKey(0) and the cv2.destroyAllWindows() functions to close the window and terminate the program.

We will be using the colored version of the Lena image.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200711092856/lena.jpg)

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import cv2

 

# function to display the coordinates of

# of the points clicked on the image 

def click_event(event, x, y, flags, params):

 

 # checking for left mouse clicks

 if event == cv2.EVENT_LBUTTONDOWN:

 

 # displaying the coordinates

 # on the Shell

 print(x, ' ', y)

 

 # displaying the coordinates

 # on the image window

 font = cv2.FONT_HERSHEY_SIMPLEX

 cv2.putText(img, str(x) + ',' +

 str(y), (x,y), font,

 1, (255, 0, 0), 2)

 cv2.imshow('image', img)

 

 # checking for right mouse clicks 

 if event==cv2.EVENT_RBUTTONDOWN:

 

 # displaying the coordinates

 # on the Shell

 print(x, ' ', y)

 

 # displaying the coordinates

 # on the image window

 font = cv2.FONT_HERSHEY_SIMPLEX

 b = img[y, x, 0]

 g = img[y, x, 1]

 r = img[y, x, 2]

 cv2.putText(img, str(b) + ',' +

 str(g) + ',' + str(r),

 (x,y), font, 1,

 (255, 255, 0), 2)

 cv2.imshow('image', img)

 

# driver function

if __name__=="__main__":

 

 # reading the image

 img = cv2.imread('lena.jpg', 1)

 

 # displaying the image

 cv2.imshow('image', img)

 

 # setting mouse hadler for the image

 # and calling the click_event() function

 cv2.setMouseCallback('image', click_event)

 

 # wait for a key to be pressed to exit

 cv2.waitKey(0)

 

 # close the window

 cv2.destroyAllWindows()  
  
---  
  
 __

 __

 **Output :**

https://media.geeksforgeeks.org/wp-
content/uploads/20200714083457/cv2-clicking.mp4

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

