Build an Application for Changing PC’s Wallpaper using Python



 **Prerequisite:**Python GUI – tkinter

In this article, we are going to write a script for background changing
application using the **py-wallpaper** module in Python. The **py-wallpaper**
module is used to change the background wallpaper. Before starting we need to
install py-wallpaper.

 **Installation:**

To install this type the below command in the terminal.

    
    
    pip install py-wallpaper
    

### Getting Started

Import modules.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import modules

from wallpaper import set_wallpaper, get_wallpaper  
  
---  
  
 __

 __

Now you can get your current background image location with get_wallpaper
attributes and you can change with set_wallpaper.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# get current wallpaper's path

print(get_wallpaper())

 

# set your photo

set_wallpaper("location/to/image.jpg")  
  
---  
  
 __

 __

 **Output:**

    
    
    D:\img\wallpapersden.com_money-heist_3840x2232.jpg
    

**Background changer Application with** **Tkinter** **:** This Script
implements the above Implementation into a GUI.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import modules

from tkinter import *

from tkinter import filedialog

from wallpaper import set_wallpaper

 

# user define funtion

def change_wall():

 

 # set your photo

 try:

 set_wallpaper(str(path.get()))

 check = "success"

 

 except:

 

 check = "Wallpaper not found !"

 result.set(check)

 

 

def browseFiles():

 filename = filedialog.askopenfilename(initialdir="/",

 title="Select a File",

 filetypes=(("jpeg files", "*.jpg"), ("all files",
"*.*")))

 path.set(filename)

 

 # Change label contents

 label_file_explorer.configure(text="File Opened: "+filename)

 return filename

 

 

# object of tkinter

# and background set for red

master = Tk()

master.configure(bg='light grey')

 

# Variable Classes in tkinter

result = StringVar()

path = StringVar()

 

 

label_file_explorer = Label(

 master, text="Select a image", width=100, fg="blue")

 

 

# Creating label for each information

# name using widget Label

Label(master, text="Select image : ", bg="light
grey").grid(row=0, sticky=W)

Label(master, text="Status :", bg="light grey").grid(row=3,
sticky=W)

 

 

# Creating lebel for class variable

# name using widget Entry

Label(master, text="", textvariable=result,

 bg="light grey").grid(row=3, column=1, sticky=W)

 

# creating a button using the widget

# Button that will call the submit function

b = Button(master, text="Open", command=browseFiles,
bg="white")

b.grid(row=0, column=2, columnspan=2, rowspan=2,
padx=5, pady=5,)

 

label_file_explorer.grid(column=1, row=1)

 

c = Button(master, text="Apply", command=change_wall,
bg="white")

c.grid(row=2, column=2, columnspan=2, rowspan=2,
padx=5, pady=5,)

 

mainloop()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200911203558/Screenshot169-660x489.png)

After selecting this wallpaper.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200911203601/Screenshot170-660x278.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

