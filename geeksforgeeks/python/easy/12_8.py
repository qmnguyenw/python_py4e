Python OpenCV | cv2.imshow() method



 **OpenCV-Python** is a library of Python bindings designed to solve computer
vision problems. cv2.imshow() method is used to display an image in a window.
The window automatically fits to the image size.  

> **Syntax:** cv2.imshow(window_name, image)  
>  **Parameters:**  
> **window_name:** A string representing the name of the window in which image
> to be displayed.  
> **image:** It is the image that is to be displayed.  
>  **Return Value:** It doesn’t returns anything.  
>

**Image used for all the below examples:**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190802021607/geeks14.png)

**Example #1:**  

  

  

__

__  
__

__

__  
__  
__

# Python program to explain cv2.imshow() method

 

# importing cv2 

import cv2 

 

# path 

path = r'C:\Users\Rajnish\Desktop\geeksforgeeks.png'

 

# Reading an image in default mode

image = cv2.imread(path)

 

# Window name in which image is displayed

window_name = 'image'

 

# Using cv2.imshow() method 

# Displaying the image 

cv2.imshow(window_name, image)

 

#waits for user to press any key 

#(this is necessary to avoid Python kernel form crashing)

cv2.waitKey(0) 

 

#closing all open windows 

cv2.destroyAllWindows()   
  
---  
  
__

__

**Output:**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190802022327/Annotation-2019-08-02-022111.png)

**Example #2:**  

__

__  
__

__

__  
__  
__

# Python program to explain cv2.imshow() method

 

# importing cv2

import cv2

 

# path

path = r'C:\Users\Rajnish\Desktop\geeksforgeeks.png'

 

# Reading an image in grayscale mode

image = cv2.imread(path, 0)

 

# Window name in which image is displayed

window_name = 'image'

 

# Using cv2.imshow() method

# Displaying the image

cv2.imshow(window_name, image)

 

# waits for user to press any key

# (this is necessary to avoid Python kernel form crashing)

cv2.waitKey(0)

 

# closing all open windows

cv2.destroyAllWindows()  
  
---  
  
 __

 __

 **Output:**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190802022316/Annotation-2019-08-02-022133.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

