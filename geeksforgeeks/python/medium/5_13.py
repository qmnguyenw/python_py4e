Application for Internet speed test using pyspeedtest in Python



While troubleshooting with Internet speed. We need to first check internet
bandwidth speed. So, **pyspeedtest** module test network bandwidth using
Speedtest.net servers. So, before starting we need to install **pyspeedtest**
into your system. Run these code to your command line

    
    
    pip install pyspeedtest

 **Approach:**

  * Import pyspeedtest
  * Create object for **SpeedTest()**
  * Check ping with **ping()**
  * Check Download speed with **download()**
  * Check Upload speed with **upload()**

Below is the implementation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pyspeedtest

 

 

test = pyspeedtest.SpeedTest("www.youtube.com")

 

test.ping()

test.download()

test.upload()  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    253.4427046775818
    16461.88637373227
    19425388.307319913
    

**Speed Test Application with Tkinter:** This Script implements the above
Implementation into a GUI.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pyspeedtest

from tkinter import *

 

 

def Speed_test():

 t = pyspeedtest.SpeedTest(e1.get())

 myping.set(t.ping())

 down.set(t.download())

 

 

master = Tk()

myping = StringVar()

down = StringVar()

 

Label(master, text="Website URL").grid(row=0, sticky=W)

Label(master, text="Ping Result:").grid(row=3, sticky=W)

Label(master, text="Download Result:").grid(row=4, sticky=W)

 

result = Label(master, text="", textvariable=myping,

 ).grid(row=3, column=1, sticky=W)

 

result2 = Label(master, text="", textvariable=down,

 ).grid(row=4, column=1, sticky=W)

 

 

e1 = Entry(master)

e1.grid(row=0, column=1)

b = Button(master, text="Cheak", command=Speed_test)

b.grid(row=0, column=2, columnspan=2, rowspan=2,
padx=5, pady=5)

 

mainloop()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200821152542/Screenshot23.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

