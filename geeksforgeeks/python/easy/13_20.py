Progressbar widget in Tkinter | Python



The purpose of this widget is to reassure the user that something is
happening. It can operate in one of two modes –  
In **determinate mode** , the widget shows an indicator that moves from
beginning to end under program control.  
In **indeterminate mode** , the widget is animated so the user will believe
that something is in progress. In this mode, the indicator bounces back and
forth between the ends of the widget.

 **Syntax:**

    
    
    widget_object = Progressbar(parent, **options)
    

  
**Code #1** In **determinate** mode

 __

 __  
 __

 __

 __  
 __  
 __

# importing tkinter module

from tkinter import * from tkinter.ttk import *

 

# creating tkinter window

root = Tk()

 

# Progress bar widget

progress = Progressbar(root, orient = HORIZONTAL,

 length = 100, mode = 'determinate')

 

# Function responsible for the updation

# of the progress bar value

def bar():

 import time

 progress['value'] = 20

 root.update_idletasks()

 time.sleep(1)

 

 progress['value'] = 40

 root.update_idletasks()

 time.sleep(1)

 

 progress['value'] = 50

 root.update_idletasks()

 time.sleep(1)

 

 progress['value'] = 60

 root.update_idletasks()

 time.sleep(1)

 

 progress['value'] = 80

 root.update_idletasks()

 time.sleep(1)

 progress['value'] = 100

 

progress.pack(pady = 10)

 

# This button will initialize

# the progress bar

Button(root, text = 'Start', command = bar).pack(pady = 10)

 

# infinite loop

mainloop()  
  
---  
  
 __

 __

 **Output:**  

https://media.geeksforgeeks.org/wp-
content/uploads/20190430235939/demonstration_of_progressbar_widget.mp4

  
  
**Code #2:** In **indeterminate** mode

 __

 __  
 __

 __

 __  
 __  
 __

# importing tkinter module

from tkinter import * from tkinter.ttk import *

 

# creating tkinter window

root = Tk()

 

# Progress bar widget

progress = Progressbar(root, orient = HORIZONTAL,

 length = 100, mode = 'indeterminate')

 

# Function responsible for the updation

# of the progress bar value

def bar():

 import time

 progress['value'] = 20

 root.update_idletasks()

 time.sleep(0.5)

 

 progress['value'] = 40

 root.update_idletasks()

 time.sleep(0.5)

 

 progress['value'] = 50

 root.update_idletasks()

 time.sleep(0.5)

 

 progress['value'] = 60

 root.update_idletasks()

 time.sleep(0.5)

 

 progress['value'] = 80

 root.update_idletasks()

 time.sleep(0.5)

 

 progress['value'] = 100

 root.update_idletasks()

 time.sleep(0.5)

 

 progress['value'] = 80

 root.update_idletasks()

 time.sleep(0.5)

 

 progress['value'] = 60

 root.update_idletasks()

 time.sleep(0.5)

 

 progress['value'] = 50

 root.update_idletasks()

 time.sleep(0.5)

 

 progress['value'] = 40

 root.update_idletasks()

 time.sleep(0.5)

 

 progress['value'] = 20

 root.update_idletasks()

 time.sleep(0.5)

 progress['value'] = 0

 

 

progress.pack(pady = 10)

 

# This button will initialize

# the progress bar

Button(root, text = 'Start', command = bar).pack(pady = 10)

 

# infinite loop

mainloop()  
  
---  
  
 __

 __

 **Output:**  

https://media.geeksforgeeks.org/wp-
content/uploads/20190501001802/progressbar_in_indeterminate_mode.mp4

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

