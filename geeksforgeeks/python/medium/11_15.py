Test Internet Speed using Python



 **Prerequisites:** Python Programming Language

Python is a high-level widely used general-purpose language. Python can be
used for many tasks such as web development, machine learning, Gui
applications. It can also be used for testing Internet speed. Python provides
various libraries for doing the same. One such library is speedtest-cli.
This library is a command-line interface for testing internet bandwidth using
speedtest.net

#### Installation

This module does not come built-in with Python. To install it type the below
command in the terminal.

    
    
    pip install speedtest-cli
    

After installing the above package one can check if the package is installed
correctly or not by doing the version check. The version of the package can be
checked using the following command

    
    
    speedtest-cli --version
    

![Checking seedtest-cli version](https://media.geeksforgeeks.org/wp-
content/uploads/20200213185821/speedtest-cli-version1.png)

  

  

#### Speedtest-cli Package

Speedtest-cli is a module that is used in the command-line interface for
testing internet bandwidth using speedtest.net. To get the speed in the
megabits type the below command in the terminal.

    
    
    speedtest-cli
    

![Speedtest-cli](https://media.geeksforgeeks.org/wp-
content/uploads/20200213185724/speedtest-cli1.png)

The above command gives the speed test result is in Megabits. To get the
result in Bytes we can use the following command.

    
    
    speedtest-cli --bytes
    

![speedtest-cli-bytes](https://media.geeksforgeeks.org/wp-
content/uploads/20200213185738/speedtest-cli-bytes1.png)

The pictorial version of your speed test result can also be retrieved using
this module. To do the same type the below command in the terminal.

    
    
    speedtest-cli --share
    

![pictoral version of internet speed](https://media.geeksforgeeks.org/wp-
content/uploads/20200213185807/speedtest-cli-share1.png)

It returns a link on which we can visit on our browser and see the graphical
representation of various kinds of our internet speed.

![pictoral version of internet speed](https://media.geeksforgeeks.org/wp-
content/uploads/20200213185811/speedtest-cli-share-preview1.png)

  

  

To print a simpler version of the speed test result containing only Ping,
Download & Upload results instead of detailed output.

    
    
    speedtest-cli --simple
    

![simple result of internet speed](https://media.geeksforgeeks.org/wp-
content/uploads/20200213185814/speedtest-cli-simple1.png)

**Using Python script to check the internet speed**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to test

# internet speed

 

import speedtest 

 

 

st = speedtest.Speedtest()

 

option = int(input('''What speed do you want to test: 

 

1) Download Speed 

 

2) Upload Speed 

 

3) Ping 

 

Your Choice: '''))

 

 

if option == 1: 

 

 print(st.download()) 

 

elif option == 2: 

 

 print(st.upload()) 

 

elif option == 3: 

 

 servernames =[] 

 

 st.get_servers(servernames) 

 

 print(st.results.ping) 

 

else:

 

 print("Please enter the correct choice !")   
  
---  
  
__

__

**Output:**

![output](https://media.geeksforgeeks.org/wp-
content/uploads/20200213185708/Output135.png)  
![output](https://media.geeksforgeeks.org/wp-
content/uploads/20200213185714/Output221.png)

To get the list of all the available options, type the below command in the
terminal.

  *     speedtest-cli -h

![speedtest-cli --h](https://media.geeksforgeeks.org/wp-
content/uploads/20200213185747/Speedtest-cli-h1.png)

  *     speedtest-cli --help

![speedtest-cli --help](https://media.geeksforgeeks.org/wp-
content/uploads/20200213185754/speedtest-cli-help1.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

