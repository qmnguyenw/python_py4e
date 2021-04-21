How to save pyttsx3 results to MP3 or WAV file?



In this article, we will see how to generate and save _pyttsx3_ results as mp3
and wav file. _Pyttsx3_ is a python module that provides a Text to Speech API.
We can use this API to convert the text into voice.

### Environment setup:

To use pyttsx3 we have to install _espeak_ and _ffmpeg_ first.

    
    
    sudo apt update
    sudo apt install espeak
    sudo apt install ffmpeg

Additionally, we need to install the latest version of _pyttsx3_

    
    
    python3 -m pip install pyttsx3

We can confirm the installation by importing the module.

    
    
    import pyttsx3

If the above statement runs without error, the environment setup is
successful.

### Using Pyttsx3

  * First, we have to initialize the _pyttsx3_ engine. The _init()_ method does that for us.
  * Next, we need to create a string with the text we want to convert to audio.
  * The _say()_ method takes the string as a parameter. It will set the string it has to speak.
  * Since the speech will take a while to play on the speaker of the machine, we need to wait for the process to complete. Hence, we need to call the _runAndWait()_ method in order to let the interpreter stop the execution till then.
  * Below is the code for the above steps:

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Import the required module

import pyttsx3

 

# Create a string

string = "Lorem Ipsum is simply dummy text " \

 + "of the prting and typesetting industry."

 

# Initialize the Pyttsx3 engine

engine = pyttsx3.init()

 

# Command it to speak the given string

engine.say(string)

 

# Wait until above command is not finished.

engine.runAndWait()  
  
---  
  
 __

 __

