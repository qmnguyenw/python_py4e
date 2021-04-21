Language Translator Using Google API in Python



 **API** stands for **Application Programming Interface**. It acts as an
intermediate between two applications or software. In simple terms, API acts
as a messenger that takes your request to destinations and then brings back
its response for you. Google API is developed by Google to allow
communications with their servers and use their API keys to develop projects.

In this tutorial, we are going to use Google API to build a Langauge
Translator which can translate one language to another language. On the
internet, we can see lots of projects on Speech Recognitions, Speech to text,
text to speech, etc. but here in this project we are going to build something
more advance than that.

Let’s assume a scenario, we are traveling in Spain and we don’t know how to
speak Spanish or we are in any other country and we don’t know their native
language, then we can use this tool to overcome the problem. We can translate
between all those languages which are present in **google translator**.

### Installation

Now to Check what languages it supports we have to use **google trans**
library. We can use pip to install it.

    
    
    pip install googletrans
    

Now to check which languages it supports to run the following code.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# To Print all the languages that google

# translator supports

import googletrans

 

 

print(googletrans.LANGUAGES)  
  
---  
  
 __

 __

 **Output:**

![google-trans-python](https://media.geeksforgeeks.org/wp-
content/uploads/20200430163105/google-trans-python.png)

Now let’s start building Language Translator. To begin with the coding part,
we need to install some dependencies. While installing Pyaudio you might get
an error of portaudio. For details of installation of pyaudio click here.

    
    
    pip install pyaudio
    pip install SpeechRecognition
    pip install gtts
    

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Importing necessary modules required

import speech_recognition as spr

from googletrans import Translator

from gtts import gTTS

import os

 

 

# Creating Recogniser() class object

recog1 = spr.Recognizer()

 

# Creating microphone instance

mc = spr.Microphone()

 

 

# Capture Voice

with mc as source:

 print("Speak 'hello' to initiate the Translation !")

 print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

 recog1.adjust_for_ambient_noise(source, duration=0.2)

 audio = recog1.listen(source)

 MyText = recog1.recognize_google(audio) 

 MyText = MyText.lower()

 

# Here initialising the recorder with 

# hello, whatever after that hello it

# will recognise it.

if 'hello' in MyText:

 

 # Translator method for translation

 translator = Translator()

 

 # short form of english in which 

 # you will speak

 from_lang = 'en'

 

 # In which we want to convert, short 

 # form of hindi

 to_lang = 'hi'

 

 with mc as source:

 

 print("Speak a stentence...")

 recog1.adjust_for_ambient_noise(source, duration=0.2)

 

 # Storing the speech into audio variable

 audio = recog1.listen(source)

 

 # Using recognize.google() method to

 # convert audio into text

 get_sentence = recog1.recognize_google(audio)

 

 # Using try and except block to improve

 # its efficiency.

 try:

 

 # Printing Speech which need to 

 # be translated.

 print("Phase to be Translated :"+ get_sentence)

 

 # Using translate() method which requires 

 # three arguments, 1st the sentence which

 # needs to be translated 2nd source language

 # and 3rd to which we need to translate in 

 text_to_translate = translator.translate(get_sentence, 

 src= from_lang,

 dest= to_lang)

 

 # Storing the translated text in text 

 # variable 

 text = text_to_translate.text 

 

 # Using Google-Text-to-Speech ie, gTTS() method

 # to speak the translated text into the 

 # destination language which is stored in to_lang.

 # Also, we have given 3rd argument as False because

 # by default it speaks very slowly

 speak = gTTS(text=text, lang=to_lang, slow= False) 

 

 # Using save() method to save the translated 

 # speech in capture_voice.mp3

 speak.save("captured_voice.mp3") 

 

 # Using OS module to run the translated voice.

 os.system("start captured_voice.mp3")

 

 # Here we are using except block for UnknownValue 

 # and Request Error and printing the same to

 # provide better service to the user.

 except spr.UnknownValueError:

 print("Unable to Understand the Input")

 

 except spr.RequestError as e:

 print("Unable to provide Required Output".format(e))  
  
---  
  
 __

 __

 **Output:**

    
    
    Speak 'hello' to initiate the Translation !
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Speak a stentence...
    Phase to be Translated :what are you doing

https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200430164710/captured_voice.mp3

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

