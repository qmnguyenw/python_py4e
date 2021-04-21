How to install OpenCV for Python in Windows?



 **Prerequisite:** Python Language Introduction  
  
OpenCV is the huge open-source library for computer vision, machine learning,
and image processing and now it plays a major role in real-time operation
which is very important in today’s systems. By using it, one can process
images and videos to identify objects, faces, or even the handwriting of a
human. When it integrated with various libraries, such as Numpuy, python is
capable of processing the OpenCV array structure for analysis. To Identify
image patterns and its various features we use vector space and perform
mathematical operations on these features.

To install OpenCV, one must have Python and PIP, preinstalled on their system.
To check if your system already contains Python, go through the following
instructions:

Open the **Command line** (search for **cmd** in the Run dialog( __**\+ R** ).  
Now run the following command:

    
    
    python --version
    

If Python is already installed, it will generate a message with the Python
version available.  
![python-version-check-windows](https://media.geeksforgeeks.org/wp-
content/uploads/20200117124014/python-version-check-windows.jpg)

If Python is not present, go through How to install Python on Windows? and
follow the instructions provided.  
  
**PIP** is a package management system used to install and manage software
packages/libraries written in Python. These files are stored in a large “on-
line repository” termed as Python Package Index (PyPI).  
To check if PIP is already installed on your system, just go to the command
line and execute the following command:

  

  

    
    
    pip -V

![Verification of pip](https://media.geeksforgeeks.org/wp-
content/uploads/20200117170656/pip-verification-windows.jpg)

If PIP is not present, go through How to install PIP on Windows? and follow
the instructions provided.

### Downloading and Installing OpenCV:

OpenCV can be directly downloaded and installed with the use of pip (package
manager). To install OpenCV, just go to the command-line and type the
following command:

    
    
    pip install opencv-python

 **Beginning with the installation:**

  *  **Type the command in the Terminal and proceed:**  
![Getting-Started](https://media.geeksforgeeks.org/wp-
content/uploads/20200122190245/OpenCV-Installation-Windows-01.jpg)

  *  **Collecting Information and downloading data:**  
![Downloading-Data-for-OpenCV](https://media.geeksforgeeks.org/wp-
content/uploads/20200122190247/OpenCV-Installation-Windows-02.jpg)

  *  **Installing Packages:**  
![Installing-Packages-OpenCV](https://media.geeksforgeeks.org/wp-
content/uploads/20200122190249/OpenCV-Installation-Windows-03.jpg)

  *  **Finished Installation:**  
![Finishing-Installation-OpenCV](https://media.geeksforgeeks.org/wp-
content/uploads/20200122190251/OpenCV-Installation-Windows-04.jpg)

To check if OpenCV is correctly installed, just run the following commands to
perform a version check:

    
    
    python
    >>>import cv2
    >>>print(cv2.__version__)
    

![OpenCV-Verification](https://media.geeksforgeeks.org/wp-
content/uploads/20200122190253/OpenCV-Verification.jpg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

