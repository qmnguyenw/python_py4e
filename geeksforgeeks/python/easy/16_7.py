Audio processing using Pydub and Google speechRecognition API



Audio files are a widespread means of transferring information. So, let’s see
how to break down audio files (.wav files) into smaller chunks, and to
recognize the content in them and store it to a text file. To know more about
audio files and their formats, refer Audio_formats.

 **Need to break down an audio file?**

When we do any processing on audio files, it takes a lot of time. Here,
processing can mean anything. For example, we may want to increase or decrease
the frequency of the audio, or as done in this article, recognize the content
in the audio file. By breaking it down into small audio files called chunks,
we can ensure that the processing happens fast.

 **Required Installations:**

    
    
    pip3 install pydub
    pip3 install audioread
    pip3 install SpeechRecognition

There are majorly two steps in the program.

  

  

 **Step #1:** It deals with slicing the audio files into small chunks of a
constant interval. The slicing can be done with, or without overlap. Overlap
means that the next chunk created will start from a constant time backward, so
that during the slicing if any audio/word gets cut, it can be covered by this
overlap. For example, if the audio file is 22 seconds, and the overlap is 1.5
seconds, the timing of these chunks will be:

    
    
      chunk1 : 0 - 5 seconds
      chunk2 : 3.5 - 8.5 seconds
      chunk3 : 7 - 12 seconds
      chunk4 : 10.5 - 15.5 seconds
      chunk5 : 14 - 19.5 seconds
      chunk6 : 18 - 22 seconds

We can ignore this overlap by setting the overlap to 0.

 **Step #2:** It deals with working with the sliced audio file to do whatever
the user requires. Here, for demonstration purposes, the chunks have been
passed through the Google Speech recognition module, and the text has been
written to a separate file. To understand how to use the Google Speech
Recognition module to recognize the audio from a microphone, refer this. In
this article, we will be using the sliced audio files to recognize the
content.

 _Step #2_ is done in a loop inside _Step #1_. As soon as the audio file is
sliced into the chunk, the chunk is recognized. This process continues till
the end of the audio file.

 **Example:**

    
    
    **Input :**  **Geek.wav**
    
    
    **Output :**
    Screenshot of cmd running the code:
    ![](https://media.geeksforgeeks.org/wp-content/uploads/chunks.png)
    
    Text File: recognized
    
    

  
Below is the implementation:

 __

 __  
 __

 __

 __  
 __  
 __

# Import necessary libraries

from pydub import AudioSegment

import speech_recognition as sr

 

# Input audio file to be sliced

audio = AudioSegment.from_wav("1.wav")

 

'''

Step #1 - Slicing the audio file into smaller chunks.

'''

# Length of the audiofile in milliseconds

n = len(audio)

 

# Variable to count the number of sliced chunks

counter = 1

 

# Text file to write the recognized audio

fh = open("recognized.txt", "w+")

 

# Interval length at which to slice the audio file.

# If length is 22 seconds, and interval is 5 seconds,

# The chunks created will be:

# chunk1 : 0 - 5 seconds

# chunk2 : 5 - 10 seconds

# chunk3 : 10 - 15 seconds

# chunk4 : 15 - 20 seconds

# chunk5 : 20 - 22 seconds

interval = 5 * 1000

 

# Length of audio to overlap. 

# If length is 22 seconds, and interval is 5 seconds,

# With overlap as 1.5 seconds,

# The chunks created will be:

# chunk1 : 0 - 5 seconds

# chunk2 : 3.5 - 8.5 seconds

# chunk3 : 7 - 12 seconds

# chunk4 : 10.5 - 15.5 seconds

# chunk5 : 14 - 19.5 seconds

# chunk6 : 18 - 22 seconds

overlap = 1.5 * 1000

 

# Initialize start and end seconds to 0

start = 0

end = 0

 

# Flag to keep track of end of file.

# When audio reaches its end, flag is set to 1 and we break

flag = 0

 

# Iterate from 0 to end of the file,

# with increment = interval

for i in range(0, 2 * n, interval):

 

 # During first iteration,

 # start is 0, end is the interval

 if i == 0:

 start = 0

 end = interval

 

 # All other iterations,

 # start is the previous end - overlap

 # end becomes end + interval

 else:

 start = end - overlap

 end = start + interval 

 

 # When end becomes greater than the file length,

 # end is set to the file length

 # flag is set to 1 to indicate break.

 if end >= n:

 end = n

 flag = 1

 

 # Storing audio file from the defined start to end

 chunk = audio[start:end]

 

 # Filename / Path to store the sliced audio

 filename = 'chunk'+str(counter)+'.wav'

 

 # Store the sliced audio file to the defined path

 chunk.export(filename, format ="wav")

 # Print information about the current chunk

 print("Processing chunk "+str(counter)+". Start = "

 +str(start)+" end = "+str(end))

 

 # Increment counter for the next chunk

 counter = counter + 1

 

 # Slicing of the audio file is done.

 # Skip the below steps if there is some other usage

 # for the sliced audio files.

 

 

'''

Step #2 - Recognizing the chunk and writing to a file.

'''

 

 # Here, Google Speech Recognition is used

 # to take each chunk and recognize the text in it.

 

 # Specify the audio file to recognize

 

 AUDIO_FILE = filename

 

 # Initialize the recognizer

 r = sr.Recognizer()

 

 # Traverse the audio file and listen to the audio

 with sr.AudioFile(AUDIO_FILE) as source:

 audio_listened = r.listen(source)

 

 # Try to recognize the listened audio

 # And catch expections.

 try: 

 rec = r.recognize_google(audio_listened)

 

 # If recognized, write into the file.

 fh.write(rec+" ")

 

 # If google could not understand the audio

 except sr.UnknownValueError:

 print("Could not understand audio")

 

 # If the results cannot be requested from Google.

 # Probably an internet connection error.

 except sr.RequestError as e:

 print("Could not request results.")

 

 # Check for flag.

 # If flag is 1, end of the whole audio reached.

 # Close the file and break.

 if flag == 1:

 fh.close()

 break  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/audiopro.png)

 **recognized.txt** –  
![](https://media.geeksforgeeks.org/wp-content/uploads/recog.png)  
As we can see in the above screenshot, all these chunks are stored in the
local system. We have now successfully sliced the audio file with an overlap
and recognized the content from the chunks.

 **Advantages of this method:**

  * The interval can be set to any length depending on how long we need the chunks to be.
  * Overlap ensures that no data is lost even if any word is said precisely at the end of the interval.
  * The chunks can all be stored in different audio files and used later if need be.
  * Any processing which can be done on an audio file can be done in these chunks as well, as they are just audio files.

 **Disadvantages of this method:**

  * Using Google Speech Recognition requires an active internet connection.
  * After the overlap, some text processing should be done to remove the duplicate words recognized.
  * The accuracy of Google Speech Recognition varies on a lot of factors like background noise, speaker’s accent etc.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

