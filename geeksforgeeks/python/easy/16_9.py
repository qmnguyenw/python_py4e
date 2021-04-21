Python Text To Speech | pyttsx module



 **pyttsx** is a cross-platform text to speech library which is platform
independent. The major advantage of using this library for text-to-speech
conversion is that it works offline. However, _pyttsx_ supports only Python
2.x. Hence, we will see pyttsx3 which is modified to work on both Python 2.x
and Python 3.x with the same code.

 **Use this command for Installation:**

    
    
    pip install pyttsx3

  
**Usage –**  
First we need to import the library and then initialise it using init()
function. This function may take 2 arguments.  
init(driverName string, debug bool)

  *  **drivername :** [Name of available driver] **_sapi5_** on Windows | **_nsss_** on MacOS
  *  **debug:** to enable or disable debug output

After initialisation, we will make the program speak the text using say()
function. This method may also take 2 arguments.  
say(text unicode, name string)

  *  **text :** Any text you wish to hear.
  *  **name :** To set a name for this speech. (optional)

Finally, to run the speech we use runAndWait() All the say() texts won’t
be said unless the interpreter encounters runAndWait().

  

  

 **Code #1:** Speaking Text

 __

 __  
 __

 __

 __  
 __  
 __

# importing the pyttsx library

import pyttsx3

 

# initialisation

engine = pyttsx3.init()

 

# testing

engine.say("My first code on text-to-speech")

engine.say("Thank you, Geeksforgeeks")

engine.runAndWait()  
  
---  
  
 __

 __

  
**Code #2:** Listening for events

 __

 __  
 __

 __

 __  
 __  
 __

import pyttsx3

 

def onStart():

 print('starting')

 

def onWord(name, location, length):

 print('word', name, location, length)

 

def onEnd(name, completed):

 print('finishing', name, completed)

 

engine = pyttsx3.init()

 

engine.connect('started-utterance', onStart)

engine.connect('started-word', onWord)

engine.connect('finished-utterance', onEnd)

 

sen = 'Geeks for geeks is a computer portal for Geeks'

 

 

engine.say(sen)

engine.runAndWait()  
  
---  
  
 __

 __

 **Why pyttsx?**  
It works offline, unlike other text-to-speech libraries. Rather than saving
the text as audio file, _pyttsx_ actually speaks it there. This makes it more
reliable to use for voice-based projects.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

