Progress Bars in Python



Understandably, we get a little impatient when we do not know how much time a
process is going to take, for example, a for loop or a file downloading or an
application starting up.

To distract us from that we were given the libraries **tqdm** and
**progressbar** in Python language which allows us to give a visual
illustration of the process completion time using a progress bar. Loading bars
are often seen on game screens as the resources required for the game to run
are being acquired to the main memory.

## Using tqdm

##

#### What It Does

It wraps an iterable with the tqdm to decorate it with the methods built-in
with tqdm and make a loading bar. This will take the users’ mind off of how
long the process is taking to complete.

#### How To Use

All we need to do is, install the tqdm package by typing this line in your
terminal and start writing the code.

  

  

    
    
    ->pip install tqdm

And type this code in your editor.

 __

 __  
 __

 __

 __  
 __  
 __

from tqdm import tqdm

 

for i in tqdm (range (100), desc="Loading..."):

 pass  
  
---  
  
 __

 __

 **Output:**

![python-tqdm1](https://media.geeksforgeeks.org/wp-
content/uploads/20200312165740/python-tqdm1.png)

This gives a very fast loading bar because there’s nothing in the loop., you
can replace the pass keyword with whatever work you want to do in the for
loop.

 __

 __  
 __

 __

 __  
 __  
 __

from tqdm import tqdm

import time

 

 

for i in tqdm (range (101), 

 desc="Loading…", 

 ascii=False, ncols=75):

 time.sleep(0.01)

 

print("Complete.")  
  
---  
  
 __

 __

 **Output:**

![python-tqdm-2](https://media.geeksforgeeks.org/wp-
content/uploads/20200312170057/python-tqdm-2.png)

## Using progressbar

##

#### How To Install

For command-line interface

  

  

    
    
    pip install progressbar 
    (or)
    pip install progressbar2

#### Working

It does everything the same as tqdm package, that is it decorates the
iterable with the built-in widgets to make an animated progress bar or even a
colorful one. Widgets are objects which display depending on the progress bar.

However, the progress bar and the progress bar 2 packages have a lot of extra,
useful methods than the tqdm package. For example, we can make an animated
loading bar.

 __

 __  
 __

 __

 __  
 __  
 __

import progressbar

import time

 

 

# Function to create 

def animated_marker():

 

 widgets = ['Loading: ', progressbar.AnimatedMarker()]

 bar = progressbar.ProgressBar(widgets=widgets).start()

 

 for i in range(50):

 time.sleep(0.1)

 bar.update(i)

 

# Driver's code

animated_marker()  
  
---  
  
 __

 __

 **Output:**  

https://media.geeksforgeeks.org/wp-content/uploads/20200304194841/prog4.py-
Python-Visual-Studio-Code-2020-02-07-23-21-09.mp4

In progressbar.AnimatedMarker(), we can pass any sequence of characters to
animate. The default arguments are '|/-\|'

Here’s another example using some of the commonly used widgets of the
ProgressBar class.

 __

 __  
 __

 __

 __  
 __  
 __

import time

import progressbar

 

widgets = [' [',

 progressbar.Timer(format= 'elapsed time: %(elapsed)s'),

 '] ',

 progressbar.Bar('*'),' (',

 progressbar.ETA(), ') ',

 ]

 

bar = progressbar.ProgressBar(max_value=200, 

 widgets=widgets).start()

 

for i in range(200):

 time.sleep(0.1)

 bar.update(i)  
  
---  
  
 __

 __

 **Output:**  
![python-progressbar](https://media.geeksforgeeks.org/wp-
content/uploads/20200304200711/p225.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

