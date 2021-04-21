Download Video in MP3 format using PyTube



YouTube is the world’s most common video sharing site, and you can experience
a situation as a hacker where you want to script something to download videos.
For this, We present Pytube to you.

  * Pytube is a lightweight, Python-written library. It does not have third-party dependencies and strives to be extremely secure.
  * Pytube also simplifies pipelining, allowing you to define callback functionality for various download events, such as progress or completion.
  * Finally, pytube also provides a command-line feature that allows you to stream videos directly from the terminal easily.

To do our task, we will some libraries especially the pytube from python. For
this, we have to import it. To import pytube, we can use the commands
according to the python version.

    
    
    For Python2 : pip install pytube
    For Python3 : pip3 install pytube
    For pyube3 : pip install pytube3

To save the audio file, we are using the os module and import by using the
command given below :

    
    
    pip install os_sys

 **Procedure:**

  * First, we need to import the required (pytube and os) module.
  * Then we take input from the user i.e; the link of the YouTube video.
  * As, we need only an audio file from that video, so we use the filter method.
  * Now we need to set the output path of the audio file, which we will do by using the os module.
  * Now finally we can change the audio extension to MP3 and play our audio.

 **Implementation:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing packages

from pytube import YouTube

import os

 

# url input from user

yt = YouTube(

 str(input("Enter the URL of the video you want to download: \n>>
")))

 

# extract only audio

video = yt.streams.filter(only_audio=True).first()

 

# check for destination to save file

print("Enter the destination (leave blank for current directory)")

destination = str(input(">> ")) or '.'

 

# download the file

out_file = video.download(output_path=destination)

 

# save the file

base, ext = os.path.splitext(out_file)

new_file = base + '.mp3'

os.rename(out_file, new_file)

 

# result of success

print(yt.title + " has been successfully downloaded.")  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-content/uploads/20210216162351/Output.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

