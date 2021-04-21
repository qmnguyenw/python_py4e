Python | Image blurring using OpenCV



 **Image Blurring** refers to making the image less clear or distinct. It is
done with the help of various low pass filter kernels.

 **Advantages of blurring:**

  * It helps in Noise removal. As noise is considered as high pass signal so by the application of low pass filter kernel we restrict noise.
  * It helps in smoothing the image.
  * Low intensity edges are removed.
  * It helps in hiding the details when necessary. For e.g. in many cases police deliberately want to hide the face of the victim, in such cases blurring is required.

 **Important types of blurring:**

  *  **Gaussian Blurring:** Gaussian blur is the result of blurring an image by a Gaussian function. It is a widely used effect in graphics software, typically to reduce image noise and reduce detail. It is also used as a preprocessing stage before applying our machine learning or deep learning models.  
E.g. of a Gaussian kernel(3×3)  
![  1/16 \\quad \\begin{bmatrix} 1 & 2 & 1 \\\\ 2 & 4 & 2\\\\ 1 & 2 & 1 \\\\
\\end{bmatrix}  ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-0e80b99ad85fefbbc12134e069537987_l3.png)

  *  **Median Blur:** The Median Filter is a non-linear digital filtering technique, often used to remove noise from an image or signal. Median filtering is very widely used in digital image processing because, under certain conditions, it preserves edges while removing noise. It is one of the best algorithms to remove Salt and pepper noise.
  *  **Bilateral Blur:** A bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing filter for images. It replaces the intensity of each pixel with a weighted average of intensity values from nearby pixels. This weight can be based on a Gaussian distribution. Thus, sharp edges are preserved while discarding the weak ones.

 **Below is the Python code:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

import cv2

import numpy as np

 

image =
cv2.imread('C://Geeksforgeeks//image_processing//fruits.jpg')

 

cv2.imshow('Original Image', image)

cv2.waitKey(0)

 

# Gaussian Blur

Gaussian = cv2.GaussianBlur(image, (7, 7), 0)

cv2.imshow('Gaussian Blurring', Gaussian)

cv2.waitKey(0)

 

# Median Blur

median = cv2.medianBlur(image, 5)

cv2.imshow('Median Blurring', median)

cv2.waitKey(0)

 

 

# Bilateral Blur

bilateral = cv2.bilateralFilter(image, 9, 75, 75)

cv2.imshow('Bilateral Blurring', bilateral)

cv2.waitKey(0)

cv2.destroyAllWindows()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190417162731/Screenshot-2831.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

