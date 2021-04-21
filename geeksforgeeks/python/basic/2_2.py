How to Play and Record Audio in Python?



As python can mostly do everything one can imagine including playing and
recording audio. This article will make you familiar with some python
libraries and straight-forwards methods using those libraries for playing and
recording sound in python, with some more functionalities in exchange for few
extra intended python lines.

Most of the audio files are in MP3 and WAV file formats. WAV audio files are
the simplest digital audio format with lossless high recording rates as a
result WAV files are large compared to other formats. For the same reason, MP3
formats are used which are small in size and compresses files with very little
difference to overall sound quality. Also, it is very easy to convert WAV to
MP3 with open-source and free software which are widely available over the
internet.

##  **Playing Audio**

Below mentioned are some python libraries with which you can play various
audio formats in python including MP3 formats, WAV formats, and even NumPy
arrays.

**Method 1: Using Playsound**

The ready-to-use package for playing audio files with only a single line of
code. One can play WAV or MP3 files with it. It’s a single function module
with no dependencies for playing sound.

  

  

Documentation of playsound library mentions that it has been tested for WAV
and MP3 files, but may also work with other file formats whose testing was
left up to the user. The playsound module contains only one thing – the
function (also named) playsound.

Following are the code lines to play a file:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#import the library

from playsound import playsound 

 

playsound('full_path/filename.mp3')  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210106104353/1.playsound.mp4

 **Method 2: Using Simpleaudio.**

 **Example 1:**

It is a cross-platform python library for playback of both mono and stereo WAV
files with no other dependencies for audio playback. Python 3.7 and up is
officially supported on macOS, Windows, and Linux.

Following is the simple code to play a .wav format file although it consumes
few more lines of code compared to the above library:

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import library

import simpleaudio as sa

 

# to check all the functions in succession

# to verify the installation

import simpleaudio.functionchecks as fc

fc.run_all()

 

# Path to file

f_name = 'myfile.wav'

 

# create WaveObject instances

# directly from WAV files on disk

wave_obj = sa.WaveObject.from_wave_file(f_name) 

 

# Audio playback

play = wave_obj.play() 

 

# To stop after playing the whole audio

play.wait_done() 

play.stop()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210106104928/2.-simpleaudio.mp4

 **Example 2:**

simpleaudio can be utilized to play NumPy and Python arrays & bytes objects
using simpleaudio.play_buffer() Numpy arrays can be used to store audio but
there are some crucial requirements. If they are to store stereo audio, the
array must have two columns that contain one channel of audio data each. They
must also have a signed 16-bit integer d-type and the sample amplitude values
must consequently fall between -32768 to 32767. Below is the code to generate
a NumPy array and play it back using simpleaudio.play_buffer().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

import simplesound as sa

# Note frequecies

first_freq = 400

nxt_freq = first_freq * 2 ** (7 / 12)

 

# samples per second

smpl_rate = 44100

# Note duration in seconds

seconds = 3

 

# Generate array(timesteps) with 

# seconds*sample_rate steps, 

# ranging between 0 and seconds

arr = np.linspace(0, seconds, seconds * smpl_rate, False)

 

# Generate a 400Hz Sine wave

first_note = np.sin(first_freq * arr * 2 * np.pi)

nxt_note = np.sin(nxt_freq * arr * 2 * np.pi)

 

# merging the notes

tape = np.hstack((first_note,nxt_note))

 

# normalizing to 16-bit range 

# after concatinating the note notes

tape *= 32767 / np.max(np.abs(tape))

 

# Converting to 16-bit data

tape = tape.astype(np.int16)

 

# Start audio

play = sa.play_buffer(tape, 1, 2, smpl_rate)

 

# Wait for audio playback to finish before exiting

play.wait_done()

play.stop()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210106105228/2.1-simpleaudio.mp4

 **Method 3: Using** **winsound.**

 **Example 1:**

It’s the built-in module to access a basic sound playing mechanism. It allows
you to play WAV files only (it does not support any other file formats) or
beep your speaker, but it works only on Windows as the name suggests WINsound.
It’s the built-in module so no extra installation is required.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#Import windound

import winsound

 

winsound.PlaySound(path_to_file, winsound.SND_FILENAME)  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210106110137/3.1-winsound.mp4

 **Example 2:**

It can also be used to beep your speaker or Playing Windows default sound(s).
In the following code beep sound of 5000Hz is played for 1000ms following the
windows exit sound.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#Import windound

import winsound

 

#Beep at frequency = 5000 Hz for duration of 1000 ms

winsound.Beep(5000, 1000) 

 

#windows exit sound after completion of above

winsound.PlaySound("SystemExit", winsound.SND_ALIAS)  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210106110140/3.2-winsound.mp4

The main disadvantage of this library is that it is only for Windows operating
system user and also do not support playback any other files rather than WAV
formats.

 **Method 4: Using sounddevice.**

This Python module provides bindings for the PortAudio library and a few
convenience function(s) to play and record NumPy arrays that contain audio
signals. It is available for Linux, macOS, and Windows operating systems.

In the following code, a line containing ‘ sf.read() ‘ extracts out all the
raw audio data along with the sampling rate of the file as stored in its RIFF
header; and ‘ sounddevice.wait() ‘ ensures that the script terminates after
the ‘ sd.play(data,sr) ‘ finishes playing the audio.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import libraries

import sounddevice as sd

import soundfile as sf

 

# Extract data and sampling rate from file

array, smp_rt = sf.read(path_of_file, dtype = 'float32') 

 

# start the playback 

sd.play(array, smp_rt)

 

# Wait until file is done playing

status = sd.wait() 

 

# stop the sound

sd.stop()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210106112410/4.1-sounddevice.mp4

 **Method 5: Using pydub.**

Even though pydub can easily open and save WAV files without any other
dependencies, must need to have at least one audio playback package from
(simpleaudio, pyaudio, ffplay, and avplay ) pre-installed. It gives pure
python implementation for audio manipulation.

Following code imports two libraries, the first library to load the file and
the second library to play the loaded file. Also, two ways are represented to
load the .wav file.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from pydub import AudioSegment

from pydub.playback import play

 

tape = AudioSegment.from_file('path_to_myfile.wav',
format='wav')

tape = AudioSegment.from_wav('path_to_myfile.wav')

 

play(tape)  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210106112416/5.1-pydub.mp4

 **Method 6: Using pyaudio.**

PyAudio is another cross-platform audio library for Python. While it has more
capability than simpleaudio library, such as recording and continuous audio
streaming, it largely depends on having PortAudio which results in more
complicated installation. It also provides Python bindings for PortAudio, the
cross-platform audio I/O library as provided by python-sounddevice. With
PyAudio, you can easily use Python to play and record audio on a variety of
platform.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

''' Play a WAVE file '''

import pyaudio

import wave

 

filename = 'path-to_file.wav'

 

# Set chunk size of 1024 samples per data frame

chunk = 1024

 

# Open the soaudio/sound file 

af = wave.open(filename, 'rb')

 

# Create an interface to PortAudio 

pa = pyaudio.PyAudio()

 

# Open a .Stream object to write the WAV file

# 'output = True' indicates that the 

# sound will be played rather than

# recorded and opposite can be used for recording

stream = pa.open(format =
pa.get_format_from_width(af.getsampwidth()),

 channels = af.getnchannels(),

 rate = af.getframerate(),

 output = True)

 

# Read data in chunks

rd_data = af.readframes(chunk)

 

# Play the sound by writing the audio

# data to the Stream using while loop

while rd_data != '':

 stream.write(rd_data)

 rd_data = af.readframes(chunk)

 

# Close and terminate the stream

stream.stop_stream()

stream.close()

pa.terminate()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210106121909/6.-pyaudio_play.mp4

##  **Recording Audio**

Now just switching to the recording mode of the article. Few of the above-
mentioned libraries are used for the same, both playing and recording can be
explained collectively but for many, it might get a bit confusing. So
different dedicated sections are preferred here.

Note- Before using any library for recording, make sure the microphone of your
device is actually connected and is ON also not Muted. one can check the same
using operating system features and settings.

 **Method 1. Using python-sounddevice**

This library allows you to play (explained above) and record NumPy arrays
containing audio signal information. This module requires scipy or wavio to
save the recorded audio, this means scipy or wavio library should be pre-
installed along with Numpy before using this package for recording.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import required libraries

import sounddevice as sd

from scipy.io.wavfile import write

import wavio as wv

 

# Sampling frequency

frequency = 44400

 

# Recording duration in seconds

duration = 3.5

 

# to record audio from

# sound-device into a Numpy

recording = sd.rec(int(duration * frequency),

 samplerate = freq, channels = 2)

 

# Wait for the audio to complete

sd.wait()

 

# using scipy to save the recording in .wav format

# This will convert the NumPy array

# to an audio file with the given sampling frequency

write("recording0.wav", freq, recording)

 

# using wavio to save the recording in .wav format

# This will convert the NumPy array to an audio

# file with the given sampling frequency

wv.write("recording1.wav", recording, freq, sampwidth=2)  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210106114323/1.-record_soundevice.mp4

As stated in the Audio section sounddevice had a default option to specify the
channel and frequency for the repeated use. After that no need to pass this
option as arguments in sd.rec() method. Following code represents the same
along with one can also change the data type of recorded array from default
type of float32 to others.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import sounddevice as sd

 

sd.default.samplerate = 4400

sd.default.channels = 2

 

myrecording = sd.rec(int(duration * fs))

 

# change the data type: pass a new argument in .rec() of dtype

# myrecording = sd.rec(int(duration * fs), dtype='float64')

 

sd.wait()  
  
---  
  
 __

 __

#### Simultaneous Playback& Recording

To Play an array named my_arr and Record at the same time. Here sample rate is
smpl_rate

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import sounddevice as sd

import numpy as np

 

smpl_rate = 44100

 

my_arr = np.random.uniform(-1,1,smpl_rate)

recordd= sd.playrec(my_arr, smpl_rate, channels=2)

 

sd.wait()  
  
---  
  
 __

 __

https://media.geeksforgeeks.org/wp-content/uploads/20210101111541/play_rec.mp4

 **Method 2: Using pyaudio.**

As above, we played audio using pyaudio by reading the pyaudio.Stream(). To
record audio we must write to this same stream. Following is the code to
record a few seconds of audio and save the same to a .wav file:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pyaudio

import wave

 

# Record in chunks of 1024 samples

chunk = 1024

 

# 16 bits per sample

sample_format = pyaudio.paInt16 

chanels = 2

 

# Record at 44400 samples per second

smpl_rt = 44400

seconds = 4

filename = "path_of_file.wav"

 

# Create an interface to PortAudio

pa = pyaudio.PyAudio() 

 

stream = pa.open(format=sample_format, channels=chanels, 

 rate=smpl_rt, input=True, 

 frames_per_buffer=chunk)

 

print('Recording...')

 

# Initialize array taht be used for storing frames

frames = [] 

 

# Store data in chunks for 8 seconds

for i in range(0, int(smpl_rt / chunk * seconds)):

 data = stream.read(chunk)

 frames.append(data)

 

# Stop and close the stream 

stream.stop_stream()

stream.close()

 

# Terminate - PortAudio interface

pa.terminate()

 

print('Done !!! ')

 

# Save the recorded data in a .wav format

sf = wave.open(filename, 'wb')

sf.setnchannels(chanels)

sf.setsampwidth(pa.get_sample_size(sample_format))

sf.setframerate(smpl_rt)

sf.writeframes(b''.join(frames))

sf.close()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210106121905/2.-record_pyaudio.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

