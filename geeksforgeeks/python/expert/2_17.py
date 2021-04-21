How to Automate VPN to change IP location on Ubuntu using Python?



To Protect Our system from unauthorized users Access you can spoof our
system’s IP Address using VPN service provided by different organizations. You
can set up a VPN on your system for free.

After you set up and log in to the VPN over the Ubuntu system you need to
manually connect with different VPN servers after some duration. We can
automate it using python so that automatically the IP address of our system
keeps changing after some duration so that no one can have track of our system
anyhow. It will make our system more protected.

#### Follow the steps to Automate VPN using Python:

 **Step 1:** Open your terminal (Ctrl+Alt+T) and create a file using _gedit_
by typing the following command on the terminal.

    
    
    gedit gfg.py
    

**Step 2:** import the modules of python into the opened file.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import required modules

import os

from time import sleep

import random  
  
---  
  
 __

 __

