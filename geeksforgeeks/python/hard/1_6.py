Storing OpenCV Image in SQLite3 with Python



 **OpenCV** is a huge open-source library for computer vision, machine
learning, and image processing. OpenCV supports a wide variety of programming
languages like Python, C++, Java, etc. It can process images and videos to
identify objects, faces, or even the handwriting of a human. When it is
integrated with various libraries, such as Numpy. Which is a highly optimized
library for numerical operations, then the number of weapons increases in your
Arsenal i.e whatever operations one can do in Numpy can be combined with
OpenCV.

 **SQLite** is a self-contained, high-reliability, embedded, full-featured,
public-domain, SQL database engine. It is the most used database engine on the
World Wide Web. Python has a library to access SQLite databases, called
sqlite3, intended for working with this database which has been included with
Python package since version 2.5.

In this article, we will store an OpenCV image in sqlite3 database with
Python. Let’s take this image “gfg.png” as an example:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210228231058/gfg-300x300.png)

###  **Step-by-step Approach:**

  * First import the necessary libraries.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import neccessary libraries

import cv2

import sqlite3

import pandas as pd  
  
---  
  
 __

 __

