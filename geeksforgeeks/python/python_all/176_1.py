What is Image Blurring



 **What is convolution in 2D?**  
Image is denoted as matrix inside computer. An image contains a lot of
features like edge, contrast etc. In image processing features have to be
extracted from the image for further study of image.  
Convolution is a fundamental operation on images in which a mathematical
operation is applied to each pixel to get the desired result.  
For this purpose, another matrix called as **kernel** is used which is smaller
in size of image. This is also called filter. This filter is applied on each
pixel of the image and new value obtained is the value of that pixel. The
image obtained is called **filtered image**.  
In kernel each cell contain some value, that kernel is kept above the pixel
and corresponding values are multiplied and then summed up this value obtained
is new the value of pixel.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Untitled-
drawing-3-4.jpg)

 **What is Blurring**  
If a blurred image is observed carefully then a common thing to notice is that
image is smooth meaning edges are not observed. A filter used for blurring is
also called **low pass filter** , because it allows low frequency to enter and
stop high frequency. Here frequency means the change of pixel value. Around
edge pixel value changes rapidly as blur image is smooth so high frequency
should be filtered out.  
For blur purpose a filter with every call having value 1 is used because to
blur image a pixel value should be close to neighbor value.  
In filter it is divided by 9 for normalization otherwise value of a pixel will
increase resulting in more contrast which is not the goal.

![](https://media.geeksforgeeks.org/wp-content/uploads/Untitled-
drawing-4-3.jpg)

We can choose the size of the kernel depending on how much we want to smoothen
the image. Choosing a bigger size will be averaging over a larger area. This
tends to increase the smoothening effect.

 __

 __  
 __

 __

 __  
 __  
 __

# Write Python3 code here

 

import cv2

import numpy as np

 

image = cv2.imread('geek.jpg')

 

# making filter of 3 by 3 filled with 1 divide 

# by 9 for normalization

blur_filter1 = np.ones((3, 3), np.float)/(9.0)

 

# making filter of 5 by 5 filled with 1 divide

# by 25 for normalization

blur_filter2 = np.ones((5, 5), np.float)/(25.0)

 

# making filter of 7 by 7 filled with 1 divide 

# by 49 for normalization

blur_filter3 = np.ones((7, 7), np.float)/(49.0)

 

image_blur1 = cv2.filter2D(image, -1, blur_filter1)

image_blur2 = cv2.filter2D(image, -1, blur_filter2)

image_blur3 = cv2.filter2D(image, -1, blur_filter3)

 

cv2.imshow('geek', image)

cv2.imshow('geek_blur1', image_blur1)

cv2.imshow('geek_blur2', image_blur2)

cv2.imshow('geek_blur3', image_blur3)

 

cv2.waitKey(0)

cv2.destroyAllWindows()  
  
---  
  
 __

 __

###  **Output**

 **Original image**  
![](https://media.geeksforgeeks.org/wp-content/uploads/ima1.png)

  

  

* * *

 **Blurred with filter of 3 x 3**  
![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2018-10-14-19-21-37.png)

* * *

 **Blurred with filter of 5 x 5**  
![](https://media.geeksforgeeks.org/wp-content/uploads/img2-10.png)

* * *

 **Blurred with filter of 7 x 7**  
![](https://media.geeksforgeeks.org/wp-content/uploads/img3-6.png)

With large filter the images smoothed more.

Attention reader! Don’t stop learning now. Get hold of all the important CS
Theory concepts for SDE interviews with the **CS Theory Course** at a student-
friendly price and become industry ready.

My Personal Notes _arrow_drop_up_

Save

