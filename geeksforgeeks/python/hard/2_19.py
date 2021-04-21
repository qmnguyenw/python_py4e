Speech Recognition in Hindi using Python



We can use Python for Speech Recognition, it is mostly used to recognize
English words. However, in this article, we are going to use Python so that it
can also recognize Hindi words with the help of the Speech Recognition module.

#### Requirements:

  *  **Speech Recognition Module:** It is a library with the help of which Python can recognize the command given. We have to use pip for Speech Recognition. 

    
    
    pip install SpeechRecognition
    

  * **PyAudio Module:** It is a set of Python bindings for _PortAudio_ , a cross-platform C++ library interfacing with audio drivers. We need to also install _Pyaudio_ as the Speech Recognition module is dependent on it.

    
    
    pip install PyAudio
    

If the above command doesn’t work in windows then use the below commands in
the windows command prompt:

    
    
    pip install pipwin
    
    
    pipwin install pyaudio

We will use _Google Speech Recognition API_ for letting the software
understand Hindi. We will assign language as _hn-IN._

 **Below is the complete Python program to take input commands in Hindi and to
recognize them:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import required module

import speech_recognition as sr

 

 

 

# explicit function to take input commands 

# and recognize them

def takeCommandHindi():

 

 r = sr.Recognizer()

 with sr.Microphone() as source:

 

 # seconds of non-speaking audio before 

 # a phrase is considered complete

 print('Listening')

 r.pause_threshold = 0.7

 audio = r.listen(source) 

 try:

 print("Recognizing")

 Query = r.recognize_google(audio, language='hi-In')

 

 # for listening the command in indian english

 print("the query is printed='", Query, "'")

 

 # handling the exception, so that assistant can 

 # ask for telling again the command

 except Exception as e:

 print(e) 

 print("Say that again sir")

 return "None"

 return Query

 

 

 

# Driver Code

 

# call the function

takeCommandHindi()  
  
---  
  
 __

 __

 **Output:**

  

  

https://media.geeksforgeeks.org/wp-content/uploads/20201110162132/hindigfg.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

