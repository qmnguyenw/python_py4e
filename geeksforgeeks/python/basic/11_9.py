Python OpenCV | cv2.imwrite() method



 **OpenCV-Python** is a library of Python bindings designed to solve computer
vision problems. cv2.imwrite() method is used to save an image to any
storage device. This will save the image according to the specified format in
current working directory.

>  **Syntax:** cv2.imwrite(filename, image)
>
>  **Parameters:**  
>  **filename:** A string representing the file name. The filename must
> include image format like **.jpg, .png,** etc.  
>  **image:** It is the image that is to be saved.
>
>  **Return Value:** It returns true if image is saved successfully.

 **Example #1:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain cv2.imwrite() method

 

# importing cv2 

import cv2

 

# importing os module 

import os

 

# Image path

image_path = r'C:\Users\Rajnish\Desktop\GeeksforGeeks\geeks.png'

 

# Image directory

directory = r'C:\Users\Rajnish\Desktop\GeeksforGeeks'

 

# Using cv2.imread() method

# to read the image

img = cv2.imread(image_path)

 

# Change the current directory 

# to specified directory 

os.chdir(directory)

 

# List files and directories 

# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks' 

print("Before saving image:") 

print(os.listdir(directory)) 

 

# Filename

filename = 'savedImage.jpg'

 

# Using cv2.imwrite() method

# Saving the image

cv2.imwrite(filename, img)

 

# List files and directories 

# in 'C:/Users / Rajnish / Desktop / GeeksforGeeks' 

print("After saving image:") 

print(os.listdir(directory))

 

print('Successfully saved')  
  
---  
  
 __

 __

 **Output:**

    
    
    Before saving image:
    ['geeks.png']
    After saving image:
    ['geeks.png', 'savedImage.jpg']
    Successfully saved
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

