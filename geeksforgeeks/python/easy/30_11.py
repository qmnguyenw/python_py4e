Working with Images in Python



PIL is the Python Imaging Library which provides the python interpreter with
image editing capabilities. It was developed by Fredrik Lundh and several
other contributors. Pillow is the friendly PIL fork and an easy to use library
developed by Alex Clark and other contributors. We’ll be working with Pillow.

 **Installation:**

  *  **Linux:** On linux terminal type the following:
    
        pip install Pillow

Installing pip via terminal:

    
        sudo apt-get update
    sudo apt-get install python-pip

  *  **Windows:** Download the appropriate Pillow package according to your python version. Make sure to download according to the python version you have.

We’ll be working with the Image Module here which provides a class of the same
name and provides a lot of functions to work on our images.To import the Image
module, our code should begin with the following line:

    
    
     from PIL import Image

 **Operations with Images:**

  

  

  *  **Open a particular image from a path:**

 __

 __  
 __

 __

 __  
 __  
 __

#img = Image.open(path)

# On successful execution of this statement,

# an object of Image type is returned and stored in img variable)

 

try: 

 img = Image.open(path) 

except IOError:

 pass

# Use the above statement within try block, as it can 

# raise an IOError if file cannot be found, 

# or image cannot be opened.  
  
---  
  
 __

 __

  *  **Retrieve size of image** : The instances of Image class that are created have many attributes, one of its useful attribute is size.

 __

 __  
 __

 __

 __  
 __  
 __

from PIL import Image

 

filename = "image.png"

with Image.open(filename) as image:

 width, height = image.size

#Image.size gives a 2-tuple and the width, height can be obtained  
  
---  
  
 __

 __

Some other attributes are: Image.width, Image.height, Image.format, Image.info
etc.

  *  **Save changes in image:** To save any changes that you have made to the image file, we need to give path as well as image format.

 __

 __  
 __

 __

 __  
 __  
 __

img.save(path,format) 

# format is optional, if no format is specified, 

#it is determined from the filename extension  
  
---  
  
 __

 __

  *  **Rotating an Image:** The image rotation needs angle as parameter to get the image rotated.

 __

 __  
 __

 __

 __  
 __  
 __

from PIL import Image

 

def main():

 try:

 #Relative Path

 img = Image.open("picture.jpg") 

 

 #Angle given

 img = img.rotate(180) 

 

 #Saved in the same relative location

 img.save("rotated_picture.jpg")

 except IOError:

 pass

 

if __name__ == "__main__":

 main()  
  
---  
  
 __

 __

![rotating an image in python](https://media.geeksforgeeks.org/wp-
content/uploads/rotating-an-image-in-python.png)  
Note: There is an optional expand flag available as one of the argument of the
rotate method, which if set true, expands the output image to make it large
enough to hold the full rotated image.  
As seen in the above code snippet, I have used a relative path where my image
is located in the same directory as my python code file, an absolute path can
be used as well.

  *  **Cropping an Image:** Image.crop(box) takes a 4-tuple (left, upper, right, lower) pixel coordinate, and returns a rectangular region from the used image.

 __

 __  
 __

 __

 __  
 __  
 __

from PIL import Image

 

def main():

 try:

 #Relative Path

 img = Image.open("picture.jpg")

 width, height = img.size

 

 area = (0, 0, width/2, height/2)

 img = img.crop(area)

 

 #Saved in the same relative location

 img.save("cropped_picture.jpg") 

 

 except IOError:

 pass

 

if __name__ == "__main__":

 main()  
  
---  
  
 __

 __

![cropping an image in python](https://media.geeksforgeeks.org/wp-
content/uploads/cropping-an-image-in-python.png)

  *  **Resizing an Image:** Image.resize(size)- Here size is provided as a 2-tuple width and height.

 __

 __  
 __

 __

 __  
 __  
 __

from PIL import Image

 

def main():

 try:

 #Relative Path

 img = Image.open("picture.jpg")

 width, height = img.size

 

 img = img.resize((width/2, height/2))

 

 #Saved in the same relative location

 img.save("resized_picture.jpg") 

 except IOError:

 pass

 

if __name__ == "__main__":

 main()  
  
---  
  
 __

 __

![resizing an image in python](https://media.geeksforgeeks.org/wp-
content/uploads/resizing-an-image-in-python.png)

  *  **Pasting an image on another image:** The second argument can be a 2-tuple (specifying the top left corner), or a 4-tuple (left, upper, right, lower) – in this case the size of pasted image must match the size of this box region, or None which is equivalent to (0, 0).

 __

 __  
 __

 __

 __  
 __  
 __

from PIL import Image

 

def main():

 try:

 #Relative Path

 #Image on which we want to paste

 img = Image.open("picture.jpg") 

 

 #Relative Path

 #Image which we want to paste

 img2 = Image.open("picture2.jpg") 

 img.paste(img2, (50, 50))

 

 #Saved in the same relative location

 img.save("pasted_picture.jpg")

 

 except IOError:

 pass

 

if __name__ == "__main__":

 main()

 

##An additional argument for an optional image mask image is also available.  
  
---  
  
 __

 __

![pasting an image on other in Python](https://media.geeksforgeeks.org/wp-
content/uploads/pasting-an-image-on-other-in-Python.png)

  *  **Getting a Histogram of an Image:** This will return a histogram of the image as a list of pixel counts, one for each pixel in the image. (A histogram of an image is a graphical representation of the tonal distribution in a digital image. It contains what all the brightness values contained in an image are. It plots the number of pixels for each brightness value. It helps in doing the exposure settings.)  
from PIL import Image

 __

 __  
 __

 __

 __  
 __  
 __

def main():

 try:

 #Relative Path

 img = Image.open("picture.jpg") 

 

 #Getting histogram of image

 print img.histogram()

 

 except IOError:

 pass

 

if __name__ == "__main__":

 main()  
  
---  
  
 __

 __

![getting a histogram of image in python](https://media.geeksforgeeks.org/wp-
content/uploads/getting-a-histogram-of-image-in-python.png)

  *  **Transposing an Image:** This feature gives us the mirror image of an image

 __

 __  
 __

 __

 __  
 __  
 __

from PIL import Image

 

def main():

 try:

 #Relative Path

 img = Image.open("picture.jpg") 

 

 #transposing image 

 transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

 

 #Save transposed image

 transposed_img.save("transposed.jpg")

 except IOError:

 pass

 

if __name__ == "__main__":

 main()  
  
---  
  
 __

 __

![transposing an image in python](https://media.geeksforgeeks.org/wp-
content/uploads/transposing-an-image-in-python.png)

  *  **Split an image into individual bands:** Splitting an image in RGB mode, creates three new images each containing a copy of the original individual bands.

 __

 __  
 __

 __

 __  
 __  
 __

from PIL import Image

 

def main():

 try:

 #Relative Path

 img = Image.open("picture.jpg") 

 

 #splitting the image

 print img.split()

 except IOError:

 pass

 

if __name__ == "__main__":

 main()  
  
---  
  
 __

 __

![split an image in python](https://media.geeksforgeeks.org/wp-
content/uploads/split-an-image-in-python.png)

  *  **tobitmap:** Converting an image to an X11 bitmap (A plain text binary image format). It returns a string containing an X11 bitmap, it can only be used for mode “1” images, i.e. 1 bit pixel black and white images.  
from PIL import Image

 __

 __  
 __

 __

 __  
 __  
 __

def main():

 try:

 #Relative Path

 img = Image.open("picture.jpg") 

 print img.mode

 

 #converting image to bitmap

 print img.tobitmap()

 

 print type(img.tobitmap())

 except IOError:

 pass

 

if __name__ == "__main__":

 main()  
  
---  
  
 __

 __

![converting image to bitmap in python](https://media.geeksforgeeks.org/wp-
content/uploads/converting-image-to-bitmap-in-python.png)  
![converting image to bitmao in python](https://media.geeksforgeeks.org/wp-
content/uploads/converting-image-to-bitmao-in-python.png)

  *  **Creating a thumbnail:** This method creates a thumbnail of the image that is opened. It does not return a new image object, it makes in-place modification to the currently opened image object itself. If you do not want to change the original image object, create a copy and then apply this method. This method also evaluates the appropriate to maintain the aspect ratio of the image according to the size passed.  
from PIL import Image

 __

 __  
 __

 __

 __  
 __  
 __

def main():

 try:

 #Relative Path

 img = Image.open("picture.jpg") 

 

 #In-place modification

 img.thumbnail((200, 200)) 

 

 img.save("thumb.jpg")

 except IOError:

 pass

 

if __name__ == "__main__":

 main()  
  
---  
  
 __

 __

![creating thumbnail of image in python](https://media.geeksforgeeks.org/wp-
content/uploads/creating-thumbnail-of-image-in-python1.png)

This article is contributed by **Mohit Agarwal**. If you like GeeksforGeeks
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

