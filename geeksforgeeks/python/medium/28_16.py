OpenCV Python Program to blur an image



 _Note: This post contains codes that cannot be run using an online compiler.
Please make sure that you have Python 2.7 and cv2 module installed before
trying to run the program on your system._

Hi everyone! I read a brilliant work by **Aditya Prakash** – _OpenCV C++
Program to blur an image_ , so I decided to come up with something similar but
this time in Python. So, here is a very simple program with basically the same
result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to blur image

 

# Importing cv2 module

import cv2 

 

# bat.jpg is the batman image.

img = cv2.imread('bat.jpg') 

 

# make sure that you have saved it in the same folder

# You can change the kernel size as you want

blurImg = cv2.blur(img,(10,10)) 

cv2.imshow('blurred image',blurImg)

 

cv2.waitKey(0)

cv2.destroyAllWindows()  
  
---  
  
 __

 __

Output:  
![](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20201127104358/577.png)

Now, this program above is using image blurring technique called
**Averaging.** There are some other options available as well – **Gaussian
Blurring, Median Blurring, Bilateral Filtering.** Let’s make a couple of
additions in our program and compare the results.

 __

 __  
 __

 __

 __  
 __  
 __

# importing opencv CV2 module

import cv2 

 

# bat.jpg is the batman image.

img = cv2.imread('gfg.png')

 

# make sure that you have saved it in the same folder

# Averaging

# You can change the kernel size as you want

avging = cv2.blur(img,(10,10))

 

cv2.imshow('Averaging',avging)

cv2.waitKey(0)

 

# Gaussian Blurring

# Again, you can change the kernel size

gausBlur = cv2.GaussianBlur(img, (5,5),0) 

cv2.imshow('Gaussian Blurring', gausBlur)

cv2.waitKey(0)

 

# Median blurring

medBlur = cv2.medianBlur(img,5)

cv2.imshow('Media Blurring', medBlur)

cv2.waitKey(0)

 

# Bilateral Filtering

bilFilter = cv2.bilateralFilter(img,9,75,75)

cv2.imshow('Bilateral Filtering', bilFilter)

cv2.waitKey(0)

cv2.destroyAllWindows()  
  
---  
  
 __

 __

Original Image:  
![](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20201127103715/gfg4.png)  
Averaging:  
![](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20201127103842/573.png)

  

  

Gaussian Blurring:  
![](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20201127103841/574.png)

Media Blurring:  
![](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20201127103839/575.png)

Bilateral Filtering:  
![](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20201127103838/576.png)

Hope you enjoyed the post! Auf Wiedersehen!

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

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

