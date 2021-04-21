How to make a Python auto clicker?



In this article, we will see how to create an auto-clicker using Python. The
code will take input from the keyboard when the user clicks on the start key
and terminates auto clicker when the user clicks on exit key, the auto clicker
starts clicking wherever the pointer is placed on the screen. We are going to
use the **pynput** module here.

## What is Auto Clicker?

Auto-Clicker is a script where you can auto control mouse and keyboard as many
numbers of times as you want. It is controlled using user-defined keys. It
works on various platforms like Windows, Mac and Linux. Auto clicker is
present in **pywin32 module.**

### Approach:

In this project, we will use a cross-platform module **pynput** to control the
mouse and monitor the keyboard at the same time to create simple auto-clicker.
To check for mouse events we will install **pynput module** (used to control
the mouse) for this execute, **pip install pynput** in cmd.

**Note:** If you’re stuck on how to set up python-pip package on your system
then click here

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210111011753/Screenshot832.png)

Installation of pynput module

Verify whether the **pynput** module has been successfully installed into your
working environment for this, open IDLE on the system that is **cmd** or
**Python Shell.** Execute the command **import pynput,** after executing this
the output should give zero errors which means your module is successfully
installed.

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210111012253/Screenshot833.png)

Verifying module installation

### Implementation:

Let’s now proceed with the code that is required to build an **Auto-clicker**
using Python. Follow the below steps to create an auto-clicker:

 **Step 1:** Import time and threading then import Button and Controller from
**pynput.mouse** module. Import _Listener_ and _KeyCode_ from
**pynput.keyboard.**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing time and threading

import time

import threading

from pynput.mouse import Button, Controller

 

# pynput.keyboard is used to watch events of

# keyboard for start and stop of auto-clicker

from pynput.keyboard import Listener, KeyCode  
  
---  
  
 __

 __

 **Step 2:** Create four variables as mentioned below,

  *  **delay** : Delay between each click (in seconds)
  *  **button** : Button is used to click in whatever direction you want to. **Button.left | Button.middle | Button.right**
  *  **start_stop_key** : The key used for start and stop of the click while you run the program for executing the auto clicker. It should be from a key class or set using _KeyCode_.
  *  **exit_key** : The key used to terminate the auto clicker that is being executed. This should be from the key class or set using _KeyCode_.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# four variables are created to

# control the auto-clicker

delay = 0.001

button = Button.right

start_stop_key = KeyCode(char='a')

stop_key = KeyCode(char='b')  
  
---  
  
 __

 __

 **Step 3:** Create a class extending **threading.Thread.** Pass delay and
button to the class that have two flags to check if the program is executed or
not.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# threading.Thread is used

# to control clicks

class ClickMouse(threading.Thread):

 

 # delay and button is passed in class 

 # to check execution of auto-clicker

 def __init__(self, delay, button):

 super(ClickMouse, self).__init__()

 self.delay = delay

 self.button = button

 self.running = False

 self.program_running = True  
  
---  
  
 __

 __

 **Step 4:** Add methods to control the threads externally.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def start_clicking(self):

 self.running = True

 

def stop_clicking(self):

 self.running = False

 

def exit(self):

 self.stop_clicking()

 self.program_running = False  
  
---  
  
 __

 __

**Step 5:** A method is created when the thread starts, the _program_running_
runs on loop until the value comes out to be true and also create another loop
inside the existing loop where it checks if **running** is set to true or not.
In case, we are inside both loops, it will _click_ on the set button and sleep
for the set delay.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# method to check and run loop until

# it is true another loop will check 

# if it is set to true or not, 

# for mouse click it set to button 

# and delay.

def run(self):

 while self.program_running:

 while self.running:

 mouse.click(self.button)

 time.sleep(self.delay)

 time.sleep(0.1)  
  
---  
  
 __

 __

 **Step 6:** Creating an instance for the mouse controller, then create
**ClickMouse thread**. Start the instance to move into the loop inside the run
method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# instance of mouse controller is created

mouse = Controller()

click_thread = ClickMouse(delay, button)

click_thread.start()  
  
---  
  
 __

 __

**Step 7:** Create a method **on_press** which takes a key as an argument and
sets up a keyboard listener. The _start_stop_key_ matches with a **start key
(a)** when it is executed. Then the click is to be terminated when running
flag is set to True in the thread. Exit method is called in the method if the
**exit key (b)** is executed and stop the listener.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# on_press method takes

# key as argument

 

 

def on_press(key):

 

 # start_stop_key will stop clicking

 # if running flag is set to true

 if key == start_stop_key:

 if click_thread.running:

 click_thread.stop_clicking()

 else:

 click_thread.start_clicking()

 

 # here exit method is called and when

 # key is pressed it terminates auto clicker

 elif key == stop_key:

 click_thread.exit()

 listener.stop()

 

 

with Listener(on_press=on_press) as listener:

 listener.join()  
  
---  
  
 __

 __

After the code is run we can see in the output as shown below, it shows the
number of clicks the auto-clicker has made after the code is implemented. It
is compatible with Windows, Mac and Linux. Auto-Clicker is helpful software
for the systems as it let’s save a reasonable amount of time that is spent on
repeated amount of clicks.

 **Below is the complete program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing time and threading

import time

import threading

from pynput.mouse import Button, Controller

 

# pynput.keyboard is used to watch events of 

# keyboard for start and stop of auto-clicker

from pynput.keyboard import Listener, KeyCode

 

 

# four variables are created to 

# control the auto-clicker

delay = 0.001

button = Button.right

start_stop_key = KeyCode(char='a')

stop_key = KeyCode(char='b')

 

# threading.Thread is used 

# to control clicks

class ClickMouse(threading.Thread):

 

 # delay and button is passed in class 

 # to check execution of auto-clicker

 def __init__(self, delay, button):

 super(ClickMouse, self).__init__()

 self.delay = delay

 self.button = button

 self.running = False

 self.program_running = True

 

 def start_clicking(self):

 self.running = True

 

 def stop_clicking(self):

 self.running = False

 

 def exit(self):

 self.stop_clicking()

 self.program_running = False

 

 # method to check and run loop until 

 # it is true another loop will check 

 # if it is set to true or not, 

 # for mouse click it set to button 

 # and delay.

 def run(self):

 while self.program_running:

 while self.running:

 mouse.click(self.button)

 time.sleep(self.delay)

 time.sleep(0.1)

 

 

# instance of mouse controller is created

mouse = Controller()

click_thread = ClickMouse(delay, button)

click_thread.start()

 

 

# on_press method takes 

# key as argument

def on_press(key):

 

 # start_stop_key will stop clicking 

 # if running flag is set to true

 if key == start_stop_key:

 if click_thread.running:

 click_thread.stop_clicking()

 else:

 click_thread.start_clicking()

 

 # here exit method is called and when 

 # key is pressed it terminates auto clicker

 elif key == stop_key:

 click_thread.exit()

 listener.stop()

 

 

with Listener(on_press=on_press) as listener:

 listener.join()  
  
---  
  
 __

 __

Now let’s execute the python program we’ve written and then press the **start
(a)** and **stop (a)** keys in order to initiate the auto clicker.

**Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210118170728/bandicam-2021-01-18-17-05-46-930.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

