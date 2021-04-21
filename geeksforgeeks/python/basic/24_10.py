Set up Opencv with anaconda environment



If you love working on image processing and video analysis using python then
you have come to the right place. Python is one of the major languages that
can be used to process images or videos.

 **Requirements for OpenCV and Anaconda**  
– 32- or a 64-bit computer.  
– For Miniconda—400 MB disk space.  
– For Anaconda—Minimum 3 GB disk space to download and install.  
– Windows, macOS or Linux.  
– Python 2.7, 3.4, 3.5 or 3.6.

 **ANACONDA**

Anaconda is a open source software that contains jupiter, spyder etc that are
used for large data processing, data analytics, heavy scientific computing.
Anaconda works for R and python programming language. Spyder(sub-application
of Anaconda) is used for python.Opencv for python will work in skyder. Package
versions are managed by the package management system conda.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/Anaconda_Logo-300x150.png)

 **Installing Anaconda :** Head over to continuum.io/downloads/ and install
the latest version of Anaconda. Make sure to install the “Python 3.6 Version”
for the appropriate architecture. Install it with the default settings.  
![](https://chrisconlan.com/wp-content/uploads/2017/05/anaconda_1.png)

  

  

 **OPENCV**

OpenCV (Open Source Computer Vision) is a computer vision library that
contains various functions to perform operations on pictures or videos. It was
originally developed by Intel but was later maintained by Willow Garage and is
now maintained by Itseez. This library is cross-platform that is it is
available on multiple programming language such as Python, C++ etc.  
![](https://media.geeksforgeeks.org/wp-content/uploads/1200px-
OpenCV_Logo_with_text_svg_version.svg_-244x300.png)

 **Steps to import opencv on anaconda in windows environment** ‘

  1.  **Creating Anaconda Environment :**  
 **Step 1:-** Search Anaconda in your task bar and select ANACONDA NAVIGATOR.  
![](https://chrisconlan.com/wp-content/uploads/2017/05/anaconda_prompt.png)  
 **Step 2:-** Now you will see a menu with various options like Jupiter
notebook , Spyder etc. This is Anaconda Environment.  
 **Step 3:-** Select Spyder as it is Anaconda’s IDE for python and OpenCV
library will work in it only.

  2.  **Install OpenCV**  
 **Step 1 :-** After installing the anaconda open the Anaconda Prompt.

![](https://media.geeksforgeeks.org/wp-content/uploads/sca.png)  
 **Step 2 :-** Type the given command,press enter and let it download the
whole package.  
Command

    
    
    conda install -c menpo opencv
    

**Step 3 :-** Now simply import opencv in your python program in which you
want to use image processing functions.

 **Examples:** **Some basic functions of the opencv library (These functions
are performed on Windows flavour of Anaconda but it will work on linux flavor
too)**

  *  **Reading a image**
    
    
    img = cv2.imread('LOCATION OF THE IMAGE')
    

The above function imread stores the image at the given location to the
variable img.

  *  **Converting a image to greyscale**
    
    
    img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
    

The above function converts the image to grayscale and then stores it in the
variable img.

  *  **Showing the stored image**
    
    
    cv2.imshow('image',img)
    

The above function shows the image stored in img variable.

  *  **Save an image to a file**
    
    
    imwrite(filename, img)
    

The above function stores the image to the file. The image is stored in the
variable of type Mat that is in the form of a matrix.

  *  **Reading video directly from the webcam**
    
    
    cap = cv2.VideoCapture(0)
    

Stores live video from your webcam in variable cap.

  *  **Reading a video from local storage**
    
    
    cap = cv2.VideoCapture('LOCATION OF THE VIDEO')
    

Stores the video located in the given location to the variable.

  *  **To check if the video is successfully stored in the variable**
    
    
    cap.isOpened()
    

cap is the variable that contains the video. The above function returns true
if the video is successfully opened else returns false.

  *  **Release the stored video after processing is done**
    
    
    cap.release()
    

The above function releases the video stored in cap.

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

