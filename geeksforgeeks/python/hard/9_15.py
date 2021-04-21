Determine the type of an image in Python using imghdr



Suppose you are given an image type file and you need to determine the type of
that file. In simple words, you need to get the extension of that image type
file. This can be used in a project to verify whether the image you have
requested for is actually an image and with which extension does it come.

 **imghdr module**

 **Use following command for Installation:**

    
    
    npm install imghdr

 **Description:**  
The imghdr module determines the type of image contained in a file or byte
stream. The imghdr module defines the following function:

    
    
    imghdr.what(filename[, h])

Tests the image data contained in the file named by filename, and returns a
string describing the image type. If optional h is provided, the filename is
ignored and h is assumed to contain the byte stream to test.

  

  

Note: The path of the file needs to be correct with its correct name. If the
image file and the code file are in the same directory, you don’t need to
specify the whole path. Just pass the name of the file as I did in the next
example

The extensions that can be recognized in module are-‘rgb’, ‘gif’,’ pbm’,’
pgm’,’ ppm’,’ tiff’, ‘rast’, ‘xbm’, ‘jpeg’, ‘bmp’, ‘png’, ‘webp’, ‘exr’. In
Python 3.5, extensions ‘exr’ and ‘webp’ are also added.Value| Image Format|
‘rgb’| SGI ImgLib Files| ‘gif’| GIF 87a and 89a Files| ‘pbm’| Portable Bitmap
Files| ‘pgm’| Portable Graymap Files| ‘ppm’| Pportable Pixmap Files| ‘tiff’|
IFF Files| ‘rast’| Sun Raster Files| ‘xbm’| X Bitmap Files| ‘jpeg’| JPEG data
in JFIF or Exif formats| ‘bmp’| BMP Files| ‘png’| Portable Network Graphics|
‘webp’| WebP Files| ‘exr’| OpenEXR Files  
---|---  
  
 **Example :**

    
    
    Input : picture.gif
    Output : gif
    
    Input: picture.jpeg
    Output : jpeg
    

__

__  
__

__

__  
__  
__

import imghdr

x = imghdr.what("picture.gif") 

#path of image as parameter

 

print(x)  
  
---  
  
 __

 __

Output:

    
    
    gif
    

This is a simple program but used to solve big problems in real life projects.

This article is contributed by **Rishabh Bansal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

