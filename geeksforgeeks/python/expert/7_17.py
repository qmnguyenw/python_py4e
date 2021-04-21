Python | Text to Speech by using pyttsx3



 **pyttsx3** is a text-to-speech conversion library in Python. Unlike
alternative libraries, it works offline and is compatible with both Python 2
and 3. An application invokes the pyttsx3.init() factory function to get a
reference to a pyttsx3. Engine instance. it is a very easy to use tool which
converts the entered text into speech.  
The pyttsx3 module supports two voices first is female and the second is male
which is provided by “sapi5” for windows.  
It supports three TTS engines :

  *  _sapi5_ – SAPI5 on Windows
  *  _nsss_ – NSSpeechSynthesizer on Mac OS X
  *  _espeak_ – eSpeak on every other platform

 **Installataion**  
To install the pyttsx3 module, first of all, you have to open the terminal and
write

    
    
    pip install pyttsx3

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190822185833/Screenshot-3114.png)  
If you receive errors such as No module named win32com.client, No module named
win32, or No module named win32api, you will need to additionally install
pypiwin32.  
It can work on any platform. Now we are all set to write a program for
conversion of text to speech.

