Python | Speech recognition on large audio files



  
 **  
Speech recognition** is the process of converting audio into text. This is
commonly used in voice assistants like Alexa, Siri, etc. Python provides an
API called SpeechRecognition to allow us to convert audio into text for
further processing. In this article, we will look at converting large or long
audio files into text using the SpeechRecognition API in python.

## Processing Large audio files

When the input is a long audio file, the accuracy of speech recognition
decreases. Moreover, Google speech recognition API cannot recognize long audio
files with good accuracy. Therefore, we need to process the audio file into
smaller chunks and then feed these chunks to the API. Doing this improves
accuracy and allows us to recognize large audio files.

## Splitting the audio based on silence

One way to process the audio file is to split it into chunks of constant size.
For example, we can take an audio file which is 10 minutes long and split it
into 60 chunks each of length 10 seconds. We can then feed these chunks to the
API and convert speech to text by concatenating the results of all these
chunks. This method is inaccurate. Splitting the audio file into chunks of
constant size might interrupt sentences in between and we might lose some
important words in the process. This is because the audio file might end
before a word is completely spoken and google will not be able to recognize
incomplete words.

The other way is to split the audio file based on silence. Humans pause for a
short amount of time between sentences. If we can split the audio file into
chunks based on these silences, then we can process the file sentence by
sentence and concatenate them to get the result. This approach is more
accurate than the previous one because we do not cut sentences in between and
the audio chunk will contain the entire sentence without any interruptions.
This way, we don’t need to split it into chunks of constant length.

The disadvantage of this method is that it is difficult to determine the
length of silence to split because different users speak differently and some
users might pause for 1 second in between sentences whereas some may pause for
just 0.5 seconds.

  

  

## Libraries required

    
    
    **Pydub:** sudo pip3 install pydub
    **Speech recognition:** sudo pip3 install SpeechRecognition
    

**Example:**

    
    
    **Input:** peacock.wav 
    
    **Output:**
    
    exporting chunk0.wav
    Processing chunk 0
    exporting chunk1.wav
    Processing chunk 1
    exporting chunk2.wav
    Processing chunk 2
    exporting chunk3.wav
    Processing chunk 3
    exporting chunk4.wav
    Processing chunk 4
    exporting chunk5.wav
    Processing chunk 5
    exporting chunk6.wav
    Processing chunk 6
    
    
    

**Code:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

import speech_recognition as sr

 

import os

 

from pydub import AudioSegment

from pydub.silence import split_on_silence

 

# a function that splits the audio file into chunks

# and applies speech recognition

def silence_based_conversion(path = "alice-medium.wav"):

 

 # open the audio file stored in

 # the local system as a wav file.

 song = AudioSegment.from_wav(path)

 

 # open a file where we will concatenate 

 # and store the recognized text

 fh = open("recognized.txt", "w+")

 

 # split track where silence is 0.5 seconds 

 # or more and get chunks

 chunks = split_on_silence(song,

 # must be silent for at least 0.5 seconds

 # or 500 ms. adjust this value based on user

 # requirement. if the speaker stays silent for 

 # longer, increase this value. else, decrease it.

 min_silence_len = 500,

 

 # consider it silent if quieter than -16 dBFS

 # adjust this per requirement

 silence_thresh = -16

 )

 

 # create a directory to store the audio chunks.

 try:

 os.mkdir('audio_chunks')

 except(FileExistsError):

 pass

 

 # move into the directory to

 # store the audio files.

 os.chdir('audio_chunks')

 

 i = 0

 # process each chunk

 for chunk in chunks:

 

 # Create 0.5 seconds silence chunk

 chunk_silent = AudioSegment.silent(duration = 10)

 

 # add 0.5 sec silence to beginning and 

 # end of audio chunk. This is done so that

 # it doesn't seem abruptly sliced.

 audio_chunk = chunk_silent + chunk + chunk_silent

 

 # export audio chunk and save it in 

 # the current directory.

 print("saving chunk{0}.wav".format(i))

 # specify the bitrate to be 192 k

 audio_chunk.export("./chunk{0}.wav".format(i), bitrate
='192k', format ="wav")

 

 # the name of the newly created chunk

 filename = 'chunk'+str(i)+'.wav'

 

 print("Processing chunk "+str(i))

 

 # get the name of the newly created chunk

 # in the AUDIO_FILE variable for later use.

 file = filename

 

 # create a speech recognition object

 r = sr.Recognizer()

 

 # recognize the chunk

 with sr.AudioFile(file) as source:

 # remove this if it is not working

 # correctly.

 r.adjust_for_ambient_noise(source)

 audio_listened = r.listen(source)

 

 try:

 # try converting it to text

 rec = r.recognize_google(audio_listened)

 # write the output to the file.

 fh.write(rec+". ")

 

 # catch any errors.

 except sr.UnknownValueError:

 print("Could not understand audio")

 

 except sr.RequestError as e:

 print("Could not request results. check your internet connection")

 

 i += 1

 

 os.chdir('..')

 

 

if __name__ == '__main__':

 

 print('Enter the audio file path')

 

 path = input()

 

 silence_based_conversion(path)  
  
---  
  
 __

 __

 **  
Output :**

    
    
    
    recognized.txt:
    
    The peacock is the national bird of India. They have colourful feathers, two legs and 
    a small beak. They are famous for their dance. When a peacock dances it spreads its 
    feathers like a fan. It has a long shiny dark blue neck. Peacocks are mostly found in 
    the fields they are very beautiful birds. The females are known as 'Peahen1. Their 
    feathers are used for making jackets, purses etc. We can see them in a zoo. 
    
    

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

