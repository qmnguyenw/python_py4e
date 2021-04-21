Python Tkinter – ScrolledText Widget



 **Tkinter** is a built-in standard python library. With the help of Tkinter,
many GUI applications can be created easily. There are various types of
widgets available in Tkinter such as button, frame, label, menu, scrolledtext,
canvas and many more. A widget is an element that provides various controls.
ScrolledText widget is a text widget with a scroll bar. The
tkinter.scrolledtext module provides the text widget along with a scroll
bar. This widget helps the user enter multiple lines of text with convenience.
Instead of adding a Scroll bar to a text widget, we can make use of a
scrolledtext widget that helps to enter any number of lines of text.

 **Example 1 :** Python code displaying scrolledText widget.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program demonstrating

# ScrolledText widget in tkinter

 

import tkinter as tk

from tkinter import ttk

from tkinter import scrolledtext

 

# Creating tkinter main window

win = tk.Tk()

win.title("ScrolledText Widget")

 

# Title Label

ttk.Label(win, 

 text = "ScrolledText Widget Example",

 font = ("Times New Roman", 15), 

 background = 'green', 

 foreground = "white").grid(column = 0,

 row = 0)

 

# Creating scrolled text 

# area widget

text_area = scrolledtext.ScrolledText(win, 

 wrap = tk.WORD, 

 width = 40, 

 height = 10, 

 font = ("Times New Roman",

 15))

 

text_area.grid(column = 0, pady = 10, padx = 10)

 

# Placing cursor in the text area

text_area.focus()

win.mainloop()  
  
---  
  
 __

 __

 **Output :**  
![Scrolledtext widget](https://media.geeksforgeeks.org/wp-
content/uploads/20200403021652/ScrolledText_widget1.jpg)

 **Example 2 :** ScrolledText widget making tkinter text Read only.

 __

 __  
 __

 __

 __  
 __  
 __

# Importing required modules

 

import tkinter as tk

import tkinter.scrolledtext as st

 

# Creating tkinter window

win = tk.Tk()

win.title("ScrolledText Widget")

 

# Title Label

tk.Label(win, 

 text = "ScrolledText Widget Example", 

 font = ("Times New Roman", 15), 

 background = 'green', 

 foreground = "white").grid(column = 0,

 row = 0)

 

# Creating scrolled text area

# widget with Read only by

# disabling the state

text_area = st.ScrolledText(win,

 width = 30, 

 height = 8, 

 font = ("Times New Roman",

 15))

 

text_area.grid(column = 0, pady = 10, padx = 10)

 

# Inserting Text which is read only

text_area.insert(tk.INSERT,

"""\

This is a scrolledtext widget to make tkinter text read only.

Hi

Geeks !!!

Geeks !!!

Geeks !!! 

Geeks !!!

Geeks !!!

Geeks !!!

Geeks !!!

""")

 

# Making the text read only

text_area.configure(state ='disabled')

win.mainloop()  
  
---  
  
 __

 __

 **Output :**  
![scrolledtext_widget](https://media.geeksforgeeks.org/wp-
content/uploads/20200409192258/scrolledtext_widget1.png)

In the first example, as you can see the cursor, the user can enter any number
of lines of text. In the second example, the user can just read the text which
is displayed in the text box and cannot edit/enter any lines of text. We may
observe that the scroll bar disappears automatically if the text entered by
the user is less than the size of the widget.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

