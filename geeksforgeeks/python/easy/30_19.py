Mouse and keyboard automation using Python



This article illustrates how to automate movements of mouse and keyboard using
**pyautogui** module in python. This module is not preloaded with python. So
to install it run the following command:  

    
    
     pip3 install pyautogui

**Controlling mouse movements using pyautogui module**

Python tracks and controls mouse using the coordinate system of the screen.
Suppose the resolution of your screen is 1920X1080, then your screen’s
coordinate system looks like this:  

![gui in python](https://media.geeksforgeeks.org/wp-
content/uploads/MouseAndKeyboardAutomationPython.png)

  

  

  * **size():** This function is used to get Screen resolution.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import pyautogui

print(pyautogui.size())  
  
---  
  
 __

 __

Save this file with .py extension, and then run the file.  
This python code use size() function to output your screen resolution in x, y
format:  
Output:  

    
    
     (1920, 1080)

Note: Some of the codes provided in this article might not run on
geeksforgeeks IDE, since geeksforgeeks IDE doesn’t have the required modules
to run these codes. But these codes can be easily run locally on your PC by
installing python and following the instructions provided in the article.  

  * **moveTo():** use this function to move the mouse in pyautogui module.   

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import pyautogui

pyautogui.moveTo(100, 100, duration = 1)  
  
---  
  
 __

 __

This code uses moveTo() function, which takes x and y coordinates, and an
optional duration argument. This function moves your mouse pointer from it’s
current location to x, y coordinate, and takes time as specified by duration
argument to do so. Save and run this python script to see your mouse pointer
magically moving from its current location to coordinates (100, 100), taking 1
second in this process.  

  * **moveRel() function:** moves the mouse pointer relative to its previous position.   

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import pyautogui

pyautogui.moveRel(0, 50, duration = 1)  
  
---  
  
 __

 __

This code will move mouse pointer at (0, 50) relative to its original
position. For example, if mouse position before running the code was (1000,
1000), then this code will move the pointer to coordinates (1000, 1050) in
duration 1 second.  

  * **position():** function to get current position of the mouse pointer.   

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import pyautogui

print(pyautogui.position())  
  
---  
  
 __

 __

Output: coordinates where your mouse was residing at the time of executing the
program.  

  * **click():** Function used for clicking and dragging the mouse.   

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import pyautogui

pyautogui.click(100, 100)  
  
---  
  
 __

 __

This code performs a typical mouse click at the location (100, 100).  
We have two functions associated with the drag operation of the mouse,
**dragTo and dragRel**. They perform similar to moveTo and moveRel functions,
except they hold the left mouse button while moving, thus initiating a drag.  
This functionality can be used at various places, like moving a dialog box, or
drawing something automatically using a pencil tool in MS Paint. To draw a
square in paint:  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import time

# a module which has functions related to time.

# It can be installed using cmd command:

# pip install time, in the same way as pyautogui.

import pyautogui

time.sleep(10)

# makes program execution pause for 10 sec

pyautogui.moveTo(1000, 1000, duration = 1)

# moves mouse to 1000, 1000.

pyautogui.dragRel(100, 0, duration = 1)

# drags mouse 100, 0 relative to its previous position,

# thus dragging it to 1100, 1000

pyautogui.dragRel(0, 100, duration = 1)

pyautogui.dragRel(-100, 0, duration = 1)

pyautogui.dragRel(0, -100, duration = 1)  
  
---  
  
 __

 __

Before running the code, open MS paint in the background with the pencil tool
selected. Now run the code, quickly switch to MS paint before 10 seconds
(since we have given 10 second pause time using sleep() function before
running the program).  
After 10 seconds, you will see a square being drawn in MS paint, with its top-
left edge at 1000, 1000, and edge length 100 pixels.

  

  

  *  **scroll():** scroll function takes no. of pixels as an argument, and scrolls the screen up to a given number of pixels.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import pyautogui

pyautogui.scroll(200)  
  
---  
  
 __

 __

This code scrolls the active screen up to 200 pixels.  

  * **typewrite():** You can automate typing of the string by using typewrite() function. just pass the string which you want to type as an argument of this function.   

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import pyautogui

pyautogui.click(100, 100)

pyautogui.typewrite("hello Geeks !")  
  
---  
  
 __

 __

Suppose a text field was present at coordinates 100, 100 on-screen, then this
code will click the text field to make it active and type “hello Geeks!” in
it.  

  * **Passing key names:** You can pass key names separately through typewrite() function.   

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import pyautogui

pyautogui.typewrite(["a", "left", "ctrlleft"])  
  
---  
  
 __

 __

This code is the automatic equivalent of typing “a”, pressing the left arrow
key, and pressing the left control key.  

  * **Pressing hotkey combinations:** Use hotkey() function to press the combination of keys like ctrl-c, ctrl-a, etc.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import pyautogui

pyautogui.hotkey("ctrlleft", "a")  
  
---  
  
 __

 __

This code is the automatic equivalent of pressing left ctrl and “a”
simultaneously. Thus in windows, this will result in the selection of all text
present on the screen.

 **Example:**

To send a message in WhatsApp and delete it for everyone automatically. You
need to have Whatsapp already opened in chrome, to run this. After running
this code, open the WhatsApp tab on chrome.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pyautogui as pg

import time

def delete_for_everyone():

 pg.click(807, 979)

 pg.typewrite("hello")

 pg.typewrite(["enter"])

 time.sleep(2)

 pg.click(1621, 896)

 pg.click(1621, 896)

 

 # time.sleep(1)

 pg.click(1693, 859)

 

 # time.sleep(1)

 pg.click(1014, 669)

 

 # time.sleep(1)

 pg.click(1111, 605)

 

a=20

time.sleep(10)

while(a!=0):

 delete_for_everyone()

 a=a-1  
  
---  
  
 __

 __

This article is contributed by **tkkhhaarree**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

