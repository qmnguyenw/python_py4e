Convert Text to Speech in Python



There are several APIs available to convert text to speech in Python. One of
such APIs is the Google Text to Speech API commonly known as the gTTS API.
gTTS is a very easy to use tool which converts the text entered, into audio
which can be saved as a mp3 file.

The gTTS API supports several languages including English, Hindi, Tamil,
French, German and many more. The speech can be delivered in any one of the
two available audio speeds, fast or slow. However, as of the latest update, it
is not possible to change the voice of the generated audio.

###  **Installation**

To install the gTTS API, open terminal and write

    
    
    pip install gTTS
    

This works for any platform.  
Now we are all set to write a sample program that converts text to speech.

 __

 __  
 __

 __

 __  
 __  
 __

# Import the required module for text

# to speech conversion

from gtts import gTTS

 

# This module is imported so that we can 

# play the converted audio

import os

 

# The text that you want to convert to audio

mytext = 'Welcome to geeksforgeeks!'

 

# Language in which you want to convert

language = 'en'

 

# Passing the text and language to the engine, 

# here we have marked slow=False. Which tells 

# the module that the converted audio should 

# have a high speed

myobj = gTTS(text=mytext, lang=language, slow=False)

 

# Saving the converted audio in a mp3 file named

# welcome 

myobj.save("welcome.mp3")

 

# Playing the converted file

os.system("mpg321 welcome.mp3")  
  
---  
  
 __

 __

###  **Output**

    
    
    The output of the above program should be a 
    voice saying, 'Welcome to geeksforgeeks!'
    

  

  

This article is contributed by **Akhil Goel**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

