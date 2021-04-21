Python | asksaveasfile() function in Tkinter



Python provides a variety of modules with the help of which one may develop
GUI (Graphical User Interface) applications. Tkinter is one of the easiest and
fastest way to develop GUI applications.

While working with files one may need to open files, do operations on files
and after that to save file. asksaveasfile() is the function which is used
to save user’s file (extension can be set explicitly or you can set default
extensions also). This function comes under the **class filedialog**.

Below is the Code:

 __

 __  
 __

 __

 __  
 __  
 __

# importing all files from tkinter

from tkinter import *

from tkinter import ttk

 

# import only asksaveasfile from filedialog

# which is used to save file in any extension

from tkinter.filedialog import asksaveasfile

 

root = Tk()

root.geometry('200x150')

 

# function to call when user press

# the save button, a filedialog will

# open and ask to save file

def save():

 files = [('All Files', '*.*'), 

 ('Python Files', '*.py'),

 ('Text Document', '*.txt')]

 file = asksaveasfile(filetypes = files, defaultextension =
files)

 

btn = ttk.Button(root, text = 'Save', command = lambda :
save())

btn.pack(side = TOP, pady = 20)

 

mainloop()  
  
---  
  
 __

 __

 **Output #1:** Directory before saving any file (folder is initially empty)  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190403163934/folder_before_saving_a_file-300x239.png)

 **Output #2:** Dialogbox when user presses the save button (dialog box to
save file is opened). You may see in the output Python file as default is
selected.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190403164037/creating_new_python_file-300x208.png)

  

  

 **Output #3:** Directory after saving 2 Python files (one may also change the
type of file)  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190403164217/content_of_folder_after_saving_2_file-300x233.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

