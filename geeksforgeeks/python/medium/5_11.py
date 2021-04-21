Python Script to check PC last reboot time



psutil is a cross-platform library for retrieving information on running
processes and system utilization(CPU, memory, disks, networks, sensors) in
Python. The Python script below can be run in both Windows and Linux. psutil
library can be installed using the terminal by:

 **In Windows:**

    
    
    pip install psutil
    

**In** **Linux:**

    
    
    sudo apt-get install gcc python3-dev
    sudo pip3 install psutil
    

**Code:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import psutil

import datetime

 

# returns the time in seconds since the epoch

last_reboot = psutil.boot_time()

 

# coverting the date and time in readable format

print(datetime.datetime.fromtimestamp(last_reboot))  
  
---  
  
 __

 __

