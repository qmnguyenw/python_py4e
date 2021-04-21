Convert Text to Speech in Python using win32com.client



There are several APIs available to convert text to speech in python. One of
such APIs available in the python library commonly known as win32com library.
It provides a bunch of methods to get excited about and one of them is the
Dispatch method of the library. Dispatch method when passed with the argument
of **SAPI.SpVoice** It interacts with the Microsoft Speech SDK to speak what
you type in from the keyboard.  
Examples:

    
    
    Input : Hello World
    Output : 
    https://media.geeksforgeeks.org/wp-content/uploads/hello-world.m4a
    
    Input : 121
    Output : https://media.geeksforgeeks.org/wp-content/uploads/121.m4a
    

**Installation**  
To install the win32com.client module , open terminal and write

    
    
    pip install pypiwin32
    

This works on Windows platform. Now we are all set to write a sample program
that converts text to speech.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to convert

# text to speech

 

# import the required module from text to speech conversion

import win32com.client

 

# Calling the Disptach method of the module which 

# interact with Microsoft Speech SDK to speak

# the given input from the keyboard

 

speaker = win32com.client.Dispatch("SAPI.SpVoice")

 

while 1:

 print("Enter the word you want to speak it out by computer")

 s = input()

 speaker.Speak(s)

 

# To stop the program press

# CTRL + Z  
  
---  
  
 __

 __

Input:

    
    
     Welcome to geeks for geeks

Output:

  

  

    
    
    https://media.geeksforgeeks.org/wp-content/uploads/audio.m4a
    

This article is contributed by **Subhajit Saha**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

