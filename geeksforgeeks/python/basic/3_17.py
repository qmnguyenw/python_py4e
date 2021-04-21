Setup OpenCV With PyCharm Environment



If you love working on image processing and video analysis using python then
you have come to the right place. Python is one of the key languages which is
used to process videos and images.

#### Requirements for OpenCV:

  * 32- or a 64-bit computer.
  * Windows, macOS or Linux.
  * Python 2.7, 3.4, 3.5 or 3.6.

### PyCharm

PyCharm is a cross-platform IDE used in computer programming specifically for
Python. The platform developed by JetBrains is mainly used in code analysis,
graphical debugger etc… It supports web development with Django as well as
Data Science with Anaconda.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200920011726/Untitleddrawing-660x412.jpg)

#### Official Website: https://www.jetbrains.com/pycharm/

### OpenCV

OpenCV (Open Source Computer Vision) is a computer vision library that
contains various functions to perform operations on pictures or videos. It was
initially built by Intel but later managed by Willow Garag, presently it is
managed by Itseez. It is a cross-platform library which available for
programming languages apart from python.

![](https://media.geeksforgeeks.org/wp-content/uploads/1200px-
OpenCV_Logo_with_text_svg_version.svg_-244x300.png)

  

  

### Steps to import OpenCV on PyCharm:

 **1)** Go to the terminal option at the bottom of the IDE window.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200920012752/Untitleddrawing1-660x301.jpg)

**2)** The pip (package manager) can also be used to download and install
OpenCV. To install OpenCV, just type the following command:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

pip install opencv-python  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200920013226/Untitleddrawing2-660x171.jpg)

 **3)** Now simply import OpenCV in your python program in which you want to
use image processing functions.

To check if OpenCV is correctly installed, just run the following program in
PyCharm to perform a version check:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import cv2

print("GeeksForGeeks")

print("Your OpenCV version is: " + cv2.__version__)  
  
---  
  
 __

 __

#### Output:

    
    
    GeeksForGeeks
    Your OpenCV version is: 4.4.0
    

![](https://media.geeksforgeeks.org/wp-content/uploads/20200920013759/gfg.jpg)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

