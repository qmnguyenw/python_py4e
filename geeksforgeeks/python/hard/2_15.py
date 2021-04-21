Convert files from jpg to png and vice versa using Python



 **Prerequisite:**Pillow Library

Sometime it is required to attach the Image where we required image file with
the specified extension. And we have the image with the different extension
which needs to be converted with specified extension like in this we will
convert the image having Extension of **PNG to JPG** and Vice-Versa

And Also we will be creating the **GUI interface** to the Code so we will
require the Library **tkinter** **Tkinter**is a Python binding to the **Tk**
GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is
Python’s de facto standard GUI.

**Follow the below Steps:**

 **Step 1:** Import the library.

  

  

    
    
    from PIL import Image

 **Step 2:** JPG to PNG

    
    
    To covert the image From JPG to PNG : {Syntax}
    
    img = Image.open("Image.jpg")
    img.save("Image.png")

 **Step 3:** PNG → JPG

    
    
    To convert the Image From PNG to JPG
    
    img = Image.open("Image.png")
    img.save("Image.jpg")

Adding the GUI interface

    
    
    from tkinter import *

 **Approach:**

  1. In Function **jpg_to_png** we first Check whether The Selecting the image is in the same Format ( _.jpg)_ which to convert to . _png_ if not then return Error.
  2. Else Covert the image the to _.png_
  3. To open the Image we use the Function in tkinter called the **FileDialog** which helps to open the image from the folder  
from tkinter import filedialog as fd

  4. Same Approach for the PNG to JPG

 **Below is the Implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import all prerequisite

from tkinter import *

from tkinter import filedialog as fd

import os

from PIL import Image

from tkinter import messagebox

 

root = Tk()

 

# naming the GUI interface to image_conversion_APP

root.title("Image_Conversion_App")

 

# creating the Function which converts the jpg_to_png

def jpg_to_png():

 global im1

 

 # import the image from the folder

 import_filename = fd.askopenfilename()

 if import_filename.endswith(".jpg"):

 

 im1 = Image.open(import_filename)

 

 # after converting the image save to desired

 # location with the Extersion .png

 export_filename = fd.asksaveasfilename(defaultextension=".png")

 im1.save(export_filename)

 

 # displaying the Messaging box with the Sucess

 messagebox.showinfo("success ", "your Image converted to Png")

 else:

 

 # if Image select is not with the Format of .jpg 

 # then display the Error

 Label_2 = Label(root, text="Error!", width=20,

 fg="red", font=("bold", 15))

 Label_2.place(x=80, y=280)

 messagebox.showerror("Fail!!", "Something Went Wrong...")

 

 

def png_to_jpg():

 global im1

 import_filename = fd.askopenfilename()

 

 if import_filename.endswith(".png"):

 im1 = Image.open(import_filename)

 export_filename = fd.asksaveasfilename(defaultextension=".jpg")

 im1.save(export_filename)

 

 messagebox.showinfo("success ", "your Image converted to jpg ")

 else:

 Label_2 = Label(root, text="Error!", width=20,

 fg="red", font=("bold", 15))

 Label_2.place(x=80, y=280)

 

 messagebox.showerror("Fail!!", "Something Went Wrong...")

 

 

button1 = Button(root, text="JPG_to_PNG", width=20,
height=2, bg="green",

 fg="white", font=("helvetica", 12, "bold"),
command=jpg_to_png)

 

button1.place(x=120, y=120)

 

button2 = Button(root, text="PNG_to_JPEG", width=20,
height=2, bg="green",

 fg="white", font=("helvetica", 12, "bold"),
command=png_to_jpg)

 

button2.place(x=120, y=220)

root.geometry("500x500+400+200")

root.mainloop()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201207185258/image1.gif)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

