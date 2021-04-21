Plotting Various Sounds on Graphs using Python and Matplotlib



In this article, we will explore the way of visualizing sounds waves using
Python and Matplotlib.

### Modules Needed

**1.** **Matplotlib** **:** Install Matplotlib using the below command:

    
    
    pip install matplotlib
    

**2.** **Numpy** **:** Numpy gets installed automatically installed with
Matplotlib. Although, if you face any import error, use the below command to
install Numpy

    
    
    pip install numpy
    

**Note:** If you are on Linux like me, then you might need to use **pip3**
instead of **pip** or you might create a virtual environment and run the above
command.

### Approach

  * Import matplotlib, Numpy, wave, and sys module.
  * Open the audio file using the _wave.open()_ method.
  * Read all frames of the opened sound wave using _readframes_ () function.
  * Store the frame rate in a variable using the _getframrate_ () function.
  * Finally, plot the x-axis in seconds using frame rate.
  * Use the matplotlib.figure() function to plot the derived graph
  * Use labels as per the requirement.

Below is the implementation.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# imports

import matplotlib.pyplot as plt

import numpy as np

import wave, sys

 

# shows the sound waves

def visualize(path: str):

 

 # reading the audio file

 raw = wave.open(path)

 

 # reads all the frames 

 # -1 indicates all or max frames

 signal = raw.readframes(-1)

 signal = np.frombuffer(signal, dtype ="int16")

 

 # gets the frame rate

 f_rate = raw.getframerate()

 

 # to Plot the x-axis in seconds 

 # you need get the frame rate 

 # and divide by size of your signal

 # to create a Time Vector 

 # spaced linearly with the size 

 # of the audio file

 time = np.linspace(

 0, # start

 len(signal) / f_rate,

 num = len(signal)

 )

 

 # using matlplotlib to plot

 # creates a new figure

 plt.figure(1)

 

 # title of the plot

 plt.title("Sound Wave")

 

 # label of x-axis

 plt.xlabel("Time")

 

 # actual ploting

 plt.plot(time, signal)

 

 # shows the plot 

 # in new window

 plt.show()

 

 # you can also save

 # the plot using

 # plt.savefig('filename')

 

 

if __name__ == "__main__":

 

 # gets the command line Value

 path = sys.argv[1]

 

 visualize(path)  
  
---  
  
 __

 __

 **Output:**

![plotting sound in python](https://media.geeksforgeeks.org/wp-
content/uploads/20200725122651/image121.png)

So, we are done with coding, now it’s the moment of truth. Let’s check if it
actually works or not. You can try out any audio file but make sure that it
has to be a **wav** file. If you have some other file type then you can use
**ffmpeg** to convert it to wav file. If you want then feel free to download
the audio file we will be using. You can download it using this link, but do
try out other files too.  
To run the code, you need to pass the path of the audio file in the command
line. To do that type the following in your terminal:

    
    
    python soundwave.py sample_audio.wav
    

It is important to note that name of the Python file is **soundwave.py** and
the name of the audio file is **sample_audio.wav**. You need to change these
according to your system. Now, a new window should have popped up and should
be seeing a sound wave plot. If you have used my audio, then your plot should
look something like this.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

