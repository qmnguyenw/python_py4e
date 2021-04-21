Python Program to Create a Lap Timer



In this article, we will make a simple timer to calculate lap-time intervals
using Python.

### Module used

 **time:** This module provides various time-related functions. It is a part
of Python’s standard library and does not require installation.

 **Approach:**  
The user needs to press ENTER to complete each lap. The timer keeps counting
till CTRL+C is pressed. For each lap we calculate the lap time by subtracting
the current time from the total time at the end of the previous lap. The
_time()_ function of the _time_ module, returns the current epoch time in
milliseconds.

Below is the implementation:  

__

__  
__

__

__  
__  
__

# importing libraries

import time

 

 

# Timer starts

starttime=time.time()

lasttime=starttime

lapnum=1

 

print("Press ENTER to count laps.\nPress CTRL+C to stop")

 

try:

 while True:

 

 # Input for the ENTER key press

 input()

 

 # The current lap-time

 laptime=round((time.time() - lasttime), 2)

 

 # Total time elapsed 

 # since the timer started

 totaltime=round((time.time() - starttime), 2)

 

 # Printing the lap number,

 # lap-time and total time

 print("Lap No. "+str(lapnum)) 

 print("Total Time: "+str(totaltime))

 print("Lap Time: "+str(laptime))

 

 print("*"*20)

 

 # Updating the previous total time

 # and lap number

 lasttime=time.time()

 lapnum+=1

 

# Stopping when CTRL+C is pressed

except KeyboardInterrupt:

 print("Done")  
  
---  
  
 __

 __

 **Output:**

    
    
    ENTER to count laps.
    Press CTRL+C to stop
    
    Lap No. 1
    Total Time: 1.09
    Lap Time: 1.09
    ********************
    
    Lap No. 2
    Total Time: 2.66
    Lap Time: 1.41
    ********************
    
    Lap No. 3
    Total Time: 5.06
    Lap Time: 2.23
    ********************
    
    Lap No. 4
    Total Time: 5.63
    Lap Time: 0.4
    ********************
    Done
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

