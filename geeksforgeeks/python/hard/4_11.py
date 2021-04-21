Create Copy-Move GUI using Tkinter in Python



Everyone reading this post is well aware of the importance of Coping the file
or moving the file from one specific location to another. In this post, we
have tried to explain not only the program but added some exciting pieces of
Interface. Up to now, many of you may get about what we are talking about.
Yes, you are right, We are going to use “Tkinter” and “shutil” for this
project. So we will start it by Installing Packages.  

### Modules Required:

  *  **shutil :** Python _**shutil module**_ enables us to operate with file objects easily and without diving into file objects a lot. It takes care of low-level semantics like creating file objects, closing the files once they are copied, and allows us to focus on the business logic of our program. shutil is the native library, you don’t need to install it externally, just import, while you use it.
  *  **tkinter :** Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit or in simple words Tkinter is used as a python Graphical User interface. Tkinter is also the native library, you don’t need to install it externally, just import, while you use it.

The GUI would look like the below image:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210116125856/Screenshot240-660x121.png)

 **Below is the implementation:**  

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Importing necessary packages

import shutil

import tkinter as tk

from tkinter import *

from tkinter import messagebox, filedialog

 

# Defining CreateWidgets() function to

# create necessary tkinter widgets

def CreateWidgets():

 link_Label = Label(root, text ="Select The File To Copy : ",

 bg = "#E8D579")

 link_Label.grid(row = 1, column = 0,

 pady = 5, padx = 5)

 

 root.sourceText = Entry(root, width = 50,

 textvariable = sourceLocation)

 root.sourceText.grid(row = 1, column = 1,

 pady = 5, padx = 5,

 columnspan = 2)

 

 source_browseButton = Button(root, text ="Browse",

 command = SourceBrowse, width = 15)

 source_browseButton.grid(row = 1, column = 3,

 pady = 5, padx = 5)

 

 destinationLabel = Label(root, text ="Select The Destination :
",

 bg ="#E8D579")

 destinationLabel.grid(row = 2, column = 0,

 pady = 5, padx = 5)

 

 root.destinationText = Entry(root, width = 50,

 textvariable = destinationLocation)

 root.destinationText.grid(row = 2, column = 1,

 pady = 5, padx = 5,

 columnspan = 2)

 

 dest_browseButton = Button(root, text ="Browse",

 command = DestinationBrowse, width = 15)

 dest_browseButton.grid(row = 2, column = 3,

 pady = 5, padx = 5)

 

 copyButton = Button(root, text ="Copy File",

 command = CopyFile, width = 15)

 copyButton.grid(row = 3, column = 1,

 pady = 5, padx = 5)

 

 moveButton = Button(root, text ="Move File",

 command = MoveFile, width = 15)

 moveButton.grid(row = 3, column = 2,

 pady = 5, padx = 5)

def SourceBrowse():

 

 # Opening the file-dialog directory prompting

 # the user to select files to copy using

 # filedialog.askopenfilenames() method. Setting

 # initialdir argument is optional Since multiple

 # files may be selected, converting the selection

 # to list using list()

 root.files_list = list(filedialog.askopenfilenames(initialdir
="C:/Users/AKASH / Desktop / Lockdown Certificate / Geek For Geek"))

 

 # Displaying the selected files in the root.sourceText

 # Entry using root.sourceText.insert()

 root.sourceText.insert('1', root.files_list)

 

def DestinationBrowse():

 # Opening the file-dialog directory prompting

 # the user to select destination folder to

 # which files are to be copied using the

 # filedialog.askopendirectory() method.

 # Setting initialdir argument is optional

 destinationdirectory = filedialog.askdirectory(initialdir
="C:/Users/AKASH / Desktop / Lockdown Certificate / Geek For Geek")

 # Displaying the selected directory in the

 # root.destinationText Entry using

 # root.destinationText.insert()

 root.destinationText.insert('1', destinationdirectory)

 

def CopyFile():

 # Retrieving the source file selected by the

 # user in the SourceBrowse() and storing it in a

 # variable named files_list

 files_list = root.files_list

 # Retrieving the destination location from the

 # textvariable using destinationLocation.get() and

 # storing in destination_location

 destination_location = destinationLocation.get()

 # Looping through the files present in the list

 for f in files_list:

 

 # Copying the file to the destination using

 # the copy() of shutil module copy take the

 # source file and the destination folder as

 # the arguments

 shutil.copy(f, destination_location)

 messagebox.showinfo("SUCCESSFULL")

 

def MoveFile():

 

 # Retrieving the source file selected by the

 # user in the SourceBrowse() and storing it in a

 # variable named files_list'''

 files_list = root.files_list

 # Retrieving the destination location from the

 # textvariable using destinationLocation.get() and

 # storing in destination_location

 destination_location = destinationLocation.get()

 # Looping through the files present in the list

 for f in files_list:

 

 # Moving the file to the destination using

 # the move() of shutil module copy take the

 # source file and the destination folder as

 # the arguments

 shutil.move(f, destination_location)

 messagebox.showinfo("SUCCESSFULL")

# Creating object of tk class

root = tk.Tk()

 

# Setting the title and background color

# disabling the resizing property

root.geometry("830x120")

root.title("Copy-Move GUI")

root.config(background = "black")

 

# Creating tkinter variable

sourceLocation = StringVar()

destinationLocation = StringVar()

 

# Calling the CreateWidgets() function

CreateWidgets()

 

# Defining infinite loop

root.mainloop()  
  
---  
  
 __

 __

