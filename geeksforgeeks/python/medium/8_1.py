Mahotas – Otsu’s method



In this article we will see how we can implement otsu’s method in mahotas. In
computer vision and image processing, Otsu’s method, named after Nobuyuki
Otsu, is used to perform automatic image thresholding. In the simplest form,
the algorithm returns a single intensity threshold that separate pixels into
two classes, foreground and background.

In this tutorial we will use “luispedro” image, below is the command to load
it.

    
    
    mahotas.demos.load('luispedro')

Below is the luispedro image  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200620223605/final517.png)

In order to do this we will use mahotas.otsu method

>  **Syntax :** mahotas.otsu(image)
>
>  
>
>
>  
>
>
>  **Argument :** It takes image object as argument
>
>  **Return :** It returns integer

 **Note :** Input image should be filtered or should be loaded as grey

In order to filter the image we will take the image object which is
numpy.ndarray and filter it with the help of indexing, below is the command to
do this

    
    
    image = image[:, :, 0]

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing required librries

import mahotas

import mahotas.demos

import numpy as np

from pylab import imshow, gray, show

from os import path

 

# loading the image

photo = mahotas.demos.load('luispedro')

 

# showing original image

print("Origial Image")

imshow(photo)

show()

 

# loading image as grey

photo = mahotas.demos.load('luispedro', as_grey = True)

 

# converting image type to unit8

# beacuse as_grey returns floating values

photo = photo.astype(np.uint8)

 

# otsu method

T_otsu = mahotas.otsu(photo)

 

# printing otsu value

print("Otsu Method value : " + str(T_otsu))

 

print("Image threshold using Otsu Mehtod")

# showing image

# image values should be greater than otsu value

imshow(photo > T_otsu)

show()  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200620231514/1st91.png)

 **Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing required libraries

import mahotas

import numpy as np

from pylab import imshow, show

import os

 

 

# loading iamge

img = mahotas.imread('dog_image.png')

 

 

# setting filter to the image

img = img[:, :, 0]

 

imshow(img)

show()

 

 

# otsu method

T_otsu = mahotas.otsu(img)

 

# printing otsu value

print("Otsu Method value : " + str(T_otsu))

 

print("Image threshold using Otsu Mehtod")

# showing image

# image values should be greater than otsu value

imshow(img > T_otsu)

show()  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200620231742/2nd118.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

