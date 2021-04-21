How to find available WiFi networks using Python?



WiFi (Wireless Fidelity) is a wireless technology that allows devices such as
computers (laptops and desktops), mobile devices (smartphones and wearables),
and other equipment (printers and video cameras) to interface with the
Internet. We can find out the names of the WiFi names with the help of Python.
We need to have the basics of networking to help us know what we need and what
we do not need.

###  **Module required**

  *  **subprocess:** The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. We do not need to use pip to install it as the subprocess module comes preinstalled.

With the subprocess module, we need to use the **check_output()** method. We
will pass a list of the things we will need to know about the WiFi networks.
We will need netsh, wlan, show and network. These parameters are passed for
storing the outputs in them and then converting it to strings to display the
outputs.

> **Syntax:** subprocess.check_output(args, *, stdin=None, stderr=None,
> shell=False, universal_newlines=False)
>
>  **Parameters:**
>
>   *  **args:** The arguments used to launch the process. This may be a list
> or a string.
>   *  **stdin:** Value of standard input stream to be passed as
> pipe(os.pipe()).
>   *  **stdout:** Value of output obtained from standard output stream.
>   *  **stderr:** also known as standard error, is the default file
> descriptor where a process can write error messages. Basically the value of
> the error(if any)
>   *  **shell:** It is a boolean parameter.If True the commands get executed
> through a new shell environment.
>   *  **universal_newlines:** It is a boolean parameter .If true files
> containing stdout and stderr are opened in universal newline mode.
>

>
>  **Returns:** Information about the networks
>
>  
>
>
>  
>

Now here is the code for it

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the subprocess module

import subprocess

 

# using the check_output() for having the network term retrival

devices =
subprocess.check_output(['netsh','wlan','show','network'])

 

# decode it to strings

devices = devices.decode('ascii')

device s= devices.replace("\r","")

 

# displaying the information

print(devices)  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-content/uploads/20201016211715/gfgvedio.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

