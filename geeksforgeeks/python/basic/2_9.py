How to Display Multiple Images in One Window using OpenCV Python?



 **Prerequisites:**Opencv

In this article, we will show how to display Multiple Images In One window
using OpenCV in Python.

###  **Approach**

  * Import module
  * Load the Multiple images using **cv2.imread()**
  * Concatenate the images using **concatenate(),** with axis value provided as per orientation requirement
  * Display all the images using **cv2.imshow()**
  * Wait for keyboard button press using **cv2.waitKey()**
  * Exit window and destroy all windows using **cv2.destroyAllWindows()**

###  **Functions Used**

  *  **cv2.imread()** **:** reads an image file from the given specific location
  *  **concatenate((image1,image2), axis):** concatenates multiple images along a given mentioned axis (horizontal or vertical), The value of axis is given as 1 for combining them horizontally and 0 for combining them vertically.
  *  **cv2.imshow()** **:** displays an image in a window
  *  **cv2.waitKey()** **:** is a keyboard binding function. Its argument is the time in milliseconds. The function waits for specified milliseconds for any keyboard event.
  *  **cv2.destroyAllWindows():** If you have multiple windows open and you do not need those to be open, you can use cv2.destroyAllWindows() to close those all.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import cv2

import numpy as np

 

# Read First Image

img1 = cv2.imread('GFG.png')

 

# Read Second Image

img2 = cv2.imread('GFG.png')

 

 

# concatanate image Horizontally

Hori = np.concatenate((img1, img2), axis=1)

 

# concatanate image Vertically

Verti = np.concatenate((img1, img2), axis=0)

 

cv2.imshow('HORIZONTAL', Hori)

cv2.imshow('VERTICAL', Verti)

 

cv2.waitKey(0)

cv2.destroyAllWindows()  
  
---  
  
 __

 __

 **Input:**

  

  

GFG.png

![](https://media.geeksforgeeks.org/wp-content/uploads/20201214204639/GFG.png)

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201214204953/Screenshot298.png)![](https://media.geeksforgeeks.org/wp-
content/uploads/20201214205020/Screenshot299.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

