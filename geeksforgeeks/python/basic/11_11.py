Python | Working with the Image Data Type in pillow



In this article, we will look into some attributes of an Image object that
will give information about the image and the file it was loaded from. For
this, we will need to import image module from pillow.

 **Image we will be working on :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190719163022/cat2-225x300.jpg)

 **size() method –** It helps to get the dimensions of an image.

> IMG = Image.open( _Image_path_ )  
> croppedIm = _IMG_.size

 __

 __  
 __

 __

 __  
 __  
 __

# import Image module

from PIL import Image

 

# open the image

catIm = Image.open('D:/cat.jpg')

 

# Display the dimensions of the image

print(catIm.size)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    (400, 533)

 **Getting height and width separately –** It helps us to get the height and
width of the image.

 __

 __  
 __

 __

 __  
 __  
 __

# import Image module

from PIL import Image

 

# Open the image

catIm = Image.open('D:/cat.jpg')

 

# Create two different variables 

# The first one will contain width and 

# the second one will contain height

width, height = catIm.size

 

# Display height and width

print(height)

print(width)  
  
---  
  
 __

 __

 **Output :**

    
    
    400
    533

  
**filename() method –** It helps us to get the filename of the image.

> IMG = Image.open( _Image_path_ )  
> croppedIm = _IMG_.filename

 __

 __  
 __

 __

 __  
 __  
 __

# import the Image module

from PIL import Image

 

# Open the image

catIm = Image.open('D:/cat.jpg')

 

# print the filename

print(catIm.filename)  
  
---  
  
 __

 __

 **Output :**

    
    
    D:/cat.jpg

  
**format() method –** It helps us to get the format the image is in.

> IMG = Image.open( _Image_path_ )  
> croppedIm = _IMG_.format

 __

 __  
 __

 __

 __  
 __  
 __

# import the image

from PIL import Image

 

# open the image

catIm = Image.open('D:/cat.jpg')

 

# print the format of the image

print(catIm.format)  
  
---  
  
 __

 __

 **Output :**

    
    
    JPEG

  
**format_description() method –** It helps us to get the format description of
the image.

> IMG = Image.open( _Image_path_ )  
> croppedIm = _IMG_.format_description

 __

 __  
 __

 __

 __  
 __  
 __

# import the image

from PIL import Image

 

# open the image

catIm = Image.open('D:/cat.jpg')

 

# print the format description of the image

print(catIm.format_description)  
  
---  
  
 __

 __

 **Output :**

    
    
    JPEG (ISO 10918)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

