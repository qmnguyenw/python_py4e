Python Script to Shutdown your PC using Voice Commands



Yes, it is possible with the help of terminal and some modules in Python
through which one can shut down a PC by just using voice commands

###  **Required Modules:**

  *  **OS module:** It is an in-built module in python that provides function for interacting with the operating system.
  *  **Speech Recognition module:** It is an external module in python whose functionality depends on the voice commands of the user.
  *  **Pyttsx3 module:** it is a text-to-speech conversion library in Python.

###  **Installation:**

    
    
    pip install SpeechRecognition
    pip install pyttsx3
    

### Role of Terminal:

In terminal there are many tags for the shutdown command, however we will use
the _/s_ tag with it to shut down the system.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200915202856/terminal-300x179.png)

### Below are the steps to create a program to shut doe=wn PC using Voice
Commands:

 **Step 1:** Create a class _Gfg_ and then create its methods, create
_takeCommands() method_ to take commands as input.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import SpeechRecognition as sr

 

# Create class

class Gfg:

 

 # Method to take voice commands as input

 def takeCommands(self):

 

 # Using Recognizer and Microphone Method for input voice commands

 r = sr.Recognizer()

 with sr.Microphone() as source:

 print('Listening')

 

 # Number pf seconds of non-speaking audio before

 # a phrase is considered complete

 r.pause_threshold = 0.7

 audio = r.listen(source)

 

 # Voice input is identified

 try:

 

 # Listening voice commands in indian english

 print("Recognizing")

 Query = r.recognize_google(audio, language='en-in')

 

 # Displaying the voice command

 print("the query is printed='", Query, "'")

 

 except Exception as e:

 

 # Displaying exception

 print(e) 

 print("Say that again sir")

 return "None"

 return Query  
  
---  
  
 __

 __

