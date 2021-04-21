Speech Recognition in Python using Google Speech API



  
Speech Recognition is an important feature in several applications used such
as home automation, artificial intelligence, etc. This article aims to provide
an introduction on how to make use of the SpeechRecognition library of Python.
This is useful as it can be used on microcontrollers such as Raspberri Pis
with the help of an external microphone.

 **Required Installations**

The following must be installed:

  1.  **Python Speech Recognition module:**
    
         sudo pip install SpeechRecognition 

  2. **PyAudio:** Use the following command for linux users
    
        sudo apt-get install python-pyaudio python3-pyaudio

If the versions in the repositories are too old, install pyaudio using the
following command

    
        sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && 
    sudo pip install pyaudio

Use pip3 instead of pip for python3.  
Windows users can install pyaudio by executing the following command in a
terminal

  

  

    
        pip install pyaudio

 **Speech Input Using a Microphone and Translation of Speech to Text**

  1.  **Configure Microphone (For external microphones):** It is advisable to specify the microphone during the program to avoid any glitches.  
Type **lsusb** in the terminal. A list of connected devices will show up. The
microphone name would look like this

    
        USB Device 0x46d:0x825: Audio (hw:1, 0)

Make a note of this as it will be used in the program.

  2.  **Set Chunk Size:** This basically involved specifying how many bytes of data we want to read at once. Typically, this value is specified in powers of 2 such as 1024 or 2048
  3.  **Set Sampling Rate:** Sampling rate defines how often values are recorded for processing
  4.  **Set Device ID to the selected microphone** : In this step, we specify the device ID of the microphone that we wish to use in order to avoid ambiguity in case there are multiple microphones. This also helps debug, in the sense that, while running the program, we will know whether the specified microphone is being recognized. During the program, we specify a parameter device_id. The program will say that device_id could not be found if the microphone is not recognized.
  5.  **Allow Adjusting for Ambient Noise:** Since the surrounding noise varies, we must allow the program a second or too to adjust the energy threshold of recording so it is adjusted according to the external noise level.
  6.  **Speech to text translation:** This is done with the help of Google Speech Recognition. This requires an active internet connection to work. However, there are certain offline Recognition systems such as PocketSphinx, but have a very rigorous installation process that requires several dependencies. Google Speech Recognition is one of the easiest to use.

The Above steps have been implemented below:

 __

 __  
 __

 __

 __  
 __  
 __

#Python 2.x program for Speech Recognition

 

import speech_recognition as sr

 

#enter the name of usb microphone that you found

#using lsusb

#the following name is only used as an example

mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"

#Sample rate is how often values are recorded

sample_rate = 48000

#Chunk is like a buffer. It stores 2048 samples (bytes of data)

#here. 

#it is advisable to use powers of 2 such as 1024 or 2048

chunk_size = 2048

#Initialize the recognizer

r = sr.Recognizer()

 

#generate a list of all audio cards/microphones

mic_list = sr.Microphone.list_microphone_names()

 

#the following loop aims to set the device ID of the mic that

#we specifically want to use to avoid ambiguity.

for i, microphone_name in enumerate(mic_list):

 if microphone_name == mic_name:

 device_id = i

 

#use the microphone as source for input. Here, we also specify 

#which device ID to specifically look for incase the microphone 

#is not working, an error will pop up saying "device_id undefined"

with sr.Microphone(device_index = device_id, sample_rate =
sample_rate, 

 chunk_size = chunk_size) as source:

 #wait for a second to let the recognizer adjust the 

 #energy threshold based on the surrounding noise level

 r.adjust_for_ambient_noise(source)

 print "Say Something"

 #listens for the user's input

 audio = r.listen(source)

 

 try:

 text = r.recognize_google(audio)

 print "you said: " + text

 

 #error occurs when google could not understand what was said

 

 except sr.UnknownValueError:

 print("Google Speech Recognition could not understand audio")

 

 except sr.RequestError as e:

 print("Could not request results from Google 

 Speech Recognition service; {0}".format(e))  
  
---  
  
 __

 __

 **Transcribe an Audio file to text**

If we have an audio file that we want to translate to text, we simply have to
replace the source with the audio file instead of a microphone.  
Place the audio file and the program in the same folder for convenience. This
works for WAV, AIFF, of FLAC files.  
An implementation has been shown below

 __

 __  
 __

 __

 __  
 __  
 __

#Python 2.x program to transcribe an Audio file

import speech_recognition as sr

 

AUDIO_FILE = ("example.wav")

 

# use the audio file as the audio source

 

r = sr.Recognizer()

 

with sr.AudioFile(AUDIO_FILE) as source:

 #reads the audio file. Here we use record instead of

 #listen

 audio = r.record(source) 

 

try:

 print("The audio file contains: " + r.recognize_google(audio))

 

except sr.UnknownValueError:

 print("Google Speech Recognition could not understand audio")

 

except sr.RequestError as e:

 print("Could not request results from Google Speech 

 Recognition service; {0}".format(e))  
  
---  
  
 __

 __

 **Troubleshooting**

The following problems are commonly encountered

  1.  **Muted Microphone:** This leads to input not being received. To check for this, you can use alsamixer.  
It can be installed using

  

  

    
    
    sudo apt-get install libasound2 alsa-utils alsa-oss

Type **amixer**. The output will look somewhat like this

    
    
    Simple mixer control 'Master', 0
      Capabilities: pvolume pswitch pswitch-joined
      Playback channels: Front Left - Front Right
      Limits: Playback 0 - 65536
      Mono:
      Front Left: Playback 41855 [64%] [on]
      Front Right: Playback 65536 [100%] [on]
    Simple mixer control 'Capture', 0
      Capabilities: cvolume cswitch cswitch-joined
      Capture channels: Front Left - Front Right
      Limits: Capture 0 - 65536
      Front Left: Capture 0 [0%] [off] #switched off
      Front Right: Capture 0 [0%] [off]
    

As you can see, the capture device is currently switched off. To switch it on,
type **alsamixer**  
As you can see in the first picture, it is displaying our playback devices.
Press F4 to toggle to Capture devices.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Alsamixer-capture.jpg)

In the second picture, the highlighted portion shows that the capture device
is muted. To unmute it, press space bar  
![](https://media.geeksforgeeks.org/wp-content/uploads/Muted-capture-
device.jpg)

As you can see in the last picture, the highlighted part confirms that the
capture device is not muted.  
![](https://media.geeksforgeeks.org/wp-content/uploads/unmuted-capture-
device.jpg)

*  **Current microphone not selected as capture device:**  
In this case, the microphone can be set by typing **alsamixer** and selecting
sound cards. Here, you can select default microphone device.  
As shown in the picture, the highlighted portion is where you have to select
sound card.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Alsamixer-
soundcard.jpg)

The second picture shows the screen selection for sound card  
![](https://media.geeksforgeeks.org/wp-content/uploads/sound_card.png)

*  **No Internet Connection:** The speech to text conversion requires an active internet connection.

