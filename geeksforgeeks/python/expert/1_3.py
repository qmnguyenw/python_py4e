OpenCV – Alpha blending and masking of images



 **Alpha blending** is the process of overlaying a foreground image on a
background image.

We take these two images to blend :

  

![](https://media.geeksforgeeks.org/wp-content/uploads/20210228231058/gfg.png)

gfg.png

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210228231145/apple.jpeg)

apple.jpeg

 **Steps :**

  * First, we will import OpenCV.
  * We read the two images that we want to blend.
  * The images are displayed.
  * We have a while loop that runs while the choice is 1.
  * Enter an alpha value.
  * Use **cv2.addWeighted()** to add the weighted images.
  * We display and save the image as _alpha_{image}.png_.
  * To continue and try out more alpha values, press 1. Else press 0 to exit.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import cv2

 

img1 = cv2.imread('gfg.png')

img2 = cv2.imread('apple.jpeg')

 

img2 = cv2.resize(img2, img1.shape[1::-1])

 

cv2.imshow("img 1",img1)

 

cv2.waitKey(0)

 

cv2.imshow("img 2",img2)

 

cv2.waitKey(0)

 

choice = 1

 

while (choice) :

 

 alpha = float(input("Enter alpha value"))

 

 dst = cv2.addWeighted(img1, alpha , img2, 1-alpha, 0)

 

 cv2.imwrite('alpha_mask_.png', dst)

 

 img3 = cv2.imread('alpha_mask_.png')

 

 cv2.imshow("alpha blending 1",img3)

 

 cv2.waitKey(0)

 

 choice = int(input("Enter 1 to continue and 0 to exit"))  
  
---  
  
 __

 __

 **Outputs:**

  

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210228231350/alphaalpha.png)

alpha = 0.8

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210228232035/alphamask.png)

alpha = 0.5

 **Alpha masking:**

> We can create a black and white mask from an image with a transparent
> background.

  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20210228202616/Eulg1.png)

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import cv2

im = cv2.imread("spectacles.png", cv2.IMREAD_UNCHANGED)

_, mask = cv2.threshold(im[:, :, 3], 0, 255,
cv2.THRESH_BINARY)

cv2.imwrite('mask.jpg', mask)  
  
---  
  
 __

 __

 **Output:**

  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20210228203301/alphamask.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

