Python | pack() method in Tkinter



The Pack geometry manager packs widgets in rows or columns. We can use options
like **fill** , **expand** , and **side** to control this geometry manager.  
Compared to the **grid** manager, the **pack** manager is somewhat limited,
but it’s much easier to use in a few, but quite common situations:

  * Put a widget inside a frame (or any other container widget), and have it fill the entire frame
  * Place a number of widgets on top of each other
  * Place a number of widgets side by side

 **Code #1:** Putting a widget inside frame and filling entire frame. We can
do this with the help of **expand** and **fill** options.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing tkinter module

from tkinter import * from tkinter.ttk import *

# creating Tk window

master = Tk()

# cretaing a Fra, e which can expand according

# to the size of the window

pane = Frame(master)

pane.pack(fill = BOTH, expand = True)

# button widgets which can also expand and fill

# in the parent widget entirely

# Button 1

b1 = Button(pane, text = "Click me !")

b1.pack(fill = BOTH, expand = True)

# Button 2

b2 = Button(pane, text = "Click me too")

b2.pack(fill = BOTH, expand = True)

# Execute Tkinter

master.mainloop()  
  
---  
  
 __

 __

 **Output:**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190606133427/Capture34-3.png)

  

  

**Code #2:** Placing widgets on top of each other and side by side. We can do
this by side option.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing tkinter module

from tkinter import *

# from tkinter.ttk import *

# creating Tk window

master = Tk()

# cretaing a Fra, e which can expand according

# to the size of the window

pane = Frame(master)

pane.pack(fill = BOTH, expand = True)

# button widgets which can also expand and fill

# in the parent widget entirely

# Button 1

b1 = Button(pane, text = "Click me !",

 background = "red", fg = "white")

b1.pack(side = TOP, expand = True, fill = BOTH)

# Button 2

b2 = Button(pane, text = "Click me too",

 background = "blue", fg = "white")

b2.pack(side = TOP, expand = True, fill = BOTH)

# Button 3

b3 = Button(pane, text = "I'm also button",

 background = "green", fg = "white")

b3.pack(side = TOP, expand = True, fill = BOTH)

# Execute Tkinter

master.mainloop()  
  
---  
  
 __

 __

 **Output:**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190606134014/Capture34-3.png)

**Code #3:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing tkinter module

from tkinter import *

# from tkinter.ttk import *

# creating Tk window

master = Tk()

# cretaing a Fra, e which can expand according

# to the size of the window

pane = Frame(master)

pane.pack(fill = BOTH, expand = True)

# button widgets which can also expand and fill

# in the parent widget entirely

# Button 1

b1 = Button(pane, text = "Click me !",

 background = "red", fg = "white")

b1.pack(side = LEFT, expand = True, fill = BOTH)

# Button 2

b2 = Button(pane, text = "Click me too",

 background = "blue", fg = "white")

b2.pack(side = LEFT, expand = True, fill = BOTH)

# Button 3

b3 = Button(pane, text = "I'm also button",

 background = "green", fg = "white")

b3.pack(side = LEFT, expand = True, fill = BOTH)

# Execute Tkinter

master.mainloop()  
  
---  
  
 __

 __

 **Output:**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190606134218/Capture155-300x69.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

