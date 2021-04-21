minsize() method in Tkinter | Python



In Tkinter, **minsize()** method is used to set the minimum size of the
Tkinter window. Using this method user can set window’s initialized size to
its minimum size, and still be able to maximize and scale the window larger.

 **Syntax:**

    
    
    master.minsize(height, width)

Here, height and width are in pixels.

 **Code #1:** Root window without minimum size that means you can shrink
window as much you want.

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

 **Output:**  
Initial root window without alteration in size  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190413225527/Capture34-2.png)

  

  

Root window after shrunken down, see the window is completely shrunken because
it has no minimum geometry.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190413225842/shrunked.png)

 **Code #2:** Root window with minimum size.

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

 

# setting the minimum size of the root window

root.minsize(150, 100)

 

# Adding widgets to the root window

Label(root, text = 'GeeksforGeeks', 

 font =('Verdana', 15)).pack(side = TOP, pady = 10)

Button(root, text = 'Click Me !').pack(side = TOP)

 

mainloop()  
  
---  
  
 __

 __

 **Output:**  
Initial window  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190413230046/initial3.png)

Expanded window (we can expand window as much as we want because we haven’t
set the maximum size of the window).  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190413230146/expanded-300x127.png)

Window shrunken to it’s minimum size (one cannot shrunk it any further).  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190413230313/minimum1.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

