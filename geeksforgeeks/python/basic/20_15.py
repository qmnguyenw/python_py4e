Writing files in background in Python



How to write files in background in Python?  
The idea is to us multi-threading in Python. It allows us to write files in
the background while working on another operation. In this article, we will
make a ‘Asyncwrite.py’ named file to demonstrate it. This program adds two
numbers while it will also write a file in background. **Please run this
program on your own system so that you can see the file made**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to write file in

# background

 

# Importing the threading and time 

# modules

import threading

import time

 

# Inherting the base class 'Thread'

class AsyncWrite(threading.Thread): 

 

 def __init__(self, text, out):

 

 # calling superclass init

 threading.Thread.__init__(self) 

 self.text = text

 self.out = out

 

 def run(self):

 

 f = open(self.out, "a")

 f.write(self.text + '\n')

 f.close()

 

 # waiting for 2 seconds after writing

 # the file

 time.sleep(2)

 print("Finished background file write to",

 self.out)

 

def Main():

 

 message = "Geeksforgeeks"

 background = AsyncWrite(message, 'out.txt')

 background.start()

 

 print("The program can continue while it writes")

 print("in another thread")

 print("100 + 400 = ", 100 + 400)

 

 # wait till the background thread is done

 background.join() 

 print("Waited until thread was complete")

 

if __name__=='__main__':

 Main()  
  
---  
  
 __

 __

  
 **Output:**

    
    
    Enter a string to store: HelloWorld
    The program can continue while it writes in another thread
    100 + 400 = 500
    Finished background file write to out.txt
    Waited until  thread was complete
    

The program will ask to enter a string and will calculate the sum of two
numbers and in the background, it writes the ‘entered string’ to the output
file named ‘out.txt’.Check your directory where your ‘Asyncwrite.py’ file
exists and you’ll also find a file named ‘out.txt’ with your string stored in
it.

