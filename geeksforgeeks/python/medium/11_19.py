Video to Audio convert using Python



 **Prerequisites:** Python Programming Language

There are several libraries and techniques available in Python for the
conversion of Video to Audio. One such library is **Movie Editor**.

MoviePy can read and write all the most common audio and video formats,
including GIF, and runs on Windows/Mac/Linux, with Python 2.7+ and 3 (or only
Python 3.4+ from v.1.0)

#### Installation

To install the **Movie Editor** Library, open terminal and write :

    
    
    pip install moviepy
    

**Note:** This module automatically installs FFmpeg. However, you might prompt
to install in some cases.

  

  

#### Installing FFmpeg

 **Windows:**

  * Download the build from here.
  * Unzip the build in any folder.
  * Open the CMD with adminstrative rights.
  * Run the below command for setting the environment variable.
    
        setx /M PATH "path\to\ffmpeg\bin;%PATH%"

 **Linux:**

Write the below commands in the terminal.

    
    
    sudo add-apt-repository ppa:mc3man/trusty-media  
    sudo apt-get update  
    sudo apt-get install ffmpeg  
    sudo apt-get install frei0r-plugins

 **Implementation**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert video to audio

import moviepy.editor as mp

 

# Insert Local Video File Path 

clip = mp.VideoFileClip(r"Video File")

 

# Insert Local Audio File Path

clip.audio.write_audiofile(r"Audio File")  
  
---  
  
 __

 __

 **Output:**

![python-video-to-audio](https://media.geeksforgeeks.org/wp-
content/uploads/20200211125956/python-video-to-audio.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

