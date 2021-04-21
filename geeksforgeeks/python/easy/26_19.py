Create a stopwatch using python



This article focus on creating a stopwatch using Tkinter in python  
 **Tkinter** : Tkinter is the standard GUI library for Python. Python when
combined with Tkinter provides a fast and easy way to create GUI applications.
Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.
It’s very easy to get started with Tkinter, here are some sample codes to get
your hands on Tkinter in python.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to create a

# a new window using Tkinter

# importing the required libraires

import tkinter

 

# creating a object 'top' as instance of class Tk

top = tkinter.Tk()

 

# This will start the blank window

top.mainloop()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/capture_1.jpg)  

 **Creating Stopwatch using Tkinter**

Now lets try to create a program using Tkinter module to create a stopwatch.  
A stopwatch is a handheld timepiece designed to measure the amount of time
elapsed from a particular time when it is activated to the time when the piece
is deactivated. A large digital version of a stopwatch designed for viewing at
a distance, as in a sports stadium, is called a stop clock. In manual timing,
the clock is started and stopped by a person pressing a button. In fully
automatic time, both starting and stopping are triggered automatically, by
sensors.

 **Required Modules:** We are only going to use Tkinter for creating GUI and
no other libraries will be used in this program.

  

  

 **Source Code:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate a stop watch

# using Tkinter 

#importing the required libraries 

import tkinter as Tkinter 

from datetime import datetime

counter = 66600

running = False

def counter_label(label): 

 def count(): 

 if running: 

 global counter 

 

 # To manage the intial delay. 

 if counter==66600: 

 display="Starting..."

 else:

 tt = datetime.fromtimestamp(counter)

 string = tt.strftime("%H:%M:%S")

 display=string 

 

 label['text']=display # Or label.config(text=display) 

 

 # label.after(arg1, arg2) delays by 

 # first argument given in milliseconds 

 # and then calls the function given as second argument. 

 # Generally like here we need to call the 

 # function in which it is present repeatedly. 

 # Delays by 1000ms=1 seconds and call count again. 

 label.after(1000, count) 

 counter += 1

 

 # Triggering the start of the counter. 

 count() 

 

# start function of the stopwatch 

def Start(label): 

 global running 

 running=True

 counter_label(label) 

 start['state']='disabled'

 stop['state']='normal'

 reset['state']='normal'

 

# Stop function of the stopwatch 

def Stop(): 

 global running 

 start['state']='normal'

 stop['state']='disabled'

 reset['state']='normal'

 running = False

 

# Reset function of the stopwatch 

def Reset(label): 

 global counter 

 counter=66600

 

 # If rest is pressed after pressing stop. 

 if running==False: 

 reset['state']='disabled'

 label['text']='Welcome!'

 

 # If reset is pressed while the stopwatch is running. 

 else: 

 label['text']='Starting...'

 

root = Tkinter.Tk() 

root.title("Stopwatch") 

 

# Fixing the window size. 

root.minsize(width=250, height=70) 

label = Tkinter.Label(root, text="Welcome!", fg="black",
font="Verdana 30 bold") 

label.pack() 

f = Tkinter.Frame(root)

start = Tkinter.Button(f, text='Start', width=6,
command=lambda:Start(label)) 

stop = Tkinter.Button(f,
text='Stop',width=6,state='disabled', command=Stop) 

reset = Tkinter.Button(f, text='Reset',width=6,
state='disabled', command=lambda:Reset(label)) 

f.pack(anchor = 'center',pady=5)

start.pack(side="left") 

stop.pack(side ="left") 

reset.pack(side="left") 

root.mainloop()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20191014225504/a118.jpg)  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20191014225604/a213.jpg)

https://media.geeksforgeeks.org/wp-content/uploads/2017-10-26-at-19-18-25.mp4

This article is contributed by **Subhajit Saha**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

