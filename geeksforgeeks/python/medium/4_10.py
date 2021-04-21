Create a Sideshow application in Python



In this article, we will create a slideshow application i.e we can see the
next image without changing it manually or by clicking.

#### Modules Required:

  *  **Tkinter:** The tkinter package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit.
  *  **Pillow:** The Python Imaging Library adds image processing capabilities to your Python interpreter. This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities. It can be installed using the below command:

    
    
    pip install Pillow
    

#### Step-by-step Approach:

  * Firstly we have to import the modules.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import required modules

import tkinter as tk

from tkinter import *

from PIL import Image

from PIL import ImageTk  
  
---  
  
 __

 __

  * Load the images.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# adjust window

root = tk.Tk()

root.geometry("200x200")

 

# loading the images

img = ImageTk.PhotoImage(Image.open("photo1.png"))

img2 = ImageTk.PhotoImage(Image.open("photo2.png"))

img3 = ImageTk.PhotoImage(Image.open("photo3.png"))

 

l = Label()

l.pack()  
  
---  
  
 __

 __

  * Now we have to make a function called _move_ to make the image move(It here means that one image appears and after a movement, it disappears.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# using recursion to slide to next image

x = 1

 

# function to change to next image

def move():

 global x

 if x == 4:

 x = 1

 if x == 1:

 l.config(image=img)

 elif x == 2:

 l.config(image=img2)

 elif x == 3:

 l.config(image=img3)

 x = x+1

 root.after(2000, move)

 

# calling the function

move()  
  
---  
  
 __

 __

  * Now we have to just call the mainloop function of tkinter to end the task.

## Python3

