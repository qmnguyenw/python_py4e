Binding Function with double click with Tkinter ListBox



 **Prerequisites:** Python GUI – tkinter, Python | Binding function in Tkinter

Tkinter in Python is GUI (Graphical User Interface) module which is widely
used for creating desktop applications. It provides various basic widgets to
build a GUI program.

To bind Double click with Listbox we use Binding functions in Python and then
we execute the required actions based on the item selected in Listbox.  
Below is the implementation:

 __

 __  
 __

 __

 __  
 __  
 __

from tkinter import *

 

def go(event):

 cs = Lb.curselection()

 

 # Updating label text to selected option

 w.config(text=Lb.get(cs))

 

 # Setting Background Colour

 for list in cs:

 

 if list == 0:

 top.configure(background='red')

 elif list == 1:

 top.configure(background='green')

 elif list == 2:

 top.configure(background='yellow')

 elif list == 3:

 top.configure(background='white')

 

 

top = Tk()

top.geometry('250x275')

top.title('Double Click')

 

# Creating Listbox

Lb = Listbox(top, height=6)

# Inserting items in Listbox

Lb.insert(0, 'Red')

Lb.insert(1, 'Green')

Lb.insert(2, 'Yellow')

Lb.insert(3, 'White')

 

# Binding double click with left mouse

# button with go function

Lb.bind('<Double-1>', go)

Lb.pack()

 

# Creating Edit box to show selected option

w = Label(top, text='Default')

w.pack()

top.mainloop()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/20200331203718/Doubl-
Click-in-tkintr.gif)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

