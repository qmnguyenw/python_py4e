PyQt5 – The Color Game



In this article we will see how we can create a color game using PyQt5. In
this game user has to score maximum by naming the color name of the color of
given word and in order to confuse the player the text will be of different
color name. Below is how color game looks like

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200605204249/final455.png)

>  **GUI Implementation Steps :**  
>  1\. Create a head label to show the name of the game, set its features like
> alignment color etc.  
> 2\. Create a instruction label to tell the instruction to the user  
> 3\. Create a push button to start/ reset the game  
> 4\. Create Label to show the score  
> 5\. Create a line edit to get the input from user  
> 6\. Create a label for count down of 30 seconds
>
>  **Back-end implementation steps :**  
>  1\. Create start flag, a list of colors, counter value variable and score
> value variable  
> 2\. Create a timer object which call a method after one second  
> 3\. Inside the timer method check for the start flag if its true set counter
> value to the counter label and decrement the count value  
> 4\. Check if counter variable is equal to zero then make the start flag
> false and make the line edit disable  
> 5\. Add action to the start button  
> 6\. Inside the start button action make the start value to true set count
> value to 30 and clear the line edit text  
> 7\. Get the random choice from the color list and set that color to the
> color label  
> 8\. Again get the random choice from the list and set that text to the label  
> 9\. Add action to the line edit when enter is pressed  
> 10\. Inside the action of line edit check for the entered text with the
> random choice if matches increment the score value and change the color
> label color and text with another random value.

Below is the implementation

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui

from PyQt5.QtGui import *

from PyQt5.QtCore import *

import random

import sys

 

 

class Window(QMainWindow):

 

 def __init__(self):

 super().__init__()

 

 # setting title

 self.setWindowTitle("Python ")

 

 # setting geometry

 self.setGeometry(100, 100, 500, 500)

 

 # calling method

 self.UiComponents()

 

 # showing all the widgets

 self.show()

 

 # counter

 self.count_value = 30

 

 # score

 self.score_value = 0

 

 # start flag

 self.start_Flag = False

 

 # list of possible colour.

 self.color_list = ['Red', 'Blue', 'Green', 'Pink',
'Black',

 'Yellow', 'Orange', 'Purple', 'Brown']

 

 

 # method for components

 def UiComponents(self):

 

 # creating head label

 head = QLabel("Color Game", self)

 

 # setting geometry to the head

 head.setGeometry(100, 10, 300, 60)

 

 # font

 font = QFont('Times', 14)

 font.setBold(True)

 font.setItalic(True)

 font.setUnderline(True)

 

 # setting font to the head

 head.setFont(font)

 

 # setting alignment of the head

 head.setAlignment(Qt.AlignCenter)

 

 # instruction label

 instruction = QLabel("Instruction : Enter the Color not the text. "

 "Press Start button to start the game "

 "Note : Time limit for game is 30 seconds", self)

 

 # making it multi line

 instruction.setWordWrap(True)

 

 # setting geometry to the label

 instruction.setGeometry(20, 60, 460, 60)

 

 # creating start button

 start = QPushButton("Start / Reset", self)

 

 # setting geometry to the push button

 start.setGeometry(200, 120, 100, 35)

 

 # adding action to the start button

 start.clicked.connect(self.start_action)

 

 # creating a score label

 self.score = QLabel("Score : 0", self)

 

 # setting geometry

 self.score.setGeometry(160, 170, 180, 50)

 

 # setting alignment

 self.score.setAlignment(Qt.AlignCenter)

 

 # setting font

 self.score.setFont(QFont('Times', 16))

 

 # setting style sheet

 self.score.setStyleSheet("QLabel"

 "{"

 "border : 2px solid black;"

 "color : green;"

 "background : lightgrey;"

 "}")

 

 # creating label to show color

 self.color = QLabel("Color Name", self)

 

 # setting geometry

 self.color.setGeometry(50, 230, 400, 120)

 

 # setting alignment

 self.color.setAlignment(Qt.AlignCenter)

 

 # setting font

 self.color.setFont(QFont('Times', 30))

 

 # creating a line edit

 self.input_text = QLineEdit(self)

 

 # setting geometry

 self.input_text.setGeometry(150, 340, 200, 50)

 

 # setting font

 self.input_text.setFont(QFont('Arial', 14))

 

 # making line edit disabled

 self.input_text.setDisabled(True)

 

 # adding action to it when enter is pressed

 self.input_text.returnPressed.connect(self.input_action)

 

 # creating a timer label

 self.count = QLabel("30", self)

 

 # setting geometry

 self.count.setGeometry(225, 430, 50, 50)

 

 # setting alignment

 self.count.setAlignment(Qt.AlignCenter)

 

 # setting font

 self.count.setFont(QFont('Times', 14))

 

 # setting style sheet

 self.count.setStyleSheet("border : 2px solid black;"

 "background : lightgrey;")

 

 # creating a timer object

 timer = QTimer(self)

 

 # adding action to the timer

 timer.timeout.connect(self.show_time)

 

 # start timer

 timer.start(1000)

 

 def show_time(self):

 

 if self.start_Flag:

 

 # showing count value to label

 self.count.setText(str(self.count_value))

 

 # checking if count value is zero

 if self.count_value == 0:

 

 # making start flag to false

 self.start_Flag = False

 

 # making line edit widget disable

 self.input_text.setDisabled(True)

 

 

 # decrementing the count value

 self.count_value -= 1

 

 

 

 

 def start_action(self):

 

 # making start flag true

 self.start_Flag = True

 

 # resetting score

 self.score.setText("Score : 0")

 self.score_value = 0

 

 # resetting count value

 self.count_value = 30

 

 # clearing line edit text

 self.input_text.clear()

 

 # making line edit enabled

 self.input_text.setEnabled(True)

 

 # getting random color

 self.random_color = random.choice(self.color_list)

 

 # making color choice random color

 self.random_color.lower()

 

 # setting random color to the label

 self.color.setStyleSheet("color : " + self.random_color +
";")

 

 # getting another random color name

 random_text = random.choice(self.color_list)

 

 # setting text to label

 self.color.setText(random_text)

 

 

 

 def input_action(self):

 

 # get the line edit test

 text = self.input_text.text()

 

 # making text lower case

 text.lower()

 

 # checking text with random color

 if text == self.random_color:

 # clearing line edit text

 self.input_text.clear()

 

 # incrementing score value

 self.score_value += 1

 

 # setting score to the score label

 self.score.setText("Score : " + str(self.score_value))

 

 # getting random color

 self.random_color = random.choice(self.color_list)

 

 # making color choice random color

 self.random_color.lower()

 

 # setting random color to the label

 self.color.setStyleSheet("color : " + self.random_color +
";")

 

 # getting another random color name

 random_text = random.choice(self.color_list)

 

 # setting text to label

 self.color.setText(random_text)

 

 

 

# create pyqt5 app

App = QApplication(sys.argv)

 

# create the instance of our Window

window = Window()

 

# start the app

sys.exit(App.exec())  
  
---  
  
 __

 __

 **Output :**  

https://media.geeksforgeeks.org/wp-
content/uploads/20200605205414/Python-2020-06-05-20-53-13.mp4

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

