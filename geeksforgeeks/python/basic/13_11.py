maxsize() method in Tkinter | Python



This method is used to set the **maximum size** of the root window (maximum
size a window can be expanded). User will still be able to shrink the size of
the window to the minimum possible.

 **Syntax :**

    
    
     master.maxsize(height, width) 

Here, height and width are in pixels.

 **Code #1:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing only those functions

# which are needed

from tkinter import *

from tkinter.ttk import *

from time import strftime

 

# creating tkinter window

root = Tk()

 

# Adding widgets to the root window

Label(root, text = 'GeeksforGeeks', 

 font =('Verdana', 15)).pack(side = TOP, pady = 10)

 

Button(root, text = 'Click Me !').pack(side = TOP)

 

mainloop()  
  
---  
  
 __

 __

 **Output :**  
Initial size of the window (maximum size of the window is not set)  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190416223115/initial4.png)

  

  

Expanded size of the window (this window can be expanded til the size of the
screen because size is not fixed).  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190416223245/expanded1-300x205.png)  
  
**Code #2:** Fixing maximum size of the root window

 __

 __  
 __

 __

 __  
 __  
 __

# importing only those functions

# which are needed

from tkinter import *

from tkinter.ttk import *

from time import strftime

 

# creating tkinter window

root = Tk()

 

# Fixing the size of the root window.

# No one can now expand the size of the

# root window than the specified one.

root.maxsize(200, 200)

 

# Adding widgets to the root window

Label(root, text = 'GeeksforGeeks', 

 font =('Verdana', 15)).pack(side = TOP, pady = 10)

 

Button(root, text = 'Click Me !').pack(side = TOP)

 

mainloop()  
  
---  
  
 __

 __

 **Output :**  
Maximum expanded size of the window  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190416224858/maximum2.png)

 **Note:**Tkinter also offers a minsize() method which is used to set the
minimum size of the window.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

