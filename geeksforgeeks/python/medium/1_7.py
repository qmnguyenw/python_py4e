How to create a multiline entry with Tkinter?



 **Tkinter** is a library in Python for developing GUI. It provides various
widgets for developing GUI(Graphical User Interface). The Entry widget in
tkinter helps to take user input, but it collects the input limited to a
single line of text. Therefore, to create a Multiline entry text in tkinter
there are a number of ways.

**Methods to create multiline entry with tkinter:**

  1. Using Text Widget
  2. Using ScrolledText widget

 **Method 1:** Using Tkinter Text Widget

A text widget provides a multi-line text area for the user. The text widget
instance is created with the help of the text class. It is also used to
display text lines and also allows editing the text.

 **Syntax:**

  

  

    
    
    Text( root, optional parameters, ... )

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import tkinter as tk

from tkinter import ttk

 

 

window = tk.Tk()

window.title("Text Widget Example")

window.geometry('400x200')

 

ttk.Label(window, text="Enter your comment :",

 font=("Times New Roman", 15)).grid(

 column=0, row=15, padx=10, pady=25)

 

# Text Widget

t = tk.Text(window, width=20, height=3)

 

t.grid(column=1, row=15)

 

window.mainloop()  
  
---  
  
 __

 __

 **Output:**

![multiline text widget tkinter](https://media.geeksforgeeks.org/wp-
content/uploads/20210308171922/multilinetextwidgettkinter.gif)

The above output of the example lets the user enter text in multiple lines.
But it does not show all the text entered by the user beyond the height of the
text widget i.e., height=3. As it shows only 3 lines of text, therefore using
a scroll bar for such multiline texts will solve the problem.

 **Example 2:** Adding Scrollbar to text widget

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import tkinter as tk

 

 

window = tk.Tk()

window.title("Text Widget with Scrollbar")

 

text = tk.Text(window, height=8, width=40)

scroll = tk.Scrollbar(window)

text.configure(yscrollcommand=scroll.set)

text.pack(side=tk.LEFT)

 

scroll.config(command=text.yview)

scroll.pack(side=tk.RIGHT, fill=tk.Y)

 

insert_text = """GEEKSFORGEEKS :

A Computer Science portal for geeks.

It contains well written, well thought

and well explained computer science and

programming articles, quizzes and

many more.

GeeksforGeeks realises the importance of programming practice in the field
of

Computer Science.

That is why, it also provides an option of practicing problems.

This huge database of problems is created by programming experts.

The active team of GeeksforGeeks makes the learning process

interesting and fun.

"""

 

text.insert(tk.END, insert_text)

tk.mainloop()  
  
---  
  
 __

 __

 **Output:**

  

  

![multiline tkinter 1](https://media.geeksforgeeks.org/wp-
content/uploads/20210308172253/multilinetkinter1.gif)

 **Method 2:** Using ScrolledText tkinter Widget

Instead of adding a scroll bar to a text widget as seen in example 2, we can
directly use the ScrolledText tkinter widget for multiline entry by the user.
This widget automatically adds the scroll bar as the text gets increased than
the height of the scrolledText widget.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import tkinter as tk

from tkinter import ttk

from tkinter import scrolledtext

 

 

root = tk.Tk()

 

root.title("ScrolledText Widget Example")

 

ttk.Label(root, text="ScrolledText Widget Example",

 font=("Times New Roman", 15)).grid(column=0,
row=0)

ttk.Label(root, text="Enter your comments :", font=("Bold",
12)).grid

(column=0, row=1)

 

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD,

 width=40, height=8,

 font=("Times New Roman", 15))

 

text_area.grid(column=0, row=2, pady=10, padx=10)

 

# placing cursor in text area

text_area.focus()

root.mainloop()  
  
---  
  
 __

 __

 **Output:**

![scroll text tkinter](https://media.geeksforgeeks.org/wp-
content/uploads/20210308173152/scrolltexttkinter.gif)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

