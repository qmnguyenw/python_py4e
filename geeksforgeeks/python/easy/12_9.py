Python OpenCV | cv2.imread() method



 **OpenCV-Python** is a library of Python bindings designed to solve computer
vision problems.  
cv2.imread() method loads an image from the specified file. If the image
cannot be read (because of missing file, improper permissions, unsupported or
invalid format) then this method returns an empty matrix.

>  **Syntax:** cv2.imread(path, flag)
>
>  **Parameters:**  
>  **path:** A string representing the path of the image to be read.  
>  **flag:** It specifies the way in which image should be read. It’s default
> value is **cv2.IMREAD_COLOR**
>
>  **Return Value:** This method returns an image that is loaded from the
> specified file.

 **Note:** The image should be in the working directory or a full path of
image should be given.

  

  

All three types of flags are described below:

>  **cv2.IMREAD_COLOR:** It specifies to load a color image. Any transparency
> of image will be neglected. It is the default flag. Alternatively, we can
> pass integer value **1** for this flag.  
>  **cv2.IMREAD_GRAYSCALE:** It specifies to load an image in grayscale mode.
> Alternatively, we can pass integer value **0** for this flag.  
>  **cv2.IMREAD_UNCHANGED:** It specifies to load an image as such including
> alpha channel. Alternatively, we can pass integer value **-1** for this
> flag.

 **Image used for all the below examples:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190802021607/geeks14.png)

 **Example #1:** Using default flag

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain cv2.imread() method

 

# importing cv2 

import cv2

 

# path

path = r'C:\Users\Rajnish\Desktop\geeksforgeeks.png'

 

# Using cv2.imread() method

img = cv2.imread(path)

 

# Displaying the image

cv2.imshow('image', img)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190802022327/Annotation-2019-08-02-022111.png)

 **Example #2:**  
Loading an image in **grayscale** mode

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain cv2.imread() method

 

# importing cv2 

import cv2

 

# path

path = r'C:\Users\Rajnish\Desktop\geeksforgeeks.png'

 

# Using cv2.imread() method

# Using 0 to read image in grayscale mode

img = cv2.imread(path, 0)

 

# Displaying the image

cv2.imshow('image', img)  
  
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

