Creating a multiple Selection using Tkinter



 **Prerequisites:** Python Tkinter – ListBox Widget, Scrollable ListBox in
Python-tkinter

Tkinter is a GUI library in python which is easy to read and understand. In
Tkinter, multiple selections can be done using the List box widget. Generally,
a Listbox displays different items in the form of a list. A list box widget
provides one or more selections of items from a list. There are many options
available in a Listbox widget that makes the user select multiple options. By
assigning the select mode option as multiple, the user can able to select
multiple options. If the select mode option is single then only one option can
be selected by the user.  
The selectmode option of a listbox widget can be single, browse, multiple or
extended.

  *  **single** – Selects one line of text.
  *  **browse** – It is a default option where the user can select one line of text.
  *  **multiple** – Selects multiple lines of text without dragging from first line of option to last line.
  *  **extended** – User can select and drag adjacent multiple lines of text.

 **Syntax :**

    
    
    list_box = Listbox(root, options, ....)
    

**Example 1:** Python program displaying limited items in the listbox.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program demonstrating

# Multiple selection in Listbox widget

 

 

from tkinter import *

 

window = Tk()

window.geometry('100x150')

 

# Choosing selectmode as multiple 

# for selecting multiple options

list = Listbox(window, selectmode = "multiple")

 

# Widget expands horizontally and

# vertically by assigning both to 

# fill option

list.pack(expand = YES, fill = "both")

 

# Taking a list 'x' with the items 

# as languages

x = ["C", "C++", "Java", "Python", "R",

 "Go", "Ruby", "JavaScript", "Swift"]

 

for each_item in range(len(x)):

 

 list.insert(END, x[each_item])

 

 # coloring alternative lines of listbox

 list.itemconfig(each_item,

 bg = "yellow" if each_item % 2 == 0 else "cyan")

 

window.mainloop()  
  
---  
  
 __

 __

 **Output :**

  

  

https://media.geeksforgeeks.org/wp-content/uploads/20200420183159/multiple-
slection-tkinter.webm

From the above multiple selection Listbox, the user can select multiple
options. As there are limited items in the Listbox that fit into the
prescribed size, the user can able to see all the items. But if there are more
items to be displayed to the user then all the items are not visible at once
in a Listbox. Hence, attaching a scrollbar to a Listbox is necessary if there
are more items to be displayed in a list. This can be done by the
yscrollcommand option(to scroll vertically) in Listbox.

 **Example 2:** Python program displaying List box with attached scroll bar.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program demonstrating Multiple selection

# in Listbox widget with a scrollbar

 

 

from tkinter import *

 

window = Tk()

window.title('Multiple selection')

 

# for scrolling vertically

yscrollbar = Scrollbar(window)

yscrollbar.pack(side = RIGHT, fill = Y)

 

label = Label(window,

 text = "Select the languages below : ",

 font = ("Times New Roman", 10), 

 padx = 10, pady = 10)

label.pack()

list = Listbox(window, selectmode = "multiple", 

 yscrollcommand = yscrollbar.set)

 

# Widget expands horizontally and 

# vertically by assigning both to

# fill option

list.pack(padx = 10, pady = 10,

 expand = YES, fill = "both")

 

x =["C", "C++", "C#", "Java", "Python",

 "R", "Go", "Ruby", "JavaScript", "Swift",

 "SQL", "Perl", "XML"]

 

for each_item in range(len(x)):

 

 list.insert(END, x[each_item])

 list.itemconfig(each_item, bg = "lime")

 

# Attach listbox to vertical scrollbar

yscrollbar.config(command = list.yview)

window.mainloop()  
  
---  
  
 __

 __

 **Output :**

https://media.geeksforgeeks.org/wp-content/uploads/20200420183240/multiple-
slection-python-tkinter-scrollable.webm

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

