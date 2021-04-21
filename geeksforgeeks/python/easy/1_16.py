How to play sounds in Python with Tkinter?



Python GUI tkinter is very useful when we want to take data from users. User
attracts from GUI. GUI is very helpful in day to day life. A graphical user
interface helps us to make our daily tasks easier and very productive. If you
want to play music with the help of python GUI tkinter, then you come in the
right way. For playing sound/music with help of python you need to install the
required modules. This, module will help to play sound.

 **There are two modules to play sound with the help of tkinter python:**

  1. pygame : It is a cross-platform module to create games and GUI’s.
  2. playsound: It is a cross-platform module and its function name is playsound()

Let’s see how we can play sound/music with help of tkinter python GUI. You
have to save your mp3 file in the same folder where you save your python file
or you have to give the full path of the mp3 file. The mp3 file used the below
methods is given here.

https://media.geeksforgeeks.org/wp-content/uploads/20210110085700/1.wav

 **Method 1: (Using playsound)**

To install playsound use this command

  

  

    
    
    pip install playsound 

**Steps Needed**

  1. First importing required modules.
  2. Initializing the Tk() and putting it in the variable for further use.
  3. Define a function for trigger it with help of a button.
  4. Create a button to trigger a function with the help of a command.

>  **Syntax :** playsound(sound, block=True)

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing required module

from playsound import playsound

from tkinter import*

 

root = Tk() 

root.title('GeeksforGeeks sound player') #giving the title for our
window

root.geometry("500x400")

 

# making funtion 

def play():

 playsound('1.mp3')

 

# title on the screen you can modify it 

title=Label(root,text="GeeksforGeeks",bd=9,relief=GROOVE,

 font=("times new
roman",50,"bold"),bg="white",fg="green") 

title.pack(side=TOP,fill=X) 

 

# making a button which triger the funtion so sound can be playeed

play_button = Button(root, text="Play Song",
font=("Helvetica", 32),

 relief=GROOVE, command=play)

play_button.pack(pady=20)

 

info=Label(root,text="Click on the button above to play song ",

 font=("times new roman",10,"bold")).pack(pady=20)

root.mainloop()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210115142517/15.01.2021_14.20.15_REC.mp4

 **Method 2: (Using pygame)**

To install pygame use this command

    
    
    pip install pygame

 **Steps Needed**

  1. When code will run then there one window open.
  2. In the window, there is one button. When we click on it there one function will start which plays the song.
  3. The function needs to be defined above to play the sound.
  4. Then make a mp3 file that is present on the same folder or when the mp3 file is not present on the same folder then give its full path to play the sound. (Be careful about this)

>  **Syntax:** mixer.music.load(“song.mp3”)

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing required libaraies

from tkinter import *

import pygame

 

root = Tk()

root.title('GeeksforGeeks sound player')

 

root.geometry("500x400")

 

pygame.mixer.init()# initialise the pygame

 

def play():

 pygame.mixer.music.load("1.mp3")

 pygame.mixer.music.play(loops=0)

 

title=Label(root,text="GeeksforGeeks",bd=9,relief=GROOVE,

 font=("times new
roman",50,"bold"),bg="white",fg="green") 

title.pack(side=TOP,fill=X) 

 

play_button = Button(root, text="Play Song",
font=("Helvetica", 32), command=play)

play_button.pack(pady=20)

root.mainloop()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210115142621/15.01.2021_14.23.27_REC.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

