Convert BGR and RGB with Python – OpenCV



 **Prerequisites:** OpenCV

 **OpenCV** is a huge open-source library for computer vision, machine
learning, and image processing. OpenCV supports a wide variety of programming
languages like Python, C++, Java, etc. It can process images and videos to
identify objects, faces, or even the handwriting of a human. In this article,
we will convert a **BGR** image to **RGB** with **python** and **OpenCV**.

OpenCV uses BGR image format. So, when we read an image using cv2.imread() it
interprets in BGR format by default.

We can use cvtColor() method to convert a BGR image to RGB and vice-versa.

>  **Syntax:** cv2.cvtColor(code)
>
>  
>
>
>  
>
>
> **Parameter:**
>
>   *  **cv2.COLOR_BGR2RGB** – BGR image is converted to RGB.
>   *  **cv2.COLOR_RGB2BGR** – RGB image is converted to BGR.
>

Converting a BGR image to RGB and vice versa can have several reasons, one of
them being that several image processing libraries have different pixel
orderings.

### Approach

  * Import module
  * Read image
  * Convert it using cvtColor()
  * Add wait key
  * Add destroy window mechanism

 **Image used:** Apple

First, we will display the image as it is imported which means in BGR format.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import cv2

 

image = cv2.imread("/content/gfg.jpeg")

cv2.imshow('image',image)

cv2.waitKey(0)

cv2.destroyAllWindows()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210201174538/gfg-200x157.jpeg)

  

  

Now to convert BGR to RGB implementation is given below.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import cv2

 

image = cv2.imread("/content/gfg.jpeg")

 

# converting BGR to RGB

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

 

cv2.imshow('image', image_rgb)

cv2.waitKey(0)

cv2.destroyAllWindows()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210201174702/gfg-200x157.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

