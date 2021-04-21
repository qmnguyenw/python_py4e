How to create animated meteogram Python?



 **Meteogram** is also known as Meteorogram which is a graphical
representation of one or more meteorological variables with respect to time,
whether observed or forecast for a particular location.

## Structure of Meteogram

In Meteogram time is plotted along X-axis while the values of different
weather parameters are plotted along the Y-axis. The most common weather
parameters are Precipitation, Temperature, Air Pressure, Cloud Cover, Wind
Speed, and Wind Direction.

**Each frame contains 5-day Meteogram each having different graphs based on
weather parameters as:**

  * Temperature pictograms which will also display the time from sunrise to sunset,
  * Cloud Cover with different altitudes
  * Wind speed forecast will show in which direction the winds travel.

## Creating Animated Meteogram

Before we start creating Meteogram you should register on the Meteoblue
website and subscribe to the newsletter about your **Geolocation.** To get a
few Meteograms of your preferrable location it’ll take a few days to give you
the Meteogram. Then we wait for a few days to get almost 7-8 day Meteograms of
the geolocation and download the attachments of the Meteograms once we receive
them through email. Here in this case we have collected around 9 Meteograms
and created an animation of the Meteograms.

## Modules Needed

Using **imageio library** to create animated meteograms, has various functions
which allow us to read and write a wide range of image data including animated
images. The library can be installed using the command **pip.**

  

  

 **Pathlib** is a module in Python that provides object API for working with
files and directories.

    
    
    imageio
    pathlib

In our kernel, import the meteograms in the folder or directory and give the
title to the folder of your choice. Here, the title is **“Meteogram”.** The
**imageio library** supports all kinds of image formats. To read all the
images stored in the folder/directory execute the following command using
**imread() method** which is used to create NumPy array for all the images
with RGBA values then the Meteograms are stored in the list **image_list.**

Animating the Meteogram by storing the sample Meteogram attachments in a
directory and naming the folder as Meteogram **,** then using **imageio**
package animate or create a GIF for the attachments/images stored inside the
directory. Here, we import the **imageio** library and **pathlib** module then
to check the paths of images i.e **image_path** that are stored in the Email.

  * **image_path.glob(‘*.png’):** glob is the given pattern in the directory **‘source_images’** represented by this path, yields all matching files of any kind. ***** this pattern means it is recursive globbing.

>  **Syntax:** Path.glob(pattern)

  *  **imageio.imread(file_name):** For reading an image from a specified URI we have to use imageio.imread() method. Then this image is appended into the image_list which is then used for writing mages to animate the image (Meteogram)

>  **Syntax:** imageio.imread(“filename or path”)
>
>  **Parameter-**
>
>  **filename/path:** Absolute or Relative path of the image file.
>
>  **Returns:** numpy array which comes with a dict of metadata at its meta
> attribute.
>
>  
>
>
>  
>

 **Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing path library from pathlib package

from pathlib import Path

 

# extracting meteograms by specifying

# path of the folder

image_path = Path('../input/meteogram')

 

# images from folder is stored in image_list

images = list(image_path.glob('*.png'))

image_list = []

for file_name in images:

 

 # imread() creating numpy array

 # of every image stored in image_list

 image_list.append(imageio.imread(file_name))  
  
---  
  
 __

 __

The **image_list** command will display the data in the form of arrays for
every meteogram. Now proceeding to create an animated meteogram use
**mimwrite() method** after this the animated meteogramm will then be saved in
the directory specified by you and is in **.gif format.**

 **imageio.mimwrite():** using this function will write images to a specified
file **animated_meteogram.gif** taken from the **image_list**

>  **Syntax:** imageio.mimwrite(uri, ims, format=None, **kwargs)
>
>  **Parameter:**
>
>  **uri:** a file name or file object. ImageIO will write some images into
> this file.(e.g: animated_from_images.gif )
>
>  **ims:** a list of image data. Each image data you can read by
> imageio.imread() function
>
>  **format:** The format of uri, it can be .png, .gif etc

 **Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

imageio.mimwrite('animated_meteogram.gif', image_list)  
  
---  
  
 __

 __

After executing the above code animation of the Meteogram will be created and
the output is saved in the root directory in the name of
**animated_meteogram.gif** which will then animate the Meteogram.

### Below is the Complete Python Implementation:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import imageio packages

# Generate GIF/animation of meteogram

import imageio

from pathlib import Path

 

 

image_path = Path('../input/meteogram')

images = list(image_path.glob('*.png'))

 

# create an array to

# store meteogram images

image_list = []

for file_name in images:

 image_list.append(imageio.imread(file_name))

 

# to verify all images are read

image_list

 

# using this function will write images to a

# specified file animated_meteogram.gif

imageio.mimwrite('animated_meteogram.gif', image_list)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210217162949/meteogramweb-660x437.png)

Now let’s execute the python program we’ve written and this will show the
animation of the Meteogram we collected by extracting the attachments from the
email. In the below video we can see that a GIF file is created which is the
animated Meteogram as executed above.

https://media.geeksforgeeks.org/wp-
content/uploads/20210301182627/bandicam-2021-03-01-15-32-29-015_9fUYZRwE_HHY4.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

