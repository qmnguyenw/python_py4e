Python: Convert Speech to text and text to Speech



Speech Recognition is an important feature in several applications used such
as home automation, artificial intelligence, etc. This article aims to provide
an introduction on how to make use of the SpeechRecognition and pyttsx3
library of Python.

 **Installation required:**

  *  **Python Speech Recognition module:**
    
        pip install speechrecognition

  *  **PyAudio:** Use the following command for linux users
    
    
    sudo apt-get install python3-pyaudio
    

Windows users can install pyaudio by executing the following command in a
terminal

    
    
    pip install pyaudio
    

  * **Python pyttsx3 module:**
    
    
    pip install pyttsx3
    

**Speech Input Using a Microphone and Translation of Speech to Text**

  *  **Allow Adjusting for Ambient Noise:** Since the surrounding noise varies, we must allow the program a second or too to adjust the energy threshold of recording so it is adjusted according to the external noise level.
  *  **Speech to text translation:** This is done with the help of Google Speech Recognition. This requires an active internet connection to work. However, there are certain offline Recognition systems such as PocketSphinx, but have a very rigorous installation process that requires several dependencies. Google Speech Recognition is one of the easiest to use.

 **Translation of Speech to Text:**

  

  

First, we need to import the library and then initialize it using init()
function. This function may take 2 arguments.

    
    
    init(driverName string, debug bool)
    

  * **drivername:** [Name of available driver] sapi5 on Windows | nsss on MacOS
  * debug: to enable or disable debug output

After initialization, we will make the program speak the text using say()
function.  
This method may also take 2 arguments.

    
    
    say(text unicode, name string)
    

  * **text:** Any text you wish to hear.
  *  **name:** To set a name for this speech. (optional)

Finally, to run the speech we use runAndWait() All the say() texts won’t be
said unless the interpreter encounters runAndWait().

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to translate

# speech to text and text to speech

 

 

import speech_recognition as sr

import pyttsx3 

 

# Initialize the recognizer 

r = sr.Recognizer() 

 

# Function to convert text to

# speech

def SpeakText(command):

 

 # Initialize the engine

 engine = pyttsx3.init()

 engine.say(command) 

 engine.runAndWait()

 

 

# Loop infinitely for user to

# speak

 

while(1): 

 

 # Exception handling to handle

 # exceptions at the runtime

 try:

 

 # use the microphone as source for input.

 with sr.Microphone() as source2:

 

 # wait for a second to let the recognizer

 # adjust the energy threshold based on

 # the surrounding noise level 

 r.adjust_for_ambient_noise(source2, duration=0.2)

 

 #listens for the user's input 

 audio2 = r.listen(source2)

 

 # Using ggogle to recognize audio

 MyText = r.recognize_google(audio2)

 MyText = MyText.lower()

 

 print("Did you say "+MyText)

 SpeakText(MyText)

 

 except sr.RequestError as e:

 print("Could not request results; {0}".format(e))

 

 except sr.UnknownValueError:

 print("unknown error occured")  
  
---  
  
 __

 __

    
    
    Input: voice speech (Hi buddy how are you)

