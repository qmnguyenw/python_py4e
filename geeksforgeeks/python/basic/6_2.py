Create GUI for Downloading Youtube Video using Python



 **Prerequisites:** Python GUI – tkinter

YouTube is a very popular video-sharing website. Downloading a
video’s/playlist from YouTube is a tedious task. Downloading that video
through Downloader or trying to download it from a random website which
increase’s the risk of licking your personal data. Using the Python Tkinter
package, this task is very simple-efficient-safe. Few bunch codes will
download the video for you. For this, there are two Python libraries –
**Tkinter** and **pytube**.

### Modules Required

  *  **pytube :** pytube is a light-weight, simple-to-use, dependency-free Python library which is used for downloading videos from the web.pytube, is not the auto-configured library. You need to install it before using it. Installation of pytube is easy when you have pip. In the Terminal or Command Prompt, type the following command to install pytube.

 **If you are on Mac OS X or Linux, chances are that one of the following two
commands will work for you:**

> pip install pytube  
> git clone git://github.com/NFicano/pytube.git pytube | cd pytube | python
> setup.py install

 **If you are on Window’s**

  

  

    
        pip install pytube3

  *  **Tkinter :**Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit or in simple word Tkinter is used for as Python Graphical User interface. Tkinter is the native library, you don’t need to install externally, just import, while you use.

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Importing necessary packages

import tkinter as tk

from tkinter import *

from pytube import YouTube

from tkinter import messagebox, filedialog

 

 

# Defining CreateWidgets() function

# to create necessary tkinter widgets

def Widgets():

 link_label = Label(root, 

 text="YouTube link :",

 bg="#E8D579")

 link_label.grid(row=1,

 column=0,

 pady=5,

 padx=5)

 

 root.linkText = Entry(root,

 width=55,

 textvariable=video_Link)

 root.linkText.grid(row=1, 

 column=1,

 pady=5,

 padx=5,

 columnspan = 2)

 

 destination_label = Label(root, 

 text="Destination :",

 bg="#E8D579")

 destination_label.grid(row=2,

 column=0,

 pady=5,

 padx=5)

 

 root.destinationText = Entry(root,

 width=40,

 textvariable=download_Path)

 root.destinationText.grid(row=2, 

 column=1,

 pady=5,

 padx=5)

 

 browse_B = Button(root, 

 text="Browse",

 command=Browse,

 width=10,

 bg="#05E8E0")

 browse_B.grid(row=2,

 column=2,

 pady=1,

 padx=1)

 

 Download_B = Button(root,

 text="Download", 

 command=Download, 

 width=20,

 bg="#05E8E0")

 Download_B.grid(row=3,

 column=1,

 pady=3,

 padx=3)

 

# Defining Browse() to select a 

# destination folder to save the video

 

def Browse():

 # Presenting user with a pop-up for

 # directory selection. initialdir 

 # argument is optional Retrieving the

 # user-input destination directory and

 # storing it in downloadDirectory

 download_Directory = filedialog.askdirectory(initialdir="YOUR
DIRECTORY PATH")

 

 # Displaying the directory in the directory

 # textbox

 download_Path.set(download_Directory)

 

# Defining Download() to download the video

def Download():

 

 # getting user-input Youtube Link

 Youtube_link = video_Link.get()

 

 # select the optimal location for

 # saving file's

 download_Folder = download_Path.get()

 

 # Creating object of YouTube()

 getVideo = YouTube(Youtube_link)

 

 # Getting all the available streams of the

 # youtube video and selecting the first

 # from the

 videoStream = getVideo.streams.first()

 

 # Downloading the video to destination 

 # directory

 videoStream.download(download_Folder)

 

 # Displaying the message

 messagebox.showinfo("SUCCESSFULLY", 

 "DOWNLOADED AND SAVED IN\n"

 + download_Folder)

 

# Creating object of tk class

root = tk.Tk()

 

# Setting the title, background color 

# and size of the tkinter window and 

# disabling the resizing property

root.geometry("600x120")

root.resizable(False, False)

root.title("YouTube_Video_Downloader")

root.config(background="#000000")

 

# Creating the tkinter Variables

video_Link = StringVar()

download_Path = StringVar()

 

# Calling the Widgets() function

Widgets()

 

# Defining infinite loop to run

# application

root.mainloop()  
  
---  
  
 __

 __

 **Output:**

![python-download-youtube-video](https://media.geeksforgeeks.org/wp-
content/uploads/20200602183648/python-download-youtube-video.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

