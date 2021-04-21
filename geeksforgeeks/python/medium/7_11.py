Build a Virtual Assistant Using Python



Virtual desktop assistant is an awesome thing. If you want your machine to run
on your command like Jarvis did for Tony. Yes it is possible. It is possible
using Python. Python offers a good major library so that we can use it for
making a virtual assistant. Windows has Sapi5 and Linux has Espeak which can
help us in having the voice from our machine. It is a weak A.I.

### Modules needed

  *  **pyttsx3:** pyttsx is a cross-platform text to speech library which is platform independent. The major advantage of using this library for text-to-speech conversion is that it works offline. To install this module type the below command in the terminal.

    
    
    pip install pyttsx3

  *  **SpeechRecognition:** It allow us to convert audio into text for further processing. To install this module type the below command in the terminal.

    
    
    pip install SpeechRecognition

  *  **webbrowser:** It **** provides a high-level interface which allows displaying Web-based documents to users. To install this module type the below command in the terminal.

    
    
    pip install webbrowser

  *  **Wikipedia:** It is used to fetch a variety of information from the Wikipedia website. To install this module type the below command in the terminal.

    
    
    pip install wikipedia

## Methods used for Virtual Assistant

#### 1) Speak Method

Speak Method will help us in taking the voice from the machine. Here is the
code explanation of Speak Method

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def speak(audio):

 

 engine = pyttsx3.init()

 # getter method(gets the current value

 # of engine property)

 voices = engine.getProperty('voices')

 

 # setter method .[0]=male voice and 

 # [1]=female voice in set Property.

 engine.setProperty('voice', voices[0].id)

 

 # Method for the speaking of the the assistant

 engine.say(audio) 

 

 # Blocks while processing all the currently

 # queued commands

 engine.runAndWait()  
  
---  
  
 __

 __

#### **2) Take query method**

This method will check for the condition. If the condition is true it will
return output. We can add any number if conditions for it and if the condition
satisfy we will get the desired output.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def Take_query():

 

 # calling the Hello function for 

 # making it more interactive

 Hello()

 

 # This loop is infinite as it will take

 # our queries continuously until and unless

 # we do not say bye to exit or terminate 

 # the program

 while(True):

 

 # taking the query and making it into

 # lower case so that most of the times 

 # query matches and we get the perfect 

 # output

 query = takeCommand().lower()

 if "open geeksforgeeks" in query:

 speak("Opening GeeksforGeeks ")

 

 # in the open method we just to give the link

 # of the website and it automatically open 

 # it in your default browser

 webbrowser.open("www.geeksforgeeks.com")

 continue

 

 elif "open google" in query:

 speak("Opening Google ")

 webbrowser.open("www.google.com")

 continue

 

 elif "which day it is" in query:

 tellDay()

 continue

 

 elif "tell me the time" in query:

 tellTime()

 continue

 

 # this will exit and terminate the program

 elif "bye" in query:

 speak("Bye. Check Out GFG for more exicting things")

 exit()

 

 elif "from wikipedia" in query:

 

 # if any one wants to have a information

 # from wikipedia

 speak("Checking the wikipedia ")

 query = query.replace("wikipedia", "")

 

 # it will give the summary of 4 lines from 

 # wikipedia we can increase and decrease 

 # it also.

 result = wikipedia.summary(query, sentences=4)

 speak("According to wikipedia")

 speak(result)

 

 elif "tell me your name" in query:

 speak("I am Jarvis. Your deskstop Assistant")  
  
---  
  
 __

 __

#### 3) takeCommand method

This method is for taking the commands and recognizing the command from the
speech_Recognition module

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# this method is for taking the commands

# and recognizing the command from the

# speech_Recognition module we will use

# the recongizer method for recognizing

def takeCommand():

 

 r = sr.Recognizer()

 

 # from the speech_Recognition module 

 # we will use the Microphone module

 # for listening the command

 with sr.Microphone() as source:

 print('Listening')

 

 # seconds of non-speaking audio before 

 # a phrase is considered complete

 r.pause_threshold = 0.7

 audio = r.listen(source)

 

 # Now we will be using the try and catch

 # method so that if sound is recognized 

 # it is good else we will have exception 

 # handling

 try:

 print("Recognizing")

 

 # for Listening the command in indian

 # english we can also use 'hi-In' 

 # for hindi recognizing

 Query = r.recognize_google(audio, language='en-in')

 print("the command is printed=", Query)

 

 except Exception as e:

 print(e)

 print("Say that again sir")

 return "None"

 

 return Query  
  
---  
  
 __

 __

#### *)tellTime method

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

def tellTime(self):

# This method will give the time

 time = str(datetime.datetime.now())

 # the time will be displayed like this "2020-06-05 17:50:14.582630"

 # nd then after slicing we can get time

 print(time)

 hour = time[11:13]

 min = time[14:16]

 self.Speak(self, "The time is sir" + hour + "Hours and"
+ min + "Minutes") 

"""

 This method will take time and slice it "2020-06-05 17:50:14.582630" from
11 to 12 for hour

 and 14-15 for min and then speak function will be called and then it will
speak the current 

 time

 """  
  
---  
  
 __

 __

#### 4) Hello method

This is just used to greet the user with a hello message.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def Hello():

 # This function is for when the assistant 

 # is called it will say hello and then 

 # take query

 speak("hello sir I am your desktop assistant. /

 Tell me how may I help you")  
  
---  
  
 __

 __

#### 5) Main method

Main method is the method where all the files get executed so we will call the
Take_query method here so that it can recognize and tell or give us the
desired output.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

if __name__ == '__main__':

 

 # main method for executing

 # the functions

 Take_query()  
  
---  
  
 __

 __

**Complete Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pyttsx3

import speech_recognition as sr

import webbrowser 

import datetime 

import wikipedia 

 

 

# this method is for taking the commands

# and recognizing the command from the

# speech_Recognition module we will use

# the recongizer method for recognizing

def takeCommand():

 

 r = sr.Recognizer()

 

 # from the speech_Recognition module 

 # we will use the Microphone module

 # for listening the command

 with sr.Microphone() as source:

 print('Listening')

 

 # seconds of non-speaking audio before 

 # a phrase is considered complete

 r.pause_threshold = 0.7

 audio = r.listen(source)

 

 # Now we will be using the try and catch

 # method so that if sound is recognized 

 # it is good else we will have exception 

 # handling

 try:

 print("Recognizing")

 

 # for Listening the command in indian

 # english we can also use 'hi-In' 

 # for hindi recognizing

 Query = r.recognize_google(audio, language='en-in')

 print("the command is printed=", Query)

 

 except Exception as e:

 print(e)

 print("Say that again sir")

 return "None"

 

 return Query

 

def speak(audio):

 

 engine = pyttsx3.init()

 # getter method(gets the current value

 # of engine property)

 voices = engine.getProperty('voices')

 

 # setter method .[0]=male voice and 

 # [1]=female voice in set Property.

 engine.setProperty('voice', voices[0].id)

 

 # Method for the speaking of the the assistant

 engine.say(audio) 

 

 # Blocks while processing all the currently

 # queued commands

 engine.runAndWait()

 

def tellDay():

 

 # This function is for telling the

 # day of the week

 day = datetime.datetime.today().weekday() + 1

 

 #this line tells us about the number 

 # that will help us in telling the day

 Day_dict = {1: 'Monday', 2: 'Tuesday', 

 3: 'Wednesday', 4: 'Thursday', 

 5: 'Friday', 6: 'Saturday',

 7: 'Sunday'}

 

 if day in Day_dict.keys():

 day_of_the_week = Day_dict[day]

 print(day_of_the_week)

 speak("The day is " + day_of_the_week)

 

 

def tellTime():

 

 # This method will give the time

 time = str(datetime.datetime.now())

 

 # the time will be displayed like 

 # this "2020-06-05 17:50:14.582630"

 #nd then after slicing we can get time

 print(time)

 hour = time[11:13]

 min = time[14:16]

 speak(self, "The time is sir" + hour + "Hours and" +
min + "Minutes") 

 

def Hello():

 

 # This function is for when the assistant 

 # is called it will say hello and then 

 # take query

 speak("hello sir I am your desktop assistant. /

 Tell me how may I help you")

 

 

def Take_query():

 

 # calling the Hello function for 

 # making it more interactive

 Hello()

 

 # This loop is infinite as it will take

 # our queries continuously until and unless

 # we do not say bye to exit or terminate 

 # the program

 while(True):

 

 # taking the query and making it into

 # lower case so that most of the times 

 # query matches and we get the perfect 

 # output

 query = takeCommand().lower()

 if "open geeksforgeeks" in query:

 speak("Opening GeeksforGeeks ")

 

 # in the open method we just to give the link

 # of the website and it automatically open 

 # it in your default browser

 webbrowser.open("www.geeksforgeeks.com")

 continue

 

 elif "open google" in query:

 speak("Opening Google ")

 webbrowser.open("www.google.com")

 continue

 

 elif "which day it is" in query:

 tellDay()

 continue

 

 elif "tell me the time" in query:

 tellTime()

 continue

 

 # this will exit and terminate the program

 elif "bye" in query:

 speak("Bye. Check Out GFG for more exicting things")

 exit()

 

 elif "from wikipedia" in query:

 

 # if any one wants to have a information

 # from wikipedia

 speak("Checking the wikipedia ")

 query = query.replace("wikipedia", "")

 

 # it will give the summary of 4 lines from 

 # wikipedia we can increase and decrease 

 # it also.

 result = wikipedia.summary(query, sentences=4)

 speak("According to wikipedia")

 speak(result)

 

 elif "tell me your name" in query:

 speak("I am Jarvis. Your deskstop Assistant")

 

if __name__ == '__main__':

 

 # main method for executing

 # the functions

 Take_query()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200612204652/pythondesktopassistant.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

