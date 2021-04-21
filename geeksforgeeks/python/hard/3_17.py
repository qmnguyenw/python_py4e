Create a Python Script Notifying to take a break



We generally do not take breaks when we are using our laptop or PC. It might
affect our eyesight as well as mind. So with Python, we can make a program
that can notify us that we have to take a break start again after sometime
when the user again starts working on the laptop.

### Modules needed

  *  **pyttsx3 –** It is a text-to-speech conversion library in Python. An application invokes the pyttsx3.init() factory function to get a reference to a pyttsx3. It is a very easy to use tool which converts the entered text into speech. To install this module type the below command in the terminal.

    
    
    pip install pyttsx3

  *  **plyer –** Plyer module is used to access the features of the hardware. This module does not comes built-in with Python. We need to install it externally. To install this module type the below command in the terminal.

    
    
    pip install plyer 

When we start our laptop or PC we will just have to run the Python program and
we will schedule the operation like after every 50 min our PC or laptop will
give us a notification as well as speak to us to take a break. Many times we
just ignore the notifications that are given to us but with a laptop speaking
us will help us remind that we have to take a break.

 **Creating the Speak Method:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pyttsx3

from plyer import notification

import time

 

 

# Speak method

def Speak(self, audio):

 

 # Calling the intial constructor 

 # of pyttsx3

 engine = pyttsx3.init('sapi5')

 

 # Calling the getter method

 voices = engine.getProperty('voices')

 

 # Calling the setter method

 engine.setProperty('voice', voices[1].id)

 

 engine.say(audio)

 engine.runAndWait()  
  
---  
  
 __

 __

 **Creating the Take_break method that will create a pop-up notification for
our windows**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def Take_break():

 

 Speak("Do you want to start sir?")

 question = input()

 

 if "yes" in question:

 Speak("Starting Sir")

 

 if "no" in question:

 Speak("We will automatically start after 5 Mins Sir.")

 time.sleep(5*60)

 Speak("Starting Sir")

 

 # A notification we will held that 

 # Let's Start sir and with a message of

 # will tell you to take a break after 45

 # mins for 10 seconds

 while(True):

 notification.notify(title="Let's Start sir",

 message="will tell you to take a break after 45 mins",

 timeout=10)

 

 # For 45 min the will be no notification but 

 # after 45 min a notification will pop up.

 time.sleep(0.5*60)

 

 Speak("Please Take a break Sir")

 

 notification.notify(title="Break Notification",

 message="Please do use your device after sometime as you have"

 "been continuously using it for 45 mins and it will affect your eyes",

 timeout=10)

 

 

# Driver's Code 

if __name__ == '__main__':

 Take_break()  
  
---  
  
 __

 __

 **Below is the Complete Code**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pyttsx3

from plyer import notification

import time

 

 

# Speak method

def Speak(self, audio):

 

 # Calling the intial constructor 

 # of pyttsx3

 engine = pyttsx3.init('sapi5')

 

 # Calling the getter method

 voices = engine.getProperty('voices')

 

 # Calling the setter method

 engine.setProperty('voice', voices[1].id)

 

 engine.say(audio)

 engine.runAndWait()

 

 

def Take_break():

 

 Speak("Do you want to start sir?")

 question = input()

 

 if "yes" in question:

 Speak("Starting Sir")

 

 if "no" in question:

 Speak("We will automatically start after 5 Mins Sir.")

 time.sleep(5*60)

 Speak("Starting Sir")

 

 # A notification we will held that 

 # Let's Start sir and with a message of

 # will tell you to take a break after 45

 # mins for 10 seconds

 while(True):

 notification.notify(title="Let's Start sir",

 message="will tell you to take a break after 45 mins",

 timeout=10)

 

 # For 45 min the will be no notification but 

 # after 45 min a notification will pop up.

 time.sleep(0.5*60)

 

 Speak("Please Take a break Sir")

 

 notification.notify(title="Break Notification",

 message="Please do use your device after sometime as you have"

 "been continuously using it for 45 mins and it will affect your eyes",

 timeout=10)

 

 

# Driver's Code 

if __name__ == '__main__':

 Take_break()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200730204140/python-
break-notification.webm

 **Note:** A voice command is also generated.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

