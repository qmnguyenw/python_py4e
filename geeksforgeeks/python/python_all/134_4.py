Python | Copy and Paste Images onto other Image using Pillow



In this article, we will learn how to copy an image over another image using
pillow library. We will use image module from pillow and copy() and
paste() methods to achieve this task.

We will need to create copies of both images so that it does not affect the
original image with the help of copy() method and then paste the image on
the other image with the help of paste() method.

 **Input images –**

Image1:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190719161411/cat1-225x300.jpg)

Image2:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190719161521/core.jpg)

  

  

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# import image module from pillow

from PIL import Image

 

# open the image

Image1 = Image.open('D:\cat.jpg')

 

# make a copy the image so that the 

# original image does not get affected

Image1copy = Image1.copy()

Image2 = Image.open('D:\core.jpg')

Image2copy = Image2.copy()

 

# paste image giving dimensions

Image1copy.paste(Image2copy, (0, 0))

 

# save the image 

Image1copy.save('D:\pasted2.png')  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190719161321/pasted2-225x300.png)

 **Example 2:** Changing paprameters to place the Image2 on face of the cat in
the Image1.

 __

 __  
 __

 __

 __  
 __  
 __

# import image module from pillow

from PIL import Image

 

# open the image

Image1 = Image.open('D:\cat.jpg')

 

# make a copy the image so that 

# the original image does not get affected

Image1copy = Image1.copy()

Image2 = Image.open('D:\core.jpg')

Image2copy = Image2.copy()

 

# paste image giving dimensions

Image1copy.paste(Image2copy, (70, 150))

 

# save the image 

Image1copy.save('D:\pasted2.png')  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190724103511/pasted21-225x300.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

