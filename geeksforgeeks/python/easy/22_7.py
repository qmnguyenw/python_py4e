Color game using Tkinter in Python



Prerequisite : Python GUI Tkinter

TKinter is widely used for developing GUI applications. Along with
applications, we can also use Tkinter GUI to develop games.

Let’s try to make a game using Tkinter. In this game player has to enter color
of the word that appears on the screen and hence the score increases by one,
the total time to play this game is 30 seconds. Colors used in this game are
Red, Blue, Green, Pink, Black, Yellow, Orange, White, Purple and Brown.
Interface will display name of different colors in different colors. Player
has to identify the color and enter the correct color name to win the game.  
  
Below is the implementation of above game :

 __

 __  
 __

 __

 __  
 __  
 __

# import the modules

import tkinter

import random

 

# list of possible colour.

colours = ['Red','Blue','Green','Pink','Black',

 'Yellow','Orange','White','Purple','Brown']

score = 0

 

# the game time left, initially 30 seconds.

timeleft = 30

 

# function that will start the game.

def startGame(event):

 

 if timeleft == 30:

 

 # start the countdown timer.

 countdown()

 

 # run the function to

 # choose the next colour.

 nextColour()

 

# Function to choose and

# display the next colour.

def nextColour():

 

 # use the globally declared 'score'

 # and 'play' variables above.

 global score

 global timeleft

 

 # if a game is currently in play

 if timeleft > 0:

 

 # make the text entry box active.

 e.focus_set()

 

 # if the colour typed is equal

 # to the colour of the text

 if e.get().lower() == colours[1].lower():

 

 score += 1

 

 # clear the text entry box.

 e.delete(0, tkinter.END)

 

 random.shuffle(colours)

 

 # change the colour to type, by changing the

 # text _and_ the colour to a random colour value

 label.config(fg = str(colours[1]), text =
str(colours[0]))

 

 # update the score.

 scoreLabel.config(text = "Score: " + str(score))

 

 

# Countdown timer function 

def countdown():

 

 global timeleft

 

 # if a game is in play

 if timeleft > 0:

 

 # decrement the timer.

 timeleft -= 1

 

 # update the time left label

 timeLabel.config(text = "Time left: "

 + str(timeleft))

 

 # run the function again after 1 second.

 timeLabel.after(1000, countdown)

 

 

# Driver Code

 

# create a GUI window

root = tkinter.Tk()

 

# set the title

root.title("COLORGAME")

 

# set the size

root.geometry("375x200")

 

# add an instructions label

instructions = tkinter.Label(root, text = "Type in the colour"

 "of the words, and not the word text!",

 font = ('Helvetica', 12))

instructions.pack() 

 

# add a score label

scoreLabel = tkinter.Label(root, text = "Press enter to start",

 font = ('Helvetica', 12))

scoreLabel.pack()

 

# add a time left label

timeLabel = tkinter.Label(root, text = "Time left: " +

 str(timeleft), font = ('Helvetica', 12))

 

timeLabel.pack()

 

# add a label for displaying the colours

label = tkinter.Label(root, font = ('Helvetica', 60))

label.pack()

 

# add a text entry box for

# typing in colours

e = tkinter.Entry(root)

 

# run the 'startGame' function 

# when the enter key is pressed

root.bind('<Return>', startGame)

e.pack()

 

# set focus on the entry box

e.focus_set()

 

# start the GUI

root.mainloop()  
  
---  
  
 __

 __

 **Output :**  

https://media.geeksforgeeks.org/wp-content/uploads/tkinter_game.mp4

 **Note :** Above code may not run on online IDE because of TKinter module.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

