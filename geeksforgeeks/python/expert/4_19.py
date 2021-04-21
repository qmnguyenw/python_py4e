Python – Get Today’s Current Day using Speech Recognition



We often don’t remember the day of the date due to our load of work we are
doing. So, here is a Python program with the help of which we can find the day
of the date with just a simple chat with our laptop or mobile.

### Modules Needed

  *  **DateTime:** This is a Library in Python with the help of which we can manipulate the date and time. It comes preinstalled with python so we don’t have to install.
  *  **pyttsx3:** This is text to speech conversion library. It helps in communicating with the user. This module does not come built-in with Python. To install it type the below command in the terminal.

    
    
    pip install pyttsx3

  *  **SpeechRecognition:** It helps in Speech Recognition. Speech recognition is the process of converting audio into text. This module does not come built-in with Python. To install it type the below command in the terminal.

    
    
    pip install SpeechRecognition

Now Let’s Code The program for telling date with the help of Speech
Recognition.

 **Step 1:** Make the method for taking the commands. So that our program can
take our commands.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import datetime

import pyttsx3

import speech_recognition as sr

 

 

def take_commands():

 

 # Making the use of Recognizer and Microphone

 # Method from Speech Recognition for taking

 # commands

 r = sr.Recognizer()

 

 with sr.Microphone() as source:

 print('Listening')

 

 # seconds of non-speaking audio before

 # a phrase is considered complete

 r.pause_threshold = 0.7

 audio = r.listen(source)

 try:

 print("Recognizing")

 

 # for listening the command in indian english

 Query = r.recognize_google(audio, language='en-in')

 

 # for printing the query or the command that we give

 print("the query is printed='", Query, "'")

 except Exception as e:

 

 # this method is for handling the exception 

 # and so that assistant can ask for telling 

 # again the command

 print(e) 

 print("Say that again sir")

 return "None"

 

 return Query  
  
---  
  
 __

 __

 **Step 2:** Make the Speak method so that our Program can speak to us.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def Speak(audio):

 

 # intial constructor of pyttsx3

 engine = pyttsx3.init()

 

 # getter and setter method

 voices = engine.getProperty('voices')

 engine.setProperty('voice', voices[1].id)

 engine.say(audio)

 engine.runAndWait()  
  
---  
  
 __

 __

 **Step 3:** Tell the day method

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def tellDay():

 

 # the weekday method is a method from datetime

 # library which helps us to an integer 

 # corresponding to the day of the week

 # this dictionary will help us to map the

 # integer with the day and we will check for

 # the condition and if the condition is true

 # it will return the day

 day = datetime.datetime.today().weekday() + 1

 

 Day_dict = {1: 'Monday', 2: 'Tuesday', 3:
'Wednesday',

 4: 'Thursday', 5: 'Friday', 6: 'Saturday',

 7: 'Sunday'}

 

 if day in Day_dict.keys():

 day_of_the_week = Day_dict[day]

 print(day_of_the_week)

 Speak("The day is " + day_of_the_week)  
  
---  
  
 __

 __

 **Step 4:** The main method which will help us to execute the program

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

if __name__ == '__main__': 

 command=take_commands()

 

 if "day" in command:

 tellDay()  
  
---  
  
 __

 __

 **Whole Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import datetime

import pyttsx3

import speech_recognition as sr

 

 

def take_commands():

 

 # Making the use of Recognizer and Microphone

 # Method from Speech Recognition for taking

 # commands

 r = sr.Recognizer()

 

 with sr.Microphone() as source:

 print('Listening')

 

 # seconds of non-speaking audio before

 # a phrase is considered complete

 r.pause_threshold = 0.7

 audio = r.listen(source)

 try:

 print("Recognizing")

 

 # for listening the command in indian english

 Query = r.recognize_google(audio, language='en-in')

 

 # for printing the query or the command that we give

 print("the query is printed='", Query, "'")

 except Exception as e:

 

 # this method is for handling the exception 

 # and so that assistant can ask for telling 

 # again the command

 print(e) 

 print("Say that again sir")

 return "None"

 

 return Query

 

def Speak(audio):

 

 # intial constructor of pyttsx3

 engine = pyttsx3.init()

 

 # getter and setter method

 voices = engine.getProperty('voices')

 engine.setProperty('voice', voices[1].id)

 engine.say(audio)

 engine.runAndWait()

 

def tellDay():

 

 # the weekday method is a method from datetime

 # library which helps us to an integer 

 # corresponding to the day of the week

 # this dictionary will help us to map the

 # integer with the day and we will check for

 # the condition and if the condition is true

 # it will return the day

 day = datetime.datetime.today().weekday() + 1

 

 Day_dict = {1: 'Monday', 2: 'Tuesday', 3:
'Wednesday',

 4: 'Thursday', 5: 'Friday', 6: 'Saturday',

 7: 'Sunday'}

 

 if day in Day_dict.keys():

 day_of_the_week = Day_dict[day]

 print(day_of_the_week)

 Speak("The day is " + day_of_the_week)

 

# Driver Code

if __name__ == '__main__': 

 command=take_commands()

 

 if "day" in command:

 tellDay()  
  
---  
  
 __

 __

 **Output:**

    
    
    Listening
    Recognizing
    the query is printed=' today's day '
    Wednesday

 **Note:** A voice generated output is also created.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

