How to Make a Process Monitor in Python?



A process monitor is a tool that displays the system information like
processes, memory, network, and other stuff. There are plenty of tools
available, but we can make our own process monitor using Python. In Python,
there is a module called **psutil** that we can use to grab various
information about our system

## Modules Needed

  *  **psutil** : Type the below command in the terminal to install this module.

    
    
    python3 -m pip install psutil 

  * **Prettytable:** To print the data on console, we can use a formatter module **PrettyTable** :

    
    
    python3 -m pip install prettytable

## Using psutil

 **psutil** provides lots of features to monitor the system. We will see some
of them in brief:

  *  **First, we need to import psutil:**

    
    
    import psutil

  *  **List the process ids:**

    
    
    psutil.pids()  # [1,2,.....4352]

  *  **Fetch process information:**

    
    
    process_id = 1
    psutil.Process(process_id)  
    # psutil.Process(pid=1, name='systemd', status='sleeping', started='19:49:25')

  *  **We can access various keys of this process:**

    
    
    process = psutil.Process(process_id)
    process.name()
    process.status()

  *  **Accessing battery status:**

    
    
    psutil.sensors_battery()    
    psutil.sensors_battery().percent

  *  **Accessing Network Interfaces:**

    
    
    psutil.net_if_stats()  
    psutil.net_if_stats()['wlo1'].isup    # True

  *  **We can also check the memory:**

    
    
    psutil.virtual_memory()
    psutil.virtual_memory().total    # 8180498432 (In Bytes)
    psutil.virtual_memory().used    # 2155720704
    psutil.virtual_memory().available   # 5563060224

Now that we know some basic features, we can implement the process monitor.
Create a new python file and add the following code in it. The code below
works on Linux distributions. For other operating systems, some functions may
slightly differ.

 **Approach:**

  * Import the required packages.
  * Clear the console using the call() function of the subprocess module. We can use the ‘clear’ or ‘cls’ command depending on OS.
  * Fetch the battery information
  * Fetch the network information and print it as PrettyTable
  * Fetch the memory information
  * Fetch the process information
  * Create a delay. We have created a 1-second delay using time.sleep(1)
  * Press CTRL+C to stop the program.

 **Below is the implementation:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import the required libraries

import psutil

import time 

from subprocess import call 

from prettytable import PrettyTable

 

# Run an infinite loop to constantly monitor the system

while True:

 

 # Clear the screen using a bash command

 call('clear')

 


print("==============================Process
Monitor\


======================================")

 

 # Fetch the battery information

 battery = psutil.sensors_battery().percent 

 print("----Battery Available: %d "%(battery,) + "%")

 

 # We have used PrettyTable to print the data on console.

 # t = PrettyTable(<list of headings>)

 # t.add_row(<list of cells in row>)

 

 # Fetch the Network information

 print("----Networks----")

 table = PrettyTable(['Network', 'Status', 'Speed'])

 for key in psutil.net_if_stats().keys():

 name = key 

 up = "Up" if psutil.net_if_stats()[key].isup else "Down"

 speed = psutil.net_if_stats()[key].speed

 table.add_row([name, up, speed])

 print(table)

 

 # Fetch the memory information

 print("----Memory----")

 memory_table = PrettyTable(["Total", "Used",

 "Available", "Percetage"])

 vm = psutil.virtual_memory()

 memory_table.add_row([

 vm.total,

 vm.used,

 vm.available,

 vm.percent

 ])

 print(memory_table)

 

 

 # Fetch the last 10 processes from available processes

 print("----Processes----")

 process_table = PrettyTable(['PID', 'PNAME', 'STATUS',

 'CPU', 'NUM THREADS'])

 

 for process in psutil.pids()[-10:]:

 

 # While fetching the processes, some of the subprocesses may exit 

 # Hence we need to put this code in try-except block

 try:

 p = psutil.Process(process)

 process_table.add_row([

 str(process),

 p.name(),

 p.status(),

 str(p.cpu_percent())+"%",

 p.num_threads()

 ])

 

 except Exception as e:

 pass

 print(process_table)

 

 # Create a 1 second delay

 time.sleep(1)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210303170025/Screenshotfrom20210303165316.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

